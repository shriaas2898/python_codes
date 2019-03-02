#pgrogram to find largest n adjacent digits product

def contains_zero(number):
    while(number%10):
        number//=10
    return (number>0)
def product_of_digits(number):
    product=1
    while(number):
        product*=(number%10)
        number//=10
    return product

number=input("Enter the number")
no_of_digit=int(input("Enter number of digits"))
max_num=int("9"*no_of_digit)
print(max_num)
greatest_digits=int(number[0:no_of_digit])
min_diff=max_num-greatest_digits

for i in range(1,len(number)-no_of_digit):
    digits=int(number[i:i+no_of_digit])
    diff=max_num-digits
    if (diff<min_diff):
        if(contains_zero(digits)==False):
            min_diff=diff
            greatest_digits=digits

print("Greatest product="+str(product_of_digits(greatest_digits)))
print("of digits of number="+str(greatest_digits))
