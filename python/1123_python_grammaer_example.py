# Q1. 답지
# https://docs.python.org/3.5/library/datetime.html?highlight=datetime#module-datetime
import datetime

now = datetime.datetime.now()
nowDate = now.strftime('%Y/%m/%d')

class date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d
        
    def __str__(self):
        return "%s년 %s월 %s일 " % (int(self.y), int(self.m), int(self.d))
    
    def setDayName(self, newY, newM, newD):
        self.y = newY
        self.m = newM
        self.d = newD
        
    def getDayName(self):
        return ['월', '화', '수', '목', '금', '토', '일'][datetime.date(int(self.y), int(self.m), int(self.d)).weekday()]
    
p = date('2018','11','23')
data = p.getDayName()
print(str(p))
print(data + '요일')



# Q2. 답지
word = "abc    ABC AbC abC   "
delSpace = word.rstrip().replace(" ","")
for i in delSpace:
    if(i.islower() == True):
        delSpace = delSpace.replace(i,"")

print(delSpace)