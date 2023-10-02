# from typing import Optional
# import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QWidget




class mywindow(QMainWindow):

     def __init__(self, parent=None):
        super().__init__(parent)

        central_widget = QWidget()  # Crie um widgets
        self.setCentralWidget(central_widget)  # Defina o widgets na janela ; tb conhecido como widge central

        layout = QGridLayout(central_widget)  # Defina o layout no widget central

        btt = QPushButton("testando")# estilo de btt
        btt.setStyleSheet('font-size: 50px;')
        layout.addWidget(btt,1,1) #adicionando botoes no canto que eu quero 

        btt2 = QPushButton("testando")# estilo de btt
        btt2.setStyleSheet('font-size: 50px;')
        layout.addWidget(btt2,2,2)#adicionando botoes no canto que eu quero 

       

if __name__ == '__main__':
    app = QApplication([])  # Inicialize a aplicação
    window = mywindow()
    window.show()
    app.exec()  # O loop da aplicação