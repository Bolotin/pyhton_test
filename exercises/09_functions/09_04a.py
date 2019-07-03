def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    return any(word in command for word in ignore)

def parse_config(file_name, ignore):
    result = {}
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip('\n')
            if not line or line.startswith('!') or ignore_command(line, ignore):
                continue
            elif not line.startswith(' '):
                first_layer_cmd = line
                result[first_layer_cmd] = []
            elif not line.startswith('  '):
                second_layer_cmd = line.strip()
                result[first_layer_cmd].append(second_layer_cmd)
            elif line.startswith('  '):
                third_layer_cmd = line.strip()
                if type(result[first_layer_cmd]) == list:
                    result[first_layer_cmd] = {key:[] for key in result[first_layer_cmd]}
                result[first_layer_cmd][second_layer_cmd].append(third_layer_cmd)
    return result

ignore = ['duplex', 'alias', 'Current configuration']
file_name = 'config_r1.txt'

for key,value in parse_config(file_name, ignore).items():
    print(key)
    print(value)
