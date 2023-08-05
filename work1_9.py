import time
def display(func):
    name=func.__name__
    def wrapper():
        print(name)
        t1=time.time()
        result=func()
        t2=time.time()
        print(t1)
        print(t2)
        print(t2-t1)
        return result
    return wrapper

def is_primer(num):
    if num<2:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num % i==0:
                return False
        return True

@display
def count_primer():
    count=0
    for i in range(1,10001):
        if is_primer(i):
            count+=1
    return count

count=count_primer()
print(count)
