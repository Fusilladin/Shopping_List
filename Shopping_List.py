# Create a new empty list named shopping_list
# Create a function named add_to_list
    # that declares a paramater named item
# Add the item to the list

shopping_list=[]
add_to_list.append=input("What do you want to add to the shopping list?  ")



def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
""")

show_help()
while True:
    new_item = input("> ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue

# Call add_to_list with new_item as an argument
