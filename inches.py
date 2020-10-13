

MAX = 3

def main():
    lst = []
    for counter in range(MAX):
        feet = float(input("\nEnter the number of feet in numerics: "))
        lst.append(feet)
        feetToInches(feet)
    print("\nThe total values entered by the user is", "{:,}".format(sum(lst)),".")
    print("\nProgram terminated normally.")
    
def feetToInches(number):
    inches = number * 12
    print("There are", inches, "inches in", "{:,}".format(number), "feet.")
    
    
main()


