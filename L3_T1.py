import random
import time


def time_of_function(function):
    def wrapper(*args):
        start_val = time.time()
        function(*args)
        end_val = time.time()
        time_funk = end_val - start_val
        return time_funk
    return wrapper


my_list = []
my_dict = {}


@time_of_function
def list_app(i=1):
    for i in range(i):
        my_list.append(random.choice(range(1000, 10000000000)))
    return my_list


@time_of_function
def dict_app(i=1):
    for i in range(i):
        my_dict[i] = (random.choice(range(1000, 10000000000)))
    return my_dict

@time_of_function
def change_list(lst):
    for i in range(10000):  
        lst.pop(i)
    for j in range(1000):
        lst[j] = lst[j + 1]  


print(list_app(1000000))
print(dict_app(1000000))