# EX5.Create function to count of number 5 in array [2,3,5,0,11,5,2]
def sum(array):
    count=0
    for i in range(len(array)):
        if array[i]==5:
            count+=1
    return count
array=[2,3,5,0,11,5,2]
print(sum(array))