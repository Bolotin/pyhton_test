from re import search

def return_match(filename, regex):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            data = search(regex, line)
            if data:
                result.append(data.group())
    return result

if __name__ == '__main__':
    filename = 'sh_ip_int_br.txt'
    regex = '(\d{1,3}\.){3}\d{1,3}'
    print(return_match(filename, regex))
