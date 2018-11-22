class password:
    def __init__(self, list1=[1,1,1,1,1],list2=[1,1,1,1,1]):
        self.list1 = list1
        self.list2 = list2
        self.binary1 = []
        self.binary2 = []
        
        # 리스트 길이만큼 각 값들을 2진수로 변환하여 새로운 리스트에 넣는다.
        for i in range(len(self.list1)):
                self.binary1.append((bin(self.list1[i]).lstrip('0b')).zfill(5))
            
        for i in range(len(self.list2)):
                self.binary2.append((bin(self.list2[i]).lstrip('0b')).zfill(5))

        print(self.binary1,'와', self.binary2)
        
    def compareList(self):
        self.password = []
        self.chac = ''
        for i in range(5):
            # 00000과 00001을 비교(각 리스트의 첫번째 인덱스 문자열 비교)한 후
            # 그 다음 인덱스 비교를 위해 초기화 필수
            # 초기화하지 않으면 그 전 문자열에 덧붙이는 꼴
            self.chac = ''
            for j in range(5):
                if((int(self.binary1[i][j]) == 0) and (int(self.binary2[i][j]) == 0)):
                    self.chac = self.chac+ " "
                else:
                    self.chac = self.chac+"#"
            self.password.append(self.chac)
        print(self.password)
        
        
        
passwd = password([15,15,15,15,15],[2,2,2,2,2])
passwd.compareList()

'''<result>
    ['01111', '01111', '01111', '01111', '01111'] 와 ['00010', '00010', '00010', '00010', '00010']
    [' ####', ' ####', ' ####', ' ####', ' ####']
'''
