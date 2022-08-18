def isValidMobileNumber(number):
    if len(number)!= 12:
        return False
    for i in range(0,3):
        if not number[i].isdigit() :
            return False
     
    for i in range(4,7):
        if not number[i].isdigit() :
            return False
         
    for i in range(8,12):
        if not number[i].isdigit() :
            return False
    return True



message="bnanbsdasda404-790-1083klamfdasmjd404-587-5520"

print("This string ",message," below phone numbers:")

for i in range(0, len(message)):
    if isValidMobileNumber(message[i:i+12]) :
       print(message[i:i+12])
         





