# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-05-27 16:54:25
# @Last Modified by:   Teiei
# @Last Modified time: 2018-05-27 20:21:52
import numpy as np
import pandas as pd
print(" #########  5 Operations between DataFrame and Series (DataFrame和Series之间的操作)")
# 
# 先举个numpy的例子帮助理解，可以考虑成一个二维数组和它的一行：
print("一个表格(矩阵)减去一行(行向量）,则表格中的每一行都要减去这一行")
arr = np.arange(12.).reshape((3, 4))
print("\n\narr =\n\n",arr,
	"\n\narr[0] = \n\n",arr[0],
	"\n\narr - arr[0] = \n\n",arr - arr[0])
print("# 可以看到，这个减法是用在了每一行上。这种操作叫broadcasting，在Appendix A有更详细的解释。DataFrame和Series的操作也类似：")
print("------------------------------------")


# DataFrame跟上面一样
print("### DataFrame 减去 series ")
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),
                    index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
print("\n\nframe =\n\n",frame,
	"\n\nseries = \n\n",series,
	"\n\nframe - series= \n\n",frame - series) # 可以理解为series的index与dataframe的列匹配，broadcasting down the rows(向下按行广播):
print("------------------------------------")



print("##如果一个index既不在DataFrame的column中，也不再series里的index中，那么结果也是合集：")
# In[105]:
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
frame + series2
'''
series2 = 
b    0
e    1
f    2
series2 可看做：

        b   d    e   f
Utah    0  NaN   1   2
Ohio    0  NaN   1   2
Texas   0  NaN   1   2
Oregon  0  NaN   1   2

而frame=
frame =

           b     d     e
Utah    0.0   1.0   2.0
Ohio    3.0   4.0   5.0
Texas   6.0   7.0   8.0
Oregon  9.0  10.0  11.0
可以看做
        b   d    e   f
Utah    0  1     2   NAN
Ohio    3  4     5   NAN
Texas   6  7     8   NAN
Oregon  9  10    11  NAN

'''
print("\n\nframe =\n\n",frame,
	"\n\nseries2 = \n\n",series2, 
	"\n\nframe + series2= \n\n",frame + series2) #
print("------------------------------------")
print("## 如果想要广播列，去匹配行，必须要用到算数方法sub(这里sub是减法？)：")
# In[106]:
series3 = frame['d']
frame.sub(series3, axis='index')
print("\n\nframe =\n\n",frame,
	"\n\nseries3 = \n\n",series3, 
	"\n\nframe.sub(series3, axis='index')= \n\n",frame.sub(series3, axis='index')) ## 注意这里必须加'index'
print("------------------------------------")
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