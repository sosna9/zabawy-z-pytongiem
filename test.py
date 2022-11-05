def plus_one(number):
    return number + 1


def function_call(function):
    number_to_add = 5
    return function(number_to_add)


# print(function_call(plus_one))


def odd_even_compositions(array1, array2):
    sum1 = 0
    sum2 = 0
    if array1[0] < 0:
        array1[0] *= -1
        for i in range(len(array1)):
            print(i)
            sumarr1 = pow(i, 10)
            print(sumarr1)
    else:
        for i in array1:
            print(i)
            sumarr1 = i


array = [-1, 2, 3]
array2 = [1,2,2,2]
odd_even_compositions(array, array2)



array = [1, 2, 3]
print(len(array))