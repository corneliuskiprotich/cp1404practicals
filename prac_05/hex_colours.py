COLORS = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}

print("Color names and codes:")
for name, code in COLORS.items():
    print(f"{name} - {code}")

while True:
    color_name = input("Enter a color name (or blank to stop): ").upper()
    if color_name == "":
        break
    try:
        print(f"The code for {color_name} is {COLORS[color_name]}")
    except KeyError:
        print("Invalid color name.")
