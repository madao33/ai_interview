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
