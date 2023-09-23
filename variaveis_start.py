f = 0
print(f)

f = "abc"
print(f)

print("isto é uma string " + str(123))

def AlgumaFuncao():
    global f
    f = "def"
    print(f)

AlgumaFuncao()
print(f)

