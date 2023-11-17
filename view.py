import os
import json
from copy import deepcopy as dcp
from testdb.const import *

dirname = os.path.dirname(os.path.abspath(os.path.expanduser(__file__)))

data = json.loads(open(os.path.join(dirname, 'testdb/uuid_all.json'), 'rb').read())

f = open('index.log', 'wb')

for i in data:
    a = dcp(data[i])
    if a[TYPE] == ARTWORK:
        src = a[ALIAS][0]
        if src not in ['某科学的超电磁炮', '魔法禁书目录']:
            continue
        for j in a[LINK]:
            for k in a[LINK][j]:
                dst = data[k][ALIAS][0]
                node = {'source': src, 'target': dst, 'type': "resolved", 'rela': "角色"}
                node = str(node)
                node = node.replace("'type'", 'type').replace("'source'", 'source').replace("'target'", 'target')
                node += ',\n'
                # print(node+',')
                f.write(node.encode('utf8'))
