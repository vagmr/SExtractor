# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\Porj\Python\SExtractor\ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 520)
        MainWindow.setMinimumSize(QtCore.QSize(640, 520))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.mainDirLabel = QtWidgets.QLabel(self.widget)
        self.mainDirLabel.setMaximumSize(QtCore.QSize(16777215, 100))
        self.mainDirLabel.setObjectName("mainDirLabel")
        self.horizontalLayout_7.addWidget(self.mainDirLabel)
        self.mainDirEdit = QtWidgets.QLineEdit(self.widget)
        self.mainDirEdit.setObjectName("mainDirEdit")
        self.horizontalLayout_7.addWidget(self.mainDirEdit)
        self.mainDirButton = QtWidgets.QPushButton(self.widget)
        self.mainDirButton.setObjectName("mainDirButton")
        self.horizontalLayout_7.addWidget(self.mainDirButton)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 65))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.engineNameBox = QtWidgets.QComboBox(self.widget_2)
        self.engineNameBox.setObjectName("engineNameBox")
        self.horizontalLayout_2.addWidget(self.engineNameBox)
        self.outputFileBox = QtWidgets.QComboBox(self.widget_2)
        self.outputFileBox.setObjectName("outputFileBox")
        self.horizontalLayout_2.addWidget(self.outputFileBox)
        self.outputPartBox = QtWidgets.QComboBox(self.widget_2)
        self.outputPartBox.setObjectName("outputPartBox")
        self.outputPartBox.addItem("")
        self.outputPartBox.addItem("")
        self.horizontalLayout_2.addWidget(self.outputPartBox)
        self.extractButton = QtWidgets.QPushButton(self.widget_2)
        self.extractButton.setObjectName("extractButton")
        self.horizontalLayout_2.addWidget(self.extractButton)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 2)
        self.verticalLayout.addWidget(self.widget_2)
        self.sampleLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sampleLabel.setFont(font)
        self.sampleLabel.setObjectName("sampleLabel")
        self.verticalLayout.addWidget(self.sampleLabel)
        self.sampleBrowser = QtWidgets.QTextEdit(self.tab)
        self.sampleBrowser.setObjectName("sampleBrowser")
        self.verticalLayout.addWidget(self.sampleBrowser)
        self.extraFuncTabs = QtWidgets.QTabWidget(self.tab)
        self.extraFuncTabs.setEnabled(True)
        self.extraFuncTabs.setMinimumSize(QtCore.QSize(0, 0))
        self.extraFuncTabs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.extraFuncTabs.setObjectName("extraFuncTabs")
        self.nameListTab = QtWidgets.QWidget()
        self.nameListTab.setEnabled(True)
        self.nameListTab.setObjectName("nameListTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.nameListTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.nameListEdit = QtWidgets.QLineEdit(self.nameListTab)
        self.nameListEdit.setEnabled(True)
        self.nameListEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.nameListEdit.setObjectName("nameListEdit")
        self.verticalLayout_4.addWidget(self.nameListEdit)
        self.extraFuncTabs.addTab(self.nameListTab, "")
        self.regNameTab = QtWidgets.QWidget()
        self.regNameTab.setObjectName("regNameTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.regNameTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.regNameBox = QtWidgets.QComboBox(self.regNameTab)
        self.regNameBox.setMinimumSize(QtCore.QSize(0, 30))
        self.regNameBox.setObjectName("regNameBox")
        self.verticalLayout_5.addWidget(self.regNameBox)
        self.extraFuncTabs.addTab(self.regNameTab, "")
        self.verticalLayout.addWidget(self.extraFuncTabs)
        self.widget_5 = QtWidgets.QWidget(self.tab)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cutOffCheck = QtWidgets.QCheckBox(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cutOffCheck.setFont(font)
        self.cutOffCheck.setChecked(True)
        self.cutOffCheck.setTristate(False)
        self.cutOffCheck.setObjectName("cutOffCheck")
        self.horizontalLayout_5.addWidget(self.cutOffCheck)
        self.outputFileExtraBox = QtWidgets.QComboBox(self.widget_5)
        self.outputFileExtraBox.setObjectName("outputFileExtraBox")
        self.horizontalLayout_5.addWidget(self.outputFileExtraBox)
        self.verticalLayout.addWidget(self.widget_5)
        self.verticalLayout.setStretch(3, 5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.tab_3)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.mergeDirLabel = QtWidgets.QLabel(self.widget_4)
        self.mergeDirLabel.setMaximumSize(QtCore.QSize(16777215, 100))
        self.mergeDirLabel.setObjectName("mergeDirLabel")
        self.horizontalLayout_8.addWidget(self.mergeDirLabel)
        self.mergeDirEdit = QtWidgets.QLineEdit(self.widget_4)
        self.mergeDirEdit.setObjectName("mergeDirEdit")
        self.horizontalLayout_8.addWidget(self.mergeDirEdit)
        self.mergeDirButton = QtWidgets.QPushButton(self.widget_4)
        self.mergeDirButton.setObjectName("mergeDirButton")
        self.horizontalLayout_8.addWidget(self.mergeDirButton)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.tab_3)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 65))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mergeFuncBox = QtWidgets.QComboBox(self.widget_3)
        self.mergeFuncBox.setObjectName("mergeFuncBox")
        self.mergeFuncBox.addItem("")
        self.mergeFuncBox.addItem("")
        self.horizontalLayout_3.addWidget(self.mergeFuncBox)
        self.mergeLineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.mergeLineEdit.setObjectName("mergeLineEdit")
        self.horizontalLayout_3.addWidget(self.mergeLineEdit)
        self.mergeButton = QtWidgets.QPushButton(self.widget_3)
        self.mergeButton.setObjectName("mergeButton")
        self.horizontalLayout_3.addWidget(self.mergeButton)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.widget_3)
        spacerItem = QtWidgets.QSpacerItem(20, 141, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.readmeBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.readmeBrowser.setObjectName("readmeBrowser")
        self.verticalLayout_3.addWidget(self.readmeBrowser)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.extraFuncTabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SExtractor"))
        self.mainDirLabel.setText(_translate("MainWindow", "工作目录"))
        self.mainDirButton.setText(_translate("MainWindow", " 选择文件夹 "))
        self.outputPartBox.setItemText(0, _translate("MainWindow", "单文档导出"))
        self.outputPartBox.setItemText(1, _translate("MainWindow", "多文档导出"))
        self.extractButton.setText(_translate("MainWindow", "提取/写入"))
        self.sampleLabel.setText(_translate("MainWindow", "引擎脚本示例"))
        self.extraFuncTabs.setTabText(self.extraFuncTabs.indexOf(self.nameListTab), _translate("MainWindow", "强制设定名字"))
        self.extraFuncTabs.setTabText(self.extraFuncTabs.indexOf(self.regNameTab), _translate("MainWindow", "选择匹配规则"))
        self.cutOffCheck.setText(_translate("MainWindow", "译文长度截断填充为原文长度(bin模式下)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "提取写入"))
        self.mergeDirLabel.setText(_translate("MainWindow", "工作目录"))
        self.mergeDirButton.setText(_translate("MainWindow", " 选择文件夹 "))
        self.mergeFuncBox.setItemText(0, _translate("MainWindow", "合并"))
        self.mergeFuncBox.setItemText(1, _translate("MainWindow", "分割"))
        self.mergeLineEdit.setText(_translate("MainWindow", "0"))
        self.mergeButton.setText(_translate("MainWindow", "开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "合并分割"))
        self.readmeBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">&gt;提取写入：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">输出原文：<span style=\" font-weight:600; color:#00aa00;\">transDic.output.json    </span><span style=\" font-weight:600; color:#000000;\">&gt;&gt;</span><span style=\" font-weight:600; color:#00aa00;\"> </span>输入译文：<span style=\" font-weight:600; color:#00aa00;\">transDic.json</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">输出原文：<span style=\" font-weight:600; color:#ffaa00;\">all.orig.json        </span><span style=\" font-weight:600; color:#000000;\">&gt;&gt; </span>输入译文：<span style=\" font-weight:600; color:#ffaa00;\">all.trans.json</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">&gt;&gt;正则匹配：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ffaa00;\">skip=</span><span style=\" color:#000000;\">表示跳过，</span><span style=\" font-weight:600; color:#ffaa00;\">search=</span><span style=\" color:#000000;\">表示搜索</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">匹配只处理命名分组</span><span style=\" font-weight:600; color:#00aa00;\">(</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14px; font-weight:600; color:#00aa00;\">?P&lt;组名&gt;</span><span style=\" font-weight:600; color:#00aa00;\">)</span><span style=\" color:#000000;\">：</span><span style=\" font-weight:600; color:#00aa00;\">name</span><span style=\" color:#000000;\">人名，</span><span style=\" font-weight:600; color:#00aa00;\">msg</span><span style=\" color:#000000;\">对话，</span><span style=\" font-weight:600; color:#00aa00;\">unfinish</span><span style=\" color:#000000;\">未结束对话（导出时与下一行合并）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">原文不要包含\\r\\n</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">json格式只会操作value，</span><span style=\" color:#ff0000;\">value为空会复制key到value</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">&gt;合并分割：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">合并时会缓存子文件信息，分割时<span style=\" font-weight:600; color:#00aa00;\">行数填0</span>则表示使用该缓存</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "说明"))
