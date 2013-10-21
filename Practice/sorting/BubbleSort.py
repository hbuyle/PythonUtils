import Sort

class BubbleSort(Sort.Sort):

    def sort(self, arr):
        """ Sorts array with bubble sort """
        didSwap = True
        while didSwap:
            didSwap = False
            for i in range(0, len(arr) -1):
                first = arr[i]
                second = arr[i+1]
                if (second < first):
                    self.swap(arr, i, i+1)
                    didSwap = True
        return arr

    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

ms = BubbleSort()
print(ms.sort([-2, 45, 0, 1, 1, -5, 3, 4, 5]))
print(ms.sort([]))
print(ms.sort([42]))
print(ms.sort(["lemon", "banana","apple"]))
ms.benchmark()




