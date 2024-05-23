import random

#WORD LIST
translations = {
    
    #INSERISCI QUI LE PAROLE CON LA RELATIVA TRADUZIONE, il formato e': "parolaItaliana": "parolainglese",

    #ESEMPIO:
    # "bevanda in bottiglia": "bottled drink",
    # "delfino": "dolphin",

}
print("Per uscire dal programma digita: esci")
corrette=0
sbagliate=0
def check_translation():
    global corrette
    global sbagliate
    while True:
        italian_word = random.choice(list(translations.keys()))
        print(f"\nTraduci la seguente parola: {italian_word}")
        
        user_translation = input("Inserisci la traduzione (o scrivi 'esci' per uscire): ").strip().lower()
        
        if user_translation == 'esci':  # Controlla se l'utente vuole uscire
            print(f"Hai fornito {corrette} risposte corrette e {sbagliate} risposte sbagliate.") # Stampa il punteggio finale
            input("Premere un tasto per uscire...")
            break # Esce dal loop
        
        if user_translation == translations[italian_word].lower():
            print("Corretto")
            corrette=corrette+1
        else:
            print(f"La traduzione corretta era: {translations[italian_word]}")
            sbagliate=sbagliate+1

#chiamata della funzione
check_translation()