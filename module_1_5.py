immutable_var = 1, 2, 5, 'Dima'
print(immutable_var, ['Комментарий: кортедж в () неизменяемый'])
#immutable_var [0] = 200
#print(immutable_var)
mutable_list = [1, 2, 5, 'Dima']
print(mutable_list)
mutable_list[0] =  300
print(mutable_list)
mutable_list[-1] = 'Kolya'
print(mutable_list)