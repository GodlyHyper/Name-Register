textfile = open("Names.txt", "w")

a = input("[+] What's your name: ")

print("Hello,",a)

textfile.write('Registered Name: ' + a)
textfile.close()