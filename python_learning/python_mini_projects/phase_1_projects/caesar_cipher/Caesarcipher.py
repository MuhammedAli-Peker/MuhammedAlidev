# str.maketrans("ab","ez") seçili harfleri harflerle değiştiri a=e, b=z
#translate() ile beraber çalışır

#Freedcodecamp Caesar cipher mini project

def caser_cipher(text,shift,encrypt=True):
    if not isinstance(shift,int):
        return "Shifth must be a integer"
    if shift<0 or shift>25:
        return "Shift must be greater than 0 and less than 25"
    
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alphabet_up=alphabet.upper()
    
    if not encrypt:
        shift=-shift
    
    shifted_alphabet=alphabet[shift:] + alphabet[:shift]
    shifted_alphabet_up=shifted_alphabet.upper()
    translation_table=str.maketrans(
            alphabet + alphabet_up,                      
            shifted_alphabet + shifted_alphabet_up                    
                                    )
    
    encrypted_text = text.translate(translation_table)
    return encrypted_text
    
    
def encrypt(text,shift):
    return caser_cipher(text,shift)
def decrypt(text,shift):
    return caser_cipher(text,shift,False)
encryped_text=encrypt("freecodecamp",3)
decrypted_text=decrypt("iuhhfrghfdps",3)
print(encryped_text)
print(decrypted_text)