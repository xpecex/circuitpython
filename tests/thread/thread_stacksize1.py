# test setting the thread stack size
#
# MIT license; Copyright (c) 2016 Damien P. George on behalf of Pycom Ltd

import sys
import _thread

# different implementations have different minimum sizes
if sys.implementation == 'micropython':
    sz = 2 * 1024
else:
    sz = 32 * 1024

def foo():
    pass

def thread_entry():
    foo()
    with lock:
        global n_finished
        n_finished += 1

# test set/get of stack size
print(_thread.stack_size())
print(_thread.stack_size(sz))
print(_thread.stack_size() == sz)
print(_thread.stack_size())

lock = _thread.allocate_lock()
n_thread = 2
n_finished = 0

# set stack size and spawn a few threads
_thread.stack_size(sz)
for i in range(n_thread):
    _thread.start_new_thread(thread_entry, ())

# busy wait for threads to finish
while n_finished < n_thread:
    pass
print('done')