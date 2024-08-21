import ldap

l = ldap.initialize('ldap://10.0.3.11')
basedn = "ou=Groups,dc=eb,dc=co,dc=ua"
#scope = ldap.SCOPE_ONELEVEL
scope = ldap.SCOPE_SUBTREE
filterexp = 'cn=ana*'        # Фильтруем выбррку по логину
#attrlist = ['uid','sambaAcctFlags', 'gecos','sambaHomePath','objectClass','displayName']
#results = l.search_s(basedn, scope, filterexp, attrlist)
attrlist = ['cn', 'gidNumber', 'memberUid', 'objectClass']
results = l.search_s(basedn, scope, filterexp, attrlist)

for result in results:
    print('rez0',result[0])
    print('rez1',result[1])

    gid = result[1].get('cn')
    users = result[1].get('memberUid')

#    login =  result[1].get('uid', 'No uid')
#    if 'displayName' in result[1]:
#        uname = result[1]['displayName'][0].decode('utf-8')
#    else:
#        uname = 'Нема ПІБ'
#    if 'sambaAcctFlags' in result[1]:
#        islock = result[1]['sambaAcctFlags'][0].decode('utf-8')
#    else:
#        islock = 'No sambaAcctFlags'
#    if 'gecos' in result[1]:
#        gecos = result[1]['gecos'][0].decode('utf-8')
#    else:
#        gecos = 'No gecos'
#    if 'sambaHomePath' in result[1]:
#        sambahomepath = result[1]['sambaHomePath'][0].decode('utf-8')
#    else:
#        sambahomepath = 'No sambaHomePath'

    print(gid[0])
    print(users[1])
#    print(login[0].decode('utf-8'), uname, gecos, islock, sambahomepath)
#    print(login[0].decode('utf-8')+'|'+uname+'|'+gecos+'|'+islock+'|'+sambahomepath)
#    if sambahomepath.find('\\SALO') == 1 and islock[1] == 'U':
#        print(login[0].decode('utf-8') + '@industrialbank.ua',uname)
    

