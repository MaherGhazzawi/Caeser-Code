def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result

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

   

   
   








