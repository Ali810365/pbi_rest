from library.groups import Groups

groups = Groups()
test = None

def pretty_print():
    for group in groups.get_groups(10, skip=1, filter="contains(name, 'Test')")['value']:
        print(group['name'])

#print(groups.get_groups(10, filter="contains(name,'Intune Compliance Data Warehouse App')"))
#print(groups.get_groups(10))
#print(groups.get_users(test))

#pretty_print()
