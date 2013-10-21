import Sort

class MergeSort(Sort.Sort):

    def sort(self, arr):
        """ Sorts array with merge sort """
        if len(arr) <= 1:
            return arr
        mid = int(len(arr) / 2)
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        """ Merges two sorted lists """
        left_pointer = 0
        right_pointer = 0
        result = []
        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer] < right[right_pointer]:
                result.append(left[left_pointer])
                left_pointer += 1
            else:
                result.append(right[right_pointer])
                right_pointer += 1
        #Adds remaining items to result
        for i in range(left_pointer , len(left)):
            result.append(left[i])
        for i in range(right_pointer , len(right)):
            result.append(right[i])
        return result


ms = MergeSort()
print(ms.sort([-2, 45, 0, 1, 1, -5, 3, 4, 5]))
print(ms.sort([]))
print(ms.sort([42]))
print(ms.sort(["lemon", "banana","apple"]))
ms.benchmark()




