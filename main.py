meme_dict = {

    "cringe":"Qualcosa di eccezionalmente strano o imbarazzante",

    "lol": "Una risposta comune a qualcosa di divertente",

    "stan": "Essere un grande fan di qualcuno o qualcosa, fino al punto di idolatrarlo.",

    "yeet": "Espressione utilizzata per indicare l'azione di lanciare qualcosa con forza, spesso seguita da un movimento brusco del braccio.",

    "fomo": "Paura di perdere qualcosa o di essere escluso da un evento o un'esperienza divertente.",

    "lit": "Qualcosa di eccitante o divertente, di solito associato a una festa o a un evento vivace.",

    "salty": "Essere arrabbiato o risentito per qualcosa di piccolo o insignificante.",

    "squad": "Un gruppo di amici stretti o persone con cui si ha un forte legame.",

}

 

for i in range(5):

    parola = input("Scrivi una parola che non capisci:").lower()

    if parola in meme_dict.keys():

        print(f"{parola.capitalize()}: {meme_dict[parola]}")

    else:

        print("Non esiste questa parola")
