print("***********************************************************************")
print("======================PROGRAM FOR UNIT CONVERSION======================")
length_value = float(input("-> Enter a number to convert: "))
print('1: "Centimeter to Foot"')
print('2: "Feet to Inches"')
print('3: "Sqft to Sqmtrs"')
print('4: "Sqft to Hectre"')
print('5: "Sqft to Acres"')
print("***********************************************************************")
length_convert = int(input("Which conversion you want to do from 1 to 5: "))
print("Result = ")
if length_convert == 1:
    print("{} cm is equal to {} foot.".format(length_value, length_value / 30.48))
elif length_convert == 2:
    print("{} feet is equal to {} inch.".format(length_value, length_value * 12))
elif length_convert == 3:
    print("{} sqft is equal to {} sqmt.".format(length_value, length_value / 10.7639))
elif length_convert == 4:
    print("{} sqft is equal to {} hectre.".format(length_value, length_value /107639.104))
elif length_convert == 5:
    print("{} sqft is equal to {} acres.".format(length_value,length_value / 43560))
else:
    print("Please type correct number from 1 to 5.")
