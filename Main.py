import requests

# API Base URL
API_URL = requests.get("https://www.dnd5eapi.co/api/spells/")

# Dictionary to store spells
spellbook = {}

def search_spell(spell_name):
    fixedspell = spell_name.lower()
    fixedspell = fixedspell.replace("","-")
    #"""Search for a spell in the D&D API and return its details."""
    url = f"https://www.dnd5eapi.co/api/spells/{fixedspell}"
    response = requests.get(url)
    try:
        spell_data = response.json()
        mydict = {
            "name": spell_data["name"],
            "level": spell_data["level"],
            "description": spell_data["desc"][0]  # First part of the description
        }
        string1 = str(f"""{spell_data["name"]} {spell_data["level"]} {spell_data["desc"][0]}""")
        return string1
    except:
        return "Spell not found."

def add_spell_to_spellbook(spell_name):
    """Add a spell to the spellbook if found."""
    spell = search_spell(spell_name)
    if spell:
        spellbook[spell_name] = spell
        print(f"Added {spell_name} to your spellbook!")

def view_spellbook():
    """Display all stored spells."""
    if not spellbook:
        print("Your spellbook is empty.")
    else:
        for spell in spellbook.values():
            print(f"{spell['name']} (Level {spell['level']}): {spell['description']}")


# Example usage
