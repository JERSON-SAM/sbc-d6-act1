row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

stars = 0

while stars < row:
    moon = 0
    while moon < col:
        if stars == 0 or stars == row -1 or moon == 0 or moon == col -1:
            print("*", end="")
        else:
            print(" ", end="")
        moon += 1
    print()
    stars += 1 
   
       