from typing import Optional
from PySide6.QtWidgets import QPushButton,QGridLayout

from padroes import MEDIU_FONT_SIZE

class Button(QPushButton):
    def __init__(self):
        super().__init__()
        self.confstyle()


    def confstyle(self):
        font = self.font()
        font.setPixelSize(MEDIU_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setProperty('cssClass', 'specialButton')



class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]