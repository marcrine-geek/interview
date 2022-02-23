# Marcrine Musimbi
# python function that prompts the user to enter their income and returns the tax they are to pay. Tax rate is 30%.

def tax(x):
# y is the tax they should pay
#     check if x is empty
    if x=='':
        print('Please enter your income')
#     if not empty
    else:
        y=int(x) * int(30)/int(100)
        print(y)
#     return y

# prompt user to enter their income
z=input('enter your income: ')
tax(z)
