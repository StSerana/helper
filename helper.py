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
    def __init__(self, name):
        super(Helper, self).__init__()
        self.name = name

    def __str__(self):
        return self.name

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