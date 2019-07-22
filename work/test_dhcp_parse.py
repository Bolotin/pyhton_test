import openpyxl
from pprint import pprint
from datetime import datetime

def get_ap_location(filename):
    result = {}
    """Expect old report .xlsx file"""
    wb = openpyxl.load_workbook(filename)
    rows = wb.active.rows
    next(rows)
    for row in rows:
        values = [cell.value for cell in row]
        result[values[0]] = values[-1]
    return result


if __name__ == '__main__':
    parsed_data = ['./tmp/CWC001_19_07_2019.csv', './tmp/CWC003_19_07_2019.csv', 'HWC001_19_07_2019.csv']
    OLD_DATA_FILENAME = 'AP_Location_19_07_2019.xlsx' #Задаем файл со старыми данными, откуда берём физические адреса
    ap_location_data = get_ap_location(OLD_DATA_FILENAME) #Получаем словарь с данными по локациям точек
    #Теперь собираем данные со всех распарсенных файлов вместе и добавляем к ним данные по локации из старых файлов
    result_filename = 'AP_DATA_{}.csv'.format(datetime.today().strftime('%d_%m_%Y'))
    print('Start collect information in resul file {}'.format(result_filename))
    pprint(get_ap_location(OLD_DATA_FILENAME))
    """
    with open(result_filename,'w') as result_file:
        result_writer = csv.writer(result_file)
        result_writer.writerow(['AP_MAC','AP_NAME','AP_ADDRESS','AP_LOCATION'])
        for parsed_filename in parsed_data:
            with open(parsed_filename) as parsed_file:
                reader = csv.reader(parsed_file)
                for row in reader:
                    AP_MAC, AP_NAME, AP_ADDRESS = row
                    AP_LOCATION = ap_location_data.get(AP_MAC, 'Неизвестен')
                    result_writer.writerow([AP_MAC,AP_NAME,AP_ADDRESS,AP_LOCATION])"""
