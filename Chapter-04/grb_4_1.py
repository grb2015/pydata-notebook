# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-05-20 09:51:25
# @Last Modified by:   Teiei
# @Last Modified time: 2018-05-21 22:11:47
import numpy as np
# Generate some random data
# 1.np产生随机数 
print('\n-------------------------1 np产生随机数 ----------------------------\n')
data = np.random.randn(2, 3)	## 2行2列的随机矩阵 list  [ [],[],[] ]
print(type(data))  ## <class 'numpy.ndarray'>
print(data)

# 2.对矩阵进行运算，numpy中国是对每个元素进行运算(这跟list = [ [],[],[] ] 不一样，python的list则是对List整体运算)。 
print('\n--------------------------2 对矩阵进行运算，numpy中国是对每个元素进行运算----------------------------\n')
d1 = data * 10
d2 = data + data
print('\n',d1)
print('\n',d2)
#python的list则是对List整体运算
''' 
test_array = [[1,2],[3,4],[5,6]]
print(test_array)
test_array1 = test_array*2;  ## 返回[[1, 2], [3, 4], [5, 6], [1, 2], [3, 4], [5, 6]]
print(test_array1)
test_array2 = test_array + test_array; ## 返回[[1, 2], [3, 4], [5, 6], [1, 2], [3, 4], [5, 6]]
print(test_array2)
'''
# 3.取得行数和列数 、元素的数据类型
print('\n--------------------------3 取得行数和列数 、元素的数据类型----------------------------\n')
print(data.shape)	# 获得行和列的值 ，返回一个tuple,即（行数，列数）
#print(type(data.shape))
print(data.dtype)   # 获得data中元素的数据类型



# 4.用np.array()来创建ndarray,传入参数是一个list
print('\n--------------------------4创建ndarray----------------------------\n')
# a. 一维
data1 = [6, 7.5, 8, 0, 1]  ## 这里是Int和float的混合
'''
print('data1 = ',data1)
for i in data1:
	print(type(i))
'''
arr1 = np.array(data1)	## 为了保证所有元素都是同一类型。全部被转为了float [ 6.   7.5  8.   0.   1. ] ,而普通的python list则不会转
print(arr1)
'''
for i in arr1:
	print(type(i))
'''
# b. 二维
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)

# c.其它创建nparray的方法
a1 = np.zeros(10)  ## 注意这里默认是float类型
a2 = np.zeros((3, 6))
a3 = np.arange(15)
a4 = np.empty(10)
print('\na1 = ',a1,'\n a2 = \n',a2,'\n a3 = ',a3,'\n a4 = ',a4) ## empty返回的是内存中的随机值，不建议使用empty

print('\n--------------------------5.数据类型----------------------------\n')
# 5.数据类型
	# 5-1 可以在创建的时候指定类型
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype,arr2.dtype)

	# 5-2  int转float
arr = np.array([1, 2, 3, 4, 5])
float_arr = arr.astype(np.float64)	
print(arr.dtype,float_arr.dtype)
	# ## 5-3 loat 转  int (小数部分会被截断)
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])  
int_arr = arr.astype(np.int32)
print('int_arr = ',int_arr)

	# 5-3 string转float
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
float_arr = numeric_strings.astype(float) 
print(numeric_strings,numeric_strings.dtype)	##
print(float_arr,float_arr.dtype)

	# 5-4 将A1的数据类型转为A2的
A1 = np.arange(10)
A2 = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
A1.astype(A2.dtype) ## 执行这个不会影响A1的值
print('A1 = ',A1)
A1 = A1.astype(A2.dtype) ## 必须接受返回值才会影响
print('A1 = ',A1)
	# 5-5 u4代表4字节的 无符号整型 ,与uint32一样,是一种简写
empty_uint32 = np.empty(8, dtype='u4')
print('\nempty_uint32 = ', empty_uint32,'\nempty_uint32.dtype = ',empty_uint32.dtype)


print('\n--------------------------6. NumPy数组的运算----------------------------\n')

print("----6-1 运算都是作用在元素上---")
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print('\n\narr =\n ',arr,'\n\narr * arr =\n ', arr * arr,'\n\narr - arr =\n ',arr - arr)

print('\n\n1 / arr = ',1 / arr,'\n\narr ** 0.5 =  ',arr ** 0.5)


arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print('\n\narr2 = \n',arr2,'\n\narr2 > arr0 = \n',arr2 > arr)

# ### Basic Indexing and Slicing
print("\n\n---6-2 基本的索引和切片(与Python list不同 ,这里会改变原来array的值!)-----")

arr = np.arange(10)
print('\n\narr = ',arr,'\n\narr[5] = ',arr[5],'\n\narr[5:8] = ',arr[5:8])

arr[5:8] = 12
print('\n\n\'set arr[5:8] = 12, then\' arr = ',arr)




arr_slice = arr[5:8]
print('arr_slice=',arr_slice)
arr_slice[1] = 12345   ## 注意这里arr_slice的修改也会改变原来的array !
print(' arr = ',arr)  

arr_slice[:] = 64
print(' arr = ',arr)  



print("\n\n---6-3 获取矩阵的每个元素(同C语言）-----")
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(
	'\n\narr2d =\n',arr2d,
	'\n\narr2d[2] = ',arr2d[2],
	'\n\narr2d[0][2] = ',arr2d[0][2],
	'\n\narr2d[0, 2] = ',arr2d[0, 2]
	)




print("\n\n---6-4 2个矩阵(3维数组)-----")

arr3d = np.array([  [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]   ])
# arr3d[0] =  [[1, 2, 3], [4, 5, 6]]
# arr3d[1] =  [[7, 8, 9], [10, 11, 12]]
# 
print('\n\narr3d = \n',arr3d,
	  '\n\narr3d[0] = \n',arr3d[0],
	  '\n\narr3d[1] = \n',arr3d[1],
	  '\n\narr3d[1, 0] = \n',arr3d[1, 0])

old_values = arr3d[0].copy()
arr3d[0] = 42		## 这个会覆盖原来的，如果不想被覆盖，只有先copy
print('\n\after set arr3d[0] = 42 , arr3d = \n ',arr3d)
arr3d[0] = old_values
print('\n\after set old_values , arr3d = \n',arr3d)


print('\n\arr3d[1, 0] = ',arr3d[1, 0])
x = arr3d[1]
print(	'\n\nx = arr3d[1],x =' ,x,
		'\n\nx[0]= ',x[0]
	)
print("\n\n---------6-5 对矩阵随意切片 ---------------")
print(	'arr =',arr,
		'arr[1:6] =',arr[1:6]		## 注意这个[1,6]实际上是[1,6) 即不包括后面的
	)

print(	'\n\narr2d = ',		arr2d,
		'\n\narr2d[:2] =' ,	arr2d[:2],	## 取前2行
		'\n\narr2d[:2, 1:] =',arr2d[:2, 1:], ## 先取前2行，再对之前去的的取2,3列
		'\n\narr2d[1, :2] =',arr2d[1, :2],  ## 取第2行前2列
		'\n\narr2d[:2, 2] = ',arr2d[:2, 2],	## 取前2行，第2列 组成一个list
		'\n\narr2d[:, :1] =',arr2d[:, :1])	## 去所有行，然后取第一列。即取表格的第一列
arr2d[:2, 1:] = 0	## 设置前2行的后2列为0
print('\n\nafter set arr2d[:2, 1:] = 0, arr2d =',arr2d)