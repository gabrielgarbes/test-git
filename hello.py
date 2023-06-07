import sys

name = None
try:
    name = str(sys.argv[1])
except:
    name = ''

if name != '':
    print("Hello {}!".format(sys.argv[1]))
else:
    print('Hello')
