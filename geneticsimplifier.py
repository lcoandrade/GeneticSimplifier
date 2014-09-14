# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeneticSimplifier
                                 A QGIS plugin
 Line simplification tool using genetic algorithms
                              -------------------
        begin                : 2014-09-11
        copyright            : (C) 2014 by Luiz Andrade
        email                : luiz.claudio@dsg.eb.mil.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from geneticsimplifierdialog import GeneticSimplifierDialog
import os.path

#Import Genetic Simplifier module
import genetic_simplifier

class GeneticSimplifier:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'geneticsimplifier_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = GeneticSimplifierDialog()

        # Obtaining the map canvas
        self.canvas = iface.mapCanvas()
        
        # Obtaining the the vector line layers
        self.allLayers = []
        self.lineLayers = []        

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/geneticsimplifier/geneticSimplify.png"),
            u"Genetic Simplifier", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Genetic Line Simplifier", self.action)        

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Genetic Line Simplifier", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):        
        # Adding the line layers into the GUI
        self.lineLayers = []
        self.allLayers = self.canvas.layers()
        for layer in self.allLayers:
            if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType() == QGis.Line:
                self.lineLayers.append(layer)
        self.dlg.insertLineLayers(self.lineLayers)
        
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # Setting the progress bar
            self.progressMessageBar = self.iface.messageBar().createMessage("Simplifying layer "+ self.dlg.currentLayer.name() + " to new layer " + self.dlg.ui.outputEdit.text() +  "...")
            self.progressBar = QProgressBar()
            self.progressBar.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
            self.progressMessageBar.layout().addWidget(self.progressBar)
            self.iface.messageBar().pushWidget(self.progressMessageBar, self.iface.messageBar().INFO)

            self.geneticThread = genetic_simplifier.GeneticSimplifier(self.dlg.ui.popSpin.value(), self.dlg.ui.spinBox.value(), self.dlg.currentLayer, self.dlg.ui.mateCombo.currentIndex(), self.dlg.ui.geneSpin.value(), self.dlg.ui.evolutionGroup.isChecked(), self.dlg.ui.crossSpin.value()/100, self.dlg.ui.mutationSpin.value()/100, self.dlg.ui.genSpin.value(), self.dlg.ui.outputEdit.text())
            QObject.connect( self.geneticThread, SIGNAL( "rangeCalculated( PyQt_PyObject )" ), self.setProgressRange )
            QObject.connect( self.geneticThread, SIGNAL( "featureProcessed()" ), self.featureProcessed )
            QObject.connect( self.geneticThread, SIGNAL( "processingFinished()" ), self.processFinished )
            QObject.connect( self.geneticThread, SIGNAL( "layerCreated( PyQt_PyObject )" ), self.layerCreated )

            # Startin the processing
            self.geneticThread.start()

    def setProgressRange( self, maximum ):
        self.progressBar.setRange( 0, maximum )
    
    def featureProcessed( self ):
        self.progressBar.setValue( self.progressBar.value() + 1 )

    def processFinished( self ):
        if self.geneticThread != None:
            self.geneticThread.stop()
            self.geneticThread = None
        
    def layerCreated(self, outLayer):
        QgsMapLayerRegistry.instance().addMapLayers([outLayer])
        
