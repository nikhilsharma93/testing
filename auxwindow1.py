# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auxwindow1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(616, 421)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setMinimumSize(QtCore.QSize(100, 0))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_run = QtGui.QWidget()
        self.tab_run.setObjectName(_fromUtf8("tab_run"))
        self.formLayoutWidget = QtGui.QWidget(self.tab_run)
        self.formLayoutWidget.setGeometry(QtCore.QRect(19, 9, 321, 311))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.checkBox_runasync = QtGui.QCheckBox(self.formLayoutWidget)
        self.checkBox_runasync.setObjectName(_fromUtf8("checkBox_runasync"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkBox_runasync)
        self.checkBox_wait = QtGui.QCheckBox(self.formLayoutWidget)
        self.checkBox_wait.setObjectName(_fromUtf8("checkBox_wait"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkBox_wait)
        self.tabWidget.addTab(self.tab_run, _fromUtf8(""))
        self.tab_save = QtGui.QWidget()
        self.tab_save.setObjectName(_fromUtf8("tab_save"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.tab_save)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(19, 9, 291, 301))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.checkBox_savePy = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.checkBox_savePy.setObjectName(_fromUtf8("checkBox_savePy"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkBox_savePy)
        self.checkBox_saveKfp = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.checkBox_saveKfp.setObjectName(_fromUtf8("checkBox_saveKfp"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkBox_saveKfp)
        self.tabWidget.addTab(self.tab_save, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        """
        self.checkBox_wait.setEnabled(False)
        self.checkBox_runasync.toggled.connect(self.checkBox_wait.setEnabled)
        self.checkBox_runasync.toggled.connect(
            lambda checked: not checked and self.checkBox_wait.setChecked(False))
        self.checkBox_wait.toggled.connect(self.checkBox_runasync.setEnabled)
        self.checkBox_wait.toggled.connect(
            lambda checked: not checked and self.checkBox_runasync.setChecked(False))
        """
        self._toggle = True
        self.checkBox_wait.setChecked(self._toggle)
        self.checkBox_runasync.setChecked(not self._toggle)
        self.checkBox_wait.clicked.connect(self.toggle)
        self.checkBox_runasync.clicked.connect(self.toggle)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def toggle(self):
        self._toggle = not self._toggle
        self.checkBox_wait.setChecked(self._toggle)
        #self.checkBox_wait.setEnabled(not self._toggle)
        self.checkBox_runasync.setChecked(not self._toggle)
        #self.checkBox_runasync.setEnabled(self._toggle)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Run Pipeline Options", None))
        self.checkBox_runasync.setText(_translate("Dialog", "Run Async", None))
        self.checkBox_wait.setText(_translate("Dialog", "Wait for completion", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_run), _translate("Dialog", "Run options", None))
        self.checkBox_savePy.setText(_translate("Dialog", "Save Python code", None))
        self.checkBox_saveKfp.setText(_translate("Dialog", "Save Kubeflow Piplines file (.yaml)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_save), _translate("Dialog", "Save options", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow_op1 = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow_op1)
    MainWindow_op1.show()
    sys.exit(app.exec_())
