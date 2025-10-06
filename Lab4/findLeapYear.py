#Victor Mmunga
#date: 9-23-2025
#lab: 4
# This program checks if a given year is leap year 


def Leap_year(year):
        if year % 4 == 0:
            if year % 100==0:
                if year% 400 ==0:
                    return True     
                else:  
                     return False       
            else:
                return True
        else:
                return False
def main():
    while True:
        year= int(input("Enter a year: "))
        answer= Leap_year(year)
        if answer:
           print("Yes")
        else:
           print("No")
if __name__ == "__main__":
      main()
           