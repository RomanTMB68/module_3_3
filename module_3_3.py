def print_params(a=1, b='tyuuio', c=True):
    print(a,b,c)

print_params()
print_params(4)
print_params(0,'tg')
print_params(*"fgh")

def print_params_1(*tigr):
    print(tigr)

print_params_1(8,11,'ball',[2,4,7],True)

print_params(b = 25)
print_params(c = [1,2,3])

values_list=['q',6,True]
print_params(*values_list)
values_dict={"a":3,"b":'sdfr',"c":False}
print_params(**values_dict)

values_list_2=[67,'ututriyore']
print_params(*values_list_2, 42)

