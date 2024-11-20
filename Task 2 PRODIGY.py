while True:
    print("=== Caesar Cipher Program ===")
    choice=input("choose an option: (E)ncrypt or (D)ecrypt: ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' to Encrypt or 'D' to Decrypt.")
        continue
    message=(input("Enter your message: "))
    shift=int(input("Enter the shift value: "))
    result=""
    for char in message:
        if char.isalpha():
            base=65 if char.isupper() else 97
        if choice=='D':
            result+=chr((ord(char)- base - shift )% 26 + base)
        elif choice=='E':
            result+=chr((ord(char)- base + shift )% 26 +base)
    else:
        result+=char
    print("Processed Message: ", result)
    x=input("Do you need any services(y/n): ")

    if x=="y":
        print("Restarting...")
    else:
        print("Thank you for using the Caesar Cipher Program. Goodbye!")
        break

        
