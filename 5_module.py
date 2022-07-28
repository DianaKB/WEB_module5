import time
from multiprocessing import Process

def factorize(*number):
    result = []
    
    for n in number:
        result_number = []
        for i in range(1, n//2 + 1):
            if n % i == 0:
                result_number.append(i)
        result_number.append(n)
        result.append(result_number)
    return result

def factorize_2(*number):
    result = []
    
    for n in number:
        result_number = []
        for i in range(1, n//2 + 1):
            if n % i == 0:
                result_number.append(i)
        result_number.append(n)
        result.append(result_number)
    return result

#start_time = time.perf_counter() 
#a, b, c, d  = factorize(128, 255, 99999, 10651060)
#end_time = time.perf_counter()
#print(f"{end_time-start_time:0.2f} second's to complete.")

#assert a == [1, 2, 4, 8, 16, 32, 64, 128]
#assert b == [1, 3, 5, 15, 17, 51, 85, 255]
#assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
#assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

start_time = time.perf_counter()
proc = Process(target=factorize_2(128, 255, 99999, 10651060))
proc.start()
proc.join()
end_time = time.perf_counter()
print(f"{end_time-start_time:0.2f} second's to complete.")
