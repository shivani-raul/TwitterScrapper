import csv
import logging
logging.basicConfig(level=logging.INFO)
class parsing:  

    def __init__(self,filename,header,value):
        self.header=header
        self.value=value
        self.filename=filename
        #self.read(self.filename)
        self.write(filename,self.header,self.value)

    def read(self,filename):
        with open('{}'.format(filename),'r') as infile:
            reader=csv.reader(infile,delimiter=",") #change delimeter as per requirement
            self.header=next(reader)
            self.value=[]
            #print(value)
            for row in reader:
                self.value.append(row)
            logging.info('Reading CSV Successfull')
            #print(value)
            #print("success--read")

            
    def write(self,filename,header,value):
        self.header=header
        self.value=value
        with open('{}'.format(filename),'w') as infile:
            writer=csv.writer(infile)
            writer.writerow(self.header)
            writer.writerows(self.value)   
            #print("success--written")
            #print("row records must go in postgres")
            logging.info('Records in POSTGRES')

    


