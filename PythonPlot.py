#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("regrex1.csv")
df.plot(kind='scatter',x='x',y='y')

plt.savefig('py_orig.png')

m, b = np.polyfit(df.x, df.y, 1)
plt.plot(df.x, m*df.x+b)

plt.savefig('py_lm.png')


# In[ ]:




