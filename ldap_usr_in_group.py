import ldap

l = ldap.initialize('ldap://10.0.3.11')
basedn = "ou=Groups,dc=eb,dc=co,dc=ua"
scope = ldap.SCOPE_ONELEVEL
filterexp = 'cn=ma*'        # фільтруємо по групі
attrlist = ['cn', 'gidNumber', 'memberUid', 'objectClass']
results = l.search_s(basedn, scope, filterexp, attrlist)

for result in results:
    gid = result[1].get('cn')
    users = result[1].get('memberUid')

    print('group -', gid[0].decode('utf-8'))
    print('users:')
    for i in range(len(users)):
        print(' ', users[i].decode('utf-8'))

