import sys 
import emails

if len(sys.argv) > 1:
    nom = sys.argv[1]
else:
    nom = input("Nom: ")

mail = emails.getmail(nom)

if nom in emails:
    print(emails[nom])
else:
    print("No trobat")