emails = {
    "Joan": "joan@example.com",
    "Maria": "maria@example.com", 
    "Pere": "pere@example.com",
    "Anna": "anna@example.com",
    "Carles": "carles@example.com",
    "Laura": "laura@example.com",
    "Marc": "marc@example.com",
    "Sofia": "sofia@example.com",
    "David": "david@example.com",
    "Elena": "elena@example.com"
}

def getmail(nom):
    nom = nom.capitalize()

    if nom in emails:
        return emails[nom]
    else:
       return ""
