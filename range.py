#write a program that print the highest number from this range [2,8,0,6,16,14,1]
# using the sort nethod to print the highest number in a list
#declaring a variable to hold the range of value
number = [2,8,0,6,16,14,1]
number.sort()

#displaying the last element of the list
print("largest number in the list is:",number[-1])

#using the loop throught method

#variable to store the largest number
highest_number = number[0]

for i in number:
    if i > highest_number:
        highest_number= i
print("largest number is:",highest_number)