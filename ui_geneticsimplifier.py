# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_geneticsimplifier.ui'
#
# Created: Sun Sep 14 13:50:40 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GeneticSimplifier(object):
    def setupUi(self, GeneticSimplifier):
        GeneticSimplifier.setObjectName(_fromUtf8("GeneticSimplifier"))
        GeneticSimplifier.resize(587, 276)
        self.gridLayout_3 = QtGui.QGridLayout(GeneticSimplifier)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.inputLabel = QtGui.QLabel(GeneticSimplifier)
        self.inputLabel.setObjectName(_fromUtf8("inputLabel"))
        self.horizontalLayout.addWidget(self.inputLabel)
        self.inputLayerCombo = QtGui.QComboBox(GeneticSimplifier)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputLayerCombo.sizePolicy().hasHeightForWidth())
        self.inputLayerCombo.setSizePolicy(sizePolicy)
        self.inputLayerCombo.setObjectName(_fromUtf8("inputLayerCombo"))
        self.horizontalLayout.addWidget(self.inputLayerCombo)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.featCountLabel = QtGui.QLabel(GeneticSimplifier)
        self.featCountLabel.setObjectName(_fromUtf8("featCountLabel"))
        self.horizontalLayout_5.addWidget(self.featCountLabel)
        self.featureCountEdit = QtGui.QLineEdit(GeneticSimplifier)
        self.featureCountEdit.setObjectName(_fromUtf8("featureCountEdit"))
        self.horizontalLayout_5.addWidget(self.featureCountEdit)
        self.featureLabel = QtGui.QLabel(GeneticSimplifier)
        self.featureLabel.setObjectName(_fromUtf8("featureLabel"))
        self.horizontalLayout_5.addWidget(self.featureLabel)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.outputEdit_2 = QtGui.QLabel(GeneticSimplifier)
        self.outputEdit_2.setObjectName(_fromUtf8("outputEdit_2"))
        self.horizontalLayout_2.addWidget(self.outputEdit_2)
        self.outputEdit = QtGui.QLineEdit(GeneticSimplifier)
        self.outputEdit.setObjectName(_fromUtf8("outputEdit"))
        self.horizontalLayout_2.addWidget(self.outputEdit)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.popSizeLabel = QtGui.QLabel(GeneticSimplifier)
        self.popSizeLabel.setObjectName(_fromUtf8("popSizeLabel"))
        self.horizontalLayout_3.addWidget(self.popSizeLabel)
        self.popSpin = QtGui.QSpinBox(GeneticSimplifier)
        self.popSpin.setMinimum(1)
        self.popSpin.setMaximum(10000)
        self.popSpin.setProperty("value", 5)
        self.popSpin.setObjectName(_fromUtf8("popSpin"))
        self.horizontalLayout_3.addWidget(self.popSpin)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.restrictionLabel = QtGui.QLabel(GeneticSimplifier)
        self.restrictionLabel.setObjectName(_fromUtf8("restrictionLabel"))
        self.horizontalLayout_4.addWidget(self.restrictionLabel)
        self.spinBox = QtGui.QSpinBox(GeneticSimplifier)
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(1000)
        self.spinBox.setSingleStep(10)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.evolutionGroup = QtGui.QGroupBox(GeneticSimplifier)
        self.evolutionGroup.setCheckable(True)
        self.evolutionGroup.setObjectName(_fromUtf8("evolutionGroup"))
        self.gridLayout = QtGui.QGridLayout(self.evolutionGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.generationsLabel = QtGui.QLabel(self.evolutionGroup)
        self.generationsLabel.setObjectName(_fromUtf8("generationsLabel"))
        self.horizontalLayout_6.addWidget(self.generationsLabel)
        self.genSpin = QtGui.QSpinBox(self.evolutionGroup)
        self.genSpin.setMinimum(1)
        self.genSpin.setMaximum(100)
        self.genSpin.setObjectName(_fromUtf8("genSpin"))
        self.horizontalLayout_6.addWidget(self.genSpin)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.mateLabel = QtGui.QLabel(self.evolutionGroup)
        self.mateLabel.setObjectName(_fromUtf8("mateLabel"))
        self.horizontalLayout_7.addWidget(self.mateLabel)
        self.mateCombo = QtGui.QComboBox(self.evolutionGroup)
        self.mateCombo.setObjectName(_fromUtf8("mateCombo"))
        self.horizontalLayout_7.addWidget(self.mateCombo)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.croosLabel = QtGui.QLabel(self.evolutionGroup)
        self.croosLabel.setObjectName(_fromUtf8("croosLabel"))
        self.horizontalLayout_8.addWidget(self.croosLabel)
        self.crossSpin = QtGui.QSpinBox(self.evolutionGroup)
        self.crossSpin.setMinimum(1)
        self.crossSpin.setMaximum(100)
        self.crossSpin.setProperty("value", 50)
        self.crossSpin.setObjectName(_fromUtf8("crossSpin"))
        self.horizontalLayout_8.addWidget(self.crossSpin)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.mutationLabel = QtGui.QLabel(self.evolutionGroup)
        self.mutationLabel.setObjectName(_fromUtf8("mutationLabel"))
        self.horizontalLayout_9.addWidget(self.mutationLabel)
        self.mutationSpin = QtGui.QSpinBox(self.evolutionGroup)
        self.mutationSpin.setMinimum(1)
        self.mutationSpin.setMaximum(100)
        self.mutationSpin.setProperty("value", 20)
        self.mutationSpin.setObjectName(_fromUtf8("mutationSpin"))
        self.horizontalLayout_9.addWidget(self.mutationSpin)
        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.geneLabel = QtGui.QLabel(self.evolutionGroup)
        self.geneLabel.setObjectName(_fromUtf8("geneLabel"))
        self.horizontalLayout_10.addWidget(self.geneLabel)
        self.geneSpin = QtGui.QSpinBox(self.evolutionGroup)
        self.geneSpin.setMinimum(1)
        self.geneSpin.setMaximum(100)
        self.geneSpin.setProperty("value", 5)
        self.geneSpin.setObjectName(_fromUtf8("geneSpin"))
        self.horizontalLayout_10.addWidget(self.geneSpin)
        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.evolutionGroup, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 4, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(GeneticSimplifier)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 5, 1, 1, 1)

        self.retranslateUi(GeneticSimplifier)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GeneticSimplifier.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GeneticSimplifier.reject)
        QtCore.QMetaObject.connectSlotsByName(GeneticSimplifier)

    def retranslateUi(self, GeneticSimplifier):
        GeneticSimplifier.setWindowTitle(_translate("GeneticSimplifier", "GeneticSimplifier", None))
        self.inputLabel.setText(_translate("GeneticSimplifier", "Input Layer:", None))
        self.featCountLabel.setText(_translate("GeneticSimplifier", "The selected layer contains:", None))
        self.featureLabel.setText(_translate("GeneticSimplifier", "features", None))
        self.outputEdit_2.setText(_translate("GeneticSimplifier", "Output Layer Name:", None))
        self.popSizeLabel.setText(_translate("GeneticSimplifier", "Population Size:", None))
        self.restrictionLabel.setText(_translate("GeneticSimplifier", "Shape Restriction:", None))
        self.evolutionGroup.setTitle(_translate("GeneticSimplifier", "Use Evolution?", None))
        self.generationsLabel.setText(_translate("GeneticSimplifier", "Number of Generations:", None))
        self.mateLabel.setText(_translate("GeneticSimplifier", "Mate Type:", None))
        self.croosLabel.setText(_translate("GeneticSimplifier", "Crossover Probability (%):", None))
        self.mutationLabel.setText(_translate("GeneticSimplifier", "Mutation Probability (%):", None))
        self.geneLabel.setText(_translate("GeneticSimplifier", "Gene Mutation Probability (%):", None))
