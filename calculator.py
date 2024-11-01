principal_amount = float(input('Enter your  amount sir/madam: '))
interest_rate = int(input('Enter your interest rate: '))
time_lapse = float(input('Enter the number of years: '))

while principal_amount <= 0:
        print('Amount can not be less than 0')
        principal_amount = float(input('Enter your  amount sir/madam: '))
while interest_rate <= 0:
 print('Interest rate can not be less that 0')
 interest_rate = int(input('Enter your interest rate: '))
while time_lapse <= 0:
 print('Time lapse can not be less than 0') 
 time_lapse = float(input('Enter the number of years: '))
 final_amount = principal_amount*pow((1+interest_rate/100), time_lapse)
 print(f'Your interest is {final_amount} after a period of {time_lapse} years')