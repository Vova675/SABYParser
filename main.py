from config import input_file_name
from parser.parser import ParserClass
from excelmaker.excelmaker import ExcelFileMakerClass
from adsender.adsender import LetterAbsenderClass

def start_parsing(table_data):
    """
    Функция для запуска парсера.
    Принемает на вход список и заполняет для дальнейшего использования
    """
    input_file = open(input_file_name, "r")

    for elem in input_file:
        parser = ParserClass(elem)
        parser.parse_data()
        table_data.append(parser.get_row_data())

    input_file.close()
    print("parsing: finish")

def create_excel_file(table_data):
    """
    Функция для записи данных в excel файл.
    Принимает на вход список данных для записи в excel файл
    """
    excel_maker = ExcelFileMakerClass()
    excel_maker.create_file(table_data)
    print("create_excel_file: finish")

def send_letter():
    """
    Функция для отправки письма на почту
    """
    adsender = LetterAbsenderClass()
    adsender.send_letter()
    print("send_letter: finish")

if __name__ == '__main__':
    table_data = []
    start_parsing(table_data)
    create_excel_file(table_data)
    send_letter()

    