import ldap

def main():
    server = "ldap://10.0.3.11"
    who = ""
    cred = ""
    keyword = "ruan"

    try:
        l = ldap.initialize(server)        
#        l = ldap.open(server)
        l.simple_bind_s(who, cred)  # connect 2 server
        print("Successfully bound to server.\n")
        print("Searching..\n")
        my_search(l, keyword)
    except ldap.LDAPError as error_message:
        print("Couldn't Connect. %s " % error_message)

def my_search(l, keyword):
    base = ""
    base = "ou=Users,dc=eb,dc=co,dc=ua"
    scope = ldap.SCOPE_SUBTREE
    filter = "cn" + "*" + keyword + "*"
    filter = 'uid=dato'
    retrive_attributes = None

    count = 0
    result_set = []
    timeout = 0

    try:
        result_id = l.search(base, scope, filter, retrive_attributes)
        while 1:
            result_type, result_data = l.result(result_id, timeout)
            if (result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)

        if len(result_set) == 0:
            print("No Results.")
            return
        for i in range(len(result_set)):
            for entry in result_set[i]:
                try:
                    name = entry[1]['cn'][0]
                    email = entry[1]['mail'][0]
                    phone = entry[1]['telephonenumber'][0]
                    desc = entry[1]['description'][0]
                    count = count + 1
                    print("%d,\nName: %s\nDescription: %snE-mail: %s\nPhone: %s\n" %(count, name, desc, email, phone))

                except:
                    pass
    except ldap.LDAPError as error_message:
        print("Search error %s" % error_message)

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
