import requests

# API Base URL
API_URL = requests.get("https://www.dnd5eapi.co/api/spells/")

# Dictionary to store spells
spellbook = {}

def search_spell(spell_name):
    """Search for a spell in the D&D API and return its details."""
    response = requests.get(API_URL + spell_name.lower().replace(" ", "-"))
    if response.status_code == 200:
        spell_data = response.json()
        return {
            "name": spell_data["name"],
            "level": spell_data["level"],
            "description": spell_data["desc"][0]  # First part of the description
        }
    else:
        print("Spell not found.")
        return None

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
add_spell_to_spellbook("fireball")
view_spellbook()
