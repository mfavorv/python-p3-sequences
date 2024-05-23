#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    if length > 0 :
        fibonacci_list.append(0)
    if length >=2:
        fibonacci_list.append(1)    
        for i in range(2, length):
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    
    print(fibonacci_list)
    pass