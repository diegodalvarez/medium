
#make a big list of integers
int_list = [3, 4, 5, 6, 5, 4, 3, 2, 1, 3, 4, 4, 3, 2, 4, 6, 2, 1, 32, 4, 55, 3, 2, 1, 4, 6, 78, 8, 5, 6, 0, 9, 8, 6, 3, 5, 6, 7, 7, 8, 8, 4, 2]

#then they make a function 
def square(x):
    return x ** 2

#do the calculation
result = [square(item) for item in int_list]

