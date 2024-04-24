import json
import Models.Note


def loadNotesFromFile(filepath):
    try:
        dictNotes = dict()
        with open(filepath, "r", encoding="utf-8") as file:
            notesFromFile = json.load(file)
            for noteId, noteData in notesFromFile.items():
                currNote = Models.Note.Note()
                currNote._Note__noteId = noteData["_Note__noteId"]
                currNote._Note__noteTitle = noteData["_Note__noteTitle"]
                currNote._Note__noteBody = noteData["_Note__noteBody"]
                currNote._Note__createdDate = noteData["_Note__createdDate"]
                dictNotes[noteId] = currNote
            print(f"Данные загружены из файла {filepath}")
    except Exception:
        print("Журнал заметок пуст!")
    finally:
        return dictNotes


def saveNoteToFile(filepath, dictNotes):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(dictNotes, file, default=lambda x: x.__dict__, indent=4, ensure_ascii=False)
        print(f"Изменения сохранены в файл {filepath}")
