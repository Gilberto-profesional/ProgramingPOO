import threading
Lock=threading.Lock()
ITERS = 1000000
x = [0]

def worker():
    for _ in range(ITERS):
        Lock.acquire()
        x[0] += 1
        Lock.release()


        #with Lock:
        #    x[0] += 1
def main():
    x[0] = 0  # you may use `global x` instead of this list trick too
    t1 = threading.Thread(target=worker)
    t2 = threading.Thread(target=worker)
  
    t1.start()
    t2.start()
    t1.join()
    t2.join()

for i in range(5):
    main()
    print(f'iteration {i}. expected x = {ITERS*2}, got {x[0]}')