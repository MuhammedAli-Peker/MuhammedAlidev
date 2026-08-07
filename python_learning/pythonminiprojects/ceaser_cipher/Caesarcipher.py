# str.maketrans("ab","ez") seçili harfleri harflerle değiştiri a=e, b=z
#translate() ile beraber çalışır
def caser_cipher(text,shift):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet=alphabet[shift:] + alphabet[:shift]