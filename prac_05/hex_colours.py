colour_codes = {"army green": "#4b5320",
                "aqua": "#00ffff",
                "ash grey": "#b2beb5",
                "barn red": "#7c0a02",
                "banana yellow": "#ffe135",
                "black": "#000000",
                "blue1": "#0000ff",
                "bone": "#e3dac9",
                "bronze": "#cd7f32",
                "bubble gum": "#ffc1cc",
                "celeste": "#b2ffff",
                "cerise": "#de3163"}

colour_choice = ("Army Green", "Aqua", "Ash Grey", "Barn Red", "Banana Yellow", "Black", "Blue1", "Bone", "Bronze", "Bubble Gum", "Cerise")
print(colour_choice)

colour = input("Enter a colour: ").lower()

while colour != "":
    if colour in colour_codes:
        print(colour.capitalize(), "is", colour_codes[colour])
    else:
        print(colour.capitalize(), "is not a valid colour")
    colour = input("Enter a colour: ").lower()


