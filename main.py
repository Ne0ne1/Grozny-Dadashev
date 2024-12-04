import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QMessageBox
from io import StringIO

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
      <x>60</x>
      <y>80</y>
      <width>711</width>
      <height>291</height>
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
   <widget class="QPushButton" name="save_button">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>400</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Save Data</string>
    </property>
   </widget>
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
        self.tableWidget: QTableWidget
        self.con = sqlite3.connect("coffee.sqlite")
        self.cursor_2 = self.con.cursor()

        self.cursor_2.execute("""create table if not exists coffee (id integer primary key, 
                              name_sort text, pow text, type text, 
                              description text, price integer, volume integer)""")
        self.titles = ["id", "name_sort", "pow", "type", "description", "price", "volume"]

        self.tableWidget.itemChanged.connect(self.item_changed)

        self.save_button.clicked.connect(self.save_results)

        self.modified = {}

    def item_changed(self, item):
        data = {}
        row = item.row()
        col = item.column()
        id = row + 1
        if id in self.modified:
            self.modified[id][self.titles[col]] = item.text()
        else:
            self.modified[id] = {
                self.titles[0]: id,
                self.titles[1]: "",
                self.titles[2]: "",
                self.titles[3]: "",
                self.titles[4]: "",
                self.titles[5]: "",
                self.titles[6]: "",
            }

        data[self.titles[col]] = self.tableWidget.item(row, col).text()

        if self.tableWidget.currentItem().row() + 1 == self.tableWidget.rowCount():
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)

    def save_results(self):
        rows = tuple(set([i.row() for i in self.tableWidget.selectedItems()]))

        if self.modified:
            cur = self.con.cursor()
            for key, value in self.modified.items():
                if list(value.values())[6]:
                    query = f"""insert into coffee({", ".join(value.keys())}) values ('{", '".join(map(str, value.values()))}')"""
                    self.cursor_2.execute(query)
                    # print(query)
            self.con.commit()
            self.modified.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
