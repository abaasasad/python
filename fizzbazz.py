for fizzbuzz in range(18):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("buzzfizz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
	
word = input()
 
sameWord = ""
for i in word:
    sameWord = i + sameWord
 
if (word == sameWord):
    print("Yes")
else:
    print("No")
