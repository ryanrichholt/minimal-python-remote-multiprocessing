import time
import threading
from multiprocessing.managers import BaseManager

class NapNetworkManager(BaseManager): pass


class HostMonitor(threading.Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        try:
            while 1:
                self.q.empty()
                time.sleep(.1)
        except EOFError:
            print('Host has died...')


def run():
    """ Start node_b.py then start a Python session. Import node_w
    and you can communicate to node_b with node_w.qA.put('msg').
    A host monitor can be started with node_w.HostMonitor(q). Send
    node_b the message 'quit' and see what happens.
    """
    port = 6000
    authkey = b'nope'

    NapNetworkManager.register('qA')
    NapNetworkManager.register('qB')
    nnm = NapNetworkManager(address=('127.0.0.1', port), authkey=authkey)
    nnm.connect()

    qA = nnm.qA()
    qB = nnm.qB()

    return qA, qB

qA, qB = run()
