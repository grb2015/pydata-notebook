# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-05-22 21:01:16
# @Last Modified by:   Teiei
# @Last Modified time: 2018-05-26 20:31:54
import pandas as pd
from pandas import Series, DataFrame

import numpy as np
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
PREVIOUS_MAX_ROWS = pd.options.display.max_rows
pd.options.display.max_rows = 20
np.set_printoptions(precision=4, suppress=True)


# ## Introduction to pandas Data Structures

# ### Series

## renbin.guo added 我的理解series就是excel中的一列，其index如果不指定即为1,2,3... 为行号
print('--------------------1 创建Series--------------------')
print('-----1-1.创建方法一，传入list 不指定index -----')
obj = pd.Series([4, 7, -5, 3])
print('\n\nobj =\n',obj,		## 注意打印结果，obj还有一个dtype: int64字段
	'\n\nobj.values =',obj.values,
	'\n\nobj.index =',obj.index)  # like range(4) obj.index = RangeIndex(start=0, stop=4, step=1)

## 2.创建方法二，传入list 并且指定index 
print('-----1-2.创建方法二，传入list 并且指定index  -----')
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print('\n\nobj2 =\n\n',obj2,	## 同理  ,还有一个dtype: int64字段
	 '\n\nobj2.index =',obj2.index) # obj2.index = Index(['d', 'b', 'a', 'c'], dtype='object')

print('\n\nobj2[\'a\']=',obj2['a'])
obj2['d'] = 6
print('\n\nafter set obj2[\'d\'] = 6,obj2[[\'c\', \'a\', \'d\']]=\n',obj2[['c', 'a', 'd']]) 


print('\n\nobj2[obj2 > 0] =\n\n ',obj2[obj2 > 0],	## 对每个元素运算
	'\n\obj2 * 2 =\n\n' ,obj2 * 2 ,		## 会对Obj2中的每个元素运算
	'\n\np.exp(obj2)=\n\n',np.exp(obj2))

print('b' in obj2)	## 在index中查找
print('e' in obj2)

## 3. 创建方法三 ，传入一个dict
print('-----1-3. 创建方法三 ，传入一个dict  ,不指定index-----')
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print('obj3=\n\n',obj3)



	## 传入一个字典，并且传入index ,虽然原来字典里有Key,但新生成的Series的index还是来自传入的index
print('-----1-4. 创建方法四 ，传入一个dict  ,指定index-----')
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print('obj4=\n\n',obj4)

	##找出obj4中为空的值
print('\n\npd.isnull(obj4)=\n',pd.isnull(obj4),
	'\n\npd.notnull(obj4)=\n' ,pd.notnull(obj4),
	'\n\nobj4.isnull() =\n',obj4.isnull())


print('\n\nobj3 + obj4 =\n',obj3 + obj4)	## 这个值对obj3和obj4共同的元素进行相加，若某些元素只在obj3或obj4一个表中，则相加后为NAN



obj4.name = 'population'	## obj4.name可看做表名?
obj4.index.name = 'state'	## 我理解就是把行取一个名字，叫state
print('\n\nobj4 =\n\n',obj4)


print('\nobj=\n',obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']	##重新修改index，从0,1,2,3变为['Bob', 'Steve', 'Jeff', 'Ryan']
print("set obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']	")
print('\nafter set index:obj=\n',obj)



print('--------------------2 创建 DataFrame 并对行、列进行操作--------------------')
## 我理解DataFrame就是一张excel表
print('--------------2-1-------------------- ')
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print('\n\nframe = \n\n',frame)
print('\n\nhead() get first 5 lines :frame.head() = \n\n',frame.head())	# head方法会选取前五行


## 该表列的显示顺序
pd.DataFrame(data, columns=['year', 'state', 'pop'])

## 增加一列debt,并且显式指定index
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four',
                             'five', 'six'])
print('\n\n added column debt ,frame2 = \n\n',frame2)	## 
print('\n\n frame2.columns = \n\n',frame2.columns)

#获取某一列
print("get one raw:")
print('\n\nframe2[state] =\n\n',frame2['state'])	## 获取state列
print('\n\nframe2.year = \n\n',frame2.year);  ## 获取year列 



## 获取 index = three这一行
print("get one line,use frame2.loc[line_index]  :")
frame2.loc['three']  # 行也可以通过位置或名称的方式进行获取，比如用loc属性
print("\n\nframe2.loc['three'] = \n\n",frame2.loc['three'])


## 给debt列赋值

frame2['debt'] = 16.5
print("\n\nset debt column = 16.5,frame2['debt'] frame2 =\n\n",frame2)
frame2['debt'] = np.arange(6.)
print('\n\nset debt column = range(6.0),frame2 =\n\n',frame2)


### Series其实就是excel的一列,这里通过Series这列来给debt赋值，通过index指定具体对哪些行赋值
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print('\n\nuse Series to set debt coulum: \n\n')
print("set frame2['debt'] = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])")
print('\n\nafter set ,frame2 =\n\n',frame2)


### 新增一列,并赋值

#frame2['eastern'] = frame2.state == 'Ohio' ## 其实就是,打个括号好点。frame2['eastern'] = (frame2.state == 'Ohio')	
frame2['eastern'] = (frame2.state == 'Ohio') ## 其实就是,打个括号好点。frame2['eastern'] = (frame2.state == 'Ohio')	
print('\n\n add column eastern ,frame2 =\n\n',frame2)



## 删除一列
del frame2['eastern']
print('\n\n del column eastern ,frame2.columns =\n\n',frame2.columns,"\n\nframe2 = ",frame2)



print('--------------2-2  另一种创建DataFrame的方法 -------------------- ')
### 注意这种创建方式，它是用列作为key的字典。看做excel表，无论行列其解释都是，对(Nevada，2001)-->2.4, (Nevada,2002)-->2.9 ...
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = pd.DataFrame(pop)
print('\n\nframe3 = \n\n',frame3)

## 将excel表中行和列换一下
print('\nframe3.T = \n',frame3.T)



### 更新index ，原来是2000~2002 现在是2001~2003
#pd.DataFrame(pop, index=[2001, 2002, 2003])  ## 这句执行要出错！


##  创建DataFrame ,Ohio和Nevada只取特定行来行创建一个DataFrame
pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
frame3_1 = pd.DataFrame(pdata)
print('\n\n从frame3 取部分行(前2行)来创建 frame3_1=\n\n',frame3_1)


### 我理解这个就是增加表头，year为行的名，state为列的名
print("我理解这个就是增加表头，year为行的名，state为列的名")
print('\nbefore  set frame3.index.name,columns.name frame3=\n',frame3)
frame3.index.name = 'year'; 
frame3.columns.name = 'state'
print('\nafter set frame3.index.name,columns.name frame3=\n',frame3)
print("## 获取表中的数据值")
print('\nframe3.values=\n',frame3.values)	## 获取表中的数据值

## 如果DataFrame各列的数据类型不同，则值数组的dtype就会选用能兼容所有列的数据类型：
print("## 如果DataFrame各列的数据类型不同，则值数组的dtype就会选用能兼容所有列的数据类型：")
print('\nframe2 =\n',frame2)
print('frame2.values = \n',frame2.values)


## 索引对象
print("## 索引对象")
#pandas的索引对象负责管理轴标签和其他元数据（比如轴名称等）。
#构建Series或DataFrame时，所用到的任何数组或其他序列的标签都会被转换成一个Index：
obj = pd.Series(range(3), index=['a', 'b', 'c'])
print("\n\nobj = \n\n",obj)
index = obj.index
print("\n\nobj.index = ",obj.index)
print("\n\nobj.index[1:] = ",obj.index[1:])


# index[1] = 'd'  # TypeError
print("Index对象是不可变的，因此用户不能对其进行修改： index[1] = 'd'  # TypeError")



labels = pd.Index(np.arange(3))
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print("\n\nbj2 = \n\n",obj2)

print("除了类似于数组，Index的功能也类似一个固定大小的集合：")
print("\n\n frame3 =\n\n",frame3)
print("\nframe3.columns =\n",frame3.columns)
print("\nexecute: 'Ohio' in frame3.columns\n",'Ohio' in frame3.columns)
print("\nexecute: 2003 in frame3.index\n",2003 in frame3.index)

print("与python的集合不同，pandas的Index可以包含重复的标签")
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
print("\n\n excute: pd.Index(['foo', 'foo', 'bar', 'bar']) =\n\n",dup_labels)


