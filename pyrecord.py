from datetime import date
import sys

class Record:
    def __init__(self,date,category,acti,cost):
        '''
        initialization of record
        '''
        self._category = category
        self._acti = acti
        self._cost = cost
        self._date = date
    
    @property
    def category(self):
        return self._category
    @property
    def acti(self):
        return self._acti
    @property
    def cost(self):
        return self._cost
    @property
    def date(self):
        return self._date
    

class Records:

    def __init__(self):
        '''
        initiate the records from 'records.txt' and assign to attribute
        '''
        def initialize():
            '''
            inner function in __init__ in order to read and get the record
            '''
            acti = []
            cost = []
            cate = []
            datetime = []
            money = 0
            temp_record = []
            try:
                with open('records.txt','r') as fh:
                    try:
                        money = int(fh.readline())
                        #read the inital money in first line of the record
                    except ValueError:
                        sys.stderr.write('Can not read the initial money.\n')

                    temp_record = fh.readlines()
                try:#read date time
                    temp_date = temp_record[0].split('[')[1]
                    temp_date = temp_date.split(']')[0]
                except:
                    sys.stderr.write("Can not read the record of date time.\n")

                try: #read activities
                    temp_acti = temp_record[1].split('[')[1]
                    temp_acti = temp_acti.split(']')[0]
                except:
                    sys.stderr.write("Can not read the record of activities.\n")

                try: #read cost
                    temp_cost = temp_record[2].split('[')[1]
                    temp_cost = temp_cost.split(']')[0]
                except:
                    sys.stderr.write("Can not read the record of cost.\n")

                try: #read categories
                    temp_cate = temp_record[3].split('[')[1]
                    temp_cate = temp_cate.split(']')[0]
                except:
                    sys.stderr.write("Can not read the record of cate.\n")

                #convert them into acti[] and cost[]
                try:
                    for i in range(len(temp_acti.split(','))):
                        temp = temp_acti.split(',')[i]
                        temp = temp.split('\'')[1]
                        acti.append(temp)
                except:
                    sys.stderr.write("Can not append the acti into program.\n")

                try:
                    for j in range(len(temp_cost.split(','))):
                        temp = temp_cost.split(',')[j]
                        temp = temp.split('\'')[1]
                        cost.append(temp)
                except:
                    sys.stderr.write("Can not append the cost into program.\n")
                try:
                    for k in range(len(temp_cate.split(','))):
                        temp = temp_cate.split(',')[k]
                        temp = temp.split('\'')[1]
                        cate.append(temp)
                except:
                    sys.stderr.write("Can not append the cate into program.\n")

                try:
                    for c in range(len(temp_date.split(','))):
                        temp = temp_date.split(',')[c]
                        temp = temp.split('\'')[1]
                        datetime.append(temp)
                except:
                    sys.stderr.write("Can not append the datetime into program.\n")

                if (acti == [] or cost == [] or cate == [] or datetime == []):
                    sys.stderr.write('Empty record\n')
                    try:
                        #money = int(input("How much money do you have?"))
                        money = 0
                        #return [int(money),temp_record]
                    except ValueError:
                        money = 0
                        sys.stderr.write("Input is not an integer.Set 0 as default value.\n")
                else:
                    print('Load file complete.')

            except FileNotFoundError:
                print("File no found.")
                try:
                    #money = int(input("How much money do you have?"))
                    money = 0
                    #return [int(money),temp_record]
                    #return [money,Record([],[],[],[])]
                except ValueError:
                    sys.stderr.write("Input is not an integer.Set 0 as initial value.\n")
                    money = 0
            temp_record = []
            for i in range(len(acti)):      
                additem = Record(datetime[i],cate[i],acti[i],cost[i])
                temp_record.append(additem)
                
            return [int(money),list(temp_record)]
        
        temp = initialize()
        self._money = temp[0]
        self._records = temp[1]
        #print(type(self._records),type(self._records[0]._date))
        


    def add(self,record,categories):
        '''
        add a new enent to the object,including category,activity,cost
        in the meanwhile, check whether the category is in categories
        '''
        given_date = True
        today = ''
        try:
            check_date = record.split(' ')[0]
            date.fromisoformat(check_date)
        except:
            check = list(check_date)
            try:#Wrong format
                int(check[1])
                sys.stderr.write('The format of date should be YYYY-MM-DD.\nFail to add a record.')
                return
            except:#Without date
                today = date.today()
                today = str(today)
                given_date = False
        if(given_date == True):
            try:
                if(categories.is_category_valid(record.split(' ')[1]) == False):
                    print("Please add it's categories.")
                    return 
                try:
                    self._money += int(record.split(' ')[3])
                except ValueError:
                    sys.stderr.write('Second input can not convert into integer.\n')
            
                temp = Record(record.split(' ')[0],record.split(' ')[1],record.split(' ')[2],record.split(' ')[3])
            
            
                self._records.append(temp)
            except:
                sys.stderr.write('Input can not convert into record.\n')
        else:
            try:
                if(categories.is_category_valid(record.split(' ')[0]) == False):
                    print("Please add it's categories.")
                    return 
                try:
                    self._money += int(record.split(' ')[2])
                except ValueError:
                    sys.stderr.write('Second input can not convert into integer.\n')
            
                temp = Record(today,record.split(' ')[0],record.split(' ')[1],record.split(' ')[2])
            
            
                self._records.append(temp)
            except:
                sys.stderr.write('Input can not convert into record.\n')
        return

    def view(self):
        '''
        print a table which show that the detail of record and the total of money
        '''
        print('\n%-10s %-15s %-20s %-6s' % ('Datetime','Categories','Description','Amount'))
        print('=' * 10,'=' * 15,'=' * 20,'=' * 6)
        for i in range(len(self._records)):
            print('%-10s %-15s %-20s %-6s' % (self._records[i]._date,self._records[i]._category,self._records[i]._acti,self._records[i]._cost))

        print('=' * 10 ,'=' * 15,'=' * 20,'=' * 6,f'\nNow you have {self._money} dollars.\n')
        return
   
    def delete(self,del_record):
        '''
        according to the parameter,delete the corresponding records in the object and update its money
        '''
        try:
            cate_del = del_record.split(' ')[0]
            acti_del = del_record.split(' ')[1]
            cost_del = del_record.split(' ')[2]
        except:
            print('Error form of input.')
        find = 0 #to check whether the record find corresponding input
        for i in range(len(self._records)):
            if(self._records[i]._acti == acti_del and self._records[i]._cost == cost_del and self._records[i]._category == cate_del):
                find = i
                break

        #recover the total_money and delete item
        #index = int(input(f'Choose which index of the records to delete.index:{correspond_index}\n'))
        self._money -= int(self._records[find]._cost)

        del(self._records[find])
        return


    def save(self):
        '''
        save the object's information into 'records.txt'
        '''
        try:
            with open('records.txt','w') as fh:
                fh.write(str(self._money))
                #fh.writelines('\n' + str(self._records[0]) + '\n' + str(self._records[1]) + '\n' + str(self._records[2]))
                length = len(self._records)
                fh.writelines('\n' + str([self._records[i]._date for i in range(length)]) +'\n'+ str([self._records[i]._acti for i in range(length)])+'\n'+ str([self._records[i]._cost for i in range(length)]) + '\n'+ str([self._records[i]._category for i in range(length)]))
            print('Save complete.')
        except:
            sys.stderr.write('Cannot save file.\n')
        finally:
            print('Exit the Pymoney program.')
        return
    def find(self,result):
        '''
        according to the parameter which passed by find_subcategories(),print corresponding records
        '''
        result = list(result)
        
        #print('\n%-10s %-15s %-20s %-6s' % ('Datetime','Categories','Description','Amount'))
        #print('=' * 10 , '=' * 15,'=' * 20,'=' * 6)
        total = 0
        output = []
        for i in range(len(self._records)):
            if(self._records[i]._category in result):
                #print('%-10s %-15s %-20s %-6s' % (self._records[i]._date,self._records[i]._category,self._records[i]._acti,self._records[i]._cost))
                output.append(Record(self._records[i]._date,self._records[i]._category,self._records[i]._acti,self._records[i]._cost))
                total += int(self._records[i]._cost)
    
        #print('=' * 10 ,'=' * 15,'=' * 20,'=' * 6,f'\nTotal amount above is {total} dollars.\n')
        return [total,output]



