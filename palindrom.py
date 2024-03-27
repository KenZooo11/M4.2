def palindrom(text):
  text = text.lower()
  length = len(text)
  for i in range(0, length // 2):
      if (text[i] != text[length - i - 1]):
        return False
  return True
  
  
wyraz1 = "słoń"
wyraz2 = "Kajak"
Wyraz3 = "adwokatka"
wyraz4 = "klawiatura"

print(palindrom(wyraz1))
print(palindrom(wyraz2))
print(palindrom(Wyraz3))
print(palindrom(wyraz4))
