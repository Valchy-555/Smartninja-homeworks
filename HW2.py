# Domaca naloga st.1

# intro
print('Hello dear guest! This program converts kilometers into miles')
# vnesi stevilo km + decide if new conversion is requested

while True:
    stevilo_km = int(input("Insert number of kilometers "))
    print("No of miles:", 0.621 * stevilo_km)
    ponovitev_konverzije = input("Would you like to do another conversion? Write yes or no: ")
    ponovitev_konverzije = ponovitev_konverzije.lower()

    if ponovitev_konverzije == "no":
        print("Thank you")
        break
    elif ponovitev_konverzije == "yes":
        print("")
    else:
        print("You inserted wrong answer")
        break
# kako bi tukaj lahko nadaljevali zanko, da ponovno vpraša?

# Domaca naloga st.2
num = int(input("Pick a number between 1 and 100: "))

for x in range(1, num+1):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("bizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)

# Domača naloga st.3

string = "Ali Si Ze Naredil Nalogo"
print(string.lower())