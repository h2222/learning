# coding = utf-8
print("hello, word")



a =set(['1','2', '3', '4'])
b = set(['3', '4', '5'])

if a&b:
    print('good')
else:
    print('bad')

its = set(['aa', 'cc'])

identity_its = set(['aa', 'bb'])
dealml_its = set(['cc', 'dd'])
ask_its = set(['ee', 'ff'])
its_dict = {'identity_its':identity_its, 'dealml_its':dealml_its, 'ask_its':ask_its}


for intent in its_dict:
    if its & its_dict[intent]:
        print('good')
    else:
        print('bad')


d = {'identity|invalid':99.8, 'ask_know|yes':98.88}

dmax =  max(zip(d.items()))

print(dmax)



