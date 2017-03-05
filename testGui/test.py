from multiprocessing import Process
import time

def f(name):
    time.sleep(4)
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.daemon=True
    p.start()
    p.terminate()
    p.join()
