import openpyxl
from pprint import pprint


if __name__ == '__main__':
    OLD_REPORT_FILENAME = 'AP_Location_23_07_2019.xlsx'
    NEW_REPORT_FILENATE = 'AP_Location_27_08_2019.xlsx'
    location = {} #Словарь с данными по локации из предыдущего отчета
    old_report = openpyxl.load_workbook(OLD_REPORT_FILENAME)
    rows = old_report.active.rows
    for row in rows:
        APMAC = row[0].value
        APLocation = row[-1].value
        location.update({APMAC:APLocation})
    old_report.close()
    new_report = openpyxl.Workbook()
    ws = new_report.active
    for APMAC,APLocation in location.items():
        ws.append([APMAC, APLocation])
    new_report.save(NEW_REPORT_FILENATE)
