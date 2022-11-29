from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog

from .workers import *

from ..communication.ros import move_robot

rc = move_robot.RobotController()

# Robot Control Callbacks
def update_velocity(window, velocity):
    # Slider has 10 steps, velocity from 0 to 1
    rc.setVelocity(velocity/10)

def move_action(window, btn):
    if btn == 'up':
        rc.moveUp()
    elif btn == 'down':
        rc.moveDown()
    elif btn == 'right':
        rc.moveRight()
    elif btn == 'left':
        rc.moveLeft()
    elif btn == 'up-left':
        rc.moveUpLeft()
    elif btn == 'up-right':
        rc.moveUpRight()
    elif btn == 'down-left':
        rc.moveDownLeft()
    elif btn == 'down-right':
        rc.moveDownRight()
    
    window.plainTextEdit.appendPlainText(f"-> Enviando {btn}")


# Worker Callbacks
def runActionInWorkerThread(window, action):
    try:
        # Monitoring
        if action == 'laser_monitor':
            worker = LaserMonitorWorker()
        elif action == 'lidar_monitor':
            worker = LidarMonitorWorker()
        # Actions
        elif action == 'slam':
            worker = SlamActionWorker(mode='stop')
        elif action == 'show_occ_map':
            worker = OccMapActinoWorker()
        elif action == 'update_planner':
            worker = UpdatePlannerAction()
        elif action == 'stock_editor':
            worker = StockEditorWorker()
        elif action == 'objectives_editor':
            worker = ObjectivesEditorWorker()
        worker.signals.finished.connect(lambda:window.plainTextEdit.appendPlainText(f"-> OK"))
        window.threadpool.start(worker)
        window.plainTextEdit.appendPlainText(f"-> Lanzado {action}")
    except Exception as e:
        print(e)
        window.plainTextEdit.appendPlainText(f"-> Problema lanzando thread")
    

