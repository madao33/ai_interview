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





