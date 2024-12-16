import time

def rangefunct(n):
    for i in range(n):
        pass

start = time.time()
rangefunct(100000)
end = time.time()
duration = end - start
print(duration)