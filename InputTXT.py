#Constant
CONST_NPARTS = 1
CONST_COST   = CONST_NPARTS + 3
CONST_COLUMN = CONST_COST + 1
CONST_ORDER  = CONST_COST + 4


class InputTXT():
    def __init__(self):
    
        self.numColumn = 0
        self.numDisk = 0
        self.buff = ''
        self.diskCost = []
        
        self.order = []

    def __Check_NPARTS(self,l):
        self.line = 0
        try:
            while l[self.line].split()[0] != 'NPARTS':
                self.line = self.line + 1

            self.buff = ''   
            for i in range(0,len(l[self.line].split()[1])):
                self.buff = self.buff + l[self.line].split()[1][i]
            try:
                self.numDisk = int(self.buff)                       # Определение количества дисков
            except ValueError:
                self.returnErr = 'Init: The disk is not a number'

            self.buff = ''                                          # Обнуляем буфер

            if self.numDisk > 20 or self.numDisk <= 0:
                self.returnErr = 'Init: Disk greater than the maximum or less than zero'

            self.line = self.line + 1

        except IndexError:
             self.returnErr = 'Err file!!!!!!!'
        
        self.__Check_COST(l)                    # Вызываем следующий этап проверки
    
    def __Check_COST(self,l):                               
        try:
            while l[self.line] != 'COST':             
                self.line = self.line + 1

            self.buff = ''    
            self.line = self.line + 1

            for i in range(len(l[self.line])):                   # Определение цены штырей и их количества
                if l[self.line][i] == ' ':
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
                    self.buff = self.buff + l[self.line][i]
            self.numColumn = self.numColumn + 1                      # Добавляем последнее значение
            try:
                self.diskCost.append(int(self.buff))
            except ValueError:
                self.returnErr = 'Init: The rod is not a number'

            self.line = self.line + 1
        except IndexError:
            self.returnErr = 'Err file!!!!!!!'
            
    def __RemoveCommentAndSpace(self, l):
            while l.count('') != 0:
                l.remove('')

            for line in l:
                if len(line) > 2:
                    if line[0] == '-' and line[0] == '-':
                        l.remove(line)
            # print(l)

            try:
                for j in range(len(l)):
                    l[j] = l[j].split(' --')[0]

                for j in range(len(l)):
                    l[j] = l[j].split('--')[0]
            except Exception:
                 self.returnErr = 'Err file!!!!!!!'
            return l
    def ReadDisk(self,fileName) -> int:
        self.returnErr = 'OK'
        try:
            self.f = open(fileName)
        except Exception:
            self.returnErr = 'File is not exist'
        if self.returnErr == 'OK':
            l = [line.strip() for line in self.f]
            self.f.close()

            l =self.__RemoveCommentAndSpace(l)
 
            self.__Check_NPARTS(l)
            
            return int(self.numDisk),int(self.numColumn),self.diskCost,self.returnErr
        
    

    def __checkOrder(self,l):
        while l[self.line] != 'ORDER':             
                self.line = self.line + 1
        self.line = self.line + 1
        startOrderLine = self.line

        while l[self.line][0] != '/':
           
            buffOrder = {}
            self.buff = ''  
            count = 1                               
            for i in range(len(l[self.line])):                   # Определение цены штырей и их количества
                if l[self.line][i] == ' ' and count == 1:
                    try:
                        buffOrder['dI'] = int(self.buff)
                        if buffOrder['dI'] > self.numDisk - 1 or buffOrder['dI'] < 0:
                            self.returnErr = 'Order: Disk greater than the maximum or less than zero'
                    except ValueError:
                        self.returnErr = 'Order: The disk is not a number'
                    self.buff = ''
                    count = count + 1
                else: 
                    if l[self.line][i] == ' ' and count == 2:
                        try:
                            buffOrder['rSrc'] = int(self.buff)
                            if buffOrder['rSrc'] > self.numColumn - 1 or buffOrder['rSrc'] < 0:
                                self.returnErr = 'Order: Rod greater than the maximum or less than zero'
                        except ValueError:
                            self.returnErr = 'Order: The rod is not a number'
                        self.buff = ''
                        count = 1
                    else:
                        self.buff = self.buff + l[self.line][i]

            try:
                buffOrder['rDst'] = int(self.buff)
                if buffOrder['rDst'] > self.numColumn - 1 or buffOrder['rDst'] < 0:
                    self.returnErr = 'Order: Rod greater than the maximum or less than zero'
                self.order.append(buffOrder)
            except ValueError:
                self.returnErr = 'Order: The rod is not a number'  

            self.line = self.line + 1                           # Переходим на следующую линию
        self.sizeOrder = self.line - startOrderLine
    


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

            l =self.__RemoveCommentAndSpace(l)

            self.__checkOrder(l)
 
        return self.order, self.sizeOrder, self.returnErr

  


if __name__ == "__main__":  

    test = InputTXT()

    FILENAME = "tests_file/oks_t2.txt" 
    disk, column, diskCost, err = test.ReadDisk(FILENAME)
    print(' Disk = ',disk,'\n','Column = ', column,'\n','Err = ', err,'\n', 'Cost', diskCost)

    order,sizeOrder, returnErr = test.ReadOrder(FILENAME)
    print(len(order), sizeOrder)
    print('Err = ', returnErr)
    for i in range(0, sizeOrder):
        print(' disk  = ',order[i]['dI'], 'columnFrom = ',order[i]['rSrc'], 'columnTo = ',order[i]['rDst'],'\n')
