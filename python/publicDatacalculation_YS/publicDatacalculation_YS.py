'''
1. 모든 지역에 거주하는 대상 가구수의 합
2. 가구당 평균 전력사용량의 총 평균
3. 가구당 평균 전기요금의 합
'''
import csv

newhouse = []
newVolt = []
newPay = []

# 데이터 다운받은 경로로 지정하기
with open("C:/0. ITStudy/0.dataset/지역별_전기요금_정보_2017.05_.csv", "r") as f:
    csv_reader = csv.reader(f)
    
    
    for row in csv_reader:
        newhouse.append(row[1].strip().replace(",",""))
        newVolt.append(row[2].strip().replace(",",""))
        newPay.append(row[3].strip().replace(",",""))


def Sum(sumList):
    sum = 0
    for i in range(1,len(sumList)):
        if(sumList[i]!=""):
            sum = int(sum + int(sumList[i]))
        else:
            pass
    return (sum)


def Avg(avgObject):
    count = 0
    for i in range(1,len(avgObject)):
        if(avgObject[i]!=""):
            count +=1
    
    return (Sum(avgObject)/count)



print('모든 지역에 거주하는 대상 가구수의 합 : ',Sum(newhouse))
print('가구당 평균 전력사용량의 총 평균 : ',Avg(newVolt))
print('가구당 평균 전기요금의 합 : ',Sum(newPay))