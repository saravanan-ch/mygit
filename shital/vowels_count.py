count = 0
word = input("enter the word :")
for i in word:
 if i in "aeiouAEIOU":
        count += 1
print(count)