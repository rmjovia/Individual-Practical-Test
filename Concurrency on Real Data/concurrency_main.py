""" 
Main driver script: 
- Runs basic threading demo 
- Concurrent dataset downloads 
- Parallel data analysis 
- Optional multiprocessing comparison 

""" 
 
import threading 
import time 
from multiprocessing import Process, Queue 
 
# Import helper functions 
from threading_demo import basic_thread_demo 
from data_utils import ( 
    download_dataset, URL_POPULATION, URL_COVID, URL_TEMP, 
    compute_population, compute_covid, compute_temperature 
) 
 
# Shared dictionary for datasets 
dataset_storage = {} 
 

# Part 5b-A: Multithreaded downloads 


def threaded_download(): 
    print("\n 5b-A) Multithreaded Dataset Download") 
    urls = { 
        "Population": URL_POPULATION, 
        "COVID": URL_COVID, 
        "Temperature": URL_TEMP 
    } 
    threads = [] 
    for name, url in urls.items(): 
        t = threading.Thread( 
            target=lambda n, u: dataset_storage.update({n: 
download_dataset(n, u)}), 
            args=(name, url) 
        ) 
        threads.append(t) 
        t.start() 
    for t in threads: 
        t.join() 
    print("All downloads complete.\n") 


# Part 5b-B: Concurrent Analysis 


def threaded_analysis(): 
    print("\n 5b-B) Concurrent Data Analysis ") 
    t1 = threading.Thread(target=compute_population, 
args=(dataset_storage["Population"],)) 
    t2 = threading.Thread(target=compute_covid, 
args=(dataset_storage["COVID"],)) 
    t3 = threading.Thread(target=compute_temperature, 
args=(dataset_storage["Temperature"],)) 
    for t in (t1, t2, t3): t.start() 
    for t in (t1, t2, t3): t.join() 
    print("All analysis threads complete.\n") 
 

# BONUS: Multiprocessing Comparison 
 
# Define top-level functions — required for multiprocessing
# They must NOT be defined inside another function

def process_population(q, data):
    """Compute population result and put it in the shared queue."""
    result = compute_population(data)
    q.put(("Population", result))

def process_covid(q, data):
    """Compute COVID result and put it in the shared queue."""
    result = compute_covid(data)
    q.put(("COVID", result))

def process_temperature(q, data):
    """Compute temperature result and put it in the shared queue."""
    result = compute_temperature(data)
    q.put(("Temperature", result))


# Main function to compare threading vs multiprocessing

def multiprocessing_comparison():
    """Compare time taken by threading and multiprocessing."""
    print("\n BONUS: Threading vs Multiprocessing ")

    # Measure threading time
    start = time.perf_counter()
    threaded_analysis()  # Call your existing threaded version
    thread_time = time.perf_counter() - start

    # Create a shared queue for collecting process results
    q = Queue()

    # Use normal functions instead of lambdas (Windows safe)
    procs = [
        Process(target=process_population, args=(q, dataset_storage["Population"])),
        Process(target=process_covid, args=(q, dataset_storage["COVID"])),
        Process(target=process_temperature, args=(q, dataset_storage["Temperature"])),
    ]

    # Measure multiprocessing time
    start = time.perf_counter()
    for p in procs:
        p.start()
    for p in procs:
        p.join()

    # Collect all results from the queue
    results = [q.get() for _ in procs]
    process_time = time.perf_counter() - start

    
    print("\nMultiprocessing Results:")
    for name, value in results:
        print(f"{name}: {value}")

    print(f"\nThreading Time: {thread_time:.4f}s")
    print(f"Multiprocessing Time: {process_time:.4f}s")
    print("Comparison complete.\n")
 
# MAIN EXECUTION 
 
if __name__ == "__main__": 
    print("\n Question 5: Concurrency on Real Data \n") 
 
    # 5a) Basic threading 
    basic_thread_demo() 
 
    # 5b-A) Download 
    threaded_download() 
 
    # 5b-B) Analysis 
    threaded_analysis() 
 
    # BONUS 
    multiprocessing_comparison() 