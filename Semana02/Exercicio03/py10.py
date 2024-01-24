weight = float(input('Weight: '))
unit = input('(K)g or (L)bs: ').lower()

if unit == 'k':
    print('Weight in Lbs: ', weight*2.204)
elif unit == 'l':
    print('Weight in Kg: ', weight/2.204)
else:
    print('Unknown unit.')