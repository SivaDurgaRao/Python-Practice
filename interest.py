'''. Indus Bank accepts both short- and long-term deposits from its clients and offers an interest according to the scheme chosen.
If the amount is left in the bank as a fixed deposit for a period of 7 years, the interest rate given by the bank is 7.5% per annum, and for any other scheme that is lesser than 7 years, the interest rate is 4.5% per annum. Mr.Ravi wants to deposit Rs.50,000 in either short term or long term scheme based on the returns.
According to Mr.Ravi’s choice of the scheme, display the following details
• Interest amount he will get per annum.
• Interest amount he will for the entire term.
• Total Principal Amount + Interest for the entire term

Input:
Enter the Fixed Deposit Scheme [Long/Short]: Long
Expected Output:
Rs.50000 invested in long term scheme, Interest amount per annum is Rs.3750.0
Rs.26250.0 is the interest that Mr.Ravi will earn after 7 years

Input:
Enter the Fixed Deposit Scheme [Long/Short]: Short Enter the Term: 6
Expected Output:
Rs.50000 invested in short term scheme, Interest amount per annum is Rs.2250.0
Rs.13500.0 is the interest that Mr.Ravi will earn after 6 years
'''
scheme=str(input("Enter the Fixed Deposit Scheme [Long/Short]:"))

time=int(input("enter the time period in years:"))
 
amount=int(input("enter the amount:"))
if time>=7:
    interest=(time*amount*0.075)
    print("interest for ",time ," years is",interest)
else:
    interest=(time*amount*0.045)
    print("interest for ",time ,"is",interest)