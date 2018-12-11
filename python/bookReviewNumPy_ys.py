# In[2]:


import numpy as np


# ## The NumPy ndarray: A Multidimensional Array Object

# In[3]:


# 댓값이 0이고 표준편차가 1인 가우시안 표준 정규 분포를 따르는 난수를 2X3행렬로 나타내기
data = np.random.randn(2, 3)
data


# In[5]:


data * 10


# In[6]:


data + data


# In[7]:


# 각 차원의 크기
data.shape


# In[8]:


# 행렬 내 데이터 타입
data.dtype


# ### Creating ndarrays

# In[10]:


data1 = [6, 7.5, 8, 0, 1]
data1


# In[11]:


# 리스트 타입을 배열로 생성
arr1 = np.array(data1)
arr1


# In[ ]:


data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2


# In[ ]:


arr2.ndim   # 차원을 알려줌
arr2.shape


# In[ ]:


arr1.dtype
arr2.dtype


# In[12]:


np.zeros(10)   # 모든 배열 값이 0인 길이가 10인 배열


# In[13]:


np.zeros((3, 6))  # 모든 배열 값이 0이고 3X6인 배열


# In[14]:


# 0~14까지의 숫자값을 데이터로 가지는 배열 생성
np.arange(15)


# ### Data Types for ndarrays

# In[ ]:


arr1 = np.array([1, 2, 3], dtype=np.float64) # datatype이 부동소수점
arr2 = np.array([1, 2, 3], dtype=np.int32)  #  datatype이 정수형
arr1.dtype # float64
arr2.dtype  # int32


# In[15]:


arr = np.array([1, 2, 3, 4, 5])
arr.dtype  # int32 - 애초에 배열 생성시 integer값 입력


# In[ ]:


float_arr = arr.astype(np.float64) # 부동소수점으로 데이터 타입 변경
float_arr.dtype  # float64


# In[16]:


arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr


# In[17]:


# 부동소수점에서 정수형으로 변환되면 소수점아래는 버려진다.
arr.astype(np.int32) 


# In[20]:


int_array = np.arange(10) #dtype = int32
int_array.dtype


# In[21]:


calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
int_array.astype(calibers.dtype) #데이터 값을 부동 소수점으로 변환하였으므로 dtype=float64


# ### Arithmetic with NumPy Arrays

# In[22]:


arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr


# In[23]:


# 1차원끼리 똑같은 위치에 있는 배열끼리 곱한다.
# [1,2,3]*[1,2,3]
# [4,5,6]*[4,5,6]
arr * arr


# In[24]:


arr - arr


# In[25]:


# 각 데이터값을 1/데이터로 보여준다.
1 / arr


# In[ ]:


arr ** 0.5


# In[26]:


arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
arr2
# arr과 arr2를 같은 위치에 있는 데이터끼리 비교해서 비교식이 참인 경우 True 반환
arr2 > arr 


# ### Basic Indexing and Slicing

# In[27]:


arr = np.arange(10)
arr
arr[5] # 5번째 index값 출력
arr[5:8] # 5번째 index~7번째 index값 출력
arr[5:8] = 12 # 5번째 index~7번째 index값을 12로 변환
arr


# In[29]:


arr_slice = arr[5:8]
arr_slice # 5번째 index~7번째 index값만 출력 [12,12,12]


# In[30]:


# copy 안했기 때문에 기존의 arr값(원본)에서 변함
arr_slice[1] = 12345
arr


# In[31]:


# arr_slice 전체를 64로 변환, 원본 데이터도 같이 변환
arr_slice[:] = 64
arr


# In[32]:


arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2] # [7,8,9] 출력


# In[35]:


arr2d[0][2]  #0번째 row 2번째 column 값 출력 =3


# In[37]:


arr2d[0, 2] #0번째 row 2번째 column 값 출력 =3


# In[47]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d


# In[48]:


arr3d[0] #0번째 배열(2차원) 출력 [[1,2,3],[4,5,6]]


# In[49]:


arr3d[0].ndim


# In[52]:


old_values = arr3d[0].copy() # 0번째 배열 복사
old_values


# In[53]:


arr3d[0] = 42 # 원본 데이터 값 (0번째 배열) 모두 42로 변환
arr3d 


# In[54]:


arr3d[0] = old_values # 바꾸기 전의 데이터를 다시 대입
arr3d # 원본 데이터 변화 => 결과적으로 원본 데이터로 되돌아옴


# In[55]:


arr3d[1, 0] # 1번째 배열의 0번째 row [7,8,9]


# In[56]:


x = arr3d[1] # 1번째 배열 전체를 x에 대입
x # [[7,8,9],[10,11,12]]
x[0] #[7,8,9]


# #### Indexing with slices

# In[59]:


arr


# In[60]:


arr[1:6] # 1번째 index값 ~ 5번째 index값 출력


# In[64]:


arr2d


# In[65]:


arr2d.shape


# In[63]:


# 배열 차원 =2이지만 배열은 1개만 존재
arr2d[:2] # 처음 0번째 row 전체  ~ 1번째 row 전체 출력


# In[66]:


arr2d[:2, 1:] # [0,1],[1,1],[0,2],[1,2] 출력


# In[67]:


arr2d[1, :2] # [1,0],[1,1] 출력


# In[ ]:


arr2d[:2, 2] # [0,2],[1,2] 출력


# In[ ]:


arr2d[:, :1] # 0번째 column값 전체 출력


# In[68]:


arr2d[:2, 1:] = 0 # # [0,1],[1,1],[0,2],[1,2]위치에 존재하는 데이터값을 0으로 변환 
arr2d


# ### Boolean Indexing

# In[69]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4) # 댓값이 0이고 표준편차가 1인 가우시안 표준 정규 분포를 따르는 난수를 7X4 행렬 형태로 배열을 만들어라.
names
data


# In[70]:


# name 중에서 'Bob'과 같은 문자열을 가진 배열 index값만 True 반환
names == 'Bob'


# In[71]:


# 위의 결과에서 True가 나온 index는 0,3이므로 data에서 0,3번째 row값만 출력
data[names == 'Bob']


# In[ ]:


data[names == 'Bob', 2:] # data에서 [0,2][0,3][3,2][3,3]위치의 값 출력
data[names == 'Bob', 3] # data에서 [0,3][3,3]위치의 값 출력


# In[72]:


mask = (names == 'Bob') | (names == 'Will') 
mask # [True, False, True, True, True, False, False]
data[mask] # 1,5,6번째 row 빼고 출력


# In[73]:


data[data < 0] = 0 # data 내에 데이터값이 음수인 경우 0으로 바꾸기
data


# In[74]:


data[names != 'Joe'] = 7  # data에서 1,5,6번째 row 뺀 다른 row 모든 값들을 7로 변환
data


# ### Transposing Arrays and Swapping Axes

# In[75]:


arr = np.arange(15).reshape((3, 5)) # 0~14까지의 15개 숫자를 3X5행렬로 배치 , 한 row 먼저 채우고 다음 row
arr


# In[76]:


arr.T # arr 데이터 전치 행렬 5X3


# In[81]:


arr = np.random.randn(6, 3)
arr


# In[80]:


np.dot(arr.T, arr) # arr과 arr전치행렬을 행렬적 곱하기


# In[83]:


arr = np.arange(16).reshape((2, 2, 4)) # 2X4행렬, 2차원으로 16개의 숫자 배열 생성 (0~15), 한 row 채우고 다음 row
arr


# In[84]:


arr.transpose((1, 0, 2)) # shape에서 row 수(1)와 dimension(0)을 자리를 바꿔서 전치 행렬은 (2,2,4) 형태
# arr.transpose((2,1,0))이면 dimension=4 row = 2 column = 2이다.


# In[ ]:


arr
arr.swapaxes(1, 2) # 1번째 축과 2번째 축 번호를 받아서 뒤바꾼다.


# ## Universal Functions: Fast Element-Wise Array Functions

# In[85]:


arr = np.arange(10)
arr
np.sqrt(arr) # 데이터의 제곱근을 구한다.


# In[92]:


x = np.random.randn(8)
x


# In[93]:


y = np.random.randn(8)
y


# In[94]:


np.maximum(x, y) # x,y 배열 중에서 같은 위치에 있는 데이터를 비교해서 큰 값을 데이터로 반환


# In[100]:


arr = np.random.randn(7) * 5
arr


# In[101]:


remainder, whole_part = np.modf(arr) # 정수부분, 소수부분으로 분해
remainder # 소수 부분


# In[102]:


whole_part # 정수부분


# In[103]:


arr
np.sqrt(arr) # 제곱근 구하기, 음수는 제곱근 없음


# In[104]:


np.sqrt(arr, arr) # 변화 없음, 제곱근 한번 구하고 끝
arr


# ### Expressing Conditional Logic as Array Operations

# In[106]:


xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])


# In[107]:


result = [(x if c else y) # cond에서 true인 경우 x값, 아닐 경우 y값을 데이터값으로 출력
          for x, y, c in zip(xarr, yarr, cond)]
result


# In[108]:


result = np.where(cond, xarr, yarr) # 위의 결과와 동일
result


# In[109]:


arr = np.random.randn(4, 4)
arr
arr > 0
np.where(arr > 0, 2, -2) # arr 각 데이터 값이 양수일 경우 2, 아닐경우 -2로 변환


# In[110]:


np.where(arr > 0, 2, arr) # set only positive values to 2 , 나머지 값은 원본 데이터값 유지


# ### Mathematical and Statistical Methods

# In[112]:


arr = np.random.randn(5, 4)
arr


# In[113]:


# arr 전체 데이터 평균값
arr.mean()
np.mean(arr)


# In[115]:


arr.sum() # arr 전체 데이터 합


# In[116]:


arr.mean(axis=1) # row 별 평균


# In[117]:


arr.sum(axis=0) # column 별 합계


# In[118]:


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
arr.cumsum() # 그 전 데이터값과 현재 데이터값을 합한 값 출력, 누적값


# In[119]:


arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
arr
arr.cumsum(axis=0) # column별 누적값 출력


# In[120]:


arr.cumprod(axis=1) # row별 누적으로 곱한값 출력


# ### Methods for Boolean Arrays

# In[ ]:


arr = np.random.randn(100)
(arr > 0).sum() # Number of positive values, 양수인 값만 더한 값 출력


# In[ ]:


bools = np.array([False, False, True, False])
bools.any()  # 하나이상의 True있으면 True 반환
bools.all()  # 모두 True이면 True 반환


# ### Sorting

# In[122]:


arr = np.random.randn(6)
arr


# In[123]:


arr.sort() # 오름차순으로 정렬
arr


# In[125]:


arr = np.random.randn(5, 3)
arr


# In[126]:


arr.sort(1) # axis=1방향으로 정렬, row 내에서만 오름차순 정렬
arr


# In[127]:


large_arr = np.random.randn(1000)
large_arr.sort()
large_arr[int(0.05 * len(large_arr))] # 5% quantile, 20분위로 쪼갠 후 1분위 값을 출력

