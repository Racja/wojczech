import threading
import random
import time


class Philosopher(threading.Thread):
    running = True

    def __init__(self, name, l_fork, r_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.l_fork = l_fork
        self.r_fork = r_fork

    def dine(self):
        while self.running:
            self.l_fork.acquire(True)
            locked = self.r_fork.acquire(False)
            if locked:
                break
            self.l_fork.release()
            print(self.name, "Zamienia widelce (dlaczego ?)")
            self.l_fork, self.r_fork = self.r_fork, self.l_fork
        else:
            return

        self.dining()
        self.r_fork.release()
        self.l_fork.release()

    def run(self):
        while self.running:
            time.sleep(random.random())
            print(self.name, "Chciałby jeść")
            self.dine()

    def dining(self):
        print(self.name, "Zaczyna jeść")
        time.sleep(random.random() * 5)
        print(self.name, "Kończy jeść i odkłada widelce (nareszcie)")


forks = []
philosophers = []

for i in range(1, 6):
    forks.append(threading.Lock())

for i in range(1, 6):
    philosophers.append(Philosopher("Filozof " + str(i), forks[i % 5], forks[(i + 1) % 5]))

Philosopher.running = True
random.seed()

for i in range(0, 5):
    philosophers[i].start()

time.sleep(30)
Philosopher.running = False
print("Filozofowie koncza uczte (czyżby program się kończył ?)")
