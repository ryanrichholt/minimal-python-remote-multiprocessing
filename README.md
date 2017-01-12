# minimal-python-remote-multiprocessing
A minimal example of the Multiprocessing remote manager in Python3

Start `manager.py` in one terminal window then start a new Python session in another. 
Import `client` and you can communicate with the manager like this:

```
>>> s = client.qA
>>> r = client.qB
>>> s.put('hi')
>>> s.put('next')
>>> print(r.get())
J
```
