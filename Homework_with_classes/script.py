
class List_compiler:
    def __init__(self):
        self.mylist = []
    
    def add_item(self, item):
        self.mylist.append(item)
    
    def compile_list(self):
        return self.mylist
    
    def binary_search(self,num):
        low = 0
        high = len(self.mylist) - 1
        while low <= high:
            mid = (low + high)
            guess = self.mylist[mid]
            if guess == num:
                return mid
            if guess > high:
                high = mid - 1
            else:
                low = mid + 1
        return None

    def bubble_sort(self,  arr):
        for i in range(len(arr)):
            for j in range(0, len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selection_sort(self, arr):
    
        for i in range(len(arr)):
            min_index= i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr 


    def quick_sort(self, arr):
        if len(arr) < 2:
            return arr
        pivot = arr[len(arr) // 2]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return self.quick_sort(less) + equal + self.quick_sort(greater)
    def bs_list(self):
        self.mylist = self.bubble_sort(self.mylist)
    def ss_list(self):
        self.mylist = self.selection_sort(self.mylist)
    def qs_list(self):
        self.mylist = self.quick_sort(self.mylist)

mylist = List_compiler()

mylist.add_item(5)
mylist.add_item(25)
mylist.add_item(9)
mylist.add_item(10)
mylist.add_item(4)
mylist.add_item(21)
mylist.add_item(35)
mylist.add_item(26)
mylist.add_item(19)
mylist.add_item(6)




# mylist.ss_list() #Selection Sort
# mylist.qs_list() #Quick Sort
mylist.bs_list() #Bubble Sort 



print(mylist.compile_list())

print(mylist.binary_search(35)) # Binary Search
