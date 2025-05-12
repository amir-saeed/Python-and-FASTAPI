import threading
import time

class SafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1
            return self.value

def worker(counter, worker_id):
    for _ in range(10):  # Each worker increases the counter 10 times
        new_value = counter.increment()
        print(f"Worker {worker_id}: Counter is now {new_value}")
        time.sleep(0.1) #small pause, so we can see what is happening.

if __name__ == "__main__":
    my_counter = SafeCounter()
    workers = []

    # Create 3 worker threads
    for i in range(3):
        worker_thread = threading.Thread(target=worker, args=(my_counter, i))
        workers.append(worker_thread)
        worker_thread.start()

    # Wait for all workers to finish
    for worker_thread in workers:
        worker_thread.join()

    print(f"Final counter value: {my_counter.value}")