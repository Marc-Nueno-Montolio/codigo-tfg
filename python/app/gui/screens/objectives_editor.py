
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets, uic

# https://www.youtube.com/watch?v=LW__NuulfxE

from PyQt5.QtWidgets import QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem

base_dir = os.path.join(os.getcwd(), os.pardir)
print(base_dir)
OBJECTIVES_ICON = os.path.join(base_dir,'assets/box_icon.webp')
ITEM_ICON = os.path.join(base_dir,'assets/gear_icon.webp')

class Objective(QStandardItem):
    def __init__(self, objective_description=' '):
        super().__init__()
        self.setText(objective_description)
        icon = QtGui.QIcon(OBJECTIVES_ICON)
        self.setIcon(icon)

class Item(QStandardItem):
    def __init__(self, item_name=''):
        super().__init__()
        self.setText(item_name)
        icon = QtGui.QIcon(ITEM_ICON)
        self.setIcon(icon)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Load User Interface
        uic.loadUi(os.path.join(base_dir, 'ui_templates/objectives_editor.ui'), self)
        self.setWindowTitle("Gestión de Pedidos / Objetivos")

        # Configure TreeView
        self.treeView.setHeaderHidden(True)
        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()
        self.treeView.setModel(treeModel)

        # Add Items to treeView
        objective_1 = Objective('Pedido 1 - Estado: Pendiente - 27/11/2022 20:00 ')
        item_1 = Item('Tornillos')
        item_2 = Item('Caja grande')
        objective_1.appendRow(item_1)
        objective_1.appendRow(item_2)
        rootNode.appendRow(objective_1)

        # Configure Selector
        self.itemSelector.addItems(['Tornillos'])

        
        # Register Callbacks:
        self.treeView.doubleClicked.connect(self.display_info)

        self.sendBtn.clicked.connect(self.create_objective)

    def display_info(self, val):
        print(val.data(), val.row(), val.column())

    def create_objective(self):
        item = self.itemSelector.currentText()
        objective_id = self.objectiveIDInput.text()
        print(item, objective_id)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()