def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    return any(word in command for word in ignore)

def parse_config(file_name,ignore):
    result = {}
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip('\n')
            if line.startswith('!') or ignore_command(line,ignore) or not line:
                continue
            elif not line.startswith(' '):
                first_layer_command = line
                result[first_layer_command] = []
            else:
                result[first_layer_command].append(line.strip())
    return result

ignore = ['duplex', 'alias', 'Current configuration']
file_name = 'config_sw1.txt'

for key,value in parse_config(file_name, ignore).items():
    print(key)
    print(value)
