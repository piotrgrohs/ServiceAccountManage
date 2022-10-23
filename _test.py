from classes.serviceAccount import list_of_serviceAccount


list = list_of_serviceAccount()
# list.save()
print('----- in file -----')
list.load()
list.show()
print(list.free_id('project1'))
list.add('app1', 'project1', 'test')

print('----- add -----')
list.show()
list.save()

# print('----- delete -----')
# list.delete(1, 'project2')
# list.delete(2, 'project2')
# list.show()
# list.save()
