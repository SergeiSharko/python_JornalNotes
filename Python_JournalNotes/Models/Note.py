from datetime import datetime
import Controller.counter as count

class Note:
    def __init__(self, noteId=str(count.counter()), noteTitle="Заголовок", noteBody="Описание заметки"):
        self.__noteId = noteId
        self.__noteTitle = noteTitle
        self.__noteBody = noteBody
        self.__createdDate = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def getNoteId(self):
        return self.__noteId

    def setNoteId(self):
        self.__noteId = str(count.counter())
    
    def getCreatedDate(self):
        return self.__createdDate
    
    def setCreatedDate(self):
        self.__createdDate = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def __str__(self):
        return f'ID: {self.__noteId} | createDate: {self.__createdDate} | titleNote: "{self.__noteTitle}" | bodyNote: "{self.__noteBody}"'
