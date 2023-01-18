# ROS Libraries


# GUI Libraries
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QObject, QThread, QThreadPool, pyqtSignal

import matplotlib
#matplotlib.use('TkAgg')

from .callbacks import *
from ..config import config


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Load User Interface
        uic.loadUi('./app/gui/ui_templates/main_app_window.ui', self)
        
        self.threadpool = QThreadPool()
        self.plainTextEdit.appendPlainText("-> Aplicación iniciada (multithreading activado con %d threads)" % self.threadpool.maxThreadCount())

        # Register Monitoring Callbacks
        self.monitorLaserBtn.clicked.connect(lambda: runActionInWorkerThread(self, 'laser_monitor'))
        self.monitorLidarBtn.clicked.connect(lambda: runActionInWorkerThread(self, 'lidar_monitor'))


        # Register Action Callbacks
        self.actionSlamBtn.clicked.connect(lambda: runActionInWorkerThread(self, 'slam'))
        self.actionOccMapBtn.clicked.connect(lambda: runActionInWorkerThread(self, 'show_occ_map'))
        self.actionPlannerBtn.clicked.connect(lambda: runActionInWorkerThread(self, 'update_planner'))

        self.actionStockBtn.clicked.connect(lambda: runActionInWorkerThread(self, 'stock_editor'))
        self.actionObjectivesBtn.clicked.connect(lambda: runActionInWorkerThread(self, 'objectives_editor'))

        # Register Manual Control Callbacks
        self.btnUp.clicked.connect(lambda: move_action(self, 'up'))
        self.btnDown.clicked.connect(lambda: move_action(self, 'down'))
        self.btnLeft.clicked.connect(lambda: move_action(self,'left'))
        self.btnRight.clicked.connect(lambda: move_action(self,'right'))

        self.btnUpRight.clicked.connect(lambda: move_action(self, 'up-right'))
        self.btnDownRight.clicked.connect(lambda: move_action(self, 'down-right'))
        self.btnUpLeft.clicked.connect(lambda: move_action(self,'up-left'))
        self.btnDownLeft.clicked.connect(lambda: move_action(self,'down-left'))

        self.velSlider.valueChanged.connect(lambda: update_velocity(self, self.velSlider.value()))