wala = []# Initialize an empty list
user = input("Enter the word: ")#Take input in the user 
# Generate the reversed version of the user, remove spaces, converted into lowercase
palindrome = "".join(reversed(user.replace(" ","").lower()))
# Store the cleaned and lowercase version of the user input in the list
j = user.replace(" ","").lower() 
wala.append(j)
# Iterate through the list (although it only has one element)
for i in wala:
    if i == palindrome:
       print(f" '{user}'. Is a Palindrome" ) # If the cleaned input is equal to its reversed version, print it's a palindrome
    # If not, print the original input and its reversed version, stating it's not a palindrome
    else:
       print(f"'{user}' reversed is {palindrome}.Is not a palindrome.")