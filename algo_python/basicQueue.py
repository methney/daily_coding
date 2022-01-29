import queue

maze = ['4','5','2','8']
nums = queue.Queue()
nums.put('0')
for i in maze:
    # print(i)
    # 이렇게하면, 무슨배열처럼 쭈루륵 다 나오느냐? 처음에 넣은순서대로 나오는데...numgs.get()을 할때마다 하나씩 나온다.
    v = nums.get()
    # print(v)
    # 몇번을 사용해야 다나오게 할지 모르므로,,그냥 이경우엔 하나의 String으로 처리를 한것 같다.  
    # 결국, 이 케이스에서는 string이나 queue나 다를게 없는거지...
    # get으로 빼고 더해서 다시 넣고.. 이런식으로 했으니.. 큐에는 결국 하나의 string만 들어가 있는거다.
    # 또한 넣을때에 새로넣을값을 앞에넣냐 뒤에넣냐에 따라 값이 달라지게되니..조심(경우에따라 사용하면된다.)
    # https://www.geeksforgeeks.org/queue-in-python/
    # together = i + v
    together = v + i
    nums.put(together)
    for j in together:
        print(j)
    print('------')
print(nums.get())


