# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'castelet.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CaseletWindow(object):
    def setupUi(self, CaseletWindow):
        CaseletWindow.setObjectName("CaseletWindow")
        CaseletWindow.resize(1280, 807)
        self.centralwidget = QtWidgets.QWidget(CaseletWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(44, 62, 80);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setMinimumSize(QtCore.QSize(0, 120))
        font = QtGui.QFont()
        font.setFamily("Segoe UI,Arial,sans-serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-weight: bold;\n"
"    padding:32px;\n"
"    background-color: #ecf0f1;\n"
"    text-align: center;")
        self.label_14.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 3)
        self.LeftHand_GridLayout = QtWidgets.QGridLayout()
        self.LeftHand_GridLayout.setObjectName("LeftHand_GridLayout")
        self.LeftHand_F4_Label = QtWidgets.QLabel(self.centralwidget)
        self.LeftHand_F4_Label.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    margin: 4px;\n"
"    background-color: #ecf0f1;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    text-align: center;")
        self.LeftHand_F4_Label.setObjectName("LeftHand_F4_Label")
        self.LeftHand_GridLayout.addWidget(self.LeftHand_F4_Label, 3, 1, 1, 1)
        self.LeftHand_F1_Label = QtWidgets.QLabel(self.centralwidget)
        self.LeftHand_F1_Label.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    margin: 4px;\n"
"    background-color: #ecf0f1;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    text-align: center;")
        self.LeftHand_F1_Label.setObjectName("LeftHand_F1_Label")
        self.LeftHand_GridLayout.addWidget(self.LeftHand_F1_Label, 0, 1, 1, 1)
        self.LeftHand_F3_Label = QtWidgets.QLabel(self.centralwidget)
        self.LeftHand_F3_Label.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    margin: 4px;\n"
"    background-color: #ecf0f1;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    text-align: center;")
        self.LeftHand_F3_Label.setObjectName("LeftHand_F3_Label")
        self.LeftHand_GridLayout.addWidget(self.LeftHand_F3_Label, 2, 1, 1, 1)
        self.LeftHand_F2_Label = QtWidgets.QLabel(self.centralwidget)
        self.LeftHand_F2_Label.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    margin: 4px;\n"
"    background-color: #ecf0f1;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    text-align: center;")
        self.LeftHand_F2_Label.setObjectName("LeftHand_F2_Label")
        self.LeftHand_GridLayout.addWidget(self.LeftHand_F2_Label, 1, 1, 1, 1)
        self.LeftHand_F5 = QtWidgets.QLabel(self.centralwidget)
        self.LeftHand_F5.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    margin: 4px;\n"
"    background-color: #ecf0f1;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    text-align: center;")
        self.LeftHand_F5.setObjectName("LeftHand_F5")
        self.LeftHand_GridLayout.addWidget(self.LeftHand_F5, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.LeftHand_GridLayout, 4, 0, 1, 1)
        self.RightHand_GridLayout = QtWidgets.QGridLayout()
        self.RightHand_GridLayout.setObjectName("RightHand_GridLayout")
        self.RightHand_F3_Label = QtWidgets.QLabel(self.centralwidget)
        self.RightHand_F3_Label.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    margin: 4px;\n"
"    background-color: #ecf0f1;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    text-align: center;")
        self.RightHand_F3_Label.setObjectName("RightHand_F3_Label")
        self.RightHand_GridLayout.addWidget(self.RightHand_F3_Label, 2, 0, 1, 1)
        self.RightHand_F1_Label = QtWidgets.QLabel(self.centralwidget)
        self.RightHand_F1_Label.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    margin: 4px;\n"
"    background-color: #ecf0f1;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    text-align: center;")
        self.RightHand_F1_Label.setObjectName("RightHand_F1_Label")
        self.RightHand_GridLayout.addWidget(self.RightHand_F1_Label, 0, 0, 1, 1)
        self.RightHand_F2_Label = QtWidgets.QLabel(self.centralwidget)
        self.RightHand_F2_Label.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    margin: 4px;\n"
"    background-color: #ecf0f1;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    text-align: center;")
        self.RightHand_F2_Label.setObjectName("RightHand_F2_Label")
        self.RightHand_GridLayout.addWidget(self.RightHand_F2_Label, 1, 0, 1, 1)
        self.RightHand_F4_Label = QtWidgets.QLabel(self.centralwidget)
        self.RightHand_F4_Label.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    margin: 4px;\n"
"    background-color: #ecf0f1;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    text-align: center;")
        self.RightHand_F4_Label.setObjectName("RightHand_F4_Label")
        self.RightHand_GridLayout.addWidget(self.RightHand_F4_Label, 3, 0, 1, 1)
        self.RightHand_F5_Label = QtWidgets.QLabel(self.centralwidget)
        self.RightHand_F5_Label.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    margin: 4px;\n"
"    background-color: #ecf0f1;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    text-align: center;")
        self.RightHand_F5_Label.setObjectName("RightHand_F5_Label")
        self.RightHand_GridLayout.addWidget(self.RightHand_F5_Label, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.RightHand_GridLayout, 4, 2, 1, 1)
        self.camera_lb = QtWidgets.QLabel(self.centralwidget)
        self.camera_lb.setMinimumSize(QtCore.QSize(480, 480))
        self.camera_lb.setStyleSheet("background-color: #f2f2f2;\n"
"    color: #333;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;")
        self.camera_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_lb.setWordWrap(True)
        self.camera_lb.setObjectName("camera_lb")
        self.gridLayout_2.addWidget(self.camera_lb, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("   color: #2c3e50;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    background-color: #ecf0f1;\n"
"    text-align: center;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 3)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.test = QtWidgets.QPushButton(self.centralwidget)
        self.test.setObjectName("test")
        self.gridLayout.addWidget(self.test, 1, 0, 1, 1)
        CaseletWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CaseletWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.menuHost = QtWidgets.QMenu(self.menubar)
        self.menuHost.setObjectName("menuHost")
        self.menuBindings = QtWidgets.QMenu(self.menubar)
        self.menuBindings.setObjectName("menuBindings")
        self.menuLeft_Hand = QtWidgets.QMenu(self.menuBindings)
        self.menuLeft_Hand.setObjectName("menuLeft_Hand")
        self.menuLThumb = QtWidgets.QMenu(self.menuLeft_Hand)
        self.menuLThumb.setObjectName("menuLThumb")
        self.menuLPointer = QtWidgets.QMenu(self.menuLeft_Hand)
        self.menuLPointer.setObjectName("menuLPointer")
        self.menuLMIddle = QtWidgets.QMenu(self.menuLeft_Hand)
        self.menuLMIddle.setObjectName("menuLMIddle")
        self.menuLRing = QtWidgets.QMenu(self.menuLeft_Hand)
        self.menuLRing.setObjectName("menuLRing")
        self.menuLPinky = QtWidgets.QMenu(self.menuLeft_Hand)
        self.menuLPinky.setObjectName("menuLPinky")
        self.menuRight_Hand = QtWidgets.QMenu(self.menuBindings)
        self.menuRight_Hand.setObjectName("menuRight_Hand")
        self.menuThumb = QtWidgets.QMenu(self.menuRight_Hand)
        self.menuThumb.setObjectName("menuThumb")
        self.menuPointer = QtWidgets.QMenu(self.menuRight_Hand)
        self.menuPointer.setObjectName("menuPointer")
        self.menuMiddle = QtWidgets.QMenu(self.menuRight_Hand)
        self.menuMiddle.setObjectName("menuMiddle")
        self.menuRing = QtWidgets.QMenu(self.menuRight_Hand)
        self.menuRing.setObjectName("menuRing")
        self.menuPinky = QtWidgets.QMenu(self.menuRight_Hand)
        self.menuPinky.setObjectName("menuPinky")
        CaseletWindow.setMenuBar(self.menubar)
        self.actionTurtleSim = QtWidgets.QAction(CaseletWindow)
        self.actionTurtleSim.setCheckable(True)
        self.actionTurtleSim.setObjectName("actionTurtleSim")
        self.actionPiCarChu = QtWidgets.QAction(CaseletWindow)
        self.actionPiCarChu.setObjectName("actionPiCarChu")
        self.actionPlaceholder = QtWidgets.QAction(CaseletWindow)
        self.actionPlaceholder.setObjectName("actionPlaceholder")
        self.actionPlaceholder_2 = QtWidgets.QAction(CaseletWindow)
        self.actionPlaceholder_2.setObjectName("actionPlaceholder_2")
        self.actionLPlaceHolder = QtWidgets.QAction(CaseletWindow)
        self.actionLPlaceHolder.setObjectName("actionLPlaceHolder")
        self.actionPlaceHolder_2 = QtWidgets.QAction(CaseletWindow)
        self.actionPlaceHolder_2.setObjectName("actionPlaceHolder_2")
        self.actionPlaceholder_3 = QtWidgets.QAction(CaseletWindow)
        self.actionPlaceholder_3.setObjectName("actionPlaceholder_3")
        self.actionFingersUp = QtWidgets.QAction(CaseletWindow)
        self.actionFingersUp.setObjectName("actionFingersUp")
        self.actionPlaceholder_4 = QtWidgets.QAction(CaseletWindow)
        self.actionPlaceholder_4.setObjectName("actionPlaceholder_4")
        self.actionPlaceholder_5 = QtWidgets.QAction(CaseletWindow)
        self.actionPlaceholder_5.setObjectName("actionPlaceholder_5")
        self.actionPlaceholder_6 = QtWidgets.QAction(CaseletWindow)
        self.actionPlaceholder_6.setObjectName("actionPlaceholder_6")
        self.actionPlaceholder_7 = QtWidgets.QAction(CaseletWindow)
        self.actionPlaceholder_7.setObjectName("actionPlaceholder_7")
        self.actionPlaceholder_8 = QtWidgets.QAction(CaseletWindow)
        self.actionPlaceholder_8.setObjectName("actionPlaceholder_8")
        self.menuHost.addAction(self.actionTurtleSim)
        self.menuHost.addAction(self.actionPiCarChu)
        self.menuLThumb.addAction(self.actionPlaceholder)
        self.menuLPointer.addAction(self.actionPlaceholder_2)
        self.menuLMIddle.addAction(self.actionLPlaceHolder)
        self.menuLRing.addAction(self.actionPlaceHolder_2)
        self.menuLPinky.addAction(self.actionPlaceholder_3)
        self.menuLeft_Hand.addAction(self.menuLThumb.menuAction())
        self.menuLeft_Hand.addAction(self.menuLPointer.menuAction())
        self.menuLeft_Hand.addAction(self.menuLMIddle.menuAction())
        self.menuLeft_Hand.addAction(self.menuLRing.menuAction())
        self.menuLeft_Hand.addAction(self.menuLPinky.menuAction())
        self.menuThumb.addAction(self.actionPlaceholder_4)
        self.menuPointer.addAction(self.actionPlaceholder_5)
        self.menuMiddle.addAction(self.actionPlaceholder_6)
        self.menuRing.addAction(self.actionPlaceholder_7)
        self.menuPinky.addAction(self.actionPlaceholder_8)
        self.menuRight_Hand.addAction(self.menuThumb.menuAction())
        self.menuRight_Hand.addAction(self.menuPointer.menuAction())
        self.menuRight_Hand.addAction(self.menuMiddle.menuAction())
        self.menuRight_Hand.addAction(self.menuRing.menuAction())
        self.menuRight_Hand.addAction(self.menuPinky.menuAction())
        self.menuBindings.addAction(self.menuLeft_Hand.menuAction())
        self.menuBindings.addAction(self.menuRight_Hand.menuAction())
        self.menubar.addAction(self.menuHost.menuAction())
        self.menubar.addAction(self.menuBindings.menuAction())

        self.retranslateUi(CaseletWindow)
        QtCore.QMetaObject.connectSlotsByName(CaseletWindow)

    def retranslateUi(self, CaseletWindow):
        _translate = QtCore.QCoreApplication.translate
        CaseletWindow.setWindowTitle(_translate("CaseletWindow", "MainWindow"))
        self.label_14.setText(_translate("CaseletWindow", "M.A.N.O.S"))
        self.LeftHand_F4_Label.setText(_translate("CaseletWindow", "LHand_Function:"))
        self.LeftHand_F1_Label.setText(_translate("CaseletWindow", "LHand_Function:"))
        self.LeftHand_F3_Label.setText(_translate("CaseletWindow", "LHand_Function:"))
        self.LeftHand_F2_Label.setText(_translate("CaseletWindow", "LHand_Function:"))
        self.LeftHand_F5.setText(_translate("CaseletWindow", "LHand_Function:"))
        self.RightHand_F3_Label.setText(_translate("CaseletWindow", "RHand_Function"))
        self.RightHand_F1_Label.setText(_translate("CaseletWindow", "RHand_function"))
        self.RightHand_F2_Label.setText(_translate("CaseletWindow", "RHand_function"))
        self.RightHand_F4_Label.setText(_translate("CaseletWindow", "RHand_function"))
        self.RightHand_F5_Label.setText(_translate("CaseletWindow", "RHand_function"))
        self.camera_lb.setText(_translate("CaseletWindow", "VIDEOSTREAM /CAMERA/RAW"))
        self.test.setText(_translate("CaseletWindow", "PushButton"))
        self.menuHost.setTitle(_translate("CaseletWindow", "Host"))
        self.menuBindings.setTitle(_translate("CaseletWindow", "Bindings"))
        self.menuLeft_Hand.setTitle(_translate("CaseletWindow", "Left Hand"))
        self.menuLThumb.setTitle(_translate("CaseletWindow", "Thumb"))
        self.menuLPointer.setTitle(_translate("CaseletWindow", "Pointer"))
        self.menuLMIddle.setTitle(_translate("CaseletWindow", "MIddle"))
        self.menuLRing.setTitle(_translate("CaseletWindow", "Ring"))
        self.menuLPinky.setTitle(_translate("CaseletWindow", "Pinky"))
        self.menuRight_Hand.setTitle(_translate("CaseletWindow", "Right Hand"))
        self.menuThumb.setTitle(_translate("CaseletWindow", "Thumb"))
        self.menuPointer.setTitle(_translate("CaseletWindow", "Pointer"))
        self.menuMiddle.setTitle(_translate("CaseletWindow", "Middle"))
        self.menuRing.setTitle(_translate("CaseletWindow", "Ring"))
        self.menuPinky.setTitle(_translate("CaseletWindow", "Pinky"))
        self.actionTurtleSim.setText(_translate("CaseletWindow", "TurtleSim"))
        self.actionPiCarChu.setText(_translate("CaseletWindow", "PiCarChu"))
        self.actionPlaceholder.setText(_translate("CaseletWindow", "Placeholder"))
        self.actionPlaceholder_2.setText(_translate("CaseletWindow", "Placeholder"))
        self.actionLPlaceHolder.setText(_translate("CaseletWindow", "PlaceHolder"))
        self.actionPlaceHolder_2.setText(_translate("CaseletWindow", "PlaceHolder"))
        self.actionPlaceholder_3.setText(_translate("CaseletWindow", "Placeholder"))
        self.actionFingersUp.setText(_translate("CaseletWindow", "FingersUp"))
        self.actionPlaceholder_4.setText(_translate("CaseletWindow", "Placeholder"))
        self.actionPlaceholder_5.setText(_translate("CaseletWindow", "Placeholder"))
        self.actionPlaceholder_6.setText(_translate("CaseletWindow", "Placeholder"))
        self.actionPlaceholder_7.setText(_translate("CaseletWindow", "Placeholder"))
        self.actionPlaceholder_8.setText(_translate("CaseletWindow", "Placeholder"))
