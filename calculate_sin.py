from hello import do_sine
import numpy as np
import time
import math
#cimport openmp


#openmp.omp_set_num_threads(28)
x = np.random.choice([0 , np.pi/2], size=(2000, 20, 20, 20, 20), replace=True)
print('shape of x is')
print(x.shape)
#print(x[0,:])

#print('number of threads before')
#print(openmp.omp_get_num_threads())
st = time.time()
y = do_sine(x)
print('total time for cython')
time_paral = time.time()-st
print(time_paral)

st = time.time()

y = np.zeros((2000,20,20,20,20))
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        for k in range(x.shape[2]):
            for l in range(x.shape[3]):
                for m in range(x.shape[4]):
                     y[i,j,k,l,m] = math.sin(x[i,j,k,l,m])

print('total time for serial python')
time_serial = time.time()-st
print(time_serial)

print('The speedup is')
print(time_serial/time_paral)
#print('number of threads after')
#print(openmp.omp_get_num_threads())


#print('shape of y')
#print(y.shape)
#print(y[0,:])

print('Im done. Good bye')


