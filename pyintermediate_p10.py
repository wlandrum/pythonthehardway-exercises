# Multiprocessing
# The point of multiprocessing is to put more power towards processing scripts
# The Global Interpreter Lock (GIL) is the cause of this and was originally implemented as a memory management safe guard
# CPUs = Cores
# The idea is to pass variables between each process
import multiprocessing

def spawn(num, num2):
    print('Spawned! {} {}'.format(num,num2))

# Will only run when the scipt is being called
if __name__ == '__main__':
    for i in range(100):
        p = multiprocessing.Process(target=spawn, args=(i,i+1))
        p.start()
        p.join() # Use this if you want to wait for important variable
