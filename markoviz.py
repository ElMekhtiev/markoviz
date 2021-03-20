# -*- coding: utf-8 -*-
"""markoviz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dAiYL2K5Imm-8KolUZH8lRKldWAwwWk6
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import quadprog
import cvxopt
# from qpsolvers import solve_qp

!pip install cvxopt
!pip install quadprog

d = pd.read_table('DATA_M_N=10_LENGTH=200.txt', header=None, delimiter = " ")
d

dt = d.T
dt.axes

securities = d.to_numpy()
print(securities[5][3])
plt.plot(securities[9])

mean_income = dt.mean()
sum_mean = mean_income.sum()
mean_income.axes
# print(mean_income)
print(sum_mean)

np_mean_income = mean_income.to_numpy()
# np_mean_income.sum()
print(np_mean_income.sum())

cov_income = dt.cov()
print(cov_income)
print(cov_income.sum().sum())

np_cov_income = cov_income.to_numpy()
double_npcov_income = 2 * npcov_income
print(np_cov_income.sum())

a = np.array([[1,2,5],[2,6,8],[5,8,3]])
b = np.triu(a)
c = np.triu(a, 1)
d = b + c
print(a)
# print(b)
print(c)
print(d)

b = np.triu(np_cov_income)
c = np.triu(np_cov_income, 1)
d = b + c
# print(d[0][1])
print(d[0][9]/np_cov_income[0][9])







