#Constant
CONST_NPARTS = 1
CONST_COST   = CONST_NPARTS + 3
CONST_COLUMN = CONST_COST + 1
CONST_ORDER  = CONST_COST + 4


class InputTXT():
    def __init__(self) -> None:
    
        self.numColumn = 0
        self.numDisk = 0
        self.buff = ''
        self.diskCost = []
        
        self.order = []

    
    def ReadDisk(self,fileName) -> int:
        self.returnErr = 'OK'
        try:
            self.f = open(fileName)
        except Exception:
            self.returnErr = 'File is not exist'
        if self.returnErr == 'OK':
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
                    self.returnErr = 'Init: The disk is not a number'

                self.buff = ''                                          # Обнуляем буфер

                if self.numDisk > 20 or self.numDisk <= 0:
                    self.returnErr = 'Init: Disk greater than the maximum or less than zero'
            else:
                 self.returnErr = 'Err file!!!!!!!'
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
                                self.returnErr = 'Init: Rod greater than the maximum or less than zero'
                        except ValueError:
                             self.returnErr = 'Init: The rod is not a number'
                        self.buff = ''
                    else:
                        self.buff = self.buff + l[CONST_COLUMN][i]
                self.numColumn = self.numColumn + 1                      # Добавляем последнее значение
                try:
                    self.diskCost.append(int(self.buff))
                except ValueError:
                    self.returnErr = 'Init: The rod is not a number'

            else:
                 self.returnErr = 'Err file!!!!!!!'

            return int(self.numDisk),int(self.numColumn),self.diskCost,self.returnErr
        
    def ReadOrder(self,fileName):
        self.returnErr = 'OK'
        try:
            self.f = open(fileName)
        except Exception:
            self.returnErr = 'File is not exist'
        if self.returnErr == 'OK':
            l = [line.strip() for line in self.f]
            self.f.close()
            # print(l)

            if l[CONST_ORDER] == 'ORDER':  
                self.buff = ''
                lineOrder = CONST_ORDER + 1                             # Стартуем со следующей строки
                while l[lineOrder][0] != '/':
                    # buffOrder = listOrder()
                    buffOrder = {}
                    self.buff = ''  
                    count = 1                               
                    for i in range(len(l[lineOrder])):                   # Определение цены штырей и их количества
                        if l[lineOrder][i] == ' ' and count == 1:
                            try:
                                buffOrder['dI'] = int(self.buff)
                                if buffOrder['dI'] > self.numDisk - 1 or buffOrder['dI'] < 0:
                                    self.returnErr = 'Order: Disk greater than the maximum or less than zero'
                            except ValueError:
                                self.returnErr = 'Order: The disk is not a number'
                            self.buff = ''
                            count = count + 1
                        else: 
                            if l[lineOrder][i] == ' ' and count == 2:
                                try:
                                    buffOrder['rSrc'] = int(self.buff)
                                    if buffOrder['rSrc'] > self.numColumn - 1 or buffOrder['rSrc'] < 0:
                                        self.returnErr = 'Order: Rod greater than the maximum or less than zero'
                                except ValueError:
                                    self.returnErr = 'Order: The rod is not a number'
                                self.buff = ''
                                count = 1
                            else:
                                self.buff = self.buff + l[lineOrder][i]

                    try:
                        buffOrder['rDst'] = int(self.buff)
                        if buffOrder['rDst'] > self.numColumn - 1 or buffOrder['rDst'] < 0:
                            self.returnErr = 'Order: Rod greater than the maximum or less than zero'
                        self.order.append(buffOrder)
                    except ValueError:
                        self.returnErr = 'Order: The rod is not a number'  

                    lineOrder = lineOrder + 1                           # Переходим на следующую линию
                self.sizeOrder = lineOrder - CONST_ORDER-1
        return self.order, self.sizeOrder, self.returnErr

  


if __name__ == "__main__":  
    test = InputTXT()

    FILENAME = "tests_file/Test1.txt" 
    disk, column, diskCost, err = test.ReadDisk(FILENAME)
    print(' Disk = ',disk,'\n','Column = ', column,'\n','Err = ', err,'\n', 'Cost', diskCost)

    order,sizeOrder, returnErr = test.ReadOrder(FILENAME)
    print('Err = ', returnErr)
    for i in range(0, sizeOrder):
        print(' disk  = ',order[i]['dI'], 'columnFrom = ',order[i]['rSrc'], 'columnTo = ',order[i]['rDst'],'\n')
