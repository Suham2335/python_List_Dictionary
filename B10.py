contacts = {
    "Ram": "9841000000",
    "Sita": "9851000000",
    "Hari": "9861000000"
}

while True:

    print("===== Contact Book =====")
    print()
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")
    print()

    n = int(input("Enter an option: "))

    print()

    if n == 1:
        name = input("Enter a name: ").capitalize()
        if name in contacts:
            print("Contact already exists.")
        else:
            num = input("Enter a number: ")
            if num.isdigit() and len(num) == 10:
                contacts[name] = num
                print("Contact added.")
            else:
                print("Invalid phone number.")

    elif n == 2:
        con = input("Enter contact name: ").capitalize()

        if con in contacts:
            print(f"Contact found: {contacts[con]}")
        else:
            print("No contact found")

    elif n == 3:
        t = input("Enter name of contact you want to update: ").capitalize()

        if t in contacts:
            ask = input("Type 'a' to update name and 'b' to update number: ").lower()

            if ask == 'a':
                namu = input("Enter new name: ").capitalize()
                contacts[namu] = contacts.pop(t)
                print("Contact updated")

            elif ask == 'b':
                nambo = input("Enter new number: ")
                if nambo.isdigit() and len(nambo) == 10:
                    contacts[t] = nambo
                    print("Contact updated")
                else:
                    print("Invalid phone number.")

            else:
                print("Invalid option.")

        else:
            print("No contact found.")

    elif n == 4:
        z = input("Enter name of contact: ").capitalize()

        if z in contacts:
            contacts.pop(z)
            print("Contact deleted.")
        else:
            print("No contact found.")

    elif n == 5:
      for name in sorted(contacts):
        print(f"{name}: {contacts[name]}")

    elif n == 6:
        print("Goodbye!")
        break

    else:
        print("Please enter a valid option.")