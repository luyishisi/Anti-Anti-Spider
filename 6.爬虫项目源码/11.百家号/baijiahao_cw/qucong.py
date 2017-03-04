lll = set()
with open('appid.txt','r') as idfile:
    for appid in idfile.readlines():
        lll.add(appid)
idfile.close()
print(len(lll))
with open('sortid.txt','w') as idfile:
    for appid in lll:
        idfile.write(appid)
        idfile.write('\n')
idfile.close()