class password:
    try:
        def __init__(self):
            self.numLength = int(input("2의 몇 제곱을 원하십니까? "))
            self.listSize1 = int(input("첫번째 리스트 길이는 얼마를 원하십니까? "))
            self.listSize2 = int(input("두번째 리스트 길이는 얼마를 원하십니까? "))
            self.list1 = []
            self.list2 = []
            self.binary1 = []
            self.binary2 = []
            
            
            if(self.numLength >= 1): #1보다 큰 경우와 0일 경우, 그 외의 경우로 나누어 처리
                if((self.listSize1 >= 1) and (self.listSize2 >= 1)):# 두 리스트의 길이는 둘 다 1 이상
                    if((self.listSize1 == self.listSize2)):# 두 리스트의 길이가 같을 때
                        for i in range(self.listSize1):
                            self.list1.append(input("첫번째 리스트에 들어갈 값을 입력해주세요 : "))
                        for i in range(self.listSize2):
                            self.list2.append(input("두번째 리스트에 들어갈 값을 입력해주세요 : "))

                        # 리스트 값 유효성 검사
                        for i in range(self.listSize1):
                            if((0 <= int(self.list1[i]) <= 2**self.numLength-1) and (str(self.list1[i]).isdigit() == True)):
                                # 0 ~ 2^n-1 사이의 값, 숫자로만 이루어져 있을 때
                                continue
                            else:
                                raise Exception('유효한 값이 아닙니다.') 
                        for i in range(self.listSize2):
                            if((0 <= int(self.list2[i]) <= 2**self.numLength-1) and (str(self.list2[i]).isdigit() == True)):
                                continue
                            else:
                                raise Exception('유효한 값이 아닙니다.')

                        # 유효성 검사가 끝나면 2진수로 변환하여 대입
                        for i in range(self.listSize1):        
                            self.binary1.append((bin(int(self.list1[i]))).lstrip('0b').zfill(self.numLength))
                        for i in range(self.listSize2):
                            self.binary2.append((bin(int(self.list2[i]))).lstrip('0b').zfill(self.numLength))

                        print(self.list1,'와',self.list2,' => ',self.binary1,'와', self.binary2)
                        
                        
                    else:
                        raise Exception('두 리스트의 길이가 같지 않습니다.')
                        
                        
                else:
                    raise Exception('리스트 길이가 유효하지 않습니다. 0보다 큰 값을 넣어주세요.')
                    
            # 2의 0제곱일 때, 값은 0과 1만 가능하다.
            elif(self.numLength == 0):
                if((self.listSize1 >= 1) and (self.listSize2 >= 1)):
                    if((self.listSize1 == self.listSize2)):
                        for i in range(self.listSize1):
                            self.list1.append(input("첫번째 리스트에 들어갈 값을 입력해주세요 : "))
                        for i in range(self.listSize2):
                            self.list2.append(input("두번째 리스트에 들어갈 값을 입력해주세요 : "))


                        for i in range(self.listSize1):
                            if((0 <= int(self.list1[i]) <= 2**self.numLength) and (str(self.list1[i]).isdigit() == True)):
                                continue
                            else:
                                raise Exception('유효한 값이 아닙니다.') 
                        for i in range(self.listSize2):
                            if((0 <= int(self.list2[i]) <= 2**self.numLength) and (str(self.list2[i]).isdigit() == True)):
                                continue
                            else:
                                raise Exception('유효한 값이 아닙니다.')

                        # num.Length가 0이므로 0으로 zfill을 채우면 의미가 없습니다. 따라서 1이상의 값이 입력되어야 합니다.
                        # 저는 여기서 5로 길이를 맞추었습니다. 각자 원하는 숫자로 입력하여도 됩니다.
                        for i in range(self.listSize1):        
                            self.binary1.append((bin(int(self.list1[i]))).lstrip('0b').zfill(5))
                        for i in range(self.listSize2):
                            self.binary2.append((bin(int(self.list2[i]))).lstrip('0b').zfill(5))

                        print(self.list1,'와',self.list2,' => ',self.binary1,'와', self.binary2)
                        
                        
                    else:
                        raise Exception('두 리스트의 길이가 같지 않습니다.')
                        
                        
                else:
                    raise Exception('리스트 길이가 유효하지 않습니다. 0보다 큰 값을 넣어주세요.')
                    
                    
            else:
                raise Exception('2의 마이너스 제곱은 처리하지 않습니다.')
                
    except Exception as e:                           
        print(e)
                
            
    def compareList(self):
        self.password = []
        self.chac = ''
        if(self.numLength >=1):
            for i in range(self.listSize1):
                self.chac = ''
                for j in range(self.numLength):
                    if((int(self.binary1[i][j]) == 0) and (int(self.binary2[i][j]) == 0)):
                        self.chac = self.chac+ " "
                    else:
                        self.chac = self.chac+"#"
                self.password.append(self.chac)
            print(self.password)
        elif(self.numLength == 0):
            for i in range(self.listSize1):
                self.chac = ''
                # init함수에서 numLength가 0이었고 zfill은 5로 채웠으므로 5번 루프가 반복되어야 합니다.
                for j in range(5):
                    if((int(self.binary1[i][j]) == 0) and (int(self.binary2[i][j]) == 0)):
                        self.chac = self.chac+ " "
                    else:
                        self.chac = self.chac+"#"
                self.password.append(self.chac)
            print(self.password)

passwd = password()
passwd.compareList()


'''<result>
    2의 몇 제곱을 원하십니까? 0
    첫번째 리스트 길이는 얼마를 원하십니까? 1
    두번째 리스트 길이는 얼마를 원하십니까? 1
    첫번째 리스트에 들어갈 값을 입력해주세요 : 1
    두번째 리스트에 들어갈 값을 입력해주세요 : 0
    ['1'] 와 ['0']  =>  ['00001'] 와 ['00000']
['    #']
'''