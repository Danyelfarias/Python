from typing import Optional
from PySide6.QtWidgets import  QBoxLayout, QMainWindow,  QWidget, QGridLayout



class MainWindow(QMainWindow):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)

        self.centra_widget = QWidget()# definicao para possibilitar wigts

        self.layout = QBoxLayout(QBoxLayout.TopToBottom)  # Definindo o layout como caixa vertical

        self.centra_widget.setLayout(self.layout)#definindo o tipo de layout do widget

        self.setCentralWidget(self.centra_widget)# no centro do corpo vai ter widgets
        self.setWindowTitle("calculadora")
    def adjustFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())#fixixanod tamanho e largura da janela
    
    
    def addWidgetToVLayout(self, widget: QWidget):
        self.layout.addWidget(widget)


    def gridLayout(self, widget: QWidget):
        self.layout= QGridLayout()
        self.layout.addLayout(QGridLayout)


