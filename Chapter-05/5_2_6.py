print("## 6 Function Application and Mapping (函数应用和映射)")
# 

import numpy as np
import pandas as pd

print("### numpy的ufuncs(element-wise数组方法)也能用在pandas的object上：")
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), 
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print("\n\nframe =\n\n",frame,
	"\n\nnp.abs(frame) = \n\n",np.abs(frame))
print("------------------------------------")
# 另一个常用的操作是把一个用在一维数组上的函数，应用在一行或一列上。要用到DataFrame中的apply函数：
## 这个在excel中相关与对所有行/列求极差。
f = lambda x: x.max() - x.min()
frame.apply(f)
print("f = lambda x: x.max() - x.min()",
	"\n\nframe =\n\n",frame,
	"\n\nframe.apply(f) =\n\n",frame.apply(f),	## axis =0 ,说明行是变化的，列是固定的。则是对一个列向量来操作
	"\n\nframe.apply(f, axis='columns') = \n\n",frame.apply(f, axis='columns'))  ## axis =1 ,则是对一个行向量来操作
print("------------------------------------")
# 这里函数f，计算的是一个series中最大值和最小值的差，在frame中的每一列，这个函数被调用一次。作为结果的series，它的index就是frame的column。
# 像是sum, mean这样的数组统计方法，DataFrame中已经集成了，所以没必要用apply。	### 相当于excel中的汇总

# apply不会返回标量，只会返回一个含有多个值的series：
print("### 自定义f(x)")
def f(x): 
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
# In[116]:
frame
# In[115]:
frame.apply(f)
print("\n\n f(x) = pd.Series([x.min(), x.max()], index=['min', 'max'])"
	"\n\nframe =\n\n",frame,
	"\n\nframe.apply(f) =\n\n",frame.apply(f)  ## 这里axis = 0,所以是对行(列向量)来进行f(x)
	)
print("------------------------------------")
# element-wise的python函数也能用。假设想要格式化frame中的浮点数，变为string。可以用apply map：
# In[117]:
format = lambda x: '%.2f' % x
# In[118]:
frame.applymap(format)
# applymap的做法是，series有一个map函数，能用来实现element-wise函数：
# In[119]:
frame['e'].map(format)

print("\n\n format = lambda x: '%.2f' % x"
	"\n\nframe =\n\n",frame,
	"\n\nframe.applymap(format) =\n\n",frame.applymap(format),  ## 这里axis = 0,所以是对行(列向量)来进行f(x)
	"\n\nframe['e'].map(format) =\n\n",frame['e'].map(format)
	)  
print("------------------------------------")

