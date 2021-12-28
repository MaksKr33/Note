from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QInputDialog,  QMainWindow, QHBoxLayout, QApplication, QPushButton,  QListWidgetItem, QPlainTextEdit
from PyQt5.QtGui import *
import sys
import os 

class Interfce(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        
        self._spusok_file()
        self.ListItem()
        self.fillle()
        self.func()
        # self.file_name()
        self.__mainText()
        self._save_button()
        self._delete_button()
        self._add_button()
        self._note_text()
        
        self.setWindowTitle ('Нотатки')
        self.setGeometry(350 ,200, 600 ,500)
        self.originalPalette = QApplication.palette()

    def __mainText(self): 
        self.text = QtWidgets.QLabel(self)    
        self.text.setText("Назва / Заголовок" )
        self.text.move(270,15 )
        self.text.setFixedWidth(200)
        self.text.setFont(QFont('Arial', 18))
    
    def ListItem (self):    
        self.Qlist = QtWidgets.QListWidget(self)
        self.Qlist.move(10,10)
        self.Qlist.setFixedSize (150,430)  
        self.Qlist.itemActivated.connect(self.open_file)
        self.Qlist.setFont(QFont('Arial', 14))
        self.Qlist.setStyleSheet("background-color: #E0FFFF")
       
    def _save_button (self):
        self.save = QPushButton(self)
        self.save.move(270,460)
        self.save.setText('Save')
        self.save.setFont(QFont('Arial', 14))
        self.save.clicked.connect(self.save_file)

    def _delete_button (self):
        self.delete = QPushButton(self)
        self.delete.move(430,460)
        self.delete.setText('Delete')
        self.delete.setFont(QFont('Arial', 14))
        self.delete.clicked.connect(self.removeSel)

    def _add_button (self):
        self.add = QPushButton(self)
        self.add.move(40,460)
        self.add.setText('+')
        self.add.setFont(QFont('Arial',18))
        self.add.clicked.connect(self.new_file)

    def _note_text(self):
        self.note_text  = QtWidgets.QTextEdit(self)
        self.note_text.setStyleSheet("background-color: #FFFF99")
        self.note_text.setObjectName("plainTextEdit")
        self.note_text.setFont(QFont('Arial',12))
        self.note_text.move(170,55)
        self.note_text.setFixedSize(400,385)
         
    def _spusok_file(self):
        absFilePath = os.path.abspath(__file__)
        pather, filename = os.path.split(absFilePath)
        if not os.path.isdir(pather + "/" + "note" ):
            os.chdir(pather)
            os.mkdir("note")
            print(pather)
            path = (f'{pather}\\note')
        else:
            path = (f'{pather}\\note') 
        self.pather = path

    def fillle(self):            # List file in Directory
        self.files = [os.path.splitext(filename)[0] for filename in os.listdir(self.pather)]
          
    # def file_name (self):
    #     self.name_file = str(self.Qlist.currentItem().text() + '.txt') 
        
    def func(self):               # Write notes in the list widget
        for n in self.files:       
            QListWidgetItem(n, self.Qlist)

    def open_file (self):         # Open the file for reading
        self.name_file = str(self.Qlist.currentItem().text() + '.txt')
        f = open(f'{self.pather}\\{self.name_file}', 'r')
        with f:
            date = f.read()
        self.note_text.setText(date)
       
    def save_file(self):         # Save the file (note)
        self.name_file = str(self.Qlist.currentItem().text() + '.txt')
        f = open(f'{self.pather}\\{self.name_file}', 'w' )
        text = self.note_text.toPlainText()
        f.write(text)
        f.close()
    
    def new_file (self):          # Create a new file (note)
        self.note_text.clear()
        text, ok = QInputDialog.getText(self, 'New_Note', 'Назва нової нотатки')
        if  ok :
            QListWidgetItem(text, self.Qlist)    
       
    def removeSel(self):          # Delete the file (note)
        self.name_file = str(self.Qlist.currentItem().text() + '.txt')
        os.remove(f'{self.pather}\\{self.name_file}')
        self.note_text.clear()
        
        listItems=self.Qlist.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.Qlist.takeItem(self.Qlist.row(item))
        

def note ():
    app = QApplication(sys.argv)
    window = Interfce()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__': 
    note()