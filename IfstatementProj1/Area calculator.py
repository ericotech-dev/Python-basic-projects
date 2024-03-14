print("****AREA CALCULATOR****")

print("""Press 1 to get the area of a square
        press 2 to get the area of a rectangle
        press 3 to get the area of a triangle
        press 4 to get the area of a circle""")

choice = int(input("Enter number from 1-4:"))

if choice == 1:
    side = float(input("Enter the length of one side:"))
    area = side**2
    print("The area of a square is", area)

elif choice == 2:
    length = float(input("Enter the length:"))
    width = float(input("Enter the width:"))
    area = length*width
    print("The area of a rectangle is", area)

elif choice == 3:
    base = float(input("Enter the base:"))
    height = float(input("Enter the height:"))
    area = 0.5*base*height
    print("The area of a triangle is", area)

elif choice == 4:
    radius = float(input("Enter the radius:"))
    area = ((22/7)*(radius**2))
    print("The area of a circle is", area)

else:
    print("invalid input")
