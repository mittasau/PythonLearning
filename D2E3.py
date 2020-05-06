def findCount(inputString):
  #words = inputString.split()
  lCharCount = 0
  uCharCount = 0
  digitCount = 0
  symbolCount = 0
  for char in inputString:
    if char.islower():
      lCharCount+=1
    elif char.isupper():
      uCharCount+=1  
    elif char.isnumeric():
      digitCount+=1
    else:
      symbolCount+=1
      
  print("lower case Chars = ", lCharCount, " upper case Chars = ", uCharCount, " Digits = ", digitCount, " Symbol = ", symbolCount)
      
inputString = "SAur@bh2020"
findCount(inputString)