files = ['1.txt', '2.txt', '3.txt']

def result_file(files_list, output_file):
    """
    Объединение предварительно отсортированных по количеству строк файлов в один с выводом служебной
    информации: название исходного файла и количество строк
    :param files_list: Список исходных файлов
    :param output_file: Итоговый файл
    :return: функция ничего не возвращает
    """
    files.sort(key=lambda file_path: sum(1 for _ in open(file_path, encoding='utf-8')))
    with open(output_file, 'w', encoding='UTF-8') as o:
        for file in files_list:
            with open(file, 'r', encoding='UTF-8') as i:
                num_lines = sum(1 for _ in i)
                o.write(f"{file}\n{num_lines}\n")

            with open(file, 'r', encoding='UTF-8') as f:
                o.write(f.read())
                o.write('\n')

result_file(files, '4.txt')