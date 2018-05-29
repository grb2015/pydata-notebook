import numpy as np
import pandas as pd
print(" ## 7 Sorting and Ranking （排序）")
# 
# 按row或column index来排序的话，可以用sort_index方法，会返回一个新的object：
print("## Series 按index排序")
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()
print("\n\nobj  =\n\n",obj ,
	"\n\nobj.sort_index() = \n\n",obj.sort_index(),
	"\n\n------------------------------------")

# 在DataFrame，可以用index或其他axis来排序：

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
print("Frame 按行或列排序")
print("\n\nframe  =\n\n",frame ,
	"\n\nframe  按行排序：frame.sort_index() = \n\n",frame.sort_index(),
	"\n\nframe  按列排序：frame.sort_index(axis=1) = \n\n",frame.sort_index(axis=1),
	"\n\n降序: frame.sort_index(axis=1, ascending=False) = \n\n",frame.sort_index(axis=1, ascending=False),
	"\n\n------------------------------------")

# 通过值来排序，用sort_values方法：
print("## Series 按值来排序")
obj = pd.Series([4, 7, -3, 2])
obj.sort_values()

# 缺失值会被排在最后：
print("\n\nobj  =\n\n",obj ,
	"\n\nobj.sort_values() = \n\n",obj.sort_values(),
	"\n\n------------------------------------")
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
obj.sort_values()
print("\n\nobj  =\n\n",obj ,
	"\n\nobj.sort_values() = \n\n",obj.sort_values(),
	"\n\n------------------------------------")
# 对于一个DataFrame，可以用一列或多列作为sort keys。这样的话，只需要把一列多多列的名字导入到sort_values即可：
print("## DataFrame 按值来排序(其实也即是按列)")
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})

frame.sort_values(by='b')
# 多列排序的话，传入一个list of names：
frame.sort_values(by=['a', 'b'])
print("\n\nframe  =\n\n",frame ,
	"\n\nframe  按b列排序：frame.sort_values(by='b') = \n\n",frame.sort_values(by='b'),
	"\n\nframe  多列排序(先按a再按b)：frame.sort_values(by=['a', 'b'])) = \n\n",frame.sort_values(by=['a', 'b']),
	"\n\n------------------------------------")

# ranking（排名）是给有效的数据分配数字。rank方法能用于series和DataFrame，rank方法默认会给每个group一个mean rank（平均排名）。rank 表示在这个数在原来的Series中排第几名，有相同的数，取其排名平均（默认）作为值：
# In[133]:
print("######## 排名 Series")
print("###### 排名过程中有相同的value怎么办?以下是几种处理")
print("###### 1.ranking()不加任何参数：  比如2个丢失第一名，则普通来讲,可能一个是一个第1一个第2,rank排名的话就是1.5 取平均")
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
obj.sort_values()
obj.rank()
# 在obj中，4和4的排名是第4名和第五名，取平均得4.5。7和7的排名分别是第六名和第七名，则其排名取平均得6.5。
print("\n\nobj  =\n\n",obj ,
	"\n\nobj.sort_values() = \n\n",obj.sort_values(),
	"\n\nobj.rank() = \n\n",obj.rank(),
	"\n\n------------------------------------")

# rank也可以根据数据被观测到的顺序来设定：
print("###### 1.ranking()加'first'参数：  rank也可以根据数据被观测到的顺序来设定，比如2个并列第一，则一个是第1一个是第2")

obj.rank(method='first')
# 这里没有给0和2(指两个数字7)赋予average rank 6.5，而是给第一个看到的7（label 0）设置rank为6，第二个看到的7（label 2）设置rank为7。
print("\n\nobj  =\n\n",obj ,
	"\n\nobj.sort_values() = \n\n",obj.sort_values(),
	"\n\nobj.rank() = \n\n",obj.rank(method='first'),
	"\n\n------------------------------------")

# 
# 也可以设置降序：
print("###### 1.ranking()加method='max'参数： 比如2个都并列第一，则2个都取第2名")
# Assign tie values the maximum rank in the group
obj.rank(ascending=False, method='max')
print("\n\nobj  =\n\n",obj ,
	"\n\nobj.sort_values() = \n\n",obj.sort_values(),
	"\n\nobj.rank(ascending=False, method='max') = \n\n",obj.rank(ascending=False, method='max'),
	"\n\nobj.rank(method='max') = \n\n",obj.rank(ascending=False, method='max'),
	"\n\n------------------------------------")

print("######## 排名 DataFrame")
# dataframe 可以根据行或列来计算rank:
# In[143]:
frame = pd.DataFrame({'b': [4.3, 7, -3, 2],
                      'a': [0, 1, 0, 1],
                      'c': [-2, 5, 8, -2.5]})
 # columns表示列与列之间的排序（即每一行里数据间的排序）,要注意frame.rank(axis='columns')打印出来的是名次
frame.rank(axis='columns')
# ![](http://oydgk2hgw.bkt.clouddn.com/pydata-book/6xv9c.png)
# # 8 Axis Indexes with Duplicate Labels (有重复label的轴索引)
print("\n\nframe  =\n\n",frame ,
	"\n\n axis='columns')即按即每一行里数据间的排序： frame.rank(axis='columns') = \n\n",frame.rank(axis='columns'),
	"\n\n------------------------------------")
# 我们看到的所有例子都有unique axis labels(index values),唯一的轴标签（索引值）。
# 一些pandas函数（reindex）,需要label是唯一的，但这并是不强制的。比如下面有一个重复的索引：
print("##### 一些不允许重复value的情况：")
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj
# index的is_unique特性能告诉我们label是否是唯一的：
obj.index.is_unique
print("\n\nobj  =\n\n",obj ,
	"\n\nobj.index.is_unique = \n\n",obj.index.is_unique,
	"\n\nobj['a']  =\n\n",obj['a'] ,	## a对应有2个值，所以返回一个List
	"\n\nobj['c'] = \n\n",obj['c'],		## 而b值对应一个值,所以返回一个标量
	"\n\n------------------------------------")
# 数据选择对于重复label则表现有点不同。如果一个label有多个值，那么就会返回一个series, 如果是label只对应一个值的话，会返回一个标量：

# 这个选择的逻辑也应用于DataFrame：

df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print("\n\ndf  =\n\n",df,
	"\n\ndf.loc['b'] = \n\n",df.loc['b'],
	"\n\n------------------------------------")