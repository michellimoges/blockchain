names = ['bob','bobbybobn','popopo','titi','ggezboi420N']

for name in names: 
    if len(name) >= 5 and ("n" in name or "N" in name):
        print(name)
print('done')

iterator = 0

while len(names) >= 1:
    names.pop()
print(names)

