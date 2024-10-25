from multiprocessing import Process, Pipe

def fun(conn):
    print('子进程发送消息')
    conn.send('你好主进程')
    print('子进程接受消息')
    print(conn.recv())
    conn.close()


if __name__ == '__main__':
    conn1, conn2 = Pipe()
    p = Process(target=fun, args=(conn2,))
    p.start()
    print("主进程接受消息: ")
    print(conn1.recv())
    print("主进程发送消息：")
    conn1.send("你好子进程")
    p.join()
    print("结束测试")
