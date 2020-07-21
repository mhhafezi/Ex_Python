print('Difference Between discard & remove methods: \n ')

my_set={12,34,56,78,90}
print('DISCARD::\nOriginal my set:' ,my_set)
print('\nDiscarding element=12 from my set',my_set.discard(12))
print('\nUpdated my set: ', my_set)


my_set={12,34,56,78,90}
print('\nREMOVE::\nOriginal my set:' ,my_set)
print('\nRemoving element=12 from my set',my_set.remove(12))
print('\nUpdated my set: ', my_set)
print('\nThey work the same when the element is in the set.')

print('Difference::')

my_set={12,34,56,78,90}
print('\nOriginal my set:' ,my_set)
print('\nDiscarding element=100 from my set',my_set.discard(100))
print('Nothing happens when discard can not find the element.')
print('\nRemoving element=100 from my set')
print(my_set.remove(100))
