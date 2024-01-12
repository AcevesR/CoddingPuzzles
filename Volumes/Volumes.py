import math

PI = 3.141592

def ask_float(prompt):
    return float(input(prompt))

def calculate_cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def calculate_cone_volume(radius, height):
    return (math.pi * radius**2 * height) / 3

def print_volume(volume):
    print(f"The volume of the figure is {volume}\n")

def main():
    while True:
        print("Hello.")
        print("Do you want to calculate the volume of...? \n1) Cylinder \n2) Cone")
        choice = int(input())
        
        if choice not in [1, 2]:
            print("\nWrong input.")
            break

        radius = ask_float("Write the value of the radius: ")
        height = ask_float("Write the value of the height: ")

        if choice == 1:
            volume = calculate_cylinder_volume(radius, height)
        else:
            volume = calculate_cone_volume(radius, height)

        print_volume(volume)

        print("\nDo you want to calculate another volume? \n1) Yes \n2) No")
        choice = int(input())

        if choice != 1:
            break

if __name__ == "__main__":
    main()
