langs=[]
langs.append("python")

langs.append("perl")

print(langs)

langs.insert(0, "php")
langs.insert(2, "lua")
print(langs)

langs.extend(("javascript","actionscript"))
print(langs)

del langs[1]
print(langs)