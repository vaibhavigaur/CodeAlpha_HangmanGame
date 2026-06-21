print("Email Extractor (without regex)\n")

file_name = input("Enter file name: ")

try:
    f = open(file_name, "r")
    data = f.read()
    f.close()
except:
    print("File not found!")
    exit()

words = data.split()

emails = []

for word in words:
    if "@" in word and "." in word:
        emails.append(word)

if len(emails) == 0:
    print("No emails found.")
else:
    print("\nEmails found:\n")
    
    for e in emails:
        print(e)

    out = open("emails.txt", "w")

    for e in emails:
        out.write(e + "\n")

    out.close()

    print("\nSaved in emails.txt")