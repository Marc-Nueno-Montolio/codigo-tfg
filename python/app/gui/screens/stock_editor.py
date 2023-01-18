
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
QTime)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
QWidget)


class App(QWidget):
    
    CONTENT_ID, CONTENT_DESCRIPTION, CONTENT_POSITION, CONTENT_UPDATED = range(4)
    
    def __init__(self):
        super().__init__()
        self.title = 'Gestión de Stock'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 240
        #self.crud = rest_client.apiClient()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.dataGroupBox = QGroupBox("Pedidos / Objetivos")
        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(True)
        self.dataView.setAlternatingRowColors(True)
        
        dataLayout = QHBoxLayout()
        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)
        
        model = self.createStockItemModel(self)
        self.dataView.setModel(model)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        self.setLayout(mainLayout)
        
        self.show()



    # Callbacks and methods

    def createStockItemModel(self,parent):
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.CONTENT_ID, Qt.Horizontal, "ID Mercancía")
        model.setHeaderData(self.CONTENT_DESCRIPTION, Qt.Horizontal, "Contenido")
        model.setHeaderData(self.CONTENT_POSITION, Qt.Horizontal, "Pos. Almacén")
        model.setHeaderData(self.CONTENT_UPDATED, Qt.Horizontal, "Última modificación")
        return model
    
    def addStockItem(self,model, content_id, content_description, content_position, content_updated):
        model.insertRow(0)
        model.setData(model.index(0, self.CONTENT_ID), content_id)
        model.setData(model.index(0, self.CONTENT_DESCRIPTION), content_description)
        model.setData(model.index(0, self.CONTENT_POSITION), content_position)
        model.setData(model.index(0, self.CONTENT_UPDATED), content_updated)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())