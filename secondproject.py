Word = input().replace(""," ").split()
minimum = len(Word)
ind = 0
while ind < len(Word)-1:
    count = 0
    let = Word[ind]
    if Word[ind + 1] == let:
         Letter,minimum = let,0 
         break
    Word[ind] = ' '
    if let in Word: 
        count = Word.index(let) - ind - 1
        minimum = min(count,minimum)
    if count == minimum: Letter = let
    # print(count,minimum)
    ind += 1
print(Letter,minimum) if minimum < len(Word) else print("No Repititive Letter in String")