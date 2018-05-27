# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-05-27 09:51:02
# @Last Modified by:   Teiei
# @Last Modified time: 2018-05-27 16:49:47



# # 5.2 Essential Functionality（主要功能）
# 
# 接下来介绍pandas中的一些主要功能，这里只介绍一些经常用到的。
# 
# # 1 Reindexing（重新索引）
print("#  1 Reindexing（重新索引） ，注意：原来的对象不会改变，也没有想drop一样有inplace  = true的方法")
# pandas中一个重要的方法是reindex，已实施在创建object的时候遵照一个新的index。如下例：



import pandas as pd

print("### 1.1 Series Reindexing")
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print('\nobj = \n',obj)


# 在series上调用reindex能更改index，如果没有对应index的话会引入缺失数据：
print("更改Index(其实这里就是增加了1个e行),这行对应的列值没有指定，默认就为NAN")
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print("\nobj2 = obj.reindex(['a', 'b', 'c', 'd', 'e']) = \n",obj2)
print("\nreindex()并不改变原来obj的值: obj = \n",obj)

# 在处理时间序列这样的数据时，我们可能需要在reindexing的时候需要修改值。method选项能做到这一点，比如，使用ffill可以实现前向值填充：:
obj3 = pd.Series(['bule', 'purple', 'yellow'], index=[0, 2, 4])
print("\nobj3 = \n",obj3)
print("### 更改Index(其实这里就是增加了几个行)，列值用它前一行的值填充， method='ffill' ,excel中也有这样的功能")
obj3.reindex(range(6), method='ffill')
print("\n obj3.reindex(range(6), method='ffill') =\n",obj3.reindex(range(6), method='ffill'))


print("### 1.2 DataFrame Reindexing")
import numpy as np

frame = pd.DataFrame(np.arange(9).reshape(3, 3),
                     index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas', 'California'])
print("\nframe = \n",frame)

print("#### 更改Index(其实这里就是增加了1行,即c行),这些行对应的列值没有指定，默认就为NAN")
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print("\nframe2 = frame.reindex(['a', 'b', 'c', 'd']) = \n",frame2)
print("\nframe = frame.reindex(['a', 'b', 'c', 'd']) = \n",frame)

# 更改columns index:
print("### 更改列,这里将原来的['Ohio', 'Texas', 'California']替换为['Texas', 'Utah', 'California'],即不要原来的Texas列了,新增一个Utah列，该类没有指定值，为NAN")
states = ['Texas', 'Utah', 'California']

f3 = frame.reindex(columns=states)
print("\nf3 = frame.reindex(columns=states) = \n",f3 )
print("\n#### reindex()并不改变原来framej的值 frame = \n",frame)
# reindex的参数：
# 
# ![](http://oydgk2hgw.bkt.clouddn.com/pydata-book/x0pq4.png)
# 
# 还可以使用loc更简洁的reindex：

# In[15]:

print("#### 利用loc方法可以同时更改行和列,这里对行增了b行，对列不要原来的Texas列了,新增一个Utah列，该类没有指定值，为NAN")
f4 = frame.loc[['a', 'b', 'c', 'd'], states]
print("\n f4 = frame.loc[['a', 'b', 'c', 'd'], states] = \n",f4 )

# # 2 Dropping Entries from an Axis (按轴删除记录) 
print("2 Dropping Entries from an Axis (按轴删除记录)  注意：原来的对象不会改变 ")
# 对于series，drop回返回一个新的object，并删去你制定的axis的值：
print("### 2.1 Series 删除行")
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print('\nobj = \n',obj)

print("### 删除c行")
new_obj = obj.drop('c')
print("\nnew_obj = obj.drop('c') = \n",new_obj)
print("\n原来的对象不会改变 obj = \n",obj)

print("### 删除c,d行")
new_obj2 = obj.drop(['d', 'c'])
print("\nnew_obj2 = obj.drop('c') = \n",new_obj2)


# 对于DataFrame，index能按行或列的axis来删除：
print("### 2.2 DataFrame 删除行")


data = pd.DataFrame(np.arange(16).reshape(4, 4),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print('\ndata= \n',data)


# 行处理：如果a sequence of labels(一个标签序列)来调用drop，会删去row labels(axis 0):
print("### 删除行，删除'Colorado', 'Ohio' 行,即前2行")
data2 = data.drop(['Colorado', 'Ohio'])
print("\ndata2 = data.drop(['Colorado', 'Ohio'])= \n",data2)

# 列处理：drop列的话，设定axis=1或axis='columns':
print("### 删除列(设置axis=1或axis='columns'以告知是删除列) ")
print("### 请删除'two'这一列,使用axis=1")
data3 = data.drop('two', axis=1)
print("\ndata3 = data.drop('two', axis=1) =\n",data3)

print("## 删除'two', 'four这2列,使用axis='columns'")
data.drop(['two', 'four'], axis='columns')
print("\ndata.drop(['two', 'four'], axis='columns') = \n",data.drop(['two', 'four'], axis='columns'))


# drop也可以不返回一个新的object，而是直接更改series or dataframe in-place:
print("### 注意：原来的对象不会改变")
print("\nobj = \n",obj)
obj2 = obj.drop('c')
print("\nobj2 = obj.drop('c')= \n",obj2)
print("\nobj = \n",obj)

print("### 如果要改变原来的对象，可以使用inplace=True")
obj3 = obj.drop('c', inplace=True)
print("\nobj3 = obj.drop('c', inplace=True) = \n",obj3)
print("\nobj = \n",obj)


# # 3 Indexing, Selection, and Filtering(索引，选择，过滤)
# 
# series indexing(obj[...]) 相当于numpy的array indexing, 而且除了整数，还可以使用series的index：

print("################## 3 Indexing, Selection, and Filtering (索引，选择，过滤)")
print(" ## 3.1Series 切片(选择行) ")

obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print("\nobj = \n",obj)
print("\nobj['b'] = \n",obj['b'])
print("\nobj[1] = \n",obj[1])
print("\nobj[2:4] = \n",obj[2:4])
# 选中行
print("\nobj[['b', 'a', 'd']] = \n",obj[['b', 'a', 'd']])
print("\nobj[[1, 3]] = \n",obj[[1, 3]])
print("\nobj[obj < 2] = \n",obj[obj < 2])

print("# 用label来slicing(切片)的时候，和python的切片不一样的在于，会包括尾节点：")
print("\nobj['b':'c'] = \n",obj['b':'c'])

print("# 可以直接给选中的label更改值：")
obj['b':'c'] = 5
print("obj['b':'c'] = 5,obj =",obj)


print(" ## 3.2 DataFrame 切片(选择行,列) ")
# 而对于DataFrame，indexing可以通过一个值或序列，选中一个以上的列：
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(" #### 3.2.1 DataFrame 选择列(直接传入一个list)")
#print("用一个值或序列对DataFrame进行索引其实就是获取一个或多个列：")

print("\ndata  = \n",data)
#print("## 得到某列,传入的是一个列的str名：")
print("\n\ndata['two']=\n\n" ,data['two'])
# print("## 得到某几列,传入一个[] list:")
print("\n\n data[['three', 'one']]=\n",data[['three', 'one']])
#print("\n\n ## 嵌套,传入的是data['three']的结果，data[data['three'] > 5]= \n",data[data['three'] > 5])
#print("## bool判断:")
print("\n\ndata < 5 =\n",data < 5)  # dataframe的indexing有一些比较特别的方式。比如通过布尔数组

# 将data中元素小于5的替换为0 ,这句执行不成功，是不是ipython特有的?
#data2 = (data[data < 5]=0)
#print("data[data < 5] = 0\n\n",data2)


#print("很特别,data[:2] 会得到前2行!(注意是行)")
print("\n\n data[:2]) = \n",data[:2]) 

print("注意!：data[1] 会报错，不能这样用，这样不能得到第一行数据\n\n\n")

print(" #### 3.2.2 DataFrame 选择行(用loc和iloc来选择)")

# ## Selection with loc and iloc(用loc和iloc来选择)
# 
# 对于label-indexing on rows, 我们介绍特别的索引符，loc and iloc. 这两个方法能通过axis labels(loc)或integer(iloc)，来选择行或列。
# 
# 一个列子，选中一行多列by label：



data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print("data = \n",data)

## 使用loc方法，指定行,列
print("\n\ndata.loc['Colorado', ['two', 'three']] = \n\n",data.loc['Colorado', ['two', 'three']] )


# 同iloc实现相同的效果：iloc是用下标来，我觉得还是不太好，可读性差

data.iloc[2, [3, 0, 1]]
print("\n\ndata.iloc[2, [3, 0, 1]] = \n\n",data.iloc[2, [3, 0, 1]])



# 一行
data.iloc[2]
print("\n\ndata.iloc[2]  = \n\n",data.iloc[2])

# In[56]:

# 取得第2,3行，第1,2,3列的数据
data.iloc[[1, 2], [3, 0, 1]]
print("\n\ndata.iloc[[1, 2], [3, 0, 1]] = \n\n",data.iloc[[1, 2], [3, 0, 1]])

# indexing函数也能用于切片，不论是single labels或lists of labels:
# 获取 :'Utah' 行，'two'列 的子表
data.loc[:'Utah', 'two']
print("\n\ndata.loc[:'Utah', 'two']\n\n",data.loc[:'Utah', 'two'])



## 获取所有行,前3列的数据。并且要第三列的数据的值大于5
data.iloc[:, :3][data.three > 5]
print("\n\ndata.iloc[:, :3][data.three > 5]\n\n",data.iloc[:, :3][data.three > 5])



# pandas中有很多用于选择和重新选择数据的方法：
# 
# ![](http://oydgk2hgw.bkt.clouddn.com/pydata-book/bwadf.png)
# 
# ![](http://oydgk2hgw.bkt.clouddn.com/pydata-book/lc2uc.png)
# 
# 注意：当设计padnas的时候，作者发现frame[:, col]这样的语法是比较冗长的，因为这是会被经常用到的一个功能。
# 作者把一些indexing的功能（lable or integer）集成在了ix这个方法上。实际中，因为这种label和integer都可以用的方式很方便，于是pandas team设计了loc和ilco来实现label-based和integer-based indexing.
# 
# 虽然ix indexing依然错在，但是已经过时，不推荐使用。
# 
print("## 4 Integer Indexes（整数索引）")
# 
# 一些新手再用integer来index的时候，总是会被绊倒。因为这种方法和python用于list和tuple的indexing方法不同。
# 
# 比如，你不希望下面的代码出现error：
# 

ser = pd.Series(np.arange(3.))
print("\nser = \n",ser) 
#print("\nser[-1])\n",ser[-1])  ## 这里报错 # 看到了，pandas在整数索引上可能会出错。这里我们有一个index包括0，1，2，但是猜测用户想要什么是很困难的：
print("\nser[0])\n",ser[0]) ## 这个是都可以的
# 为了保持连贯性，如果axis index里包含integer，那么选择数据的时候，就会是label-orented. 为了更精确地选择，使用`loc`(for label)或`ilco`(for integers):

print("\nser[:1] = \n",ser[:1])	# 选择了前2行 
#print("\nser.loc[:1] = \n",ser.loc[:1])  # 只选择了前1行
#print("\nser.iloc[:1] = \n",ser.iloc[:1]) #选择了前2行 不要太纠结这个 

# 另一方面，如果用非整数来做index，就没有歧义了：
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
print("\nser2 = \n",ser2) 
print("\nser2[-1])\n",ser2[-1])  ## 这里不会报错，因为index是非数字的



print("##### 5 Arithmetic and Data Alignment (算数和数据对齐)")
# 
# pandas一个有用的feature就是，不同index的obejct之间的算数计算。如果两个object相加，但他们各自的index并不相同，最后结果得到的index是这两个index的合集：


print("### 两个Series相加,类似于SQL中的join,只对相同的index加，其它去NAN值")
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])

s2 = pd.Series([2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1+s2
print("\n\ns1 = \n\n",s1,
	"\n\ns2 = \n\n",s2,
	"\n\ns1+s2 = \n\n",s1+s2,
	)


# 这种数据对齐的方式（internal data alignment）引入了很多缺失值在没有陈赫的位置上。这些缺失值会被用在之后的算数计算中。
# 
# 在DataFrame中，数据对齐同时发生在行和列上：



print("### 两个DataFram相加,亦然")
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                   index=['Ohio', 'Texas', 'Colorado'])

df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])

# 相加的结果就是两个DataFrame，行和列的合集：

# 因为'c'和'e'列都不在两个DataFrame里，所有全是缺失值。对于行，即使有相同的，但列不一样的话也会是缺失值。
# 

print("\n\ndf1  = \n\n",df1 ,
	"\n\ndf2  = \n\n",df2 ,
	"\n\ndf1 + df2  = \n\n",df1 + df2,
	)

# 如果两个DataFrame相加(减），而且没有column和row，结果会全是null：
print("### 两个DataFram相减,亦然")
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
'''
df1  =

    A
0  1
1  2
要注意 df1就是一个只有一列的表格,左边的0,1是系统自动给它分配的行index
print("df1[0] =",df1.iloc[0])		## 获取第0行
print("df1[1] =",df1.iloc[1])		## 获取第1行
print(df1.index)					## 打印行Index
print("df1['A'] =\n",df1['A'])		## 获取A列

'''
print("\n\ndf1  = \n\n",df1 ,
	"\n\ndf2  = \n\n",df2 ,
	"\n\ndf1 - df2  = \n\n",df1 - df2,
	)





# ### Arithmetic methods with fill values (带填充值的算数方法)
# 
# 对于上面那些缺失值，我们想要填上0：
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), 
                   columns=list('abcd'))

df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), 
                   columns=list('abcde'))

df2.loc[1, 'b'] = np.nan ## 设置（1, 'b')单元格为NAN

print(" # 不使用添加方法的结果(没有交集的都为NAN)")
print("\n\ndf1  = \n\n",df1 ,
	"\n\ndf2  = \n\n",df2 ,
	"\n\ndf1 + df2  = \n\n",df1 + df2,
	)

# 使用fill_value：


#print("# 对于上面那些缺失值，我们想要填上0：") ## 但是下面这个我觉得不是把NAN替换为0
print("### fill_value=0方法,没有交集的取各自一方的值，而不是填充为NAN")
df1.add(df2, fill_value=0)
print("\ndf1.add(df2, fill_value=0)\n",df1.add(df2, fill_value=0))

# 下表中就有很多这样灵活的算数方法：
# 
# ![](http://oydgk2hgw.bkt.clouddn.com/pydata-book/y0rr4.png)
# 
# 每一个都有一个配对的，以 r 开头，意思是反转：



print("上面用到了add方式,还有减，乘除等其它方法 ，以 r 开头，意思是反转")
1 / df1
df1.rdiv(1)


# 在reindex（重建索引）的时候，也可以使用fill_value:
df1.reindex(columns=df2.columns, fill_value=0)


print(" #########  6 Operations between DataFrame and Series (DataFrame和Series之间的操作)")
# 
# 先举个numpy的例子帮助理解，可以考虑成一个二维数组和它的一行：

# In[98]:


arr = np.arange(12.).reshape((3, 4))
arr


# In[99]:


arr[0]


# In[100]:


arr - arr[0]


# 可以看到，这个减法是用在了每一行上。这种操作叫broadcasting，在Appendix A有更详细的解释。DataFrame和Series的操作也类似：

# In[101]:


frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),
                    index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]


# In[102]:


frame


# In[103]:


series


# 可以理解为series的index与dataframe的列匹配，broadcasting down the rows(向下按行广播):

# In[104]:


frame - series


# 如果一个index既不在DataFrame的column中，也不再series里的index中，那么结果也是合集：

# In[105]:


series2 = pd.Series(range(3), index=['b', 'e', 'f'])
frame + series2


# 如果想要广播列，去匹配行，必须要用到算数方法：

# In[106]:


series3 = frame['d']
frame


# In[107]:


series3


# In[108]:


frame.sub(series3, axis='index')


# axis参数就是用来匹配轴的。在这个例子里是匹配dataframe的row index(`axis='index` or `axis=0`)，然后再广播。
# 
# # 6 Function Application and Mapping (函数应用和映射)
# 
# numpy的ufuncs(element-wise数组方法)也能用在pandas的object上：

# In[110]:


frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), 
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame


# In[111]:


np.abs(frame)


# 另一个常用的操作是把一个用在一维数组上的函数，应用在一行或一列上。要用到DataFrame中的apply函数：

# In[112]:


f = lambda x: x.max() - x.min()
frame.apply(f)


# 这里函数f，计算的是一个series中最大值和最小值的差，在frame中的每一列，这个函数被调用一次。作为结果的series，它的index就是frame的column。
# 
# 如果你传入`axis='column'`用于apply，那么函数会被用在每一行：

# In[113]:

'''
frame.apply(f, axis='columns')


# 像是sum, mean这样的数组统计方法，DataFrame中已经集成了，所以没必要用apply。
# 
# apply不会返回标量，只会返回一个含有多个值的series：

# In[114]:


def f(x): 
    return pd.Series([x.min(), x.max()], index=['min', 'max'])


# In[116]:


frame


# In[115]:


frame.apply(f)


# element-wise的python函数也能用。假设想要格式化frame中的浮点数，变为string。可以用apply map：

# In[117]:


format = lambda x: '%.2f' % x


# In[118]:


frame.applymap(format)


# applymap的做法是，series有一个map函数，能用来实现element-wise函数：

# In[119]:


frame['e'].map(format)


# # 7 Sorting and Ranking （排序）
# 
# 按row或column index来排序的话，可以用sort_index方法，会返回一个新的object：

# In[120]:


obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()


# 在DataFrame，可以用index或其他axis来排序：

# In[123]:


frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
frame


# In[124]:


frame.sort_index()


# In[125]:


frame.sort_index(axis=1)


# 默认是升序，可以设置降序：

# In[126]:


frame.sort_index(axis=1, ascending=False)


# 通过值来排序，用sort_values方法：

# In[127]:


obj = pd.Series([4, 7, -3, 2])
obj.sort_values()


# 缺失值会被排在最后：

# In[128]:


obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
obj.sort_values()


# 对于一个DataFrame，可以用一列或多列作为sort keys。这样的话，只需要把一列多多列的名字导入到sort_values即可：

# In[129]:


frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame


# In[130]:


frame.sort_values(by='b')


# 多列排序的话，传入一个list of names：

# In[131]:


frame.sort_values(by=['a', 'b'])


# ranking（排名）是给有效的数据分配数字。rank方法能用于series和DataFrame，rank方法默认会给每个group一个mean rank（平均排名）。rank 表示在这个数在原来的Series中排第几名，有相同的数，取其排名平均（默认）作为值：

# In[133]:


obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
obj


# In[138]:


obj.sort_values()


# In[136]:


obj.rank()


# 在obj中，4和4的排名是第4名和第五名，取平均得4.5。7和7的排名分别是第六名和第七名，则其排名取平均得6.5。
# 
# rank也可以根据数据被观测到的顺序来设定：

# In[141]:


obj


# In[137]:


obj.rank(method='first')


# 这里没有给0和2(指两个数字7)赋予average rank 6.5，而是给第一个看到的7（label 0）设置rank为6，第二个看到的7（label 2）设置rank为7。
# 
# 也可以设置降序：

# In[142]:


# Assign tie values the maximum rank in the group
obj.rank(ascending=False, method='max')


# dataframe 可以根据行或列来计算rank:

# In[143]:


frame = pd.DataFrame({'b': [4.3, 7, -3, 2],
                      'a': [0, 1, 0, 1],
                      'c': [-2, 5, 8, -2.5]})
frame


# In[144]:


frame.rank(axis='columns') # columns表示列与列之间的排序（即每一行里数据间的排序）


# ![](http://oydgk2hgw.bkt.clouddn.com/pydata-book/6xv9c.png)

# # 8 Axis Indexes with Duplicate Labels (有重复label的轴索引)
# 
# 我们看到的所有例子都有unique axis labels(index values),唯一的轴标签（索引值）。一些pandas函数（reindex）,需要label是唯一的，但这并是不强制的。比如下面有一个重复的索引：

# In[145]:


obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj


# index的is_unique特性能告诉我们label是否是唯一的：

# In[146]:


obj.index.is_unique


# 数据选择对于重复label则表现有点不同。如果一个label有多个值，那么就会返回一个series, 如果是label只对应一个值的话，会返回一个标量：

# In[147]:


obj['a']


# In[148]:


obj['c']


# 这个选择的逻辑也应用于DataFrame：

# In[149]:


df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df


# In[150]:


df.loc['b']

'''