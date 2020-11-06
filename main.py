# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""Проект «Справочник» 

Свойства: 
имя, фамилия, телефон, город, e-mail 
Методы: 

создание справочника 

запись (с проверкой на валидность, с проверкой на дубли); 

изменение; 

поиск (e-mail - уникальная запись) 

удаление """
class Note:
    name = ''
    surname = ''
    phone = ''
    email = ''

    def __init__(self, surname, *args):
        self.surname = surname
        return self

    def __hash__(self):
        return hash(self.email)


class Helper:
    name = "Helper"
    notes = {}

    def __init__(self):
        return self

    def add(self, note):
        if note.name[0].isUpper() and note.surname[0].isUpper() and '@' in note.email and type(note.phone) is str:
            if not (note.__hash__() in self.notes.keys()):
                self.notes.append(note.__hash__(), note)
                return True
        return None

    def change(self, note, change):
        if self.notes.__contains__(note.__hash__):
            self.notes[note.__hash__] = note
        return self.notes[note.__hash__]
    
    def search(self, email):
        if self.notes.__contains__(hash(email)):
            return self.notes[hash(email)]