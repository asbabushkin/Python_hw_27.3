# Задание 3
# Создать программу для работы с объектами класса в соответствии с вариантом.  Использовать класс string стандартной библиотеки С++.
# Реализовать:
# конструктор ;
# перегрузить оператор присваивания;
# перегрузить операции отношений (<, >, !=, ==);/

import datetime


class Document:
    def __init__(self, type, number, dateIssue, orgIssue):
        self.type = type
        self.number = number
        self.dateIssue = dateIssue
        self.orgIssue = orgIssue

    def show(self):
        print(self.type, self.number, self.dateIssue, self.orgIssue)

    # перегрузка оператора присваивания
    def assign(self, other):
        if self.type == other.type:
            self.number = other.number
            self.dateIssue = other.dateIssue
            self.orgIssue = other.orgIssue
        else:
            print('Присваивание не применимо для документов разных типов')

    # оператор '<'. Понимаем как меньший = более старый документ. Даты вводим аккуратно в формате дд/мм/гггг
    def __lt__(self, other):
        if datetime.datetime.strptime(self.dateIssue, '%d/%m/%Y') < datetime.datetime.strptime(other.dateIssue,
                                                                                               '%d/%m/%Y'):
            return True
        else:
            return False

    # оператор '>'. Понимаем как больший = более новый документ. Даты вводим аккуратно в формате дд/мм/гггг
    def __gt__(self, other):
        if datetime.datetime.strptime(self.dateIssue, '%d/%m/%Y') > datetime.datetime.strptime(other.dateIssue,
                                                                                               '%d/%m/%Y'):
            return True
        else:
            return False

    # перегрузка оператора ==
    def __eq__(self, other):
        if self.type == other.type and self.number == other.number and self.dateIssue == other.dateIssue and self.orgIssue == other.orgIssue:
            return True
        else:
            return False

    # перегрузка оператора !=
    def __ne__(self, other):
        if self.type != other.type or self.number != other.number or self.dateIssue != other.dateIssue or self.orgIssue != other.orgIssue:
            return True
        else:
            return False


doc1 = Document('паспорт', '7505 123456', '01/01/2005', 'УВД Калининского района г. Челябинска')
doc2 = Document('паспорт', '7510 987654', '01/01/2010',
                'ОУФМС России по Челябинской области в Калининском районе г. Челябинска')
doc3 = Document('водительское удостоверение', '74AB 112233', '31/12/2015', 'ГИБДД')
doc4 = Document('свидетельство о рождении', 'AB 123456', '20/12/1999',
                'Отдел ЗАГС администрации Советского района г. Челябинска')
doc5 = Document('свидетельство о рождении', 'AB 987654', '10/02/1986',
                'Отдел ЗАГС администраии Центрального района г. Челябинска')
# присваивание
print('Проверяем присваивание:')
print('Документ 1:')
doc1.show()
print('Документ 2:')
doc2.show()
print('Производим присваивание документ1 = документ2: ')
doc1.assign(doc2)
print('Теперь документ 1 равен: ')
doc1.show()
print()

# Перегрузка оператора <:
print('Первый документ:')
doc2.show()
print('Второй документ:')
doc3.show()
if doc2.__lt__(doc3):
    print('Перегрузка оператора <: Первый документ < второго (выдан ранее)')
else:
    print('Перегрузка оператора < :Первый документ не меньше второго (выдан позже или в этот же день')
print()

# Перегрузка оператора >:
print('Первый документ:')
doc4.show()
print('Второй документ: ')
doc5.show()
if doc4.__gt__(doc5):
    print('Перегрузка оператора >: Первый документ > второго (выдан позднее)')
else:
    print('Перегрузка оператора >: Первый документ не больше второго (выдан ранее или в этот же день)')
print()

# Перегрузка оператора ==:
print('Первый документ: ')
doc1.show()
print('Второй документ: ')
doc2.show()
if doc1.__eq__(doc2):
    print('Перегрузка оператора "==": Документы идентичны')
else:
    print('Перегрузка оператора "==": Документы не идентичны')
print()

# Перегрузка оператора !=:
print('Первый документ: ')
doc3.show()
print('Второй документ: ')
doc5.show()
if doc3.__ne__(doc5):
    print('Перегрузка оператора "!=": Документы не идентичны')
else:
    print('Перегрузка оператора "!=": Документы идентичны')
