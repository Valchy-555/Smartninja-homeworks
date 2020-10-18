# Domaca naloga st.1

mood = input("How do yo feel? ")

if mood == "happy":
    print("It is great to see you happy!")

elif mood == "nervous":
    print("Take a deep breath 3 times.")

elif mood == "sad":
    print("Call a friend")

elif mood == "excited":
    print("Good for you!")

elif mood == "relaxed":
    print("Woohoo zen is on!")

else:
    print("I don't recognize this mood")

# Domaca naloga st.2

secret = 5
guess = int(input("Ugani skrivno stevilo"))
if secret == guess:
    print("Bravissimo")
else:
    print("Vec srece prihodnjic!")

# Domaca naloga st.3

st1 = int(input('Vnesite prvo število: '))
st2 = int(input('Vnesite drugo število: '))
operacija = input('Vnesite računasko operacijo: ')
if operacija == "sestevanje":
    print(st1 + st2)
elif operacija == 'odstevanje':
    print(st1 - st2)
elif operacija == 'mnozenje':
    print(st1 * st2)
elif operacija == 'deljenje':
    print(st1 / st2)