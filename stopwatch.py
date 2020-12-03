import time

class StopWatch:

    def __init__(self):
        print("--- STOPWATCH START ---")
        self.start_time = time.time()
    
    def stop(self):
        self.stop_time = time.time() - self.start_time 
        print("--- STOPWATCH STOP ---")
        print("Exec time: %s seconds" % (self.stop_time))
        print("----------------------")