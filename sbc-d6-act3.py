#Take input From The user to determine the number in the pyramid
ROWS = int(input("Enter the Pyramid:"))
#Loop to print the top of the pyramid
for stars in range (ROWS, 1, -1):
    print("*" * stars)# print a row with 'stars' number of asterisk

print("*" +" "* (ROWS - 2) + "*")# # Print a row with one asterisk at the beginning and end, and spaces in between              
# Loop to print the bottom part of the pyramid
for moons in range (2, ROWS + 1):
    print("*" * moons)# Print a row with 'moons' number of asterisks 


