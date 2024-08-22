
###########1
name = input (("enter your name: "))
print ("Hello," + name + "!")

###########2
radius = float(input ("enter your radius: "))
area = 3.14 * (radius ** 2)
print ("your area is ", area)

##########3
length = float(input ("enter the length : "))
width = float(input ("enter your width  : "))
area = length * width
perimeter = 2 * (length + width)
print ("area of the rectangle is ", area)
print ("perimeter of the rectangle is ", perimeter)

############4
num1 = int(input ("enter your first integer : "))
num2 = int(input ("enter your second integer : "))
num3 = int(input ("enter your third integer : "))
sum = num1 + num2 + num3
average = sum / 3
product = num1 * num2 * num3
print ("you sum is ", sum)
print ("your product is ",product)
print ("your average is ", average)

###########5
talents=float(input ("enter talents : "))
pounds=float(input ("enter pounds : "))
lots= float(input ("enter lots : "))
pounds_per_talent = 20
lots_per_pound = 32
grams_per_lot =  13.3

grams_from_talents = talents * pounds_per_talent * lots_per_pound * grams_per_lot
grams_from_pounds = pounds * lots_per_pound * grams_per_lot
grams_from_lots = lots * grams_per_lot
total_grams = grams_from_talents + grams_from_pounds + grams_from_lots
kilograms = int(total_grams//1000)
grams = total_grams % 1000
print (f"the weight in modern units is : {kilograms} kilograms and {grams: .2f} grams.")

############6

import random
num1 = int(random.randint(0,9))
num2 = int(random.randint(0,9))
num3 = int(random.randint(0,9))
print (num1,num2,num3)
num1 = int(random.randint(0,9))
num2 = int(random.randint(0,9))
num3 = int(random.randint(0,9))
print (num1,num2,num3)
num1 = int(random.randint(0,9))
num2 = int(random.randint(0,9))
num3 = int(random.randint(0,9))
num4= int(random.randint(1,6))
print (num1,num2,num3,num4)






