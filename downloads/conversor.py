from colorama import init, Fore, Style, Back

init()

def km_mi():
    a = float(input(Fore.BLUE + "Kilometers to convert: " + Style.RESET_ALL))
    result = a / 1.609
    print(Fore.GREEN + f"{a} KM equals {result} miles" + Style.RESET_ALL)
def mi_km():
    a = float(input(Fore.BLUE + "Miles to convert: " + Style.RESET_ALL))
    result = a * 1.609
    print(Fore.GREEN + f"{a} mile(s) equals {result} KM" + Style.RESET_ALL)
def lbs_kg():
    a = float(input(Fore.BLUE + "Pounds to convert: " + Style.RESET_ALL))
    result = a / 2.205
    print(Fore.GREEN + f"{a} pound(s) equals {result} KG" + Style.RESET_ALL)
def kg_lbs():
    a = float(input(Fore.BLUE + "KG to convert:" + Style.RESET_ALL))
    result = a * 2.205
    print(Fore.GREEN + f"{a} KG equals {result} pound(s)." + Style.RESET_ALL)
def ce_fa():
    a = float(input(Fore.BLUE +"Select Degrees Celsius to convert: " + Style.RESET_ALL))
    result = (a * 9/5) + 32 
    print(Fore.GREEN + f"{a}°C == {result}°F" + Style.RESET_ALL)

def fa_ce():
    a = float(input(Fore.BLUE + "Select °F to convert: " + Style.RESET_ALL))
    result = (a - 32) * 5/9
    print(Fore.GREEN + f"{a}°F == {result}°C" + Style.RESET_ALL)

print(Fore.CYAN + "Unit converter." + Style.RESET_ALL)
print(Fore.CYAN + "Please, select an option (Option Number):" + Style.RESET_ALL)
while True:
    try:
        mode = int(input(Fore.MAGENTA + """
            1. KM -> Miles
            2. Miles -> KM
            3. KG -> lbs
            4. lbs -> KG
            5. °C -> °F
            6. °F -> °C
            >>> """ + Style.RESET_ALL))
        
        if mode == 1:
            print(Fore.MAGENTA + "Selected: Kilometers to Miles" + Style.RESET_ALL)
            km_mi()
        elif mode == 2:
            print("Selected: Miles to Kilometers" + Style.RESET_ALL)
            mi_km()
        elif mode == 3:
            print(Fore.MAGENTA + "Selected: Kilograms to pounds" + Style.RESET_ALL)
            kg_lbs()
        elif mode == 4:
            print(Fore.MAGENTA + "Selected: Kilometers to Miles" + Style.RESET_ALL)
            lbs_kg()
        elif mode == 5:
            print(Fore.MAGENTA + "Selected: °C to °F" + Style.RESET_ALL)
            ce_fa()
        elif mode == 6:
            print(Fore.MAGENTA + "Selected: °F to °C" + Style.RESET_ALL)
            fa_ce()
    except ValueError:  
            print(Fore.RED + "Incorrect option. Please retry." + Style.RESET_ALL)
            continue