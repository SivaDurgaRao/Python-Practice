string="Can you can a can as a canner can can a can ?"
# if you want to take cases into account remove this line
string=string.lower()
string=string.split(" ")
# between index=8 and 17, how many times the word 'can' occurs
print(string.count("can"))