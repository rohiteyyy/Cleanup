from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget 

from cheeky import cleanup

import sys
import os
cwd = os.getcwd()

class WelcomeScreen (QDialog):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi('gui.ui',self)
        self.getstarted.clicked.connect(self.gotostarted)
    
    def gotostarted(self):
        started = StartedScreen()
        widget.addWidget(started)
        widget.setCurrentIndex(widget.currentIndex()+1)


class StartedScreen(QDialog): 
    def __init__(self):
        super(StartedScreen, self).__init__()
        loadUi('firstime.ui',self)

        try:
            file = open('data.txt','r+')
            inp = file.readlines()
            temp = (inp[0].split('\n')[0])
            self.tempfield.setText(temp)
            modtemp = (inp[1].split('\n')[0])
            self.modtempfield.setText(modtemp)
            prefetch = (inp[2].split('\n')[0])
            self.prefetchfield.setText(prefetch)
            softdis = (inp[3].split('\n')[0])
            self.softdisfield.setText(softdis)
            file.seek(0)
            file.close()
            
        except:
            pass

        self.startcleanup.clicked.connect(self.cleanupfunction)

    def cleanupfunction(self):
        file = open('data.txt','w+')
        temp = self.tempfield.text()
        modtemp = self.modtempfield.text()
        prefetch = self.prefetchfield.text()
        softdis = self.softdisfield.text()
        file.writelines([temp+'\n',modtemp+'\n',prefetch+'\n',softdis])
        file.seek(0)
        file.close()
        
        if len(temp)==0 or len(modtemp)==0 or len(prefetch)==0 or len(softdis)==0:
            self.error.setText('*Please input all fields')
        else:
            self.error.setText('')    
            
            pro1 = cleanup(temp)
            pro2 = cleanup(modtemp)
            pro3 = cleanup(prefetch)
            pro4 = cleanup(softdis)
            if pro1 == True and pro2 == True and pro3 == True and pro4==True:
                os.chdir(cwd)
                finished = FinishedScreen()
                widget.addWidget(finished)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                self.error.setText('*Following director[y]/[ies] is incorrect')
            

class FinishedScreen(QDialog):
    def __init__(self):
        super(FinishedScreen, self).__init__()
        loadUi('finish.ui',self)

#main
app = QApplication(sys.argv)

welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setWindowTitle('Cleanup')
widget.setWindowIcon(QIcon('roxy.jpg'))
widget.setFixedHeight(801)
widget.setFixedWidth(1011)
widget.show()
try:
    sys.exit(app.exec())
except:
    print('Exiting')

