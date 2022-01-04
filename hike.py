'''4. Write code to obtain fee amount from the user and then calculate fee hike as 10% of fees and print the newly revised amount.

Input: 28500
Output: 31350.0
'''




amount = int(input('Enter fee amount'))
hike = (10*amount)/100
total_fee = amount+hike
print(total_fee)