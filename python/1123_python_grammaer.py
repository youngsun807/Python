# Q1. "2018년 11월 23일 금요일" <- 이런식으로 출력되도록 빈칸을 완성 하시오
# https://docs.python.org/3.5/library/datetime.html?highlight=datetime#module-datetime
import datetime

now = datetime.datetime.now()
nowDate = now.strftime('%Y/%m/%d')

class date:
    
    #?
        
    def getDayName(self):
        return ['월', '화', '수', '목', '금', '토', '일'][datetime.date(?).weekday()]
    
#?




# Q2. 주석 부분을 코드로 채우시오.
word = "abc    ABC AbC abC   "
delSpace = '''word에서 공백없는 문자열 대입을 위한 코드 입력.'''
for i in delSpace:
    if(i.islower() == True):
        '''소문자 문자열은 제거된 것을 delSpace에 대입하는 코드 입력'''

print(delSpace) # 결과값은 ABCACC