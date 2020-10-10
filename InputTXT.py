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

class listOrder():
    def __init__(self) -> None:
        self.disk       = 0
        self.columnFrom = 0
        self.columnTo   = 0



class InputTXT():
    def __init__(self) -> None:
        self.statusErr = enumErr()
        
        self.returnErr = self.statusErr.noErr
        self.numColumn = 0
        self.numDisk = 0
        self.buff = ''
        self.diskCost = []
        
        self.order = []

    
    def ReadDisk(self,fileName) -> int:
        try:
            self.f = open(fileName)
        except Exception:
            self.returnErr = self.statusErr.errFile
        if self.returnErr != self.statusErr.errFile:
            l = [line.strip() for line in self.f]
            self.f.close()
            # print(l)
            nparts = ''
            for i in range(0,6):
                nparts = nparts + l[CONST_NPARTS][i]
            if nparts == 'NPARTS':  
                self.buff = ''          
                for i in range(7,len(l[CONST_NPARTS])):
                    self.buff = self.buff + l[CONST_NPARTS][i]
                try:
                    self.numDisk = int(self.buff)                       # Определение количества дисков
                except ValueError:
                    self.returnErr = self.statusErr.errDisk

                self.buff = ''                                          # Обнуляем буфер

                if self.numDisk > 20 or self.numDisk <= 0:
                    self.returnErr = self.statusErr.errDisk
            else:
                self.returnErr = self.statusErr.errFile
            if l[CONST_COST] == 'COST':  
                self.buff = ''                                 
                for i in range(len(l[CONST_COLUMN])):                   # Определение цены штырей и их количества
                    if l[CONST_COLUMN][i] == ' ':
                        self.numColumn = self.numColumn + 1
                        try:
                            if int(self.buff) > 0:
                                self.diskCost.append(int(self.buff))
                            else:
                                self.diskCost.append(int(self.buff))
                                self.returnErr = self.statusErr.errColumn
                        except ValueError:
                            self.returnErr = self.statusErr.errColumn
                        self.buff = ''
                    else:
                        self.buff = self.buff + l[CONST_COLUMN][i]
                self.numColumn = self.numColumn + 1                      # Добавляем последнее значение
                try:
                    self.diskCost.append(int(self.buff))
                except ValueError:
                    self.returnErr = self.statusErr.errColumn

            else:
                self.returnErr = self.statusErr.errFile

            return int(self.numDisk),int(self.numColumn),self.diskCost,self.returnErr
        
    def ReadOrder(self,fileName):
        self.returnErr = self.statusErr.noErr
        try:
            self.f = open(fileName)
        except Exception:
            self.returnErr = self.statusErr.errFile
        if self.returnErr != self.statusErr.errFile:
            l = [line.strip() for line in self.f]
            self.f.close()
            print(l)

            if l[CONST_ORDER] == 'ORDER':  
                self.buff = ''
                lineOrder = CONST_ORDER + 1                             # Стартуем со следующей строки
                while l[lineOrder][0] != '/':
                    buffOrder = listOrder()
                    self.buff = ''  
                    count = 1                               
                    for i in range(len(l[lineOrder])):                   # Определение цены штырей и их количества
                        if l[lineOrder][i] == ' ' and count == 1:
                            try:
                                buffOrder.disk = int(self.buff)
                                if buffOrder.disk > self.numDisk - 1 or buffOrder.disk < 0:
                                    self.returnErr = self.statusErr.errOrder
                            except ValueError:
                                self.returnErr = self.statusErr.errOrder
                            self.buff = ''
                            count = count + 1
                        else: 
                            if l[lineOrder][i] == ' ' and count == 2:
                                try:
                                    buffOrder.columnFrom = int(self.buff)
                                    if buffOrder.columnFrom > self.numColumn - 1 or buffOrder.columnFrom < 0:
                                        self.returnErr = self.statusErr.errOrder
                                except ValueError:
                                    self.returnErr = self.statusErr.errOrder
                                self.buff = ''
                                count = 1
                            else:
                                self.buff = self.buff + l[lineOrder][i]

                    try:
                        buffOrder.columnTo = int(self.buff)
                        if buffOrder.columnTo > self.numColumn - 1 or buffOrder.columnTo < 0:
                                        self.returnErr = self.statusErr.errOrder
                        self.order.append(buffOrder)
                    except ValueError:
                        self.returnErr = self.statusErr.errOrder  

                    lineOrder = lineOrder + 1                           # Переходим на следующую линию
                self.sizeOrder = lineOrder - CONST_ORDER-1
        return self.order, self.sizeOrder, self.returnErr

  


test = InputTXT()


disk, column, diskCost, err = test.ReadDisk('FileInit.txt')
print(' Disk = ',disk,'\n','Column = ', column,'\n','Err = ', err,'\n', 'Cost', diskCost)

order,sizeOrder, returnErr = test.ReadOrder('FileInit.txt')
print('Err = ', returnErr)
for i in range(0, sizeOrder):
    print(' disk  = ',order[i].disk, 'columnFrom = ',order[i].columnFrom, 'columnTo = ',order[i].columnTo,'\n')
