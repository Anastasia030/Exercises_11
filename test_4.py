from task_4 import Group

group_1 = Group('22704.1')
group_1.write('22704.1.txt')

for group in Group.data_groups:
    print(group)
