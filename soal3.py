buah_buahan = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
a = []

for i in buah_buahan:
    if len(i) >= 5:
        a.append(i)

a.sort()

print(a)