'''
Дана послідовність а, що складається з символів s1, s2, .... Відомо, що символ s1
відмінний від знаку оклику і що серед s2, s3, ... є хоча б один знак оклику. Припустимо
s1, ..., sn – символи даної послідовності, що передують першому знаку оклику (n
заздалегідь не відомо). Визначити кількість пробілів серед послідовності s1, ..., sn.
Виконав студент 1 курсу групи КН 122А Опанасюк Б.М.
'''
flag1, flag2 = False, False
while True:
    try:
        str = input('Enter some literals: ')
    except ValueError:
        print('Enter correct data type!')

    if str[0] != '!':
        flag1 = True

        if '!' in str:
            flag2 = True
        else:
            print('There must be at least one "!"')
    else:
        print('There is must not be "!" on 1st position')
    if flag1 and flag2:
        break

new_str = str[str.find("!") + 1:]
print(f'New string is {new_str}')

print(f'Spaces in the new string: {new_str.count(" ")}')
