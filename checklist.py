# -*- coding: utf-8 -*-

checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    print(checklist[index])


def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    item = "√ " + str(checklist[index])
    update(index, item)

def mark_incomplete(index):
    item = str((checklist[index])[2:])
    update(index, item)

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    if function_code == "C":
        input_item = user_input("Add to List: ")
        create(input_item)
        print("Added " + str(input_item) + " to the list")

    elif function_code == "R":
        item_index = int(user_input("Index to Read: "))
        if item_index > len(checklist) - 1:
            print("Invalid index")
        else:
            read(item_index)

    elif function_code == "U":
        item_index = int(user_input("Index to Update: "))
        if item_index > len(checklist) - 1:
            print("Invalid index")
        else:
            item = user_input("Update " + checklist[item_index] + " to: ")
            update(item_index, item)

    elif function_code == "P":
        list_all_items()

    elif function_code == "D":
        item_index = int(user_input("Index to Mark Completed: "))
        if item_index > len(checklist) - 1:
            print("Invalid index")
        else:
            item = checklist[item_index]
            mark_completed(item_index)
            print("Marked " + item + " as completed")


    elif function_code == "I":
        item_index = int(user_input("Index to Mark Incomplete: "))
        if item_index > len(checklist) - 1:
            print("Invalid index")
        else:
            mark_incomplete(item_index)
            print(checklist[item_index])

    elif function_code == "Q":
        return False

    else:
        print("Unknown Option")

    return True

def clearScreen():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

running = True
clearScreen()

while running:
    selection = user_input(
        "Press C to add to list, R to read from list, U to update an item, D to mark item as done, I to mark item as incomplete, and P to display list: ").upper()
    running = select(selection)

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))
    list_all_items()

    select("C")
    list_all_items()
    select("R")
    list_all_items()

# test()
