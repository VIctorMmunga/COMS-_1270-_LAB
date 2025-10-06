#Victor Mmunga
#DATE: 9-22- 2025
#

import myShapes
import myPhysics
import myOhmsLaw
import myFinances

def main():
    running = True
    while running:
      choice = input("\nChoose a module: [myShapes], [myPhysics], [myOhmsLaw], [myFinances], or [quit]: ")

      if choice == "myShapes":
            print("1: Area of Rectangle\n2: Rectangle Perimeter\n3: Area of Circle\n4: Circle Circumference")
            option = input("Select a shape function: ")

            if option == "1":
                w = float(input("Width: "))
                h = float(input("Height: "))
                print("Area =", myShapes.areaOfRectangle(w, h))
            elif option == "2":
                w = float(input("Width: "))
                h = float(input("Height: "))
                print("Perimeter =", myShapes.rectanglePerimeter(w, h))
            elif option == "3":
                r = float(input("Radius: "))
                print("Area =", myShapes.areaOfCircle(r))
            elif option == "4":
                r = float(input("Radius: "))
                print("Circumference =", myShapes.circleCircumference(r))
            else:
                print("Invalid shape option.")
      elif choice == "myPhysics":
            print("1: Distance = Speed × Time\n2: Velocity = Acceleration × Time")
            option = input("Select a physics function: ")
            if option == "1":
                s = float(input("Speed: "))
                t = float(input("Time: "))
                print("Distance =", myPhysics.distanceSpeedTime(s, t))
            elif option == "2":
                a = float(input("Acceleration: "))
                t = float(input("Time: "))
                print("Velocity =", myPhysics.velocityAccelerationTime(a, t))
            else:
                print("Invalid physics option.")

      elif choice == "myOhmsLaw":
            print("1: Voltage\n2: Resistance\n3: Current")
            option = input("Select an Ohm's Law function: ")

            if option == "1":
                i = float(input("Current: "))
                r = float(input("Resistance: "))
                print("Voltage =", myOhmsLaw.calculateVoltage(i, r))
            elif option == "2":
                v = float(input("Voltage: "))
                i = float(input("Current: "))
                print("Resistance =", myOhmsLaw.calculateResistance(v, i))
            elif option == "3":
                v = float(input("Voltage: "))
                r = float(input("Resistance: "))
                print("Current =", myOhmsLaw.calculateCurrent(v, r))
            else:
                print("Invalid Ohm's Law option.")

      elif choice == "myFinances":
            print("1: Annual Percentage Rate\n2: Compound Amount")
            option = input("Select a finance function: ")

            if option == "1":
                p = float(input("Principal: "))
                r = float(input("Rate (decimal): "))
                t = float(input("Time (years): "))
                print("APR =", myFinances.annualPercentageRate(p, r, t))
            elif option == "2":
                p = float(input("Principal: "))
                r = float(input("Rate (decimal): "))
                t = float(input("Time (years): "))
                print("Compound Amount =", myFinances.compoundAmount(p, r, t))
            else:
                print("Invalid finance option.")

      elif choice.lower() == "quit":
            running = False
            print("Exiting program...")
      else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()