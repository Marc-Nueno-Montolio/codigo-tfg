from PyQt5.QtCore import QRunnable, QObject, pyqtSignal, pyqtSlot
from time import sleep

import os

screens_path = os.path.join(os.path.abspath(os.getcwd()), 'app', 'gui','screens')

from ..communication.matlab.tcp_client import MatlabClient
client = MatlabClient(5000)
client.connect()

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)



class ObjectivesEditorWorker(QRunnable):
    def __init__(self, *args, **kwargs):
        super(ObjectivesEditorWorker, self).__init__()
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            os.system(f"python {screens_path}/objectives_editor.py")
        finally:
            self.signals.finished.emit()

class StockEditorWorker(QRunnable):
    def __init__(self, *args, **kwargs):
        super(StockEditorWorker, self).__init__()
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            os.system(f"python {screens_path}/stock_editor.py")
        finally:
            self.signals.finished.emit()

class LaserMonitorWorker(QRunnable):
    def __init__(self, *args, **kwargs):
        super(LaserMonitorWorker, self).__init__()
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            os.system(f"python {screens_path}/real_time_laser_plot.py")
        finally:
            self.signals.finished.emit()

class LidarMonitorWorker(QRunnable):
    def __init__(self, *args, **kwargs):
        super(LidarMonitorWorker, self).__init__()
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            #os.system("python screens/real_time_lidar_plot.py")
            #client.send_command('slam')
            print('Ok')
        finally:
            self.signals.finished.emit()


class SlamActionWorker(QRunnable):
    def __init__(self, *args, **kwargs):
        super(SlamActionWorker, self).__init__()
        self.mode = kwargs['mode']
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            client.send_command('generate-slam', {"mode": "stop"})
            print('SLAM Action')
            
        finally:
            self.signals.finished.emit()



class OccMapActinoWorker(QRunnable):
    def __init__(self, *args, **kwargs):
        super(OccMapActinoWorker, self).__init__()
        self.signals = WorkerSignals()
        
    @pyqtSlot()
    def run(self):
        try:
            client.send_command('show_occ_map', [])
        finally:
            self.signals.finished.emit()


class UpdatePlannerAction(QRunnable):
    def __init__(self, *args, **kwargs):
        super(UpdatePlannerAction, self).__init__()
        self.signals = WorkerSignals()
        
    @pyqtSlot()
    def run(self):
        try:
            client.send_command('update_planner', [])
        finally:
            self.signals.finished.emit()






       