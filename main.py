# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import json
import os.path
import threading
import sys
# import keyboard
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from pynput import keyboard
from keybind import KeyBinder
from pynput.mouse import Button, Controller
mouse = Controller()

class Ui_MainWindow(object):
    def __init__(self):
        self.__hotKey_keys_dict = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']
        self.__default_setting_dict = {
            'hotKey_start': 2,
            'hotKey_stop': 3,
            'option_mouse_button': 0, # index id
            'option_mouse_action': 0, # index id
            'interval_hours': 0,
            'interval_minutes': 0,
            'interval_seconds': 0,
            'interval_milliseconds': 0,
            'interval_milliseconds0': 0,
        }
        self.restart = False
        self.doClick = False
        self.__threadBreakCounter = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 257)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setToolTipDuration(-1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)
        self.comboBox_option_mouse_button = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_option_mouse_button.setObjectName("comboBox_option_mouse_button")
        self.comboBox_option_mouse_button.addItem("")
        self.comboBox_option_mouse_button.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_option_mouse_button, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)
        self.comboBox_option_mouse_action = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_option_mouse_action.setObjectName("comboBox_option_mouse_action")
        self.comboBox_option_mouse_action.addItem("")
        self.comboBox_option_mouse_action.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_option_mouse_action, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.comboBox_hotkey_start = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_hotkey_start.setFrame(True)
        self.comboBox_hotkey_start.setObjectName("comboBox_hotkey_start")

        # creat comboBox Space
        for i in self.__hotKey_keys_dict:
            self.comboBox_hotkey_start.addItem("")

        self.gridLayout_4.addWidget(self.comboBox_hotkey_start, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)
        self.comboBox_hotkey_stop = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_hotkey_stop.setObjectName("comboBox_hotkey_stop")

        # creat comboBox Space
        for i in self.__hotKey_keys_dict:
            self.comboBox_hotkey_stop.addItem("")

        self.gridLayout_4.addWidget(self.comboBox_hotkey_stop, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_clickPoint_currentMousePoint = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_clickPoint_currentMousePoint.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_clickPoint_currentMousePoint.setChecked(True)
        self.radioButton_clickPoint_currentMousePoint.setObjectName("radioButton_clickPoint_currentMousePoint")
        self.gridLayout.addWidget(self.radioButton_clickPoint_currentMousePoint, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox_interval_milliseconds = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_interval_milliseconds.setMaximum(1000)
        self.spinBox_interval_milliseconds.setObjectName("spinBox_interval_milliseconds")
        self.gridLayout_3.addWidget(self.spinBox_interval_milliseconds, 1, 3, 1, 1)
        self.spinBox_interval_seconds = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_interval_seconds.setMaximum(60)
        self.spinBox_interval_seconds.setObjectName("spinBox_interval_seconds")
        self.gridLayout_3.addWidget(self.spinBox_interval_seconds, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 3, 1, 1)
        self.spinBox_interval_hours = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_interval_hours.setPrefix("")
        self.spinBox_interval_hours.setMaximum(24)
        self.spinBox_interval_hours.setObjectName("spinBox_interval_hours")
        self.gridLayout_3.addWidget(self.spinBox_interval_hours, 1, 0, 1, 1)
        self.spinBox_interval_minutes = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_interval_minutes.setMaximum(60)
        self.spinBox_interval_minutes.setObjectName("spinBox_interval_minutes")
        self.gridLayout_3.addWidget(self.spinBox_interval_minutes, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridLayout_7.setColumnStretch(1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionssdf = QtWidgets.QAction(MainWindow)
        self.actionssdf.setObjectName("actionssdf")
        self.actionsadas = QtWidgets.QAction(MainWindow)
        self.actionsadas.setObjectName("actionsadas")
        self.actionsaddsa = QtWidgets.QAction(MainWindow)
        self.actionsaddsa.setObjectName("actionsaddsa")
        self.actionsadsdas = QtWidgets.QAction(MainWindow)
        self.actionsadsdas.setObjectName("actionsadsdas")

        self.retranslateUi(MainWindow)

        # signals
        self.comboBox_hotkey_start.currentIndexChanged.connect(self.on_change_combobox)
        self.comboBox_hotkey_stop.currentIndexChanged.connect(self.on_change_combobox)
        self.comboBox_option_mouse_button.currentIndexChanged.connect(self.on_change_combobox)
        self.comboBox_option_mouse_action.currentIndexChanged.connect(self.on_change_combobox)
        self.spinBox_interval_hours.valueChanged.connect(self.on_change)
        self.spinBox_interval_minutes.valueChanged.connect(self.on_change)
        self.spinBox_interval_seconds.valueChanged.connect(self.on_change)
        self.spinBox_interval_milliseconds.valueChanged.connect(self.on_change)
        # self.spinBox_interval_milliseconds0.valueChanged.connect(self.on_change)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mouse auto clicker by Moein"))
        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(sys.path[0], 'mouse-icon.png')))
        self.groupBox_4.setTitle(_translate("MainWindow", "Click Options"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Mouse Button</p></body></html>"))
        self.comboBox_option_mouse_button.setItemText(0, _translate("MainWindow", "Left Button"))
        self.comboBox_option_mouse_button.setItemText(1, _translate("MainWindow", "Right Button"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Mouse Action</p></body></html>"))
        self.comboBox_option_mouse_action.setItemText(0, _translate("MainWindow", "Single Click"))
        self.comboBox_option_mouse_action.setItemText(1, _translate("MainWindow", "Duble Click"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Click Hotkey"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Start Hotkey. ctrl+ </p></body></html>"))
        index = 0

        # add name to hotKey start combobox
        for keyName in self.__hotKey_keys_dict:
            self.comboBox_hotkey_start.setItemText(index, _translate("MainWindow", keyName))
            index += 1

        # add name to hotKey stop combobox
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Stop Hotkey. ctrl+</p></body></html>"))
        index = 0
        for keyName in self.__hotKey_keys_dict:
            self.comboBox_hotkey_stop.setItemText(index, _translate("MainWindow", keyName))
            index += 1

        self.groupBox.setTitle(_translate("MainWindow", "Click Point"))
        self.radioButton_clickPoint_currentMousePoint.setText(_translate("MainWindow", "click where \nthe mouse is"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Click Interval"))
        self.label.setText(_translate("MainWindow", "Hours"))
        self.label_2.setText(_translate("MainWindow", "Minutes"))
        self.label_3.setText(_translate("MainWindow", "Seconds"))
        self.label_4.setText(_translate("MainWindow", "Milliseconds"))
        # self.label_5.setText(_translate("MainWindow", "1/100 S"))
        self.actionssdf.setText(_translate("MainWindow", "ssdf"))
        self.actionsadas.setText(_translate("MainWindow", "sadas"))
        self.actionsaddsa.setText(_translate("MainWindow", "saddsa"))
        self.actionsadsdas.setText(_translate("MainWindow", "sadsdas"))

        self.set_default_values()

    def set_hotKeys(self, start, stop):
        h = KeyBinder.activate({
            'Ctrl-' + start: self.start_click,
            'Ctrl-' + stop: self.stop_click,
        }, run_thread=True)

    def set_default_values(self):
        # if config.json not exist
        if not os.path.isfile('config.json'):
            f = open("config.json", "w")
            f.write(json.dumps(self.__default_setting_dict))
            f.close()
            print("config.json created")

        # load config.json
        f = open("config.json", "r")
        self.__settings_json = json.loads(f.read())
        f.close()

        # set values
        self.comboBox_hotkey_start.setCurrentIndex(self.__settings_json['hotKey_start'])
        self.comboBox_hotkey_start.model().item(self.__settings_json['hotKey_stop']).setEnabled(False)
        self.comboBox_hotkey_stop.setCurrentIndex(self.__settings_json['hotKey_stop'])
        self.comboBox_hotkey_stop.model().item(self.__settings_json['hotKey_start']).setEnabled(False)
        self.comboBox_option_mouse_button.setCurrentIndex(self.__settings_json['option_mouse_button'])
        self.comboBox_option_mouse_action.setCurrentIndex(self.__settings_json['option_mouse_action'])
        self.spinBox_interval_hours.setValue(self.__settings_json['interval_hours'])
        self.spinBox_interval_minutes.setValue(self.__settings_json['interval_minutes'])
        self.spinBox_interval_seconds.setValue(self.__settings_json['interval_seconds'])
        self.spinBox_interval_milliseconds.setValue(self.__settings_json['interval_milliseconds'])
        # self.spinBox_interval_milliseconds0.setValue(self.__settings_json['interval_milliseconds0'])

        # keyBind init
        self.set_hotKeys(self.comboBox_hotkey_start.currentText(), self.comboBox_hotkey_stop.currentText())

    def on_change_combobox(self, index):
        self.on_change()

    def on_change(self):
        if self.comboBox_hotkey_start.currentText() != self.__hotKey_keys_dict[self.__settings_json['hotKey_start']] or \
              self.comboBox_hotkey_stop.currentText() != self.__hotKey_keys_dict[self.__settings_json['hotKey_stop']]:
            self.restart = True

        self.comboBox_hotkey_start.model().item(self.__settings_json['hotKey_stop']).setEnabled(True)
        self.comboBox_hotkey_stop.model().item(self.__settings_json['hotKey_start']).setEnabled(True)

        self.__settings_json['hotKey_start'] = self.comboBox_hotkey_start.currentIndex()
        self.__settings_json['hotKey_stop'] = self.comboBox_hotkey_stop.currentIndex()
        self.__settings_json['option_mouse_button'] = self.comboBox_option_mouse_button.currentIndex()
        self.__settings_json['option_mouse_action'] = self.comboBox_option_mouse_action.currentIndex()
        self.__settings_json['interval_hours'] = self.spinBox_interval_hours.value()
        self.__settings_json['interval_minutes'] = self.spinBox_interval_minutes.value()
        self.__settings_json['interval_seconds'] = self.spinBox_interval_seconds.value()
        self.__settings_json['interval_milliseconds'] = self.spinBox_interval_milliseconds.value()
        # self.__settings_json['interval_milliseconds0'] = self.spinBox_interval_milliseconds0.value()

        self.comboBox_hotkey_start.model().item(self.__settings_json['hotKey_stop']).setEnabled(False)
        self.comboBox_hotkey_stop.model().item(self.__settings_json['hotKey_start']).setEnabled(False)

        f = open('config.json', 'w')
        f.write(json.dumps(self.__settings_json))
        f.close()

        if self.restart:
            python = sys.executable
            os.execl(python, python, *sys.argv)

    def interval_click(self, button, click_count, interval_time, thread_id):
        while self.__threadBreakCounter == thread_id:
            mouse.click(button, click_count)
            sleep(interval_time)

    def start_click(self):
        # print('start')
        interval_time = self.__settings_json['interval_hours'] * 60 * 60 + \
                        self.__settings_json['interval_minutes'] * 60 + \
                        self.__settings_json['interval_seconds'] + \
                        self.__settings_json['interval_milliseconds'] / 1000

        if self.__settings_json['option_mouse_button'] == 0:
            button = Button.left
        else:
            button = Button.right

        self.__threadBreakCounter += 1
        thr = threading.Thread(target=self.interval_click, args=(button, self.__settings_json['option_mouse_action'] + 1, interval_time, self.__threadBreakCounter))
        thr.start()

    def stop_click(self):
        # print("stop")
        # self.doClick = False
        self.__threadBreakCounter += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # app.aboutToQuit.connect(kl.stop_listener)
    sys.exit(app.exec_())
