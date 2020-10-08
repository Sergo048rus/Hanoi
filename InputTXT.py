

#Constant
CONST_NPARTS = 1
CONST_COST   = CONST_NPARTS + 3
CONST_COLUMN = CONST_COST + 1
CONST_ORDER  = CONST_COST + 4
class enumErr():
    def __init__(self) -> None:
        self.noErr        = 0
        self.errDisk      = 1
        self.errColumn    = 2
        self.errOrder     = 3
        self.errFile      = 4

class InputTXT():
    def __init__(self) -> None:
        self.statusErr = enumErr()
        self.returnErr = self.statusErr.noErr
        self.numColumn = 0
        self.numDisk = 0
        self.buff = ''
        self.diskCost = []
        self.counter = 0
    
    def ReadDisk(self,fileName) -> int:
        try:
            self.f = open(fileName)
        except Exception:
            self.returnErr = self.statusErr.errFile
        if self.returnErr != self.statusErr.errFile:
            l = [line.strip() for line in self.f]
            self.f.close()
            print(l)
            if l[CONST_NPARTS] == 'NPARTS':  
                self.buff = ''          
                for i in range(0,len(l[CONST_NPARTS])):
                    self.buff = self.buff + l[CONST_NPARTS][i]
                try:
                    self.numDisk = int(self.buff)               # Определение количества дисков
                except ValueError:
                    self.returnErr = self.statusErr.errDisk

                self.buff = ''                                  #Обнуляем буфер

                if self.numDisk > 20 or self.numDisk <= 0:
                    self.returnErr = self.statusErr.errDisk
            else:
                self.returnErr = self.statusErr.errFile
            if l[CONST_COST] == 'COST':                                  # Определение цены штырей и их количества
                for i in range(len(l[CONST_COLUMN])):
                    if l[CONST_COLUMN][i] == ' ':
                        self.numColumn = self.numColumn + 1
                self.numColumn = self.numColumn + 1                      # Добавляем последнее значение
                # for i in range(0,len(l[CONST_COLUMN]),2):

                #     try:
                #         self.diskCost = int(l[CONST_COLUMN][i])
                #     except ValueError:
                #         self.returnErr = self.statusErr.errColumn
            else:
                self.returnErr = self.statusErr.errFile

            return int(self.numDisk),int(self.numColumn),self.diskCost,self.returnErr
  


test = InputTXT()
disk, column, diskCost, err = test.ReadDisk('FileInit.txt')

print('Disk = ',disk,'Column = ', column,'Err = ', err, 'Cost', diskCost)
# print(type(t),t)
