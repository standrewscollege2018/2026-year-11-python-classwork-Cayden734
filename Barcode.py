length = 13 
barcode = (input("Enter a Barcode"))
if any(char.isalpha() for char in barcode):
    print("incorrect")
else:
    if len(barcode) == length:
        print(str(barcode)[:2], "Country Code")
        print(str(barcode)[2:7], "Manufacturer's Code")
        print(str(barcode)[7:12], "Product Code")
        print(str(barcode)[12:13], "Cheack Digit")
    else: 
        print("Incorrect Barcode")
        quit()





