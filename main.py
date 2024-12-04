import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>962</width>
    <height>570</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>161</y>
      <width>711</width>
      <height>181</height>
     </rect>
    </property>
    <row>
     <property name="text">
      <string/>
     </property>
    </row>
    <column>
     <property name="text">
      <string>id</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>название сорта</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>степень обжарки</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>молотый/в зернах</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>описание вкуса</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>цена</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>объем упаковки</string>
     </property>
    </column>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>962</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = StringIO(template)
        uic.loadUi(f, self)
        self.con = sqlite3.connect("films_db.sqlite")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())