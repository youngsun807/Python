from functools import reduce
class fibonacci:
    def __init__(self, list1=[1,2,3,4,5]):
        self.list1 = list1
        self.sum = reduce(lambda x,y : x+y, self.list1)
        print(self.list1)
    
    def getSum(self):
        return self.sum
    
    
    def setfibo(self):
        # 리스트 길이가 2이하인 경우 계산 필요 없으므로 원래 리스트 반환
        if(len(self.list1)<=2):
            return self.list1
        else:
            # (리스트 길이 = 3)일 경우 list1[2]가 무엇이든 간에 앞에 두 숫자로 인해 두숫자 합이 출력된다.
            # ex) [1,2,4] => [1,2,3]
            for i in range(2, len(self.list1)):
                self.list1[i] = self.list1[i-2]+self.list1[i-1]
            return self.list1
        
f = fibonacci([1,2])
print(f.getSum())
print(f.setfibo())
f1 = fibonacci([1,2,3,4,5,6,7])
f1.setfibo()