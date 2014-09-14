# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeneticSimplifierDialog
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

from PyQt4 import QtCore, QtGui
from ui_geneticsimplifier import Ui_GeneticSimplifier
# create the dialog for zoom to point

# Specific imports
import Types
from qgis.core import *

class GeneticSimplifierDialog(QtGui.QDialog, Ui_GeneticSimplifier):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.ui = Ui_GeneticSimplifier()
        self.ui.setupUi(self)
        
        # Get the available mate types
        self.ui.mateCombo.addItems(Types.MateTypes)
        
        # Connecting SIGNAL/SLOTS for the Output button
        QtCore.QObject.connect(self.ui.inputLayerCombo, QtCore.SIGNAL("currentIndexChanged (int)"), self.updateFeatureCount)
        
        self.layers = []
        self.currentLayer = None
        
    def updateFeatureCount(self, index):
        self.currentLayer = self.layers[index]
        count = self.currentLayer.featureCount()
        self.ui.featureCountEdit.setText(str(count))
        
    def saveOutputFile(self):
         fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save output file', '', "ShapeFile (*.shp)")
         #fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save output file', '', "Vector Files (*.shp *.geojson *.gml *.kml *.bna *.gdb)")
         if fileName:
            self.ui.outputEdit.setText(fileName)

    def insertLineLayers(self, layers):
        self.layers = layers
        self.ui.inputLayerCombo.clear()
        for layer in layers:
            self.ui.inputLayerCombo.addItem(layer.name(), layer.id())
