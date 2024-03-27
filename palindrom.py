def palindrom(text):
  length = len(text)
  for i in range(0, length // 2):
      if (text[i] != text[length - i - 1]):
        return False
      return True
  
wyraz1 = "potop"
wyraz2 = "kajak"
Wyraz3 = "łódź"
wyraz4 = "klawiatura"

print(palindrom(wyraz1))
print(palindrom(wyraz2))
print(palindrom(Wyraz3))
print(palindrom(wyraz4))