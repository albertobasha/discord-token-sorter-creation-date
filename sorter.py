import base64;  from datetime import datetime

tokensSorted = []
for x in open("tokens.txt", 'r').readlines():
    email, password, token = x.split(':')
    if token[0:3] == "MTA": token = f"{token.split('.')[0]}=={token.split('.')[1]}{token.split('.')[2]}"
    IDDecoded = base64.b64decode(token.split('.')[0]).decode('utf-8')
    createdAt = round(((int(IDDecoded) >> 22) + 1420070400000)/1000)
    tokensSorted.append([f'{email}:{password}:{token}', createdAt])

import os
if not os.path.isdir("results"): os.mkdir("results")
results = sorted(tokensSorted, key = lambda d: d[1])
[open(f'results/{(datetime.fromtimestamp(x[1])).strftime("%d.%m.%Y")}.txt', 'a').write(x[0]) for x in results]
