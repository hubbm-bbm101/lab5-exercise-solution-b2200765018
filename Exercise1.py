
def ex1():
    sum_odd = 0
    sum_even = 0
    number_of_even = 0
    avarage = 0
    number = int(input("Enter a number : "))
    for x in range(1,number+1) :
        if x % 2 == 1 :
            sum_odd += x
        else :
            sum_even += x
            number_of_even += 1
            avarage = sum_even / number_of_even

    return (sum_odd, avarage)

print(ex1())

