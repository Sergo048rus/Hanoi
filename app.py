########### import ###########
import sys

from PyQt5        import (QtGui, QtWidgets)
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot, QTimer)


class HanoiApp(): 
    ''' Класс приложения, запускает консоль и GUI    \n
        GUI <---> CONSOLE \n
        signalStartOrder [str][filename]  ---> \n
        signalStartOpti  [str][filename]  ---> \n
        <--- signalOrderResponse [dict][status(read+order+graph) + rodCostList + diskCount + solutionGraph] \n
        <--- signalOptiResponse  [dict][status(read+order+graph) + TODO ] \n
    '''
    def __init__(self): 
        self.app = QtWidgets.QApplication([])  # we could add args and so on

        self.threadConsole = ConsoleThread()    # inherits QThread http://qt-project.org/doc/latest/qthread.html
        self.threadGui     = QtGuiThread()      # inherits QtGui.QWidget

        self.threadConsole.finished.connect(self.app.exit)
        self.threadConsole.start()

        self.threadGui.finished.connect(self.app.exit)
                    
        sys.exit(self.app.exec_())


########### main ###########   
if __name__ == '__main__':
    app = HanoiApp()

    