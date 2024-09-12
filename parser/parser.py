from bs4 import BeautifulSoup
import requests
from config import url
from base_func import fix_person_data, fix_job_title

class ParserClass:

    def __init__(self, inn):
        """
        Инициализатор\n
        Использует url из файла config.py для подключения к сайту
        """
        self.__url = url
        self.__dict_row_data = {}
        self.__page = requests.get(self.__url + inn)
        if self.__page.status_code != 200:
            print('Error')
        self.__soup = BeautifulSoup(self.__page.text, "html.parser")

    def parse_data(self):
        """
        Метод для парсинга всех данных
        """
        self.__get_INNKPP()
        self.__get_persone_data()
        self.__get_chief_data()
        self.__get_job_title_data()
        

    def __get_INNKPP(self):
        """
        Метод для получения ИНН и КПП со страницы
        """
        INNKPP_list = [elem.string for elem in self.__soup.find_all("div", class_ = "ws-flex-grow-0 contractor-Dialog_INNKPP-pointer")]
        self.__dict_row_data["inn"] = INNKPP_list[0]
        self.__dict_row_data["kpp"] = INNKPP_list[1]

    def __get_persone_data(self):
        """
        Метод для получения персональных данных со страницы
        """
        person_data_list = [elem.string for elem in self.__soup.find_all("div", class_ = "ws-ellipsis contractorCard-ContactItem__text")]
        for elem in person_data_list:
            fix_person_data(elem, self.__dict_row_data)

    def __get_chief_data(self):
        """
        Метод для получения ФИО руководителя со страницы
        """
        chief_data_list = [elem.string for elem in self.__soup.find_all("div", class_ = "contractorCard-Chief__fullName ws-ellipsis")]
        if len(chief_data_list) != 0:
            self.__dict_row_data["name"] = chief_data_list[0]
        else:
            self.__dict_row_data["name"] = "null"

    def __get_job_title_data(self):
        """
        Метод для получения должности руководителя со страницы
        """
        job_title_data_list = [elem.string for elem in self.__soup.find_all("div", class_ = "ws-ellipsis ws-flex-grow-0")]
        if len(job_title_data_list) != 0:
            fix_job_title(job_title_data_list[0], self.__dict_row_data)
        else:
            self.__dict_row_data["job_title"] = "null"

    def get_row_data(self):
        return self.__dict_row_data

    def set_row_data(self, row_data):
        self.__dict_row_data = row_data