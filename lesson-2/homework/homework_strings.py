# Q1
name=input("Name: ")
year = int(input("Birthyear: "))
print(f"{name}, you are {2025-year} years old")

# Q2
txt = 'LMaasleitbtui'
car1 = txt[::2]
car2 = txt[1::2]
print(f"Car 1: {car1}, Car 2: {car2}")

# Q3
s = input("String: ")
print(len(s))
s.upper()
s.lower()

# Q4
string = input("String: ")
if(string==string[::-1]):
    print("yes")
else:
    print("no")

# Q5
x=input("String: ")
x=x.lower()
c=x.count('a')+x.count('e')+x.count('i')+x.count('o')+x.count('u')
print(f"{c} vowels and {len(x)-c} consonants")

# Q6
a=input("String 1: ")
b=input("String 2: ")
if(a in b):
    print("string 2 contains string 1")
elif(b in a):
    print("string 1 contains string 2")
else:
    print("no")

# Q7
sen = input("Input sentence: ")
rep = input("Replace: ")
wit = input("With: ")
sen=sen.replace(rep,wit)
print(sen)

# Q8
st = input("String: ")
print(f"first character: {st[0]}, last character: {st[-1]}")

# Q9
string1 = input("String: ")
print(string1[::-1])

# Q10
sentence = input("Sentence: ")
sentence=sentence.strip()
lst=sentence.split()
print(len(lst))

# Q11
digits = ['0','1','2','3','4','5','6','7','8','9']
str2 = input("String: ")
for digit in digits:
    if(digit in str2):
        print("yes")
        break
else:
    print("no")

# Q12
word1 = input("word: ")
word2 = input("word: ")
word3 = input("word: ")
separate = input("Separator: ")
words = [word1,word2,word3]
new_string = separate.join(words)
print(new_string)

# Q13
str3 = input("String: ")
str3.strip()
for ch in str3:
    if(ch==' '):
        str3.replace(ch,'')

# Q14
s1 = input("String 1: ")
s2 = input("String 2: ")
if(s1==s2):
    print("yes")
else:
    print("no")

# Q15
sent = input("Sentence: ")
sent.strip()
l = sent.split()
new_word = ""
for word in l:
    new_word+=word[0]
print(new_word)

# Q16
str4 = input("String: ")
char = input("character: ")
for ch in str4:
    if(ch==char):
        str4.replace(ch,'')

# Q17
str5 = input("String: ")
vowels = ['a','o','u','e','i']
for ch in str5:
    if(ch in vowels):
        str5.replace(ch, '*')

# Q18
str6 = input("String: ")
start = input("Starts with: ")
end = input("Ends with: ")
lst6 = str6.split()
if(start==lst6[0] and end==lst6[-1]):
    print("yes")
