class fio:
    def __init__(self, last_name = None, name = None):
        self.name = name
        self.last_name = last_name
    def print_fio(self):
        print(self)
    def __str__(self):
        return f"{self.last_name} {self.name}"


def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    surname = input('Введите Фамилию: ')
    name = input('Введите Имя: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f' ,{fio(surname, name)} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    book = data.split(',')
    data_to_find = input('Введите данные для поиска: ')
    contact_data = search(book, data_to_find)
    print(contact_data)
    return (contact_data)


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    # book = book.split('\n')
    contact_finded = list(filter(lambda contact: info in contact, book))
    if len(contact_finded) == 0:
        print(len(contact_finded))
        return 'Совпадений не найдено'

    elif len(contact_finded) == 1:
        return contact_finded
    else:
        print(contact_finded)
        info = input("Требуется уточнение данных, найдено несколько совпадений ")
        correction_contact = contact_finded
        return search(correction_contact,info)

def delete_data() -> None:
    """Удаляет контакт"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    contact_to_delete = find_data()
    book = list(filter(lambda contact: contact, data.split("\n")))
    if contact_to_delete:
        for x in contact_to_delete:
            book.remove(x)
    write_data(book)


def change_data() -> None:
    """Изменяет контакт"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    delete_data()
    add_data()

def write_data(data: list[str]) -> None:
    """" Записывает информацию в файл """
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write(str(data))
