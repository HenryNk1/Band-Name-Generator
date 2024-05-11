print("Welcome to the Band Name Generator")

country = input("What country do you live in: ")

Pet = input("What is your favorite pet: ")

print(f"Your band name could be {country} {Pet}")

Choice = input("Do you like the name(Y/N): ").lower()
if Choice == "y":
    print("Hope you succeed with your band!")
elif Choice == "n":
    genre = input("What genre of music does your band like? (Rock/Hip-Hop/Soul/Jazz)").lower()
    if genre == "rock":
        Artist = input("Favorite Arist: ")
        Car = input("Favorite Car: ")
        print(f"Your name could be {Artist} {Car}")
    elif genre == "hip-hop":
        Artist = input("Favorite Arist: ")
        Car = input("Favorite Car: ")
        print(f"Your name could be {Artist} {Car}")
    elif genre == "soul":
        Artist = input("Favorite Arist: ")
        Car = input("Favorite Car: ")
        print(f"Your name could be {Artist} {Car}")
    elif genre == "jazz":
        Artist = input("Favorite Arist: ")
        Car = input("Favorite Car: ")
        print(f"Your name could be {Artist} {Car}")
    else:
        print("Please Select from the options")
else:
    print("Please select from the options given")
