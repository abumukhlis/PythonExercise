from collections import deque


queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
print(queue)
# To check whether the queue is empty:
if not queue:
    print(queue)
