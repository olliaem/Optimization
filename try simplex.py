import pandas as pd
import numpy as np
A = np.array([
[3.0, 2.0, 1.0, 0.0, 0.0, 60.0],
[1.0, 2.0, 0.0, 1.0, 0.0, 40.0],
[1.0, 3.0, 0.0, 0.0, 1.0, 90.0],
])# коэффициенты ограничений 
#последняя колонка=правая сторона ограничений
c = np.array([-9.0, -8.0, 0.0, 0.0, 0.0, 0.0],)#коэфициенты нашей главной функции
row={'s1':A[0],
    's2':A[1],
    's3':A[2],
    'z': c}
df=pd.DataFrame({'row':row})
print(df)
def min_(c):#ведущий столбец
    i = c.argmin() # возвращает индекс минимума
    min_el = c[i]
    if min_el < 0:
        return i
    return -1
def minn(A, k):#ведущая строка
    m = np.inf
    i=0
    for j in range (len(A)):
        if A[j][k]==0:
            continue
        if (A[j][-1]/A[j][k]) < m and A[j][-1]/A[j][k] > 0:
            m = (A[j][-1]/A[j][k])
            i=j
    return m, i
def jordan(A, pivot_row, pivot_col):
    for j in range(len(A)):
        if j!=pivot_row:
            A[j]=A[pivot_row]*(-A[j][pivot_col])+A[j]
    return A
while min_(c) != -1:
    pivot_col = min_(c)
    val, pivot_row = minn(A, pivot_col)
    if np.isinf(val): #если бесконечность, останавливаем
        break
    A[pivot_row] /= A[pivot_row][pivot_col]
    c=A[pivot_row]*(-c[pivot_col])+c
    A = jordan(A, pivot_row, pivot_col)
    print(A)
print(c[-1])
