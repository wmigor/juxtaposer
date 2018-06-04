# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/config_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        ConfigDialog.setObjectName("ConfigDialog")
        ConfigDialog.resize(415, 179)
        self.verticalLayout = QtWidgets.QVBoxLayout(ConfigDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.l_column1 = QtWidgets.QLabel(ConfigDialog)
        self.l_column1.setObjectName("l_column1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l_column1)
        self.sb_column1 = QtWidgets.QSpinBox(ConfigDialog)
        self.sb_column1.setObjectName("sb_column1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sb_column1)
        self.l_column2 = QtWidgets.QLabel(ConfigDialog)
        self.l_column2.setObjectName("l_column2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.l_column2)
        self.sb_column2 = QtWidgets.QSpinBox(ConfigDialog)
        self.sb_column2.setObjectName("sb_column2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sb_column2)
        self.l_start = QtWidgets.QLabel(ConfigDialog)
        self.l_start.setObjectName("l_start")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.l_start)
        self.sb_start = QtWidgets.QSpinBox(ConfigDialog)
        self.sb_start.setObjectName("sb_start")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sb_start)
        self.l_end = QtWidgets.QLabel(ConfigDialog)
        self.l_end.setObjectName("l_end")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.l_end)
        self.sb_end = QtWidgets.QSpinBox(ConfigDialog)
        self.sb_end.setObjectName("sb_end")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sb_end)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.button_box = QtWidgets.QDialogButtonBox(ConfigDialog)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(ConfigDialog)
        self.button_box.rejected.connect(ConfigDialog.reject)
        self.button_box.accepted.connect(ConfigDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)

    def retranslateUi(self, ConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfigDialog.setWindowTitle(_translate("ConfigDialog", "Параметры"))
        self.l_column1.setText(_translate("ConfigDialog", "Столбец для сравнивания первой таблицы"))
        self.l_column2.setText(_translate("ConfigDialog", "Столбец для сравнивания второй таблицы"))
        self.l_start.setText(_translate("ConfigDialog", "Столбец начала второй таблицы"))
        self.l_end.setText(_translate("ConfigDialog", "Столбец конца второй таблицы"))

