from multiprocessing import Process, Queue

def fun(q, i):
    print("child process %s start put data" % i)
    q.put("i am %s communicate throught queue" % i)


if __name__ == '__main__':
    q = Queue()

    process_list = []
    
    for i in range(3):
        p = Process(target=fun, args=(q, i,))
        p.start()
        process_list.append(p)

    
    for i in process_list:
        p.join()
    
    print('main process get queue data')
    print(q.get())
    print(q.get())
    print(q.get())
    print("end test")