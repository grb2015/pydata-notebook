# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-05-20 09:45:06
# @Last Modified by:   Teiei
# @Last Modified time: 2018-05-20 12:10:01

import numpy as np
my_arr = np.arange(1000000)  ## 注意这里是arrage 而不是range
my_list = list(range(1000000))
## np.arange的速度要快很多 ！
get_ipython().run_line_magic('time', 'for _ in range(10): my_arr2 = my_arr * 2')	# rbguo added 20180520 这里的_相当于i
get_ipython().run_line_magic('time', 'for _ in range(10): my_list2 = [x * 2 for x in my_list]')


