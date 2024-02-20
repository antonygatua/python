astr = "Hello Antonny"
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

astr = '123'
try: 
    istr = int(astr)
except:
    istr = -1

print('Second', istr)

rswt = input('Enter Number: \n')
try:
    istr = int(rswt)
except:
    istr = -1

if istr > 0:
    print('Nice Work')
else:
    print('Not a number')

