import Repository.WorkWithJsonFile as workWithFile
import Models.Note


class JournalNotes:
    def __init__(self, filepath="notes.json"):
        self.filepath = filepath
        self.dictNotes = workWithFile.loadNotesFromFile(filepath)

    def addNote(self):        
        print("Добавление новой заметки!")
        newTitle = input("Введите заголовок заметки -> ")
        newBody = input("Введите описание заметки -> ")
        note = Models.Note.Note(noteTitle=newTitle, noteBody=newBody)
        while note.getNoteId() in self.dictNotes.keys():
            note.setNoteId()
        self.dictNotes[note.getNoteId()] = note
        print("Заметка добавлена в журнал!")
        workWithFile.saveNoteToFile(self.filepath, self.dictNotes)

    def printIdNotes(self):
        print("В журнале есть заметки с ID -> | ", end="")
        for key in self.dictNotes.keys():
            print(key, end=" | ")

    def printNotes(self, txt):
        if txt == "all":
            if not self.dictNotes:
                print("Журнал заметок пуст!")
            else:
                print("Журнал заметок:")
                for key in self.dictNotes:
                    print(self.dictNotes[key])

        elif txt == "ID":
            self.printIdNotes()
            idKey = input("\nВведите ID заметки -> ")
            if idKey in self.dictNotes:
                print(self.dictNotes[idKey])
            else:
                print(f"В журнале нет заметки ID={idKey}")

        elif txt == "date":
            date = input("\nВведите дату в формате: dd.mm.yyyy -> ")
            flag = True
            for value in self.dictNotes.values():
                date_note = value.getCreatedDate()
                if date == date_note[:10]:
                    print(value)
                    flag = False
            if flag:
                print(f"Заметок с датой={date} нет в журнале!")        

    def deleteNotes(self):
        self.printIdNotes()
        idKey = input("\nВведите ID удаляемой заметки -> ")
        if idKey in self.dictNotes:
            del self.dictNotes[idKey]
            print(f"Заметка с ID={idKey} успешно удалена из журнала!")
            workWithFile.saveNoteToFile(self.filepath, self.dictNotes)            
        else:
            print(f"В журнале нет заметки с ID={idKey}")

    def changeNote(self):
        self.printIdNotes()
        idKey = input("\nВведите ID изменяемой заметки -> ")
        if idKey in self.dictNotes:
            self.dictNotes[idKey]._Note__noteTitle = input("Введите новый заголовок -> ")
            self.dictNotes[idKey]._Note__noteBody = input("Введите новое описание -> ")
            self.dictNotes[idKey].setCreatedDate()
            print(f"Заметка с ID={idKey} успешно изменена!")
            workWithFile.saveNoteToFile(self.filepath, self.dictNotes)
        else:
            print(f"В журнале нет заметки с ID={idKey}")
