import UI.UserConsoleMenu as ui
import Controller.JournalNotes as jN
import Controller.counter as count

def start():
    journalNotes = jN.JournalNotes()
    while True:
        ui.userConsoleMenu()
        userInput = input("Введите пункт меню -> ")
        if userInput == '1':
            journalNotes.printNotes("all")
        elif userInput == '2':
            journalNotes.printNotes("ID")
        elif userInput == '3':
            journalNotes.printNotes("date")
        elif userInput == '4':
            journalNotes.addNote()
        elif userInput == '5':
            journalNotes.changeNote()
        elif userInput == '6':            
            journalNotes.deleteNotes()
            count.resetCounter()            
        else:
            print("Программа Журнал заметок завершена")
            break
