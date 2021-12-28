from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QInputDialog,  QMainWindow, QHBoxLayout, QApplication, QPushButton,  QListWidgetItem, QPlainTextEdit
from PyQt5.QtGui import *
import sys
import os 

class Interfce(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        
        self._file_path()
        self._ListItem()
        self._List_of_file()
        self._write_list_widget()
        # self.file_name()
        self._mainText()
        self._save_button()
        self._delete_button()
        self._add_button()
        self._note_text()
        
        self.setWindowTitle ('Нотатки')
        self.setGeometry(350 ,200, 600 ,500)
        self.originalPalette = QApplication.palette()

    def _mainText(self): 
        self.mainText = QtWidgets.QLabel(self)    
        self.mainText.setText("Назва / Заголовок" )
        self.mainText.move(270,15 )
        self.mainText.setFixedWidth(200)
        self.mainText.setFont(QFont('Arial', 18))
    
    def _ListItem (self):    
        self.ListItem = QtWidgets.QListWidget(self)
        self.ListItem.move(10,10)
        self.ListItem.setFixedSize (150,430)  
        self.ListItem.itemActivated.connect(self.open_file)
        self.ListItem.setFont(QFont('Arial', 14))
        self.ListItem.setStyleSheet("background-color: #E0FFFF")
       
    def _save_button (self):
        self.save_button = QPushButton(self)
        self.save_button.move(270,460)
        self.save_button.setText('Save')
        self.save_button.setFont(QFont('Arial', 14))
        self.save_button.clicked.connect(self.save_file)

    def _delete_button (self):
        self.delete_button = QPushButton(self)
        self.delete_button.move(430,460)
        self.delete_button.setText('Delete')
        self.delete_button.setFont(QFont('Arial', 14))
        self.delete_button.clicked.connect(self.removeSel)

    def _add_button (self):
       self.add_button = QPushButton(self)
       self.add_button.move(40,460)
       self.add_button.setText('+')
       self.add_button.setFont(QFont('Arial',18))
       self.add_button.clicked.connect(self.new_file)

    def _TextEdit(self):
        self.TextEdit  = QtWidgets.QTextEdit(self)
        self.TextEdit.setStyleSheet("background-color: #FFFF99")
        self.TextEdit.setObjectName("plainTextEdit")
        self.TextEdit.setFont(QFont('Arial',12))
        self.TextEdit.move(170,55)
        self.TextEdit.setFixedSize(400,385)
         
    def _file_path(self):           #  The path to the file folder
        absFilePath = os.path.abspath(__file__)
        pather, filename = os.path.split(absFilePath)
        if not os.path.isdir(pather + "/" + "note" ):
            os.chdir(pather)
            os.mkdir("note")
            print(pather)
            path = (f'{pather}\\note')
        else:
            path = (f'{pather}\\note') 
        self.file_path = path

    def _List_of_file(self):            # List file in Directory
        self.List_of_file = [os.path.splitext(filename)[0] for filename in os.listdir(self.file_path)]
          
    # def file_name (self):
    #     self.name_file = str(self.ListItem.currentItem().text() + '.txt') 
        
    def _write_list_widget(self):               # Write notes in the list widget
        for n in self.List_of_file:       
            QListWidgetItem(n, self.ListItem)

    def open_file (self):         # Open the file for reading
        self.name_file = str(self.ListItem.currentItem().text() + '.txt')
        f = open(f'{self.file_path}\\{self.name_file}', 'r')
        with f:
            date = f.read()
        self.TextEdit.setText(date)
       
    def save_file(self):         # Save the file (note)
        self.name_file = str(self.ListItem.currentItem().text() + '.txt')
        f = open(f'{self.file_path}\\{self.name_file}', 'w' )
        text = self.TextEdit.toPlainText()
        f.write(text)
        f.close()
    
    def new_file (self):          # Create a new file (note)
        self.TextEdit.clear()
        text, ok = QInputDialog.getText(self, 'New_Note', 'Назва нової нотатки')
        if  ok :
            QListWidgetItem(text, self.ListItem)    
       
    def removeSel(self):          # Delete the file (note)
        self.name_file = str(self.ListItem.currentItem().text() + '.txt')
        os.remove(f'{self.file_path}\\{self.name_file}')
        self.TextEdit.clear()
        
        listItems=self.ListItem.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.ListItem.takeItem(self.ListItem.row(item))
        

def note ():
    app = QApplication(sys.argv)
    window = Interfce()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__': 
    note()