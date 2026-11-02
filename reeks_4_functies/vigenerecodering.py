def codeer(origineel, sleutelwoord):
    resultaat = ""
    for i in range(len(origineel)):
        c = origineel[i]
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            s = sleutelwoord[i % len(sleutelwoord)]
            getal = (ord(c) - 65 + ord(s) - 65) % 26
            resultaat += chr(getal + 65)
        else:
            resultaat += c
    return resultaat
    
print(codeer('NOBODY EXPECTS THE SPANISH INQUISITION!', 'CIRCUS'))
print(codeer('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR'))

def decodeer(code, sleutelwoord):
    resultaat = ""
    for i in range(len(code)):
        c = code[i]
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            s = sleutelwoord[i % len(sleutelwoord)]
            getal = ((ord(c) - 65) - (ord(s) - 65)) % 26
            resultaat += chr(getal + 65)
        else:
            resultaat += c
    return resultaat

print(decodeer('PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!', 'CIRCUS'))
print(decodeer('OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!', 'ARTHUR'))