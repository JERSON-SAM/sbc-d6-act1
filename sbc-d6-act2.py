# Take input from the user for the number of rows and columns
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
# Initialize a variable to track the current row (stars)
stars = 0
# Outer loop to iterate over each row
while stars < row:
    moon = 0 # Initialize a variable to track the current column (moon)
    while moon < col:
        # Inner loop to iterate over each column within the current row
        if stars == 0 or stars == row -1 or moon == 0 or moon == col -1:
            print("*", end="")# Print '*' if the current position is on the border
        else:
            print(" ", end="")# Print ' ' (space) if the current position is inside the border
        moon += 1  # Increment the column counter
    print() # Move to the next line after printing all columns for the current row
    stars += 1 # Increment the row counter
   
       
