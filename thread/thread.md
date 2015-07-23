２．python线程
===
**线程定义**<br/>
什么是线程：线程是操作系统能够进行运算调度的最小单位，他被包含在进程中。一条线程指的是进程中一个单一顺序的控制流，一个进程中可以有多个线程。<br/>

**线程基础**<br/>
1.线程状态<br/>
线程有５种状态：新建、就绪、运行、死亡、阻塞<br/>

2.锁(lock)<br/>
为什么要引入锁？假想这样的一种情况，在一个进程中，一个线程负责从０～１创建一个列表，另一个线程负责倒序打印这个列表，这就出现了数据的不同步问题。为了处理线程之间的资源共享问题，引入了锁的概念。<br/>
如何解决？引入了锁以后，在同一时间内，只有一个线程可以获得对资源的访问，其余线程则在锁定池中等待锁定，获取资源访问权的线程已锁定。这样就解决了获取资源的不同步问题。<br/>

3.线程通信（条件变量）<br/>
还有一种情况，如果一个资源没有被创建，但是线程仍可能去访问这个资源，这就出现了错误。于是线程之间需要通信，创建资源的线程需要告诉其他线程该资源什么时候创建完成。<br/>
条件变量：条件变量condition就是应用于线程之间通信的变量。线程在接到条件变量通知前会在等待池中等待，接到通知后再进入锁定池。<br/>

4.线程阻塞<br/>
线程阻塞有三种情况:<br/>
1.同步阻塞：线程在锁定池中会进入同步阻塞状态，一旦成功获得锁定后又会恢复到运行状态<br/>
2.等待阻塞：线程在等待条件通知时会进入等待阻塞状态，一旦成功获得通知会恢复到运行状态<br/>
3.其他阻塞：调用time.sleep，join函数等等待IO方法时会进入阻塞。这个状态下线程不会释放已经获得的锁定。<br/>

**python中线程的实现**<br/>
python中线程的实现主要通过threading模块。我将通过消费者生产者模型说明python中线程的实现<br/>
在此之前，需要了解threading模块<br/>
1.threading模块提供的方法:<br/>
threading.currentThread()  获取当前运行的线程<br/>
threading.enumrate() 返回一个运行中的线程列表<br/>
threading.activeCount() 返回正在运行的线程的数量，与len(threading.enumrate())相同<br/>

2.threading模块提供的类:<br/>
1.Thread类，用于创建线程：

    import threading


    # 函数线程
    def func():
        print("func: Threading start!")



    # 类线程
    class MyThread(threading.Thread):
        def run():
            print("MyThread: Threading start!")


    # 启动线程
    thr = threading.Thread(target=func)
    thre = Thread()

    thr.start()
    thre.start()

Thread类还有join([timeout])方法，用于阻塞正在运行中的线程，

    import threading


    def context(t_join):
        print("context: threading start!")
        t_join.start()
        t_join.join()  # 阻塞t_join进程
        print("context: threading stop!")


    def join():
        print(join: threading start!)
        time.sleep(2)
        print(join: threading stop!)


    t_context = threading.Thread(target=context, args=(t_join,))
    t_join = threading.Thread(target=join)

    t_context.start()

2.Lock类<br/>
Lock 用于创建锁，下面这个例子体现了锁对于线程间资源调用的控制<br/>

    import threading
    import time


    data = 0
    lock = threading.Lock()  # 创建了一个可爱的小锁


    def func():
        global data  # 全局共享资源
        print("acquire lock: %s" % threading.currentThread.getName())

        if lock.acquire():
            print("get lock: %s" % threading.currentThread.getName())
            data += 1
            time.sleep(2)
            print("release lock: %s" % threading.currentThread.getName())
            lock.release()


    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)
    t3 = threading.Thread(target=func)

    t1.start()
    t2.start()
    t3.start()

3.Condition类<br/>
Condition类用于创建条件变量，条件变量一般会和锁相关联<br/>
acquire(): 调用与条件变量相关联的锁的acquire方法，尝试获取锁定<br/>
notify(): 从等待池中挑选一个线程进入锁定池，改线程会自动获取acquire方法<br/>
wait(): 等待通知，处于等待池中的等待阻塞状态<br/>


4.综合示例（消费者，生产者模型）<br/>

    """
    生产者和消费者是两个进程，通过条件变量在两个进程之间沟通，
    通过相关联的锁控制对商品（全局资源）的共享。
    """

    # 生产者消费者模型
    import threding
    import time


    # 商品
    product = None
    con = threading.Condition()


    def producer():
        """生产者"""
        global product  # 全局声明

        if con.acquire():
            # 生产者线程
            while True:
                if product is None:
                    print("produce ......")
                    product = "lolcat"  # lolcat　是一只可爱的小猫

                    con.notify()  # 商品生产完成，可以通知消费者啦

                con.wait()  # 等待消费者反馈
                time.sleep(2) # 进入阻塞状态


    def consumer():
        """消费者"""
        global product

        if con.acquire():
            #　消费者线程
            while True:
                if product is not None:
                    print("consuming ....")
                    produc = None  # 商品太火，卖完了

                    con.notify()  # 通知商家(生产者)

                con.wait()  # 等待新的商品
                time.sleep(2)


    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()
