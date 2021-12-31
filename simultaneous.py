from multiprocessing import Process, Queue
from main import Main
from handController import Controller

qs1 = Queue()

if __name__ == '__main__':

    s2 = Process(target=Main, args=(qs1,))
    s2.daemon = True
    s2.start()

    Controller(qs1)
    s2.join()