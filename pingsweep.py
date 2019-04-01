import subprocess
import os
import multiprocessing

DEVNULL = open(os.devnull,'w')

def pinger(job_q):
    while True:
        address = job_q.get()
        if address is None:break

        res = subprocess.call(['ping', '-c', '1', address],stdout=DEVNULL)

        if res == 0:

            print "ping to", address, "OK"

        elif res == 2:

            print "no response from", address

        else:

            print "ping to", address, "failed!"

if __name__ == '__main__':
    pool_size = 300

    jobs = multiprocessing.Queue()

    pool = [ multiprocessing.Process(target=pinger, args=(jobs,))
             for i in range(pool_size) ]

    for p in pool:
        p.start()

    for i in range(1,255):
        jobs.put('192.168.0.{0}'.format(i))
    
    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()    

#Cleanup
DEVNULL.close()