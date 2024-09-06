from config import input_file_name
from parser.parser import ParserClass
from excelmaker.excelmaker import ExcelFileMakerClass

def start_parsing(table_data):
    input_file = open(input_file_name, "r")

    for elem in input_file:
        parser = ParserClass(elem)
        parser.parse_data()
        table_data.append(parser.get_row_data())

    input_file.close()
    print("end parsing")

def create_excel_file(table_data):
    excel_maker = ExcelFileMakerClass()
    excel_maker.create_file(table_data)
    print("end create_excel_file")

if __name__ == '__main__':
    table_data = []
    start_parsing(table_data)
    create_excel_file(table_data)

    