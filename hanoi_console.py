########### import ###########
from PyQt5        import (QtGui, QtWidgets)
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot)
import InputTXT as par
import time # ! to be deleted

# Subclassing QThread http://qt-project.org/doc/latest/qthread.html
class ConsoleThread(QThread):
    # signals
    signalOrderResponse = pyqtSignal(dict)
    signalOptiResponse  = pyqtSignal(dict)

    def __init__(self):
        super(ConsoleThread, self).__init__()

    def run(self):
        counter = 0

        while True:
            time.sleep(1)
            print("console tick: {0}".format(counter))
            counter += 1
            # time.sleep(SSH_READ_TIMEOUT)
            # self.internal_counter += 1

            # #print("thread wake-up {0}".format(self.internal_counter))
            # self.itv_signal_connstat.emit(connstatus)
            # self.itv_signal_alarm_global.emit(alarm_states[0]) 
            # self.itv_signal_alarm_cnt.emit(alarm_states[1:])  
            # self.itv_signal_counter.emit(counters) 
            # self.itv_signal_plot.emit([x,ylist])

    ########### signal handlers ###########
    @pyqtSlot()
    def slotStartOrder(self, filename):
        print("slotStartOrder")
        # numDisk, numColumn, Cost, err = self.parser.ReadDisk(self.filename)
    


        
    @pyqtSlot()
    def slotStartOpti(self, filename):
        print("slotStartOpti")
        # numDisk, numColumn, Cost, err = self.parser.ReadDisk(self.filename)
