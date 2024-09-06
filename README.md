#   Парсер для сайта СБИС
Предстравленный парсер получает на вход код HTML разметки сайта [saby.ru/](https://saby.ru/profile/$inn), где $inn номер ИНН контрагента. Затем собранные данные записываются в Excel файл. 

Проект написан на python 3.10.4.

## Запуск
1. Проект расположен на [github](https://github.com/Vova675/SABYParser).
2. Использовалось виртуальное окружение __venv__
   ```bash
   python -m venv venv
   ```
3. Зависимости расположены в файле __requirements.txt__
   ```bash
   pip install -r requirements.txt
   ```
4. Конфигурационные параметры расположены в файле __config.py__
   
## Библиотеки
1. beautifulsoup4 4.12.3
2. openpyxl 3.1.5
3. requests 2.32.3
4. regex 2024.7.24
   
## Классы
1. Файл __parser\parser.py__ содержит класс __ParserClass__, который используется для считывания данных из HTML разметки
2. Файл __excelmaker\excelmaker.py__ содержит класс __ExcelFileMakerClass__, который используется для создание __Excel__ файла

