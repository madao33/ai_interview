from multiprocessing import Process, Manager

def fun(dic, lis, index):
    dic[index] = 'a'
    dic['2'] = 'b'
    lis.append(index)


if __name__ == '__main__':
    with Manager() as manager:
        dic = manager.dict()
        l = manager.list(range(5))

        process_list = [] 
        for i in range(10):
            p = Process(target=fun, args=(dic, l, i))
            p.start()
            process_list.append(p)

        for res in process_list:
            res.join()
        print(dic)
        print(l)