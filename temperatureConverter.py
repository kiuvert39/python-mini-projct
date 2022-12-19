print("\t\t\tWelcome To temperature conveter.....")
print("\t\t pleace use only lower case leters")
punit = input ("what unit have you been given?")
covertingUnit = input("enter the unit you want to convert to:")
value=input("\t\t\t\tenter the value you want to convert :")
#formulars to conver from one temperaature scale to another
# when kelvin is given to conver to  farenheit and celcus  respectively
temp_farenheit1 = ((int(value) - 273)*(9/5)) + 32
tem_celcus1 =(273 - (int)(value) )
# when celcus is given to convert to kelvin and farenheit respectively
temp_farenheit2 = (((int)(value) )*(9/5)) + 32
temp_kelvin1 = ((int)(value)  + 273)
#wwhen farenheit is given to conver from kelvin and celcus respectively
temp_kelvin2 = ((5/9)*(int)(value) ) + 459.69
tem_celcus2 = ((int)(value) - 32)*(5/9)
if punit == "celcus" and covertingUnit == "kelvin":
    # if covertingUnit == "kelvin":
      result =temp_kelvin1
      print("\t\t\t\tconverting from celcus to kelvin gives: %f K" % (result))
      print("*"*50)
elif punit == "celcus" and covertingUnit == "farenheit":
         result = temp_farenheit2
         print("\t\t\t\tconverting from celcus to farenheit gives: %f F" % (result))
         print("*" * 50)
elif punit == "kelvin" and covertingUnit =="farenheit":
    result = temp_farenheit1
    print("\t\t\t\tconverting from kelvin to farenheit gives: %f F"%(result))
    print("*" * 50)
elif punit == "kelvin" and covertingUnit =="celcus":
    result = tem_celcus1
    print("\t\t\t\tconverting from kelvin to celcus gives: %f C" % (result))
    print("*" * 50)
elif punit == "farenheit" and covertingUnit =="kelvin":
    result = temp_kelvin2
    print("\t\t\t\tconverting from farenheit to kelvin gives: %f K"%(result))
    print("*" * 50)
elif punit == "farenheit" and covertingUnit =="celcus":
    result = tem_celcus2
    print("\t\t\t\tconverting from farenheit to celcus gives: %f C" % (result))
    print("*" * 50)
else: print("\t\t\t\tinvalid temmperature unit!  prongram ended.")