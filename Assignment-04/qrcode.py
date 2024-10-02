import qrcode

name = input("Enter your name: ")
phone = input("Enter your phone number: ")

img = qrcode.make(name + " | " + phone)
img.save("some_file.png")