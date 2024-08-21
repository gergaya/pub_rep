import ldap

l = ldap.initialize('ldap://10.0.3.11')
l.search_s('ou=Users,dc=eb,dc=co,dc=ua',ldap.SCOPE_SUBTREE,'(cn=fred*)',['cn','mail'])[('cn=Fred Feuerstein,ou=Testing,dc=stroeder,dc=de', {'cn': ['Fred Feuerstein']})]
r = l.search_s('ou=Testing,dc=stroeder,dc=de',ldap.SCOPE_SUBTREE,'(objectClass=*)',['cn','mail'])
for dn,entry in r:
	print('Processing',repr(dn))
	handle_ldap_entry(entry)


#l = ldap.initialize('ldap://10.0.3.11')
#l.simple_bind_s()
#basedn = "ou=Users,dc=eb,dc=co,dc=ua"
