#create a program which
#prompt the user to enter the number of each kind of coins
#print the total value of your change in pretty format Euro symbol



ten = float(input("Please enter the number of 0.l0 euro coins that you have"))
twenty = float(input("Please enter the number of 0.20 euro coins that you have"))
fifty = float(input("Please enter the number of 0.50 euro coins that you have"))
one = float(input("Please enter the number of 1 euro coins that you have"))
two = float(input("Please enter the number of 2 euro coins that you have"))

total = float((ten*0.10)+(twenty*0.20)+(fifty*0.50)+(one*1.00)+(two*2.00))


print(f'€{total}')
