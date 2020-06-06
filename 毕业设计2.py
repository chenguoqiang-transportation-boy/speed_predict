# -*- coding: utf-8 -*-
# @Time : 2020/2/7 10:56
# @Author : 番茄炒鸡蛋
import requests
import pandas as pd
import numpy as np
import os
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_absolute_error  # 平方绝对误差
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  QMainWindow,QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QSizePolicy, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from pylab import *
'''
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
界面代码
'''
#coordinate conversion
class Ui_Form_conversion(object):
    def setupUi(self, Form_conversion):
        Form_conversion.setObjectName("Form_conversion")
        Form_conversion.setEnabled(True)
        Form_conversion.resize(387, 373)
        self.groupBox = QtWidgets.QGroupBox(Form_conversion)
        self.groupBox.setGeometry(QtCore.QRect(20, 270, 251, 81))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 211, 48))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_ccoordinate = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_ccoordinate.setObjectName("lineEdit_ccoordinate")
        self.gridLayout_2.addWidget(self.lineEdit_ccoordinate, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form_conversion)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 10, 341, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 219, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_key = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_key.setText("")
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.horizontalLayout.addWidget(self.lineEdit_key)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 241, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 21, 221, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_ocoordinate = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ocoordinate.setObjectName("lineEdit_ocoordinate")
        self.gridLayout.addWidget(self.lineEdit_ocoordinate, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.comboBox_coordinatetype = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_coordinatetype.setObjectName("comboBox_coordinatetype")
        self.comboBox_coordinatetype.addItem("")
        self.comboBox_coordinatetype.addItem("")
        self.comboBox_coordinatetype.addItem("")
        self.gridLayout.addWidget(self.comboBox_coordinatetype, 1, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Form_conversion)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 200, 121, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_conversion = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_conversion.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton_conversion.setObjectName("pushButton_conversion")
        self.retranslateUi(Form_conversion)
        self.pushButton_conversion.clicked.connect(Form_conversion.conversion)
        QtCore.QMetaObject.connectSlotsByName(Form_conversion)
    def retranslateUi(self, Form_conversion):
        _translate = QtCore.QCoreApplication.translate
        Form_conversion.setWindowTitle(_translate("Form_conversion", "坐标转换"))
        self.groupBox.setTitle(_translate("Form_conversion", "输出模块"))
        self.label_5.setText(_translate("Form_conversion", "经纬度："))
        self.groupBox_3.setTitle(_translate("Form_conversion", "输入模块"))
        self.label.setText(_translate("Form_conversion", "密钥（key）："))
        self.groupBox_2.setTitle(_translate("Form_conversion", "原坐标"))
        self.label_2.setText(_translate("Form_conversion", "经纬度："))
        self.label_4.setText(_translate("Form_conversion", "坐标系类型："))
        self.comboBox_coordinatetype.setItemText(0, _translate("Form_conversion", "gps"))
        self.comboBox_coordinatetype.setItemText(1, _translate("Form_conversion", "baidu"))
        self.comboBox_coordinatetype.setItemText(2, _translate("Form_conversion", "mapbar"))
        self.groupBox_4.setTitle(_translate("Form_conversion", "执行模块"))
        self.pushButton_conversion.setText(_translate("Form_conversion", "转换"))
#dataprocessing
class Ui_Form_dataprocessing(object):
    def setupUi(self, Form_dataprocessing):
        Form_dataprocessing.setObjectName("Form_dataprocessing")
        Form_dataprocessing.setEnabled(True)
        Form_dataprocessing.resize(619, 277)
        self.groupBox = QtWidgets.QGroupBox(Form_dataprocessing)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 291, 171))
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 60, 54, 12))
        self.label_4.setObjectName("label_4")
        self.lineEdit_starttime = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_starttime.setGeometry(QtCore.QRect(120, 60, 131, 20))
        self.lineEdit_starttime.setObjectName("lineEdit_starttime")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(31, 31, 60, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_crawltime4 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_crawltime4.setGeometry(QtCore.QRect(121, 31, 62, 20))
        self.comboBox_crawltime4.setObjectName("comboBox_crawltime4")
        self.comboBox_crawltime4.addItem("")
        self.comboBox_crawltime4.addItem("")
        self.comboBox_crawltime4.addItem("")
        self.comboBox_crawltime4.addItem("")
        self.comboBox_crawltime4.addItem("")
        self.comboBox_crawltime4.addItem("")
        self.comboBox_crawltime4.addItem("")
        self.comboBox_crawltime4.addItem("")
        self.comboBox_crawltime4.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 100, 60, 16))
        self.label.setObjectName("label")
        self.comboBox_targettype = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_targettype.setGeometry(QtCore.QRect(120, 100, 146, 20))
        self.comboBox_targettype.setObjectName("comboBox_targettype")
        self.comboBox_targettype.addItem("")
        self.comboBox_targettype.addItem("")
        self.comboBox_targettype.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 135, 84, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_targetroad = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_targetroad.setGeometry(QtCore.QRect(120, 135, 133, 20))
        self.lineEdit_targetroad.setObjectName("lineEdit_targetroad")
        self.groupBox_2 = QtWidgets.QGroupBox(Form_dataprocessing)
        self.groupBox_2.setGeometry(QtCore.QRect(80, 200, 120, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_3 = QtWidgets.QGroupBox(Form_dataprocessing)
        self.groupBox_3.setGeometry(QtCore.QRect(310, 10, 291, 261))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit_progressbar1 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_progressbar1.setGeometry(QtCore.QRect(20, 60, 251, 71))
        self.textEdit_progressbar1.setObjectName("textEdit_progressbar1")
        self.textEdit_progressbar2 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_progressbar2.setGeometry(QtCore.QRect(20, 170, 251, 71))
        self.textEdit_progressbar2.setObjectName("textEdit_progressbar2")
        self.widget = QtWidgets.QWidget(self.groupBox_3)
        self.widget.setGeometry(QtCore.QRect(20, 30, 251, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.progressBar_dataprocessing1 = QtWidgets.QProgressBar(self.widget)
        self.progressBar_dataprocessing1.setProperty("value", 0)
        self.progressBar_dataprocessing1.setObjectName("progressBar_dataprocessing1")
        self.horizontalLayout.addWidget(self.progressBar_dataprocessing1)
        self.widget1 = QtWidgets.QWidget(self.groupBox_3)
        self.widget1.setGeometry(QtCore.QRect(20, 140, 251, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.progressBar_dataprocessing2 = QtWidgets.QProgressBar(self.widget1)
        self.progressBar_dataprocessing2.setProperty("value", 0)
        self.progressBar_dataprocessing2.setObjectName("progressBar_dataprocessing2")
        self.horizontalLayout_2.addWidget(self.progressBar_dataprocessing2)
        self.retranslateUi(Form_dataprocessing)
        self.pushButton.clicked.connect(Form_dataprocessing.dataprocessing)
        QtCore.QMetaObject.connectSlotsByName(Form_dataprocessing)
    def retranslateUi(self, Form_dataprocessing):
        _translate = QtCore.QCoreApplication.translate
        Form_dataprocessing.setWindowTitle(_translate("Form_dataprocessing", "数据处理"))
        self.groupBox.setTitle(_translate("Form_dataprocessing", "输入模块"))
        self.label_4.setText(_translate("Form_dataprocessing", "开始时间："))
        self.lineEdit_starttime.setText(_translate("Form_dataprocessing", "2019-12-21"))
        self.label_3.setText(_translate("Form_dataprocessing", "爬取时间："))
        self.comboBox_crawltime4.setItemText(0, _translate("Form_dataprocessing", "1小时"))
        self.comboBox_crawltime4.setItemText(1, _translate("Form_dataprocessing", "17小时"))
        self.comboBox_crawltime4.setItemText(2, _translate("Form_dataprocessing", "1天"))
        self.comboBox_crawltime4.setItemText(3, _translate("Form_dataprocessing", "1周"))
        self.comboBox_crawltime4.setItemText(4, _translate("Form_dataprocessing", "3周"))
        self.comboBox_crawltime4.setItemText(5, _translate("Form_dataprocessing", "1个月"))
        self.comboBox_crawltime4.setItemText(6, _translate("Form_dataprocessing", "半年"))
        self.comboBox_crawltime4.setItemText(7, _translate("Form_dataprocessing", "1年"))
        self.comboBox_crawltime4.setItemText(8, _translate("Form_dataprocessing", "2年"))
        self.label.setText(_translate("Form_dataprocessing", "数据类型："))
        self.comboBox_targettype.setItemText(0, _translate("Form_dataprocessing", "长方形爬虫数据结果"))
        self.comboBox_targettype.setItemText(1, _translate("Form_dataprocessing", "正方形爬虫数据结果"))
        self.comboBox_targettype.setItemText(2, _translate("Form_dataprocessing", "指定线路爬虫数据结果"))
        self.label_2.setText(_translate("Form_dataprocessing", "指定目标路段："))
        self.groupBox_2.setTitle(_translate("Form_dataprocessing", "执行模块"))
        self.pushButton.setText(_translate("Form_dataprocessing", "运行"))
        self.groupBox_3.setTitle(_translate("Form_dataprocessing", "运行过程可视化"))
        self.label_5.setText(_translate("Form_dataprocessing", "提取指定路段："))
        self.label_6.setText(_translate("Form_dataprocessing", "形成时间序列："))
#images
class Ui_Form_images(object):
    def setupUi(self, Form_images):
        Form_images.setObjectName("Form_images")
        Form_images.resize(690, 512)
        self.tabWidget = QtWidgets.QTabWidget(Form_images)
        self.tabWidget.setGeometry(QtCore.QRect(-4, -1, 691, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_rectangle = QtWidgets.QWidget()
        self.tab_rectangle.setObjectName("tab_rectangle")
        self.label_rectangle = QtWidgets.QLabel(self.tab_rectangle)
        self.label_rectangle.setGeometry(QtCore.QRect(10, 10, 671, 471))
        self.label_rectangle.setText("")
        self.label_rectangle.setObjectName("label_rectangle")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_rectangle)
        self.textBrowser_2.setGeometry(QtCore.QRect(510, 100, 171, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab_rectangle, "")
        self.tab_square = QtWidgets.QWidget()
        self.tab_square.setObjectName("tab_square")
        self.label_square = QtWidgets.QLabel(self.tab_square)
        self.label_square.setGeometry(QtCore.QRect(10, 0, 671, 471))
        self.label_square.setText("")
        self.label_square.setObjectName("label_square")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_square)
        self.textBrowser.setGeometry(QtCore.QRect(510, 120, 171, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_square, "")
        self.tab_road = QtWidgets.QWidget()
        self.tab_road.setObjectName("tab_road")
        self.label_road = QtWidgets.QLabel(self.tab_road)
        self.label_road.setGeometry(QtCore.QRect(10, 10, 671, 471))
        self.label_road.setText("")
        self.label_road.setObjectName("label_road")
        self.label = QtWidgets.QLabel(self.tab_road)
        self.label.setGeometry(QtCore.QRect(30, 10, 381, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_road, "")

        self.retranslateUi(Form_images)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_images)

    def retranslateUi(self, Form_images):
        _translate = QtCore.QCoreApplication.translate
        Form_images.setWindowTitle(_translate("Form_images", "查看详情——区域形式"))
        self.textBrowser_2.setHtml(_translate("Form_images", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">  由于矩形对角线不能超过10公里，所以通过拼接矩形的方法，扩大爬取数据范围，长方形示例如下图方形框内的数据。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rectangle), _translate("Form_images", "长方形"))
        self.textBrowser.setHtml(_translate("Form_images", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">  由于矩形对角线不能超过10公里，所以通过拼接矩形的方法，扩大爬取数据范围，正方形示例如下图方形框内的数据。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_square), _translate("Form_images", "正方形"))
        self.label.setText(_translate("Form_images", "指定线路的示例如下图的红色路段："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_road), _translate("Form_images", "指定线路"))
#mainwindow
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 261, 111))
        self.groupBox.setObjectName("groupBox")
        self.label_gdgw = QtWidgets.QLabel(self.groupBox)
        self.label_gdgw.setGeometry(QtCore.QRect(11, 21, 168, 16))
        self.label_gdgw.setObjectName("label_gdgw")
        self.label_gdcoordinate = QtWidgets.QLabel(self.groupBox)
        self.label_gdcoordinate.setGeometry(QtCore.QRect(11, 53, 120, 16))
        self.label_gdcoordinate.setObjectName("label_gdcoordinate")
        self.label_xingzheng = QtWidgets.QLabel(self.groupBox)
        self.label_xingzheng.setGeometry(QtCore.QRect(11, 84, 120, 16))
        self.label_xingzheng.setObjectName("label_xingzheng")
        self.pushButton_coordinateconversion = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_coordinateconversion.setGeometry(QtCore.QRect(140, 80, 111, 23))
        self.pushButton_coordinateconversion.setObjectName("pushButton_coordinateconversion")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 170, 241, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 91, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_rectangle = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_rectangle.setObjectName("pushButton_rectangle")
        self.verticalLayout.addWidget(self.pushButton_rectangle)
        self.pushButton_square = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_square.setObjectName("pushButton_square")
        self.verticalLayout.addWidget(self.pushButton_square)
        self.pushButton_road = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_road.setObjectName("pushButton_road")
        self.verticalLayout.addWidget(self.pushButton_road)
        self.pushButton_images = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_images.setGeometry(QtCore.QRect(140, 60, 75, 23))
        self.pushButton_images.setObjectName("pushButton_images")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(310, 40, 141, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_dataprocessing = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_dataprocessing.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.pushButton_dataprocessing.setObjectName("pushButton_dataprocessing")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(310, 160, 141, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_predict = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_predict.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.pushButton_predict.setObjectName("pushButton_predict")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 20, 20, 321))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 150, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 330, 451, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(460, 20, 20, 321))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(300, 110, 171, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(300, 240, 171, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(10, 20, 20, 321))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(20, 10, 451, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label_gdgw.setOpenExternalLinks(True)
        self.label_gdcoordinate.setOpenExternalLinks(True)
        self.label_xingzheng.setOpenExternalLinks(True)


        self.retranslateUi(MainWindow)
        self.pushButton_coordinateconversion.clicked.connect(MainWindow.coordinatechange)
        self.pushButton_rectangle.clicked.connect(MainWindow.rectangleclick)
        self.pushButton_square.clicked.connect(MainWindow.squareclick)
        self.pushButton_road.clicked.connect(MainWindow.roadclick)
        self.pushButton_images.clicked.connect(MainWindow.imageclick)
        self.pushButton_dataprocessing.clicked.connect(MainWindow.dataprocessing)
        self.pushButton_predict.clicked.connect(MainWindow.predict)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主窗口——陈国强作品"))
        self.groupBox.setTitle(_translate("MainWindow", "模块1：模块2相关参数参考资料"))
        self.label_gdgw.setText(_translate("MainWindow", "<A href='https://lbs.amap.com/api/webservice/guide/api/trafficstatus/'>高德地图交通态势开发指南官网</a>"))
        self.label_gdcoordinate.setText(_translate("MainWindow", "<A href='https://lbs.amap.com/console/show/picker'>高德地图拾取坐标系统</a>"))
        self.label_xingzheng.setText(_translate("MainWindow", "<A href='xingzheng.html'>行政区域坐标拾取系统</a>"))
        self.pushButton_coordinateconversion.setText(_translate("MainWindow", "坐标转换"))
        self.groupBox_2.setTitle(_translate("MainWindow", "模块2：自动生成爬虫代码"))
        self.pushButton_rectangle.setText(_translate("MainWindow", "长方形区域"))
        self.pushButton_square.setText(_translate("MainWindow", "正方形区域"))
        self.pushButton_road.setText(_translate("MainWindow", "指定路线"))
        self.pushButton_images.setText(_translate("MainWindow", "查看详情"))
        self.groupBox_3.setTitle(_translate("MainWindow", "模块3：数据处理"))
        self.pushButton_dataprocessing.setText(_translate("MainWindow", "数据处理"))
        self.groupBox_4.setTitle(_translate("MainWindow", "模块4：数据预测"))
        self.pushButton_predict.setText(_translate("MainWindow", "数据预测"))
        self.pushButton.setText(_translate("MainWindow", "关闭"))
#predict
class Ui_Form_predict(object):
    def setupUi(self, Form_predict):
        Form_predict.setObjectName("Form_predict")
        Form_predict.resize(1226, 615)
        self.scrollArea = QtWidgets.QScrollArea(Form_predict)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 1181, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -466, 1162, 1701))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(700, 1701))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(860, 90, 261, 16))
        self.label.setObjectName("label")
        self.groupBox_correlation = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_correlation.setGeometry(QtCore.QRect(10, 40, 801, 531))
        self.groupBox_correlation.setObjectName("groupBox_correlation")
        self.matplotlibwidget_correlation = MatplotlibWidget(self.groupBox_correlation)
        self.matplotlibwidget_correlation.setGeometry(QtCore.QRect(10, 20, 771, 471))
        self.matplotlibwidget_correlation.setObjectName("matplotlibwidget_correlation")
        self.pushButton_correlation = QtWidgets.QPushButton(self.groupBox_correlation)
        self.pushButton_correlation.setGeometry(QtCore.QRect(360, 500, 81, 23))
        self.pushButton_correlation.setObjectName("pushButton_correlation")
        self.groupBox_arima = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_arima.setGeometry(QtCore.QRect(10, 590, 801, 531))
        self.groupBox_arima.setObjectName("groupBox_arima")
        self.matplotlibwidget_arimapre = MatplotlibWidget(self.groupBox_arima)
        self.matplotlibwidget_arimapre.setGeometry(QtCore.QRect(10, 20, 771, 471))
        self.matplotlibwidget_arimapre.setObjectName("matplotlibwidget_arimapre")
        self.pushButton_arimapre = QtWidgets.QPushButton(self.groupBox_arima)
        self.pushButton_arimapre.setGeometry(QtCore.QRect(360, 500, 81, 23))
        self.pushButton_arimapre.setObjectName("pushButton_arimapre")
        self.pushButton_arimapre.raise_()
        self.matplotlibwidget_arimapre.raise_()
        self.textEdit_arima = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_arima.setGeometry(QtCore.QRect(830, 800, 321, 201))
        self.textEdit_arima.setObjectName("textEdit_arima")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(840, 160, 291, 111))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 241, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_datavolume = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_datavolume.setObjectName("comboBox_datavolume")
        self.comboBox_datavolume.addItem("")
        self.comboBox_datavolume.addItem("")
        self.comboBox_datavolume.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_datavolume)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 70, 261, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_targetroad = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_targetroad.setObjectName("lineEdit_targetroad")
        self.horizontalLayout_2.addWidget(self.lineEdit_targetroad)
        self.progressBar_arima = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar_arima.setGeometry(QtCore.QRect(900, 740, 211, 23))
        self.progressBar_arima.setProperty("value", 0)
        self.progressBar_arima.setObjectName("progressBar_arima")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form_predict)
        self.pushButton_correlation.clicked.connect(Form_predict.correlation)
        self.pushButton_arimapre.clicked.connect(Form_predict.arimaclick)
        QtCore.QMetaObject.connectSlotsByName(Form_predict)

    def retranslateUi(self, Form_predict):
        _translate = QtCore.QCoreApplication.translate
        Form_predict.setWindowTitle(_translate("Form_predict", "数据预测"))
        self.label.setText(_translate("Form_predict", "注意：数据预测功能的实现需要1周以上的数据量"))
        self.groupBox_correlation.setTitle(_translate("Form_predict", "工作日、休息日相关性可视化"))
        self.pushButton_correlation.setText(_translate("Form_predict", "相关性可视化"))
        self.groupBox_arima.setTitle(_translate("Form_predict", "ARIMA预测"))
        self.pushButton_arimapre.setText(_translate("Form_predict", "预测"))
        self.textEdit_arima.setHtml(_translate("Form_predict", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">预测过程：</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Form_predict", "数据输入"))
        self.label_2.setText(_translate("Form_predict", "数据量："))
        self.comboBox_datavolume.setItemText(0, _translate("Form_predict", "1周"))
        self.comboBox_datavolume.setItemText(1, _translate("Form_predict", "3周"))
        self.comboBox_datavolume.setItemText(2, _translate("Form_predict", "1个月"))
        self.label_4.setText(_translate("Form_predict", "指定目标路段："))
#rectangle createcode
class Ui_Form_rectangle(object):
    def setupUi(self, Form_rectangle):
        Form_rectangle.setObjectName("Form_rectangle")
        Form_rectangle.resize(311, 225)
        self.button_code = QtWidgets.QPushButton(Form_rectangle)
        self.button_code.setGeometry(QtCore.QRect(120, 180, 75, 23))
        self.button_code.setObjectName("button_code")
        self.layoutWidget_2 = QtWidgets.QWidget(Form_rectangle)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 20, 181, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_crawltime1 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_crawltime1.setObjectName("comboBox_crawltime1")
        self.comboBox_crawltime1.addItem("")
        self.comboBox_crawltime1.addItem("")
        self.comboBox_crawltime1.addItem("")
        self.comboBox_crawltime1.addItem("")
        self.comboBox_crawltime1.addItem("")
        self.comboBox_crawltime1.addItem("")
        self.comboBox_crawltime1.addItem("")
        self.comboBox_crawltime1.addItem("")
        self.comboBox_crawltime1.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_crawltime1)
        self.layoutWidget = QtWidgets.QWidget(Form_rectangle)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 231, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_baselat = QtWidgets.QLabel(self.layoutWidget)
        self.label_baselat.setObjectName("label_baselat")
        self.gridLayout.addWidget(self.label_baselat, 2, 0, 1, 1)
        self.label_key = QtWidgets.QLabel(self.layoutWidget)
        self.label_key.setObjectName("label_key")
        self.gridLayout.addWidget(self.label_key, 0, 0, 1, 1)
        self.lineEdit_baselat = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_baselat.setObjectName("lineEdit_baselat")
        self.gridLayout.addWidget(self.lineEdit_baselat, 2, 1, 1, 1)
        self.lineEdit_key = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.gridLayout.addWidget(self.lineEdit_key, 0, 1, 1, 1)
        self.label_baselng = QtWidgets.QLabel(self.layoutWidget)
        self.label_baselng.setObjectName("label_baselng")
        self.gridLayout.addWidget(self.label_baselng, 1, 0, 1, 1)
        self.lineEdit_baselng = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_baselng.setObjectName("lineEdit_baselng")
        self.gridLayout.addWidget(self.lineEdit_baselng, 1, 1, 1, 1)

        self.retranslateUi(Form_rectangle)
        self.button_code.clicked.connect(Form_rectangle.createcode)
        QtCore.QMetaObject.connectSlotsByName(Form_rectangle)

    def retranslateUi(self, Form_rectangle):
        _translate = QtCore.QCoreApplication.translate
        Form_rectangle.setWindowTitle(_translate("Form_rectangle", "矩形代码生成"))
        self.button_code.setText(_translate("Form_rectangle", "生成代码"))
        self.label_2.setText(_translate("Form_rectangle", "爬取时间："))
        self.comboBox_crawltime1.setItemText(0, _translate("Form_rectangle", "1小时"))
        self.comboBox_crawltime1.setItemText(1, _translate("Form_rectangle", "17小时"))
        self.comboBox_crawltime1.setItemText(2, _translate("Form_rectangle", "1天"))
        self.comboBox_crawltime1.setItemText(3, _translate("Form_rectangle", "1周"))
        self.comboBox_crawltime1.setItemText(4, _translate("Form_rectangle", "3周"))
        self.comboBox_crawltime1.setItemText(5, _translate("Form_rectangle", "1个月"))
        self.comboBox_crawltime1.setItemText(6, _translate("Form_rectangle", "半年"))
        self.comboBox_crawltime1.setItemText(7, _translate("Form_rectangle", "1年"))
        self.comboBox_crawltime1.setItemText(8, _translate("Form_rectangle", "2年"))
        self.label_baselat.setText(_translate("Form_rectangle", "纬度："))
        self.label_key.setText(_translate("Form_rectangle", "密钥："))
        self.label_baselng.setText(_translate("Form_rectangle", "经度："))
#road createcode
class Ui_Form_road(object):
    def setupUi(self, Form_road):
        Form_road.setObjectName("Form_road")
        Form_road.resize(270, 243)
        self.button_code = QtWidgets.QPushButton(Form_road)
        self.button_code.setGeometry(QtCore.QRect(90, 210, 75, 23))
        self.button_code.setObjectName("button_code")
        self.layoutWidget = QtWidgets.QWidget(Form_road)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 241, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_key = QtWidgets.QLabel(self.layoutWidget)
        self.label_key.setObjectName("label_key")
        self.gridLayout.addWidget(self.label_key, 0, 0, 1, 1)
        self.lineEdit_key = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.gridLayout.addWidget(self.lineEdit_key, 0, 1, 1, 1)
        self.label_cityname = QtWidgets.QLabel(self.layoutWidget)
        self.label_cityname.setObjectName("label_cityname")
        self.gridLayout.addWidget(self.label_cityname, 1, 0, 1, 1)
        self.lineEdit_cityname = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_cityname.setObjectName("lineEdit_cityname")
        self.gridLayout.addWidget(self.lineEdit_cityname, 1, 1, 1, 1)
        self.label_roadname = QtWidgets.QLabel(self.layoutWidget)
        self.label_roadname.setObjectName("label_roadname")
        self.gridLayout.addWidget(self.label_roadname, 2, 0, 1, 1)
        self.lineEdit_roadname = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_roadname.setObjectName("lineEdit_roadname")
        self.gridLayout.addWidget(self.lineEdit_roadname, 2, 1, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(Form_road)
        self.layoutWidget_2.setGeometry(QtCore.QRect(50, 20, 181, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_crawltime3 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_crawltime3.setObjectName("comboBox_crawltime3")
        self.comboBox_crawltime3.addItem("")
        self.comboBox_crawltime3.addItem("")
        self.comboBox_crawltime3.addItem("")
        self.comboBox_crawltime3.addItem("")
        self.comboBox_crawltime3.addItem("")
        self.comboBox_crawltime3.addItem("")
        self.comboBox_crawltime3.addItem("")
        self.comboBox_crawltime3.addItem("")
        self.comboBox_crawltime3.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_crawltime3)

        self.retranslateUi(Form_road)
        self.button_code.clicked.connect(Form_road.createcode)
        QtCore.QMetaObject.connectSlotsByName(Form_road)

    def retranslateUi(self, Form_road):
        _translate = QtCore.QCoreApplication.translate
        Form_road.setWindowTitle(_translate("Form_road", "指定线路代码生成"))
        self.button_code.setText(_translate("Form_road", "生成代码"))
        self.label_key.setText(_translate("Form_road", "密钥："))
        self.label_cityname.setText(_translate("Form_road", "城市："))
        self.label_roadname.setText(_translate("Form_road", "路段名称："))
        self.label.setText(_translate("Form_road", "爬取时间："))
        self.comboBox_crawltime3.setItemText(0, _translate("Form_road", "1小时"))
        self.comboBox_crawltime3.setItemText(1, _translate("Form_road", "17小时"))
        self.comboBox_crawltime3.setItemText(2, _translate("Form_road", "1天"))
        self.comboBox_crawltime3.setItemText(3, _translate("Form_road", "1周"))
        self.comboBox_crawltime3.setItemText(4, _translate("Form_road", "3周"))
        self.comboBox_crawltime3.setItemText(5, _translate("Form_road", "1个月"))
        self.comboBox_crawltime3.setItemText(6, _translate("Form_road", "半年"))
        self.comboBox_crawltime3.setItemText(7, _translate("Form_road", "1年"))
        self.comboBox_crawltime3.setItemText(8, _translate("Form_road", "2年"))
#square createcode
class Ui_Form_square(object):
    def setupUi(self, Form_square):
        Form_square.setObjectName("Form_square")
        Form_square.resize(311, 258)
        self.button_code = QtWidgets.QPushButton(Form_square)
        self.button_code.setGeometry(QtCore.QRect(110, 210, 75, 23))
        self.button_code.setObjectName("button_code")
        self.layoutWidget_2 = QtWidgets.QWidget(Form_square)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 20, 181, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_crawltime2 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_crawltime2.setObjectName("comboBox_crawltime2")
        self.comboBox_crawltime2.addItem("")
        self.comboBox_crawltime2.addItem("")
        self.comboBox_crawltime2.addItem("")
        self.comboBox_crawltime2.addItem("")
        self.comboBox_crawltime2.addItem("")
        self.comboBox_crawltime2.addItem("")
        self.comboBox_crawltime2.addItem("")
        self.comboBox_crawltime2.addItem("")
        self.comboBox_crawltime2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_crawltime2)
        self.layoutWidget = QtWidgets.QWidget(Form_square)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 70, 231, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_baselat = QtWidgets.QLabel(self.layoutWidget)
        self.label_baselat.setObjectName("label_baselat")
        self.gridLayout.addWidget(self.label_baselat, 2, 0, 1, 1)
        self.label_key = QtWidgets.QLabel(self.layoutWidget)
        self.label_key.setObjectName("label_key")
        self.gridLayout.addWidget(self.label_key, 0, 0, 1, 1)
        self.lineEdit_baselat = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_baselat.setObjectName("lineEdit_baselat")
        self.gridLayout.addWidget(self.lineEdit_baselat, 2, 1, 1, 1)
        self.lineEdit_key = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.gridLayout.addWidget(self.lineEdit_key, 0, 1, 1, 1)
        self.label_baselng = QtWidgets.QLabel(self.layoutWidget)
        self.label_baselng.setObjectName("label_baselng")
        self.gridLayout.addWidget(self.label_baselng, 1, 0, 1, 1)
        self.lineEdit_baselng = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_baselng.setObjectName("lineEdit_baselng")
        self.gridLayout.addWidget(self.lineEdit_baselng, 1, 1, 1, 1)

        self.retranslateUi(Form_square)
        self.button_code.clicked.connect(Form_square.createcode)
        QtCore.QMetaObject.connectSlotsByName(Form_square)

    def retranslateUi(self, Form_square):
        _translate = QtCore.QCoreApplication.translate
        Form_square.setWindowTitle(_translate("Form_square", "正方形代码生成"))
        self.button_code.setText(_translate("Form_square", "生成代码"))
        self.label_2.setText(_translate("Form_square", "爬取时间："))
        self.comboBox_crawltime2.setItemText(0, _translate("Form_square", "1小时"))
        self.comboBox_crawltime2.setItemText(1, _translate("Form_square", "17小时"))
        self.comboBox_crawltime2.setItemText(2, _translate("Form_square", "1天"))
        self.comboBox_crawltime2.setItemText(3, _translate("Form_square", "1周"))
        self.comboBox_crawltime2.setItemText(4, _translate("Form_square", "3周"))
        self.comboBox_crawltime2.setItemText(5, _translate("Form_square", "1个月"))
        self.comboBox_crawltime2.setItemText(6, _translate("Form_square", "半年"))
        self.comboBox_crawltime2.setItemText(7, _translate("Form_square", "1年"))
        self.comboBox_crawltime2.setItemText(8, _translate("Form_square", "2年"))
        self.label_baselat.setText(_translate("Form_square", "纬度："))
        self.label_key.setText(_translate("Form_square", "密钥："))
        self.label_baselng.setText(_translate("Form_square", "经度："))
#dialog information   已删除，用QMessage替换
#如果想使用户体验感再好一点，可以选择将information放在“数据处理结尾处”和“arima预测结尾处，正在绘图”，未考虑运行速度，本代码未加入
#matplotlib widget
class MyMplCanvas(FigureCanvas):
    def __init__(self,parent=None,width=6,height=5,dpi=100):
        #设置中文显示
        plt.rcParams['font.family']=['SimHei']#用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False#用来正常显示负号
        #新建一个绘图对象
        self.fig=Figure(figsize=(width,height),dpi=dpi)
        #建立一个子图，如果要建立复合图，可以在这里修改
        self.axes=self.fig.add_subplot(111)
        FigureCanvas.__init__(self,self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，意思是设置FigureCanvas，使之尽可能向外填充空间'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
    '''绘制静态图，可以在这里定义自己的绘图逻辑'''

    def start_correlation_plot(self,weekdayline,weekendline):
        self.axes.plot(weekdayline, label=r'工作日', linestyle='-')  # 有无u都无所谓#
        self.axes.plot(weekendline, label=r'休息日', linestyle='--')  # 有无u都无所谓
        self.axes.set_xlabel('时间', fontproperties='SimHei', fontsize=10)
        self.axes.set_ylabel('车速', fontproperties='SimHei', fontsize=10)
        self.axes.set_title(r'休息日、工作日平均速度相关性可视化比较', fontproperties='SimHei', fontsize=12)
        self.axes.grid(True)  # 加入栅栏，缓和曲线，网格
        self.axes.legend(loc='best')

    def start_arima_plot(self,pred_arima,test,MAE_arima):
        self.axes.plot(pred_arima,label='预测值', linestyle='-')
        self.axes.plot(test,label='实际值', linestyle='--')
        self.axes.set_xlabel('时间', fontproperties='SimHei', fontsize=10)
        self.axes.set_ylabel('车速', fontproperties='SimHei', fontsize=10)
        self.axes.set_title('ARIMA模型预测结果的MAE: %.4f' % MAE_arima, fontproperties='SimHei', fontsize=12)
        self.axes.grid(True)  # 加入栅栏，缓和曲线，网格
        self.axes.legend(loc='best')

    def start_ann_plot(self,pred_ann,test,MAE_ann):
        self.axes.plot(pred_ann,label='预测值', linestyle='-')
        self.axes.plot(test,label='实际值', linestyle='--')
        self.axes.set_xlabel('时间', fontproperties='SimHei', fontsize=10)
        self.axes.set_ylabel('车速', fontproperties='SimHei', fontsize=10)
        self.axes.set_title('简单神经网络预测结果的MAE: %.4f' % MAE_ann, fontproperties='SimHei', fontsize=12)
        self.axes.grid(True)  # 加入栅栏，缓和曲线，网格
        self.axes.legend(loc='best')
class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout=QVBoxLayout(self)
        self.mpl=MyMplCanvas(self,width=6,height=5,dpi=100)
        '''下面两个绘图函数放在if name中和initUi中要过是一样的，区别在于：放在if name中不ui。show，但放在initUi，需要ui.show()，考虑简便性，将其放在initUi中'''
        #self.mpl.start_correlation_plot()# 测试静态图效果
        self.mpl_ntb=NavigationToolbar(self.mpl,self)#添加完整的工具栏

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)
'''
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
逻辑代码
'''
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.child_conversion = ChildForm_conversion()
        self.child_rectangle = ChildForm_rectangle()
        self.child_square = ChildForm_square()
        self.child_road = ChildForm_road()
        self.child_images = ChildForm_images()
        self.child_dataprocessing = ChildForm_dataprocessing()
        self.child_predict = ChildForm_predict()
    def coordinatechange(self):
        self.child_conversion.show()
    def rectangleclick(self):
        self.child_rectangle.show()
    def squareclick(self):
        self.child_square.show()
    def roadclick(self):
        self.child_road.show()
    def imageclick(self):
        self.child_images.show()
    def dataprocessing(self):
        self.child_dataprocessing.show()
    def predict(self):
        self.child_predict.show()

class ChildForm_conversion(QWidget,Ui_Form_conversion):
    def __init__(self):
        super(ChildForm_conversion, self).__init__()
        self.setupUi(self)

    def conversion(self):
        key = self.lineEdit_key.text()
        ocoordinate=self.lineEdit_ocoordinate.text()
        coordinatetype=self.comboBox_coordinatetype.currentText()

        rep = requests.get('http://restapi.amap.com/v3/assistant/coordinate/convert?key=' + key + '&locations=' + ocoordinate + '&coordsys=' + coordinatetype)
        rep.encoding = 'utf-8'
        print(rep.json())

        locations = rep.json()['locations']
        locations=eval(locations)#将str变为tuple，便于分出“逗号”前后的经纬度
        location1=round(locations[0],6)#让坐标保留至小数点后6位
        location2=round(locations[1],6)
        locations=str(location1) + ',' +str(location2)
        self.lineEdit_ccoordinate.setText(locations)
        QMessageBox.information(self,"提示","转换完成！",QMessageBox.Yes | QMessageBox.No)

class ChildForm_rectangle(QWidget,Ui_Form_rectangle):
    def __init__(self):
        super(ChildForm_rectangle, self).__init__()
        self.setupUi(self)

    def changetext(self,a1,a2,a3,a4,b1,b2,b3,b4):
        with open('crawl_rectangle.py', 'r', encoding='utf-8') as f1:
            lines = []  # 创建了一个空列表，里面没有元素
            for line in f1.readlines():
                if line != '\n':
                    lines.append(line)
            f1.close()
        with open('crawl_rectangle.py', 'w', encoding='utf-8') as f2:
            for line in lines:
                if a1 in line:
                    line = b1
                    f2.write('%s\n' % line)
                elif a2 in line:
                    line=b2
                    f2.write('%s\n' % line)
                elif a3 in line:
                    line=b3
                    f2.write('%s\n' % line)
                elif a4 in line:
                    line=b4
                    f2.write('%s\n' % line)
                else:
                    f2.write('%s' % line)
            f2.close()

    def transcrawltime(self,yhxz):
        if yhxz == '1小时':
            pqsj = '12'
        elif yhxz == '17小时':
            pqsj = '204'
        elif yhxz == '1天':
            pqsj = '288'
        elif yhxz == '1周':
            pqsj = '2016'
        elif yhxz == '3周':
            pqsj = '6048'
        elif yhxz == '1个月':
            pqsj = '8640'
        elif yhxz == '半年':
            pqsj = '51840'
        elif yhxz == '1年':
            pqsj = '103680'
        elif yhxz == '2年':
            pqsj = '207360'
        return pqsj

    def createcode(self):
        yhxz = self.comboBox_crawltime1.currentText()
        pqsj = self.transcrawltime(yhxz)
        key = "'" + self.lineEdit_key.text() + "'"
        baselng =  self.lineEdit_baselng.text()#与圆形和指定线路不通，baselng和baselat不是用于拼接URL的，不能是字符串形式
        baselat = self.lineEdit_baselat.text()
        self.changetext("pqsj=''","key = ''", "baselng = ''", "baselat = ''","pqsj=" + pqsj, "    key=" + key, "    baselng=" + baselng,"    baselat =" + baselat)

        QMessageBox.information(self,"提示","操作完成！！",QMessageBox.Yes | QMessageBox.No)

class ChildForm_square(QWidget,Ui_Form_square):
    def __init__(self):
        super(ChildForm_square, self).__init__()
        self.setupUi(self)

    def changetext(self,a1,a2,a3,a4,b1,b2,b3,b4):
        with open('crawl_square.py', 'r', encoding='utf-8') as f1:
            lines = []  # 创建了一个空列表，里面没有元素
            for line in f1.readlines():
                if line != '\n':
                    lines.append(line)
            f1.close()
        with open('crawl_square.py', 'w', encoding='utf-8') as f2:
            for line in lines:
                if a1 in line:
                    line = b1
                    f2.write('%s\n' % line)
                elif a2 in line:
                    line=b2
                    f2.write('%s\n' % line)
                elif a3 in line:
                    line=b3
                    f2.write('%s\n' % line)
                elif a4 in line:
                    line=b4
                    f2.write('%s\n' % line)
                else:
                    f2.write('%s' % line)
            f2.close()
    def transcrawltime(self,yhxz):
        if yhxz == '1小时':
            pqsj = '12'
        elif yhxz == '17小时':
            pqsj = '204'
        elif yhxz == '1天':
            pqsj = '288'
        elif yhxz == '1周':
            pqsj = '2016'
        elif yhxz == '3周':
            pqsj = '6048'
        elif yhxz == '1个月':
            pqsj = '8640'
        elif yhxz == '半年':
            pqsj = '51840'
        elif yhxz == '1年':
            pqsj = '103680'
        elif yhxz == '2年':
            pqsj = '207360'
        return pqsj


    def createcode(self):
        yhxz = self.comboBox_crawltime2.currentText()
        pqsj = self.transcrawltime(yhxz)
        key = "'" + self.lineEdit_key.text() + "'"
        baselng =  self.lineEdit_baselng.text()#与圆形和指定线路不通，baselng和baselat不是用于拼接URL的，不能是字符串形式
        baselat = self.lineEdit_baselat.text()
        self.changetext("pqsj=''","key = ''", "baselng = ''", "baselat = ''","pqsj=" + pqsj, "key=" + key, "baselng=" + baselng,"baselat =" + baselat)
        QMessageBox.information(self,"提示","操作完成！！",QMessageBox.Yes | QMessageBox.No)

class ChildForm_road(QWidget,Ui_Form_road):
    def __init__(self):
        super(ChildForm_road, self).__init__()
        self.setupUi(self)

    def changetext(self,a1,a2,a3,a4,b1,b2,b3,b4):
        with open('crawl_road.py', 'r', encoding='utf-8') as f1:
            lines = []  # 创建了一个空列表，里面没有元素
            for line in f1.readlines():
                if line != '\n':
                    lines.append(line)
            f1.close()
        with open('crawl_road.py', 'w', encoding='utf-8') as f2:
            for line in lines:
                if a1 in line:
                    line = b1
                    f2.write('%s\n' % line)
                elif a2 in line:
                    line=b2
                    f2.write('%s\n' % line)
                elif a3 in line:
                    line=b3
                    f2.write('%s\n' % line)
                elif a4 in line:
                    line=b4
                    f2.write('%s\n' % line)
                else:
                    f2.write('%s' % line)
            f2.close()
    def transcrawltime(self,yhxz):
        if yhxz == '1小时':
            pqsj = '12'
        elif yhxz == '17小时':
            pqsj = '204'
        elif yhxz == '1天':
            pqsj = '288'
        elif yhxz == '1周':
            pqsj = '2016'
        elif yhxz == '3周':
            pqsj = '6048'
        elif yhxz == '1个月':
            pqsj = '8640'
        elif yhxz == '半年':
            pqsj = '51840'
        elif yhxz == '1年':
            pqsj = '103680'
        elif yhxz == '2年':
            pqsj = '207360'
        return pqsj

    def createcode(self):
        yhxz = self.comboBox_crawltime3.currentText()
        pqsj = self.transcrawltime(yhxz)
        key="'" + self.lineEdit_key.text() + "'"
        cityname="'" + self.lineEdit_cityname.text()+ "'"
        roadname="'" + self.lineEdit_roadname.text()+ "'"
        self.changetext("pqsj=''","key = ''","cityname = ''","roadName = ''","pqsj=" + pqsj,"    key=" + key,"    cityname=" + cityname,"    roadName =" + roadname)
        QMessageBox.information(self,"提示","操作完成！！",QMessageBox.Yes | QMessageBox.No)

class ChildForm_images(QWidget,Ui_Form_images):
    def __init__(self):
        super(ChildForm_images, self).__init__()
        self.setupUi(self)
        self.label_rectangle.setPixmap( QPixmap("./images/rectangle.jpg"))
        self.label_square.setPixmap( QPixmap("./images/square.jpg"))
        self.label_road.setPixmap( QPixmap("./images/road.jpg"))

class Runthread_dataprocessing(QThread):
    signal_pb1_dataprocessing = pyqtSignal('PyQt_PyObject')
    signal_pb2_dataprocessing = pyqtSignal('PyQt_PyObject')
    signal_textedit1_dataprocessing = pyqtSignal('PyQt_PyObject')
    signal_textedit2_dataprocessing = pyqtSignal('PyQt_PyObject')
    def __init__(self,crawl_time,target_type,target_road,start_time):
        super(Runthread_dataprocessing, self).__init__()

        self.crawl_time = crawl_time
        self.target_type = target_type
        self.target_road = target_road
        self.start_time = start_time
    def run(self):
        crawl_time = self.crawl_time
        target_type = self.target_type
        target_road = self.target_road
        start_time = self.start_time
        #pb_update = 0

        try:
            os.mkdir('./提取' + target_road + '数据/')
            os.mkdir('路段平均速度')#创建文件夹'提取目标路段'和'路段平均速度'
        except:
            pass
        # '选择指定路段数据'range(crawl_time个文件)
        for i in range(crawl_time):
            try:
                inputfile = './' + target_type + '/' + str(i) + '.csv'  # './长方形爬虫数据结果/' +
                data = pd.read_csv(inputfile)  # './指定线路爬虫数据结果/' +
                lists = list(data['路名'])
                data.index = lists
                x = data.loc[target_road]
                x = x.drop(columns=['Unnamed: 0'])
                x.to_csv('./提取' + target_road + '数据/' + str(i) + '.csv', mode='a', encoding='utf-8-sig')
                str1 = '完成' + str(i) + '.csv文件的数据处理'
                self.signal_textedit1_dataprocessing.emit(str1)
                pb_update = (i / (crawl_time-1)) * 100
                self.signal_pb1_dataprocessing.emit(pb_update)

            except:
                pass

        # '路段平均速度'(仅1个csv时间序列文件)
        Timestamp = pd.date_range(start_time, periods=crawl_time, freq='5T')
        Timestamp = pd.DataFrame(Timestamp, columns=['Timestamp'])
        pieces = []

        for i in range(crawl_time):
            frame = pd.read_csv('./提取' + target_road + '数据/' + str(i) + '.csv')
            means = frame['车速'].groupby([frame['路名']]).mean()  # 求平均值
            speed = means.loc[target_road]#有无这一步无所谓
            sj = i
            data = pd.DataFrame({'时间': Timestamp.loc[sj], '车速': speed})  # 将data数据变为dataframe类型
            pieces.append(data)
            str2 = '完成' + str(i) + '.csv文件的数据处理'
            self.signal_textedit2_dataprocessing.emit(str2)
            pb_update = (i / (crawl_time-1)) * 100
            self.signal_pb2_dataprocessing.emit(pb_update)
        speed_rmnl3 = pd.concat(pieces, ignore_index=True)
        speed_rmnl3.to_csv('./路段平均速度/' + target_road + '.csv', mode='a', encoding='utf-8-sig')

class ChildForm_dataprocessing(QWidget,Ui_Form_dataprocessing):
    def __init__(self):
        super(ChildForm_dataprocessing, self).__init__()
        self.setupUi(self)

    def transcrawltime(self,yhxz):
        if yhxz == '1小时':
            crawl_time = 12
        elif yhxz == '17小时':
            crawl_time = 204
        elif yhxz == '1天':
            crawl_time = 288
        elif yhxz == '1周':
            crawl_time = 2016
        elif yhxz == '3周':
            crawl_time = 6048
        elif yhxz == '1个月':
            crawl_time = 8640
        elif yhxz == '半年':
            crawl_time = 51840
        elif yhxz == '1年':
            crawl_time = 103680
        elif yhxz == '2年':
            crawl_time = 207360
        return crawl_time

    def dataprocessing(self):
        QMessageBox.information(self,"提示","正在运行，耗时较长...",QMessageBox.Yes | QMessageBox.No)
        yhxz = self.comboBox_crawltime4.currentText()
        crawl_time = self.transcrawltime(yhxz)
        target_type = self.comboBox_targettype.currentText()
        target_road = self.lineEdit_targetroad.text()
        start_time = self.lineEdit_starttime.text()
        # 创建线程
        self.thread = Runthread_dataprocessing(crawl_time,target_type,target_road,start_time)
        # 连接信号
        self.thread.signal_pb1_dataprocessing.connect(self.updatePB1)
        self.thread.signal_pb2_dataprocessing.connect(self.updatePB2)
        self.thread.signal_textedit1_dataprocessing.connect(self.updateText1)
        self.thread.signal_textedit2_dataprocessing.connect(self.updateText2)
        # 开始线程
        self.thread.start()

    def updatePB1(self, pb_update):
        self.progressBar_dataprocessing1.setValue(pb_update)
    def updatePB2(self, pb_update):
        self.progressBar_dataprocessing2.setValue(pb_update)
    def updateText1(self, text):
        self.textEdit_progressbar1.append(text)
        self.textEdit_progressbar1.moveCursor(self.textEdit_progressbar1.textCursor().End)
    def updateText2(self, text):
        self.textEdit_progressbar2.append(text)
        self.textEdit_progressbar2.moveCursor(self.textEdit_progressbar2.textCursor().End)

class Runthread_predict(QThread):
    signal_pb_predict = pyqtSignal('PyQt_PyObject')
    signal_textedit_predict = pyqtSignal('PyQt_PyObject')
    signal_plot = pyqtSignal('PyQt_PyObject')
    def __init__(self,test,trend,seasonal,residual):
        super(Runthread_predict, self).__init__()
        self.test = test
        self.trend = trend
        self.seasonal = seasonal
        self.residual = residual
    def run(self):
        test = self.test
        trend = self.trend
        seasonal = self.seasonal
        residual = self.residual

        MAE_arima = 1000.999999
        for p in range(6):
            for q in range(6):
                trend_model = ARIMA(trend, order=(p, 2, q)).fit(disp=-1, method='css')
                n = 288
                pred_time_index = pd.date_range(start=trend.index[-1], periods=n + 1, freq='5min')[1:]
                trend_pred = trend_model.forecast(n)[0]  # add_season()
                train_season = seasonal
                train_residual = residual
                values = []
                for i, t in enumerate(pred_time_index):
                    trend_part = trend_pred[i]
                    # 相同时间的数据均值
                    season_part = train_season[train_season.index.time == t.time()].mean()
                    residual_part = train_residual[train_residual.index.time == t.time()].mean()
                    # 趋势+周期+误差界限
                    predict = trend_part + season_part + residual_part
                    values.append(predict)
                final_pred = pd.Series(values, index=pred_time_index, name='predict')
                # 将trend预测趋势弄出来
                # 评估_________均方根误差rmse，画图对比和真实值的差距
                pred = final_pred
                MAE_arima_test = mean_absolute_error(test, pred)
                if MAE_arima > MAE_arima_test:
                    MAE_arima = MAE_arima_test
                    p_min = p
                    q_min = q
                    str1 = 'p = ' + str(p) + ',q = ' + str(q) + ',MAE = ' + str(MAE_arima_test) + '，MAE↓↓'
                    self.signal_textedit_predict.emit(str1)
                else:
                    str11 = 'p = ' + str(p) + ',q = ' + str(q) + ',MAE = ' + str(MAE_arima_test) + '，p,q值不变'
                    self.signal_textedit_predict.emit(str11)

                pb_update = ((p*6+(q+1)) / 36) * 100
                self.signal_pb_predict.emit(pb_update)

        str2 = '①@@@@：使MAE最小的p,q取值为：p = ' + str(p_min) + ',q = ' + str(q_min) + ',MAE_min = ' + str(MAE_arima)
        self.signal_textedit_predict.emit(str2)
        str3 = '②****：最终确定的ARIMA模型为(' + str(p_min) + ',' + '2' + ',' + str(q_min) + ')'
        self.signal_textedit_predict.emit(str3)

        trend_model = ARIMA(trend, order=(p_min, 2, q_min)).fit(disp=-1, method='css')
        n = 288
        pred_time_index = pd.date_range(start=trend.index[-1], periods=n + 1, freq='5min')[1:]
        trend_pred = trend_model.forecast(n)[0]  # add_season()
        train_season = seasonal
        train_residual = residual
        values = []
        trend_pred_values = []  # 趋势
        for i, t in enumerate(pred_time_index):
            trend_part = trend_pred[i]
            # 相同时间的数据均值
            season_part = train_season[train_season.index.time == t.time()].mean()
            residual_part = train_residual[train_residual.index.time == t.time()].mean()
            # 趋势+周期+误差界限
            predict = trend_part + season_part + residual_part
            values.append(predict)
        final_pred = pd.Series(values, index=pred_time_index, name='predict')
        # 评估_________均方根误差rmse，画图对比和真实值的差距
        pred = final_pred

        dp_output = {
            "pred": pred,
            "MAE_arima": MAE_arima,
            "test": test
            }
        self.signal_plot.emit(dp_output)

class ChildForm_predict(QWidget,Ui_Form_predict):
    def __init__(self):
        super(ChildForm_predict, self).__init__()
        self.setupUi(self)

        #设置对应的图像不可见
        self.matplotlibwidget_correlation.setVisible(False)
        self.matplotlibwidget_arimapre.setVisible(False)
        self.textEdit_arima.setVisible(False)

    def transvolume(self,datavolume):
        if datavolume == '1周':
            divide_time = 1728          #留出1天时间作为测试集
            ann_time = 1440          #留出1天 + 1天时间作为测试集
        elif datavolume == '3周':
            divide_time = 5760          #留出1天时间作为测试集
            ann_time = 5472          #留出1天 + 1天时间作为测试集
        elif datavolume == '1个月':
            divide_time = 8352          #留出1天时间作为测试集
            ann_time = 8064          #留出1天 + 1天时间作为测试集
        else:
            print('没有选择数据划分量')
        return divide_time,ann_time
    def correlation_conpute(self):
        datavolume = self.comboBox_datavolume.currentText()
        divide_time,ann_time = self.transvolume(datavolume)
        self.target_road = self.lineEdit_targetroad.text()
        self.speed_rmnl3 = pd.read_csv('./路段平均速度/' + self.target_road + '.csv')
        self.speed_rmnl3['Timestamp'] = pd.to_datetime(self.speed_rmnl3['时间'],format='%Y-%m-%d %H:%M')  # 必须用到这一步，不然再后面的seasonal（分解周期）步骤中会出不了结果，卡起，不知道为什么，咱也没地方问啊，加上就对了
        self.speed_rmnl3.index = self.speed_rmnl3['Timestamp']
        self.speed_rmnl3 = self.speed_rmnl3['车速']
        self.train = self.speed_rmnl3[0:divide_time]

        weekend = np.where(self.train.index.weekday < 5, 'Weekday', 'Weekend')
        by_time = self.train.groupby([weekend, self.train.index.time]).mean()  # weekend(5472)/by_time(576————包含weekend的288一天和weekday的288一天)
        weekdayline = by_time.ix['Weekday']
        weekendline = by_time.ix['Weekend']
        return weekdayline,weekendline
    def correlation(self):
        weekdayline,weekendline = self.correlation_conpute()
        self.matplotlibwidget_correlation.setVisible(True)
        self.matplotlibwidget_correlation.mpl.start_correlation_plot(weekdayline,weekendline)
        QMessageBox.information(self,"提示","操作完成",QMessageBox.Yes | QMessageBox.No)
    def arimaclick(self):
        QMessageBox.information(self,"提示","请稍等，后台正在处理...",QMessageBox.Yes | QMessageBox.No)
        #划分训练集、测试集
        target_road = self.lineEdit_targetroad.text()
        speed_rmnl3 = pd.read_csv('./路段平均速度/' + target_road + '.csv')
        speed_rmnl3['Timestamp'] = pd.to_datetime(speed_rmnl3['时间'],format='%Y-%m-%d %H:%M')  # 必须用到这一步，不然再后面的seasonal（分解周期）步骤中会出不了结果，卡起，不知道为什么，咱也没地方问啊，加上就对了
        speed_rmnl3.index = speed_rmnl3['Timestamp']
        speed_rmnl3 = speed_rmnl3['车速']
        datavolume = self.comboBox_datavolume.currentText()
        divide_time,ann_time = self.transvolume(datavolume)
        train = speed_rmnl3[0:divide_time ]
        test = speed_rmnl3[divide_time:]
        ts = train
        decomposition = seasonal_decompose(ts, freq=288, two_sided=False)  # 将288个数据作为一个周期
        trend =decomposition.trend
        seasonal = decomposition.seasonal
        residual = decomposition.resid
        residual.dropna(inplace=True)
        trend.dropna(inplace=True)

        self.thread = Runthread_predict(test,trend,seasonal,residual)
        # 连接信号
        self.thread.signal_pb_predict.connect(self.updatePB)
        self.thread.signal_textedit_predict.connect(self.updateText)
        #QMessageBox.information(self,"提示","请稍等，正在绘图...",QMessageBox.Yes | QMessageBox.No)
        self.thread.signal_plot.connect(self.updatePlot)
        # 开始线程
        self.thread.start()
    def updatePB(self, pb_update):
        self.progressBar_arima.setValue(pb_update)
    def updateText(self, text):
        self.textEdit_arima.setVisible(True)
        self.textEdit_arima.append(text)
        self.textEdit_arima.moveCursor(self.textEdit_arima.textCursor().End)
    def updatePlot(self, dp_output):
        self.pred_arima = dp_output["pred"]
        self.MAE_arima = dp_output["MAE_arima"]
        self.test = dp_output["test"]
        pred_arima = self.pred_arima
        MAE_arima = self.MAE_arima
        test = self.test
        self.matplotlibwidget_arimapre.setVisible(True)
        self.matplotlibwidget_arimapre.mpl.start_arima_plot(pred_arima,test,MAE_arima)
        QMessageBox.information(self,"提示","绘图完成",QMessageBox.Yes | QMessageBox.No)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwin = MainWindow()
    mainwin.show()
    sys.exit(app.exec_())
