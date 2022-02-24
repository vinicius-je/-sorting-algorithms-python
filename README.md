<h1 align="center">Sorting Algorithms in Python</h1>

## In the example below the list that must be sorted in ascending order
## Selection Sort Algorithm Operation
```python
list = [70, 30, 80, 10, 20]
```
### Must select the lowest value element from the list, in the first execution is 10. Then change the first element in the list to 10:
```python
list = [10, 30, 80, 70, 20]
```
### Now we got a sublist:
```python
list = [10, 30, 80, 70, 20]
sublist = [30, 80, 70, 20]
```
### In a list with n elements, must repeat the execution until the element at position n-1:
```python
#first execution
list = [10, 30, 80, 70, 20]
sublist = [30, 80, 70, 20]
#second execution
list = [10, 20, 80, 70, 30]
sublist = [80, 70, 30]
#third execution
list = [10, 20, 30, 70, 80]
sublist = [70, 80]
#fourth execution
list = [10, 20, 30, 70, 80]
sublist = [80]
#end, we got the sorted list
sorted list = [10, 20, 30, 70, 80]
```

## Bubble Sort Algorithm Operation
```python
list = [10, 30, 80, 70, 20]
```
### We runs n-1 comparisons between an element and its successor n-1 times, if the value of the sucessor element is less than the element selected, we must change swap its positions:
```python
#first execution
list = [10, 30, 80, 70, 20]
#the positions of 80 was switch with 70 and 80 switch with 20 
output = [10, 30, 70, 20, 80]
#second execution
list = [10, 30, 70, 20, 80]
#the positions of 70 was switch with 20 
output = [10, 30, 20, 70, 80]
#third execution
list = [10, 30, 20, 70, 80]
output = [10, 20, 30, 70, 80]
#the positions of 30 was switch with 20 
#end, we got the sorted list
sorted list = [10, 20, 30, 70, 80]
```

