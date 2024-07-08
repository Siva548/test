from sorting_techniques import *

arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)
print("Bubble sort:", bubble_sort(arr.copy()))
print("Selection sort:", selection_sort(arr.copy()))
print("Insertion sort:", insertion_sort(arr.copy()))
print("Merge sort:", merge_sort(arr.copy()))
print("Quick sort:", quick_sort(arr.copy()))
