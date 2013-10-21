import random
import time
import abc

class Sort:

    @abc.abstractmethod
    def sort(self, arr):
        pass


    def benchmark(self):
        arr = []
        rg = random.Random()
        for i in range(0, 10000):
            arr.append(rg.random())

        start_time = time.clock()
        arr = self.sort(arr);
        end_time = time.clock();
        print("Sorted in : ", end_time - start_time, " seconds")
