########### import ###########
from PyQt5        import (QtGui, QtWidgets)
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot)


# Subclassing QThread http://qt-project.org/doc/latest/qthread.html
class ConsoleThread(QThread):
    # signals
    signalOrderResponse = pyqtSignal(dict)
    signalOptiResponse  = pyqtSignal(dict)

    def __init__(self):
        super(ConsoleThread, self).__init__()

    def run(self):
        while True:
            pass
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
        
    @pyqtSlot()
    def slotStartOpti(self, filename):
        print("slotStartOpti")
        
