# question 7
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentnumbers = alist[index]
     position = index

     while position>0 and alist[position-1]>currentnumbers:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentnumbers

alist = [2, 7, 9, 4, 1, 5, 3, 6, 0, 8]
insertionSort(alist)
print(alist)
