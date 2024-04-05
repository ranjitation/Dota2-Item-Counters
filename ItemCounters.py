import json
import tkinter as tk
from tkinter import Listbox

path = "C:/Users/Ranjith/Documents/pyprojects/DotaItemGenerator/"

# Read the hero names and items from the JSON file
with open(path + 'itemcounters.json', 'r') as json_file:
    data = json.load(json_file)
    heroes_data = data['itemcounters']
    hero_items_dict = {hero['hero_name']: (hero.get("item_list", [])) for hero in heroes_data}
    all_items = set(item for items in hero_items_dict.values() for item in items)

def update_items_list(event):
    selected_heroes = [hero_listbox.get(idx) for idx in hero_listbox.curselection()]
    selected_items = set()
    for hero in selected_heroes:
        selected_items.update(hero_items_dict.get(hero, set()))
    selected_items = sorted(selected_items)  # Sort the selected items alphabetically
    # Clear the current items in the item listbox
    item_listbox.delete(0, tk.END)
    # Insert the sorted items for the selected heroes
    for item in selected_items:
        item_listbox.insert(tk.END, item)

# Create a GUI window
root = tk.Tk()
root.title("Hero and Item Selection")

# Set the size of the window
window_width = 800
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Create a listbox to display the sorted hero names
hero_listbox = Listbox(root, selectmode=tk.MULTIPLE)
for name in sorted(hero_items_dict.keys()):
    hero_listbox.insert(tk.END, name)
hero_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
hero_listbox.bind("<<ListboxSelect>>", update_items_list)

# Create a listbox to display the unique items
item_listbox = Listbox(root)
for item in all_items:
    item_listbox.insert(tk.END, item)
item_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


# Run the GUI
root.mainloop()