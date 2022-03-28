import os
import sys
from auto_clicker.default import Default
from PyQt5 import QtGui, QtWidgets
from auto_clicker.clicker import Clicker
from auto_clicker.ui.main_window import Ui_MainWindow
from auto_clicker.setting import Setting
from keybind import KeyBinder


class GUI:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)
        self.setting = Setting()
        self.clicker = Clicker()
        self.set_icon()
        self.init_combobox()
        self.load_setting()
        self.combo_disable()
        self.set_hotkey()
        self.init_signals()

    def init_combobox(self):
        self.ui.comboBox_start.addItems(Default.hotKey_keys)
        self.ui.comboBox_stop.addItems(Default.hotKey_keys)

    def set_icon(self):
        self.mainWindow.setWindowIcon(QtGui.QIcon(os.path.dirname(__file__) + "/../images/mouse-icon.png"))

    def init_signals(self):
        # interval
        self.ui.spinBox_interval_hours.valueChanged.connect(self.update_setting)
        self.ui.spinBox_interval_minutes.valueChanged.connect(self.update_setting)
        self.ui.spinBox_interval_seconds.valueChanged.connect(self.update_setting)
        self.ui.spinBox_interval_millisecond.valueChanged.connect(self.update_setting)
        # regression
        self.ui.spinBox_regression_millisecond.valueChanged.connect(self.update_setting)
        # hotkey
        self.ui.comboBox_start.currentIndexChanged.connect(self.combo_signal)
        self.ui.comboBox_stop.currentIndexChanged.connect(self.combo_signal)
        # option
        self.ui.comboBox_option_mouse_button.currentIndexChanged.connect(self.update_setting)
        self.ui.comboBox_option_mouse_action.currentIndexChanged.connect(self.update_setting)

    def combo_disable(self):
        self.ui.comboBox_start.model().item(self.setting.data['hotKey_stop']).setEnabled(False)
        self.ui.comboBox_stop.model().item(self.setting.data['hotKey_start']).setEnabled(False)

    def combo_enable(self):
        self.ui.comboBox_start.model().item(self.setting.data['hotKey_stop']).setEnabled(True)
        self.ui.comboBox_stop.model().item(self.setting.data['hotKey_start']).setEnabled(True)

    def combo_signal(self, value):
        self.combo_enable()
        self.update_setting(value)
        # self.combo_disable()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def update_setting(self, value):
        self.collect_setting_date()
        self.setting.update()

    def show(self):
        self.mainWindow.show()
        sys.exit(self.app.exec_())

    def collect_setting_date(self):
        # hotkey
        self.setting.data['hotKey_start'] = self.ui.comboBox_start.currentIndex()
        self.setting.data['hotKey_stop'] = self.ui.comboBox_stop.currentIndex()
        # option
        self.setting.data['option_mouse_button'] = self.ui.comboBox_option_mouse_button.currentIndex()
        self.setting.data['option_mouse_action'] = self.ui.comboBox_option_mouse_action.currentIndex()
        # interval
        self.setting.data['interval_hours'] = self.ui.spinBox_interval_hours.value()
        self.setting.data['interval_minutes'] = self.ui.spinBox_interval_minutes.value()
        self.setting.data['interval_seconds'] = self.ui.spinBox_interval_seconds.value()
        self.setting.data['interval_milliseconds'] = self.ui.spinBox_interval_millisecond.value()
        # regression
        self.setting.data['regression_milliseconds'] = self.ui.spinBox_regression_millisecond.value()

    def load_setting(self):
        current_data = self.setting.data.copy()
        # hotkey
        self.ui.comboBox_start.setCurrentIndex(current_data['hotKey_start'])
        self.ui.comboBox_stop.setCurrentIndex(current_data['hotKey_stop'])
        # option
        self.ui.comboBox_option_mouse_button.setCurrentIndex(current_data['option_mouse_button'])
        self.ui.comboBox_option_mouse_action.setCurrentIndex(current_data['option_mouse_action'])
        # interval
        self.ui.spinBox_interval_hours.setValue(current_data['interval_hours'])
        self.ui.spinBox_interval_minutes.setValue(current_data['interval_minutes'])
        self.ui.spinBox_interval_seconds.setValue(current_data['interval_seconds'])
        self.ui.spinBox_interval_millisecond.setValue(current_data['interval_milliseconds'])
        # regression
        self.ui.spinBox_regression_millisecond.setValue(current_data['regression_milliseconds'])

    def set_hotkey(self):
        KeyBinder.activate({
            'Ctrl-{}'.format(Default.hotKey_keys[self.setting.data['hotKey_start']]): self.start_click,
            'Ctrl-{}'.format(Default.hotKey_keys[self.setting.data['hotKey_stop']]): self.stop_click,
        }, run_thread=True)

    def start_click(self):
        self.clicker.start(self.setting.data)

    def stop_click(self):
        self.clicker.stop()
