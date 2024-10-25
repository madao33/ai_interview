# Python知识点

## python多进程

参考链接：https://zhuanlan.zhihu.com/p/64702600

Python中的多进程是通过multiprocessing包来实现的，和多线程的threading.Thread差不多，它可以利用multiprocessing.Process对象来创建一个进程对象。这个进程对象的方法和线程对象的方法差不多也有start(), run(), join()等方法，其中有一个方法不同Thread线程对象中的[守护线程](https://zhida.zhihu.com/search?content_id=102507664&content_type=Article&match_order=1&q=守护线程&zhida_source=entity)方法是setDeamon，而Process进程对象的[守护进程](https://zhida.zhihu.com/search?content_id=102507664&content_type=Article&match_order=1&q=守护进程&zhida_source=entity)是通过设置daemon属性来完成的。

### **python多线程实现方法一**

```python
from multiprocessing import Process

def runner(pool_id):
    print(f'pool_id: {pool_id}')

if __name__ == '__main__':
    process_list = []
    pool_size = 10
    for pool_id in range(pool_size):

        p = Process(target=runner, args=(pool_id,))

        p.start()

        process_list.append(p)
    
    for p in process_list:
        p.join()

```

这里实现了真正的并行操作，就是多个CPU同时执行任务。我们知道[进程](https://zhida.zhihu.com/search?content_id=102507664&content_type=Article&match_order=20&q=进程&zhida_source=entity)是python中最小的资源分配单元，也就是进程中间的数据，内存是不共享的，每启动一个进程，都要独立分配资源和拷贝访问的数据，所以进程的启动和销毁的代价是比较大了，所以在实际中使用多进程，要根据服务器的配置来设定。

### **python多线程实现方法二-继承**

```python
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        print("test process", self.name)


if __name__ == '__main__':
    process_list = []
    for i in range(10):
        p = MyProcess(str(i))
        p.start()
        process_list.append(p)

    for i in process_list:
        p.join()
```

### **多进程间的通信**

进程是系统独立调度核分配系统资源（CPU、内存）的基本单位，进程之间是相互独立的，每启动一个新的进程相当于把数据进行了一次克隆，子进程里的数据修改无法影响到主进程中的数据，不同子进程之间的数据也不能共享，这是多进程在使用中与多线程最明显的区别。但是难道Python多进程中间难道就是孤立的吗？当然不是，python也提供了多种方法实现了多进程中间的通信和数据共享（可以修改一份数据）

**进程队列**

Queue在多线程中也说到过，在生成者消费者模式中使用，是线程安全的，是生产者和消费者中间的数据管道，那在python多进程中，它其实就是进程之间的数据管道，实现[进程通信](https://zhida.zhihu.com/search?content_id=102507664&content_type=Article&match_order=1&q=进程通信&zhida_source=entity)。

```python
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
```

### **管道Pipe**

管道Pipe和Queue的作用大致差不多，也是实现进程间的通信

```python
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

```

### **Managers**

Queue和Pipe只是实现了数据交互，并没实现数据共享，即一个进程去更改另一个进程的数据。那么就要用到Managers

```python
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
```

结果

```shell
{3: 'a', '2': 'b', 0: 'a', 2: 'a', 9: 'a', 7: 'a', 1: 'a', 4: 'a', 8: 'a', 6: 'a', 5: 'a'}
[0, 1, 2, 3, 4, 3, 0, 2, 9, 7, 1, 4, 8, 6, 5]
```

可以看到主进程定义了一个字典和一个列表，在子进程中，可以添加和修改字典的内容，在列表中插入新的数据，实现进程间的数据共享，即可以共同修改同一份数据

### 进程池

进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。就是固定有几个进程可以使用。

进程池中有两个方法：

apply：同步，一般不使用

apply_async：异步

```python
from  multiprocessing import Process,Pool
import os, time, random

def fun1(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    pool = Pool(5) #创建一个5个进程的进程池

    for i in range(10):
        pool.apply_async(func=fun1, args=(i,))

    pool.close()
    pool.join()
    print('结束测试')
```

对`Pool`对象调用`join()`方法会等待所有子进程执行完毕，调用`join()`之前必须先调用`close()`，调用`close()`之后就不能继续添加新的`Process`了。

