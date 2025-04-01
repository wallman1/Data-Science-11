import requests
import json
# API Base URL
API_URL = requests.get("https://www.dnd5eapi.co/api/spells/")
tempbook = []
# File to store spells
spellbook = open("spellbook.json", "a")
spellbook.close()

def list_spells():
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
    """Display all stored spells."""
    with open("spellbook.json", 'r') as spellbook:
        # Read the content of the file
        file_content = spellbook.read()
        if len(file_content) < 1:
            return "spellbook empty"
        else:
            return file_content