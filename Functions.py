import requests
import json
# API Base URL
API_URL = requests.get("https://www.dnd5eapi.co/api/spells/")

# Dictionary to store spells
spellbook = open("spellbook.txt", "a")
spellbook.close()

def list_spells():
    url = f"https://www.dnd5eapi.co/api/spells"
    response = requests.get(url)
    spell_data = response.json()
    print(type(spell_data))
    count = 0
    mylist = []
    try:
        for i in spell_data["results"]:
            count = count + 1
            mylist.append(spell_data["results"][count]["name"])
    except:
        pass
    #mylist = mylist.replace(",","\n")
    print(len(mylist))
    print(mylist[1])
    return mylist
    #print(spell_data)

def search_spell(spell_name):
    fixedspell = str(spell_name.lower())
    fixspell = fixedspell.replace(" ","-")
    #"""Search for a spell in the D&D API and return its details."""
    url = f"https://www.dnd5eapi.co/api/spells/{fixspell}"
    try:
        response = requests.get(url)
    
        spell_data = response.json()
        string1 = str(f"""{spell_data["name"]} {spell_data["level"]}\n {spell_data["desc"]}""")
        return string1
    except:
        return "Spell not found"
    #return "Spell not found."

def add_spell_to_spellbook(spell_name):
    """Add a spell to the spellbook if found."""
    fixedspell = str(spell_name.lower())
    fixspell = fixedspell.replace(" ","-")
    url = f"https://www.dnd5eapi.co/api/spells/{fixspell}"
    response = requests.get(url)
    spell_data = response.json()
    spell = spell_name
    lvl = str(spell_data["level"])
    x = str(spell + " Level: " + lvl)
    y = json.dumps(x)
    y = f"{y} \n"
    if spell:
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
            return str(file_content)
        


# Example usage