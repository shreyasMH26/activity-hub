import threading
_lock = threading.Lock()
def atomic_increment(counter):
    with _lock:
        counter['value'] += 1
    return counter['value']
