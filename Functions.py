import requests
import json
# API Base URL
API_URL = requests.get("https://www.dnd5eapi.co/api/spells/")
tempbook = []
# File to store spells
spellbook = open("spellbook.json", "a")
spellbook.close()

def list_spells():
    """
    Fetches and lists all spell names from the D&D 5e API.

    Makes a request to the D&D 5e API to retrieve spell data and stores the names
    of all spells in a list. Returns the list of spell names.
    
    Returns:
        list: A list of spell names.
    """
    #Gets the spell data
    url = f"https://www.dnd5eapi.co/api/spells"
    response = requests.get(url)
    spell_data = response.json()
    print(type(spell_data))
    count = 0
    mylist = []
    #Adds all spell names into a list
    try:
        for i in spell_data["results"]:
            count = count + 1
            mylist.append(spell_data["results"][count]["name"])
    except:
        pass
    return mylist


def search_spell(spell_name):
    """
    Searches for a specific spell by name from the D&D 5e API.

    This function takes a spell name as input, processes the name to make it suitable
    for a URL request, and retrieves the spell data. It returns the spell name, level,
    and description if found; otherwise, it returns a message indicating the spell was not found.

    Args:
        spell_name (str): The name of the spell to search for.

    Returns:
        str: A string containing the spell's name, level, and description, or a message indicating
             the spell was not found.
    """
    #Changes the input to be availiable for search
    fixedspell = str(spell_name.lower())
    fixspell = fixedspell.replace(" ","-")
    #Searches through the api for the spell
    url = f"https://www.dnd5eapi.co/api/spells/{fixspell}"
    try:
        #Modifies the output to be easier to read
        response = requests.get(url)
        spell_data = response.json()
        string1 = str(f"""{spell_data["name"]} {spell_data["level"]}\n {spell_data["desc"]}""")
        return string1
    except:
        return "Spell not found"

def add_spell_to_spellbook(spell_name):
    """
    Adds a spell to the user's spellbook (stored in a JSON file).

    This function searches for the specified spell by name, retrieves the data from the
    D&D 5e API, and appends the spell name and level to a JSON file (spellbook.json). 
    If the spell is added successfully, a confirmation message is printed.

    Args:
        spell_name (str): The name of the spell to be added to the spellbook.
    """
    #Changes the input to be availiable for search
    fixedspell = str(spell_name.lower())
    fixspell = fixedspell.replace(" ","-")
    #Searches through the api for the spell
    url = f"https://www.dnd5eapi.co/api/spells/{fixspell}"
    response = requests.get(url)
    spell_data = response.json()
    #Converts the data into data to be stored
    lvl = str(spell_data["level"])
    x = str(spell_name + " Level: " + lvl)
    z = str(x + "\n")
    tempbook.append(z)
    y = json.dumps(x)
    y = f"{y} \n"
    if spell_name:
        #Stores the data in a json file
        spellbook = open("spellbook.json", "a")
        spellbook.write(y)
        spellbook.close()
        print(f"Added {spell_name} to your spellbook!")


def view_spellbook():
    """
    Displays all spells currently stored in the spellbook (spellbook.json).

    Opens the spellbook JSON file and reads its contents. If the file is empty, 
    it returns a message indicating the spellbook is empty. Otherwise, it returns 
    the content of the file.

    Returns:
        str: The contents of the spellbook file or a message indicating the file is empty.
    """
    """Display all stored spells."""
    with open("spellbook.json", 'r') as spellbook:
        # Read the content of the file
        file_content = spellbook.read()
        if len(file_content) < 1:
            return "spellbook empty"
        else:
            return file_content