import time
from multiprocessing import Pool

def double(number):
    time.sleep(1)
    return(number*2)
    
result = []
start = time.time()
for i in range (20):
    result.append(double(i))
end = time.time()

print(result)
print('It takes {}'.format(end-start))

print ('And it is multiprocessing time!')
start = time.time()
pool = Pool(processes=20)
result = pool.map(double,range(20))
end = time.time()

print(result)
print('It takes {}'.format(end-start))
