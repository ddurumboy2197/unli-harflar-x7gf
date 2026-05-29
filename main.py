def matn_tanlash(matn):
    return ''.join([harf for harf in matn if harf.isalpha() and harf.lower() not in 'aeiou'])

matn = input("Matn kiriting: ")
print(matn_tanlash(matn))
