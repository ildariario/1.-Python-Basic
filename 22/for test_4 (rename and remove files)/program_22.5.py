import os

# Получение абсолютного пути по которому находится этот (запущенный, текущий) скрипт
abs_path_script = os.path.abspath(__file__)
# Получение пути к каталогу в котором лежит этот скрипт
cur_working_dir = os.path.dirname(abs_path_script)
# Изменение текущего рабочего каталога (каким бы он не был) на каталог в котором лежит этот скрипт
os.chdir(cur_working_dir)
'''# или
cur_dir, file_name = os.path.split(abs_file_path)
print(cur_dir, ' + ', file_name)
par_dir, file_name = os.path.split(cur_dir)
print(par_dir)
'''
print(f'Текеущая рабочая директория:\n\t{cur_working_dir}\n')

rm_part_list = ['[SW.BAND] ', '[SW.BAND]']
rm_file_list = ['For example_1.txt', 'For example_2.txt', 'For example_3.txt']
rename_count_dir = 0    # Кол-во переименованных папок
rename_count_file = 0   # Кол-во переименованных файлов
remove_count_file = 0   # Кол-во удаленных файлов
fail_count_rename = 0   # Кол-во неудачных попуток переименования файлов

for i_elem in os.listdir():
    # print(i_elem)
    if os.path.isdir(i_elem):   # Если элемент каталога (т.е. папки) является каталогом
        print(f'Папка: «{i_elem}»')
        for i_rm in rm_part_list:
            if i_rm in i_elem:
                new_name = i_elem.replace(i_rm, '')  # replace - заменить
                os.rename(i_elem, new_name)
                rename_count_dir += 1
                print('\t- переименована.')
                break
        else:
            print('\t- не нуждается в переименовании.')
    elif os.path.isfile(i_elem):   # Если элемент каталога (т.е. папки) является файлом
        print(f'Файл: «{i_elem}»')
        # print('Расширение:', os.path.splitext(i_elem)[1])
        if i_elem in rm_file_list:
            os.remove(i_elem)
            remove_count_file += 1
            print('\t- удалён.')
        elif os.path.splitext(i_elem)[1] == '.url':
            if os.path.splitext(i_elem)[0] in rm_file_list:
                os.remove(i_elem)
                remove_count_file += 1
                print('\t- удалён.')
        else:
            for i_rm in rm_part_list:
                if i_rm in i_elem:
                    new_name = i_elem.replace(i_rm, '')  # replace - заменить (строковый метод)
                    if os.path.exists(new_name):
                        print('\t- не удалось переименовть, т.к. файл с таким именем уже есть в папке.')
                        fail_count_rename += 1
                        break
                    else:
                        os.rename(i_elem, new_name)
                        rename_count_file += 1
                        print('\t- переименован.')
                        break
            else:
                print(f'\t- не нуждается в переименовании.')

print('\n', '*'*70, sep='')
print(f'*\tВсего переименовано папок: {rename_count_dir}')
print(f'*\tВсего переименовано файлов: {rename_count_file}')
print(f'*\tВсего удаленных файлов: {remove_count_file}')
print(f'*\tКоличество неудачных попыток переименования файлов: {fail_count_rename}')
print('*'*70)
delay = input('\nНажмите любую кнопку для завершения...')
