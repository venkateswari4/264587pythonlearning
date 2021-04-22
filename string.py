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

appendMiddle("Ault", "Kelly")
def mix_string(s1, s2):
    first_char = s1[:1] + s2[:1]
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    res = first_char + middle_char + last_char
    print("Mix String is ", res)

s1 = "Ameri"
s2 = "Japan"
mix_string(s1, s2)

