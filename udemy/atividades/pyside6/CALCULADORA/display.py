from PySide6.QtWidgets import QLineEdit,QLabel,QWidget
from padroes import BIG_FONT_SIZE,MENOR_FONT_SIZE,TEXT_MARGIN
from PySide6.QtCore import Qt




class Display(QLineEdit):
    def __init__(self,*args) :
        super().__init__(*args)
        self.confdisplay()
       



    def confdisplay(self):
        self.setStyleSheet(f'font-size:{BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE*2)
        self.setMinimumWidth(MENOR_FONT_SIZE)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

        margies = [TEXT_MARGIN for _ in range(4)]
        #isso é o mesmo que repetir 4 a palavra TEXT_MARGIN
        #EXEMPLO ............
        # LISTA = ["X"]*4
        # print(*LISTA)
        #.....................
        self.setTextMargins(*margies)
        
class info(QLabel):
    def __init__(self,text: str , parent: QWidget | None = None) -> None:
        super().__init__(text,parent)
        self.configstyle()

    def configstyle(self):
        self.setStyleSheet(f"font-size:{MENOR_FONT_SIZE}px;")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

    
