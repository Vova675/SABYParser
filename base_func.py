import regex as re

def fix_person_data(str, Dict_Row_Data):
    """
    Функция для форматирования персональных данных
    """
    if re.findall(r'\w*@\w*.\w*', str):
        Dict_Row_Data["e-mail"] = str
    elif re.findall(r'\+7 \(\d{3,5}\) \d{1,3}-\d{2}-\d{2}', str):
        Dict_Row_Data["number"] = str
    elif re.findall(r'\w*\.(com|ru)*', str):
        Dict_Row_Data["web"] = str

def fix_job_title(str, Dict_Row_Data):
    """
    Функция для форматирования должности
    """
    Dict_Row_Data["job_title"] = re.sub(r' c \d{2}\.\d{2}\.\d{2}$', "", str)