import requests
import pbd

# API Base URL
API_URL = requests.get("https://www.dnd5eapi.co/api/spells/")

# Dictionary to store spells
spellbook = open("spellbook.txt", "w")
spellbook.close()

def list_spells(sort_type):
    url = f"https://www.dnd5eapi.co/api/spells"
    response = requests.get(url)
    spell_data = response.json()
    spell_data = spell_data.sort(sort_type)
    print(spell_data)

def search_spell(spell_name):
    fixedspell = str(spell_name.lower())
    fixspell = fixedspell.replace(" ","-")
    #"""Search for a spell in the D&D API and return its details."""
    url = f"https://www.dnd5eapi.co/api/spells/{fixspell}"
    response = requests.get(url)
    
    spell_data = response.json()
    mydict = {
            "name": spell_data["name"],
            "level": spell_data["level"],
            "description": spell_data["desc"][0]  # First part of the description
        }
    string1 = str(f"""{spell_data["name"]} {spell_data["level"]}\n {spell_data["desc"]}""")
    return string1
    #return "Spell not found."

def add_spell_to_spellbook(spell_name):
    """Add a spell to the spellbook if found."""
    url = f"https://www.dnd5eapi.co/api/spells/{spell_name}"
    response = requests.get(url)
    spell_data = response.json()
    spell = spell_name
    lvl = str(spell_data["level"])
    if spell:
        spellbook = open("spellbook.txt", "a")
        spellbook.write(spell_data["name"] + " Level: " + lvl +'\n')
        spellbook.close()
        print(f"Added {spell_name} to your spellbook!")


def view_spellbook():
    """Display all stored spells."""
    spellbook = open("spellbook.txt","r")
    num1 = sum(1 for _ in spellbook)
    spellbook.close
    if num1 < 1:
        return("Your spellbook is empty.")
    else:
        spellbook = open("spellbook.txt","r")
        return(spellbook.read())


# Example usage
list_spells()