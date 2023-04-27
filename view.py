def printCommands(commands):
    index = 0
    str = ""
    for cmd in commands:
        str = str + (f"{index}- {cmd}; ")
        index = index + 1
    print(f"<<< Список команд: {str} >>>")

def printList(notes):
    if len(notes) != 0:
        print("Список заметок: ")
    for i in notes:
        printMsg(i, notes[i]["date"], notes[i]["title"]) 

def printIfEmpty(notes):
    if len(notes) == 0:
        print("Список сообщений пустой")

def printIfNotEmpty(notes):
    if len(notes) != 0:
        print(f"Список содержит {len(notes)} сообщений")        

def printCommandOutOfRange(num):
    print(f"Номер комманды не поддерживается: {num}")

def printIdOutOfRange(num):
    print(f"Идентификатор заметки не найден: {num}")   

def printMsg(id, date, title):
    print(f"идентификатор: {id}; дата: {date}; заголовок: {title}") 

def printMsgFull(id, date, title, msg):
    print(f"идентификатор: {id}; дата: {date}; заголовок: {title}")         
    print(f"сообщение заметки: {msg}") 

def getMsg():
  return input('Введите сообщение заметки: ')

def getTitle():
  return input('Введите заголовок заметки: ')


def getNumCommand():
  return int(input('Введите номер команды: '))    

def getNoteId():
    return int(input("Введите идентификатор заметки: "))