<h1 align="center">Sorting Algorithms in Python</h1>

## In the example below the list that must be sorted in ascending order
## Sort Selection Algorithm Operation
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
