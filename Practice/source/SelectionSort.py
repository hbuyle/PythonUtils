import Sort

class SelectionSort(Sort.Sort):

    def sort(self, arr):
        """ Sorts array with selection sort """

        for i in range(0, len(arr) -1):
            smallestIndex = self.findSmallest(arr, i)
            self.swap(arr, i, smallestIndex)
        return arr

    def findSmallest(self, arr, startIndex):
        smallest = arr[startIndex];
        smallestIndex = startIndex;
        for i in range(startIndex, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallestIndex = i
        return smallestIndex

    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

ms = SelectionSort()
print(ms.sort([-2, 45, 0, 1, 1, -5, 3, 4, 5]))
print(ms.sort([]))
print(ms.sort([42]))
print(ms.sort(["lemon", "banana","apple"]))
ms.benchmark()




