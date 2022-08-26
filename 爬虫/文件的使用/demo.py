new = []
f = open('data.txt', 'r')
contents = f.readlines()
for ele in contents:
    if ele[0]=='#':
        new.append(ele)
f.close()
print("\n".join(new))

new = []
f = open('data.txt', 'r')
contents = f.readlines()
for ele in contents:
    if ele.startswith('#') == False:
        new.append(ele)
f.close()
print("\n".join(new))

