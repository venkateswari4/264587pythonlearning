def getMiddleThreeChars(sampleStr):
    middleIndex = int(len(sampleStr) / 2)
    print("Original String is", sampleStr)
    middleThree = sampleStr[middleIndex - 1:middleIndex + 2]
    print("Middle three chars ", middleThree)


getMiddleThreeChars("JhonDipPeta")
getMiddleThreeChars("Jasonay")

def appendMiddle(s1, s2):
  middleIndex = int(len(s1) /2)
  print("Original Strings are", s1, s2)
  middleThree = s1[:middleIndex:]+ s2 +s1[middleIndex:]
  print("After appending new string in middle", middleThree)

appendMiddle("Aut", "Kelly")
def mix_string(s1, s2):
    first_char = s1[:1] + s2[:1]
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    res = first_char + middle_char + last_char
    print("Mix String is ", res)

s1 = "Ameri"
s2 = "Japan"
mix_string(s1, s2)

def findDigitsCharsSymbols(inputString):
  charCount = 0
  digitCount = 0
  symbolCount = 0
  for char in inputString:
      if char.islower() or char.isupper():
          charCount += 1
      elif char.isnumeric():
          digitCount += 1
      else:
          symbolCount += 1
  print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)
inputString = "P@#yn26at^&i5v"
print("total counts of chars, digits,and symbols \n")
findDigitsCharsSymbols(inputString)

def mixString(s1, s2):
  s2 = s2[::-1]
  lengthS1 = len(s1)
  lengthS2 = len(s2)
  length  = lengthS1 if lengthS1 > lengthS2 else lengthS2
  resultString=""
  for i in range(length):
      if (i < lengthS1):
          resultString = resultString + s1[i]
      if (i < lengthS2):
          resultString = resultString + s2[i]
  print(resultString)
s1 = "Abc"
s2 = "Xyz"
mixString(s1, s2)