def palindrom(text):
    text = text.lower()
    length = len(text)
    for i in range(length // 2):
        if text[i] != text[length - i - 1]:
            return False
    return True
  
  
wyraz1 = "Kajak"
wyraz2 = "wędka"
Wyraz3 = "adwokatka"
wyraz4 = "słoń"

print(palindrom(wyraz1))
print(palindrom(wyraz2))
print(palindrom(Wyraz3))
print(palindrom(wyraz4))
