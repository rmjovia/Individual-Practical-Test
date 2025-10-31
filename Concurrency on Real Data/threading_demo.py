""" 
Simple threading example: each thread prints numbers 1-5 with a 1 s delay. 

""" 
 
import threading 
import time 
 
def print_numbers(name): 
    """Thread task: print numbers 1-5 with 1 s delay.""" 
    for i in range(1, 6): 
        print(f"{name} -> {i}") 
        time.sleep(1) 
    print(f"{name} complete.\n") 
 
def basic_thread_demo(): 
    """Launch 3 threads and wait for completion.""" 
    print("\n 5a) Basic Threading") 
    threads = [] 
    for i in range(1, 4): 
        t = threading.Thread(target=print_numbers, args=(f"Thread-{i}",)) 
        threads.append(t) 
        t.start() 
    for t in threads: 
        t.join() 
    print("All threads complete.\n") 

if __name__ == "__main__":
    basic_thread_demo()
