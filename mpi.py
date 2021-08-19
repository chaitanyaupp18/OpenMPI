from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 16000 # Change it based on the domain

a,b,c=[],[],[]
for i in range(n):
    a.append(i)
    b.append(i+1)
    c.append(i+2)

nsr = n//size  # nsr -> Number of Subregions (Partitions)

start = time.time()
t = 0
while t<2:
    if rank == 0:
        for i in range(nsr*(rank+1)): # 0-3
            a[i] = b[i]+c[i] 
#             print(i,a[i],rank)
    elif rank == size-1:
        for i in range(nsr*(rank),nsr*(rank+1)): # 4-7
            a[i] = b[i]+c[i]
#             print(i,a[i],rank)
    else:
        for i in range(nsr*(rank),nsr*(rank+1)): # 12-15
            a[i] = b[i]+c[i]
#             print(i,a[i],rank)
    t = time.time() - start
    
end = time.time()
print("Time elapsed",end-start,rank)
