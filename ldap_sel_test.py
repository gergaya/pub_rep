import ldap

def main():
    server = "ldap://10.0.3.11"
    who = ""
    cred = ""
    keyword = "ruan"

    try:
        l = ldap.initialize(server)
#        l = ldap.open(server)
        l.simple_bind_s(who, cred)
        print("Successfully bound to server.\n")
        print("Searching..\n")
        my_search(l, keyword)
    except ldap.LDAPError as error_message:
        print("Couldn't Connect. %s " % error_message)

def my_search(l, keyword):
    print("Call function")

#    except:
#        pass
#    except ldap.LDAPError as error_message:
#        print error_message

if __name__=='__main__':
    main()



#l = ldap.initialize('ldap://10.0.3.11')
#l.simple_bind_s()
#basedn = "ou=Users,dc=eb,dc=co,dc=ua"
#scope = ldap.SCOPE_ONELEVEL
#scope = ldap.SCOPE_SUBTREE
##filterexp = 'uid=dato'
#filterexp = 'uid=nezhyvetslh'
#attrlist = ['gecos']
#results = l.search_s(basedn, scope, filterexp, attrlist)
#for result in results:
##    print result[0].decode('utf-8'), result[1]['name'].decode('utf-8')
##    print(result[0].decode('utf-8'), result[1]['name'].decode('utf-8'))
#    print('rez0',result[0])
#    print('rez1',result[1])
#    print('CCC')
#print('AAA')
