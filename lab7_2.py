'''
Вивести дані про працівників старших 30-ти років, які не мають вищої
освіти. Поля структури: Прізвище, Вік, Освіта, Посада.
Виконав студент 1 курсу групи КН 122А Опанасюк Б.М.
'''
while True:
    while True:
        try:
            worker_num = int(input('How many workers do you have?: '))
            break
        except ValueError:
            print('Enter correct value')
    worker_list = []
    worker_dict = {}
    count = 0
    for i in range(1, worker_num + 1):
        while True:
            try:
                surname = input('Enter worker`s surname: ')
                age = int(input(f'Enter {surname}`s age: '))
                position = input(f'Enter position of {surname}: ')
                education = int(input(f'{surname}`s education (high = 1, undergraduate = 2, secondary = 3): '))

                worker_dict['surname'] = surname
                worker_dict['age'] = age
                worker_dict['position'] = position
                worker_dict['education'] = education

                worker_list.append(worker_dict)
                worker_dict = {}

                break

            except ValueError or KeyError:
                print('Enter correct value')

    for e in range(len(worker_list)):
        em_age = worker_list[e].get('age')
        em_educ = worker_list[e].get('education')
        if em_age > 30 and em_educ == 1:
            print(worker_list[e])

    if input('Do you want to continue? Press Enter:') != '':
        break
