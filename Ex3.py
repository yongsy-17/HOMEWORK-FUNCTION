# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]
def sum(array):
    max=0
    for i in range(len(array)):
        max=array[i]
    return max
array=[2,3,5,0,11,5,2]
print(max(array))