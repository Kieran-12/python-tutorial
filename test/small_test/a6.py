txt = str(input())
characters_in_word = []


def show_letters(word):
    for character in word:
        if 65 <= ord(character) <= 90:
            ascii_value = ord(character)
            ascii_value += 32
            character = chr(ascii_value)
            characters_in_word.append(character)
        elif (
            91 <= ord(character) <= 96
            or 1 <= ord(character) <= 64
            or 123 <= ord(character) <= 127
        ):
            continue
        else:
            characters_in_word.append(character)


x = txt.split()
for i in x:
    show_letters(i)

print(characters_in_word)
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

for i in characters_in_word:
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
    if i == "a":
        a += 1
