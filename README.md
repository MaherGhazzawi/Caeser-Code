Ich erkläre diese Code Schritt für Schritt : def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

Hier haben wir eine Funktion def encrypt_caesar ist unsere Funktion danach result ist leer um unsere worten dort zu schpeichern dann for char in text: hier jedes Char wird geprüft,
dann if char.isalpha() so eine Buchstabe.
hier unsere start = ord("A") if char.isupper() else ord("a") hier sagen wir dass start ist der Anfang von die List es gebint entweder von ord("A") oder ord("a") dann hier result += chr ist die char position. 
so ord(char) Zum Beispiel ord von("A") dann ist 65 so 65 - start(65) dann haben wir 0 + schift wenn der shift 1 ist dann das verschlüssele Wort ist B. diese % 26 bleibt in der Limit von der Alphabet 
so der User kann ein Schift von 5000 entschieden egal wie groß ist den schift bleibt im Alapbet. 
so die Rechnung ist 65 - 65 + 1 = 1 % 26 = 1 A + 1 mal vorne = B 
def decrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result
    hier das System ist gleich aber gegenteil - den shift und genau gleiche Rechnung 
    answer = ""
while answer != "break":
    answer = input("Willst du einen Text verschlüsseln oder entschlüsseln? (oder 'break' zum Beenden): ").lower()
    if answer == "verschlüsseln":
        text = input("Schreib den Text hier, er wird verschlüsselt: ")
        shift = int(input("Gib die Verschiebung (Shift) ein: "))
        encrypted = encrypt_caesar(text, shift)
        print("Verschlüsselter Text:", encrypted)
    elif answer == "entschlüsseln":
        text = input("Schreib den Text hier, er wird entschlüsselt: ")
        shift = int(input("Gib die Verschiebung (Shift) ein: "))
        decrypted = decrypt_caesar(text, shift)
        print("Entschlüsselter Text:", decrypted)
    elif answer == "break":
        print("Tschüss! Viel Spaß!")
    else:
        print("Ungültige Eingabe. Bitte gib 'verschlüsseln' oder 'entschlüsseln' ein.")
        Hier die Logik ist sehr einfach while answer ist nicht gleich break bleibt dann entschieden verschlüsseln oder entschlüsseln?
