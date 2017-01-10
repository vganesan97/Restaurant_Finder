dll=raw_input('Enter e for dollar conversion or d for euro conversion: ')
if dll=='d':
    dr=raw_input('Enter an amount: ')
    dl=float(dr)
    eu=dl*0.88
    y=float("{0:.2f}".format(eu))
    print 'Your amount is equivalent to {0} euros'.format(eu)
elif dll=='e':
    de=raw_input('Enter an amount: ')
    ds=float(de)
    d=ds/0.88
    r=float("{0:.2f}".format(d))
    print 'Your amount is equivalent to {0} dollars'.format(r)
