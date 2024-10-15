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

    