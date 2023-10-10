
from PySide6.QtWidgets import QApplication

from main import MainWindow #chamando o outro arquivo que tem os dados
from PySide6.QtGui import QIcon
from padroes import widgetFile
from display import Display,info
from styles import setupthema
from btt import Button,ButtonsGrid
app = QApplication([])# inicializador 
setupthema()#feito pela funça que esta no arquivo styles , sempre colocar ele depois do aplication , pra noa dar erro.
window= MainWindow()# corpo definido no outro arquivo

# adicionando btt para teste
# label1 = QLabel('O meu texto')
# label1.setStyleSheet('font-size: 50px;')
# window.layout.addWidget(label1)
# pushbott = QPushButton('push btt')
# pushbott.setStyleSheet('font-size: 50px;')
# window.layout.addWidget(pushbott)
# window.adjustFixedSize()


#adiiconando icon

icon = QIcon(str(widgetFile)) #deixar ssempre em str para dar certo
window.setWindowIcon(icon)
app.setWindowIcon(icon)

#informaçoes do calculo
info= info("8+9")
window.addWidgetToVLayout(info)

#adicionando display
display = Display()
window.addWidgetToVLayout(display)#essa é uma funçao que foi feita no main que automaticamnte adiciona os item no layout

#convocando estilio gride de layout 
# bttgrid = ButtonsGrid()
# window.layout=bttgrid
# bttgrid.addWidget(Button)
btt = Button()
window.addWidgetToVLayout(btt)
btt = Button()
window.addWidgetToVLayout(btt)
btt = Button()
window.addWidgetToVLayout(btt)
# window.gridLayout(btt)

window.adjustFixedSize()




window.show()

app.exec()


