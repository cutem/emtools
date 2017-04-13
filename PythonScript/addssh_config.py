#! /usr/local/bin/python
import sys
if len(sys.argv) == 1:
    print '%s alias host port user [IdentityFile]' %(sys.argv[0].split('/')[-1])
    exit()
elif len(sys.argv) == 5:
    alias = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    user = sys.argv[4]
    ident = "~/.ssh/id_rsa"
elif len(sys.argv) == 6:
    alias = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    user = sys.argv[4]
    ident = sys.argv[5]
else:
    exit()

content = \
"""Host %s
    Hostname %s
    port %d
    User %s
    IdentityFile %s

"""%(alias, host, port, user, ident)

f = open('/Users/eee/.ssh/config', 'a+')
f.write(content)
f.close()

