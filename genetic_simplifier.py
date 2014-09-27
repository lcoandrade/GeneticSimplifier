#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      luiz
#
# Created:     13/03/2014
# Copyright:   (c) luiz 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os.path
import sys
import shapely.wkb
import osgeo.ogr
import random
import Types
from numpy import asarray

# Import specific modules
# Import DEAP library
# Set up current path, so that we know where to look for modules
currentPath = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from deap import base, creator, tools, algorithms
################################################################

from qgis.core import *
from PyQt4.QtGui import QProgressBar
from PyQt4.QtCore import *

class GeneticSimplifier(QThread):
    """Evolutionary Algorithm Class to simplify line vector features.
    """
    def __init__(self, population, shape, layer, mateType, geneProb, doEvolution, crossoverProb, mutationProb, generations, output, useLocalSearch):
        """Constructor.
        """
        QThread.__init__( self, QThread.currentThread() )
        
        # Creating the toolbox that will be used in the evolution
        self.toolbox = base.Toolbox()
  
        # Defining the parameters used to simplify lines
        self.limit = shape
        self.popSize = population
        self.layer = layer
        self.mateType = mateType
        self.GENEPB = geneProb
        self.doEvolution = doEvolution
        self.CXPB = crossoverProb
        self.MUTPB = mutationProb
        self.NGEN = generations
        self.outputName = output
        self.useLocalSearch = useLocalSearch
        
        self.pointsBefore = 0
        self.pointsAfter = 0
        
        # QThread
        self.mutex = QMutex()
        self.stopMe = 0
        
    def __del__(self):
        """Destructor.
        """
        pass
    
    def run(self):
        # QThread
        self.mutex.lock()
        self.stopMe = 0
        self.mutex.unlock()
        
        # Progress bar steps calculated
        self.emit( SIGNAL( "rangeCalculated( PyQt_PyObject )" ), self.layer.featureCount()*2)

        #Registering operators
        self.registerOperators(self.mateType, self.GENEPB)
        #Reads features layers, evaluates the population and do the evolution if needed
        self.readFeatures(self.doEvolution, self.CXPB, self.MUTPB, self.NGEN)
        #Creates the output layer
        self.createOutputLayer(self.outputName)
        
        # Processing ending
        self.emit( SIGNAL( "processingFinished( PyQt_PyObject )" ), (self.pointsBefore, self.pointsAfter) )
        
    def stop( self ):
        # Stopping the thread
        self.mutex.lock()
        self.stopMe = 1
        self.mutex.unlock()        
        QThread.wait( self )

    def readFeatures(self, doEvolution, CXPB, MUTPB, NGEN):
        """Reads features that will be simplified.
        """
        self.featuresDict = dict()
        for feature in self.layer.getFeatures():
            self.generatePopulation(feature, self.popSize)
            self.evaluatePopulation()
            if doEvolution:
                self.evolution(CXPB, MUTPB, NGEN)
            self.featuresDict[feature] = self.getBestIndividual()
            self.pointsBefore += self.geomVertexCount(feature.geometry())
            # Updating progress
            self.emit( SIGNAL( "featureProcessed()" ) )

    def registerOperators(self, mateType, GENEPB):
        """Defining the methodos used in this evolution.
        """
        self.mateType = mateType
        
        # Registering operators
        if self.mateType == 0:
            self.toolbox.register("mate", tools.cxOnePoint)
        elif self.mateType == 1:
            self.toolbox.register("mate", tools.cxTwoPoint)
        elif self.mateType == 2:
            self.toolbox.register("mate", tools.cxUniform)
        elif self.mateType == 3:
            self.toolbox.register("mate", tools.cxPartialyMatched)
        elif self.mateType == 4:
            self.toolbox.register("mate", tools.cxUniformPartialyMatched)
        elif self.mateType == 5:
            self.toolbox.register("mate", tools.cxOrdered)
        elif self.mateType == 6:
            self.toolbox.register("mate", tools.cxBlend)

        self.toolbox.register("evaluate", self.evaluateIndividual)
        
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=GENEPB)

        # Fixed tournament size of 3
        self.toolbox.register("select", tools.selTournament, tournsize=3)

    def generatePopulation(self, feature, size):
        """For each feature a population is created with the given parameters.
        """
        # Obtaining the OGR geometry
        geometry = feature.geometry()

        # Creating a shapely linestring using WKB
        self.original = shapely.wkb.loads(geometry.asWkb())
        # Creating the buffer that will be used to address the quality of a simplification
        self.buffer = self.original.buffer(self.limit)

        # Obtaining the chromosome (individual size)
        # The initial and final points are not considered. They should always be present in the output
        individualSize = len(self.original.coords) - 2

        # Type creation
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        # Attribute generator
        self.toolbox.register("attr_bool", random.randint, 0, 1)

        # Structure initializers
        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.attr_bool, n=individualSize)

        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        # Actual population creation
        self.population = self.toolbox.population(n=size)

    def evaluateIndividual(self, individual):
        """Evaluates the fitness of each individual.
        """
        # Creating wkb
        size = len(self.original.coords)
        wkb = None
        wkb = self.createSimplifiedLine(individual)

        # Importing from wkb
        simplifiedLine = shapely.wkb.loads(wkb)

        # Check if the simplified line is inside the original buffer
        if self.buffer.contains(simplifiedLine) == False:
            # Check the distance from all points in the original geometry to the simplified line
            for i in xrange(1, size - 1):
                point = shapely.geometry.Point(self.original.coords[i][0], self.original.coords[i][1])
                distance = point.distance(simplifiedLine)
                # If some point has a distance bigger than the limit it
                # should become a participant
                if(distance > self.limit):
                    individual[i - 1] = 1

        if self.useLocalSearch == True:
            # Perform local search to improve the individuals
            for i in xrange(1, size - 1):
                if individual[i - 1] == 1:
                    individual[i - 1] = 0
                    wkb = self.createSimplifiedLine(individual)
                    simplifiedLine = shapely.wkb.loads(wkb)
                    if self.buffer.contains(simplifiedLine) == False:
                        individual[i - 1] = 1

        # If the line is suitable the less the number of points the better
        return sum(individual),

    def evaluatePopulation(self):
        """Evaluates the fitness of the entire population.
        """
        # Calculating the fitness values for all individuals
        fitnesses = list(map(self.toolbox.evaluate, self.population))
        # Creating tuples for the pair individual/fitness
        for individual, fitness in zip(self.population, fitnesses):
            # Assigning the fitness values to the individual
            individual.fitness.values = fitness

    def evolution(self, CXPB, MUTPB, NGEN):
        """Performs evolution on the population according to the parameters
         and the number of generations.
        """
        for g in xrange(NGEN):
            # Select the next generation individuals
            offspring = self.toolbox.select(self.population, len(self.population))
            # Clone the selected individuals
            offspring = list(map(self.toolbox.clone, offspring))

            # Apply crossover on the offspring
            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if random.random() < CXPB:
                    if self.mateType == 0 or self.mateType == 1 or self.mateType == 3 or self.mateType == 5:
                        self.toolbox.mate(child1, child2)
                    elif self.mateType == 2 or self.mateType == 4 or self.mateType == 6:
                        self.toolbox.mate(child1, child2, 0.25)
                    del child1.fitness.values
                    del child2.fitness.values

            # Apply mutation on the offspring
            for mutant in offspring:
                if random.random() < MUTPB:
                    self.toolbox.mutate(mutant)
                    del mutant.fitness.values

            # Evaluate the individuals with an invalid fitness
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = map(self.toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit

            # New generation
            self.population[:] = offspring

    def getBestIndividual(self):
        """Determines the best individual.
        """
        best_ind = tools.selBest(self.population, 1)[0]

        # If the first or the end point are not presents the original line should be returned
        if best_ind.fitness.values[0] > len(self.original.coords):
#             print "Returning the original"
            return self.original.to_wkb()

        wkb = self.createSimplifiedLine(best_ind)

        return wkb

    def createSimplifiedLine(self, individual):
        """Create a WKB with the best individual.
        """
        # Create empty simplified line
        simplifiedLine = osgeo.ogr.Geometry(osgeo.ogr.wkbLineString)

        # Initial point
        start = self.original.coords[0]
        # Final point
        end = self.original.coords[-1]

        # Inserting the start point
        simplifiedLine.AddPoint(start[0], start[1])

        # Check if the genes in the individual have value 1
        for i in xrange(len(individual)):
            # If they have the value 1 the vertex i should be present in the simplified line
            if individual[i] == 1:
                # Creating the simplified line
                point = self.original.coords[i + 1]
                simplifiedLine.AddPoint(point[0], point[1])

        # Inserting the final point
        simplifiedLine.AddPoint(end[0], end[1])

        # Exporting to wkb
        return simplifiedLine.ExportToWkb()

    def createOutputLayer(self, outputName):
        """Creates the output layer.
        """
        # Create a memory layer for the output simplification
        outLayer = QgsVectorLayer("LineString?crs="+self.layer.crs().toWkt(), outputName, "memory")
        provider = outLayer.dataProvider()
        
        # Enter in edit mode
        outLayer.startEditing()
        
        # Adding attributes
        added = provider.addAttributes(self.layer.dataProvider().fields().toList())
        
        # For each feature in the selected layer we create a clone and change the geometry by the simplified one created
        for feature in self.featuresDict.keys():
            # The final simplified geometry
            wkb = self.featuresDict[feature]
            # This is important to use the fromWkb method from QgsGeometry
            simplifiedLine = shapely.wkb.loads(wkb)
            newWkb = shapely.wkb.dumps(simplifiedLine)
            
            # Creating the new geometry
            newGeom = QgsGeometry()
            newGeom.fromWkb(newWkb)
            self.pointsAfter += self.geomVertexCount(newGeom)

            # Setting the geometry on the new feture
            feature.setGeometry(newGeom)

            # Adding the feature into the file
            provider.addFeatures([feature])

            # Updating progress
            self.emit( SIGNAL( "featureProcessed()" ) )

        # Commiting changes        
        outLayer.commitChanges()
        # Updating progress
        self.emit( SIGNAL( "featureProcessed()" ) )
        
        # Show the output layer
        self.emit( SIGNAL( "layerCreated( PyQt_PyObject )" ), outLayer )
        
    def geomVertexCount(self, geometry ):
        """Calculates the number of vertexes in a geometry.
        """
        geomType = geometry.type()
        if geomType == QGis.Line:
            if geometry.isMultipart():
                pointsList = geometry.asMultiPolyline()
                points = sum( pointsList, [] )
            else:
                points = geometry.asPolyline()
            return len( points )
        elif geomType == QGis.Polygon:
            if geometry.isMultipart():
                polylinesList = geometry.asMultiPolygon()
                polylines = sum( polylinesList, [] )
            else:
                polylines = geometry.asPolygon()
            points = []
            for l in polylines:
                points.extend( l )
            return len( points )
        else:
            return None        

if __name__ == '__main__':
    pass
