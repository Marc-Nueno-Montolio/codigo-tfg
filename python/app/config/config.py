import os
from os.path import dirname, abspath

base_dir =os.path.join(dirname(dirname(abspath(__file__))))
COMMUNICATION_DIR = os.path.join(base_dir, 'communication')
CONFIG_DIR = os.path.join(base_dir, 'config')
GUI_DIR = os.path.join(base_dir, 'gui')
DB_DIR = os.path.join(base_dir, 'db')

SQL_DB_URI = 'sqlite:///' + os.path.join(DB_DIR, 'database.db')