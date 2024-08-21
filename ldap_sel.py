import ldap
#import chardet
l = ldap.initialize('ldap://10.0.3.11')
#l.simple_bind_s()   хиз наіищо треба
basedn = "ou=Users,dc=eb,dc=co,dc=ua"
#basedn = "dc=eb,dc=co,dc=ua"
scope = ldap.SCOPE_ONELEVEL
scope = ldap.SCOPE_SUBTREE
filterexp = 'uid=bogach'
#filterexp = 'cn=dato'
#filterexp = 'ou=User'
#filterexp = 'uid=nezhyvetslh'
attrlist = ['gecos']
attrlist = ['objectClass']
attrlist = ['sambaAcctFlags', 'gecos','sambaHomePath','objectClass','displayName']
#attrlist = ['cn', 'uid', 'sambaAcctFlags', 'displayName']
#results = l.search_s(basedn, scope)
#results = l.search_s(basedn, scope, filterexp, attrlist)
#results = l.search_s(basedn, scope, filterexp)
results = l.search_s(basedn, scope, filterexp)
#results = l.search_s(basedn, scope)
for result in results:
#    print result[0].decode('utf-8'), result[1]['name'].decode('utf-8')
#    print(result[0].decode('utf-8'), result[1]['name'].decode('utf-8'))
#    print('rez0',result[0])
#    print('rez1',result[1])
#    print('rez1',result[1]['displayName'])
#    print('rez1_ss',result[1]['displayName'][0])
#    print('rez1_s',result[1]['displayName'])
    uname = result[1]['displayName'][0]
    islock = result[1]['sambaAcctFlags'][0]
    login =  result[1]['uid'][0]
    gecos = result[1]['gecos'][0]
    print(login.decode('utf-8'), uname.decode('utf-8'), gecos.decode('utf-8'), islock.decode('utf-8'))
#    print('rez1',result[1]['displayName'].decode('utf-8'))
#    print(result['displayName'][0]).decode('utf-8')
#    print('rez2',result[2])
#    print('CCC')
#print('AAA')
