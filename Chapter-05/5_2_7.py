import numpy as np
import pandas as pd
print(" ## 7 Sorting and Ranking （排序）")
# 
# 按row或column index来排序的话，可以用sort_index方法，会返回一个新的object：
print("## 按index排序")
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

print("\n\nframe  =\n\n",frame ,
	"\n\nframe  按行排序：frame.sort_index() = \n\n",frame.sort_index(),
	"\n\nframe  按列排序：frame.sort_index(axis=1) = \n\n",frame.sort_index(axis=1),
	"\n\n降序: frame.sort_index(axis=1, ascending=False) = \n\n",frame.sort_index(axis=1, ascending=False),
	"\n\n------------------------------------")

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