import random
import string
import multiprocessing as mp
from multiprocessing.managers import BaseManager

class NapNetworkManager(BaseManager): pass

def maker():
    while 1:
        yield random.choice(string.ascii_letters)

m = maker()
port = 6000
authkey = b'nope'

def run():
    qA = mp.Queue()
    qB = mp.Queue()
    NapNetworkManager.register('qA', callable=lambda: qA)
    NapNetworkManager.register('qB', callable=lambda: qB)
    nnm = NapNetworkManager(address=('', port), authkey=authkey)
    nnm.start()

    qA = nnm.qA()
    qB = nnm.qB()
    qA.put('Hello from manager')
    try:
        while 1:
            message = qA.get()
            if message == 'quit':
                break
            elif message == 'next':
                print('putting next message')
                qB.put(next(m))
            else:
                print(message)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()

    
