import time
import threading


def test(name):
    for i in range(10):
        print(name)
        time.sleep(0.5)


t1 = threading.Thread(target=test, args=["ali"])
t2 = threading.Thread(target=test, args=["sajjad"])

t1.start()
t2.start()
