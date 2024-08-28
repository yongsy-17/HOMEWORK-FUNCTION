# EX4.Create function to find Min number in array [2,3,5,0,11,5,2]
def sum(array):
    min=0
    for i in range(len(array)):
        min=array[i]
    return min
array=[2,3,5,0,11,5,2]
print(min(array))