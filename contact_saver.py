print("---CONTACT SAVER---")
while True:
    print(''' 
1. SAVE CONTACT
2. RETRIEVE CONTACT
3. QUIT
          ''')
    option = input("Enter option (1-3): ").strip()
    if option == "1":
        name = input("Enter name: ").upper()
        number = input("Enter phone number: ")
        with open("contact_saver.txt", "a") as afile:
            afile.write(f"{name} - {number}\n")
            afile.close()
        print("Contact saved")
    elif option == "2":
        try:
            with open("contact_saver.txt", "r") as file:
                content = file.read()
                if content:
                    print("SAVED CONTENT\n")
                    print(content)
                else:
                    print("NO CONTACT FOUND")
        except:
            print("NO CONTACT SAVE YET, SAVE A CONTACT FIRST")
        finally:
            file.close()
    elif option == "3":
        print("Exiting...\n Exited")
        break
    else:
        print("invalid input")