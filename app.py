########### import ###########
import sys

from PyQt5        import (QtGui, QtWidgets)
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot, QTimer)

from hanoi_console import ConsoleThread


class HanoiApp(): 
    ''' Класс приложения, запускает консоль и GUI    
        GUI <---> CONSOLE \n
        signalStartOrder [str][filename]  ---> \n
        signalStartOpti  [str][filename]  ---> \n
        <--- signalOrderResponse [dict][status(read+order+graph) + rodCostList + diskCount + solutionGraph] \n
        <--- signalOptiResponse  [dict][status(read+order+graph) + TODO ] \n

        1. Создаются объекты классов консоли и интерфейса
        2. В классах объявляются соответствующие слоты и сигналы (см. hanoi_console)
        3. Подключение слотов к сигналам производится в конструкторе этого класса 
        Схема: mainThread -> dummyThreads
    '''

    def __init__(self): 
        self.app = QtWidgets.QApplication([])  # we could add args and so on

        self.threadConsole = ConsoleThread()    # inherits QThread http://qt-project.org/doc/latest/qthread.html
        # self.threadGui     = QtGuiThread()      # inherits QtGui.QWidget # ! TODO: uncomment when connected

        self.threadConsole.finished.connect(self.app.exit)
        self.threadConsole.start()

        # self.threadGui.finished.connect(self.app.exit)  # ! TODO: uncomment when connected
                    
        sys.exit(self.app.exec_())


########### main ###########   
if __name__ == '__main__':
    app = HanoiApp()

    