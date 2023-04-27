import datetime
import view 
import model

commands = ("Read file", "Save file", "Add", "Upd", "Del", "Read", "List", "Exit")

def run():
    model.getLastNoteId()
    cycle = True
    notes = dict()
    index = 0
    next = ""

    while(cycle):
        view.printCommands(commands)
        try:
            num = view.getNumCommand()  
        
            if not checkCommand(num):
                continue

            if (commands[num] == "Exit"):
                cycle = False

            elif (commands[num] == "Read file"):
                notes = readNotes(notes)
                view.printIfEmpty(notes)
                view.printIfNotEmpty(notes)

            elif (commands[num] == "Save file"):
                view.printIfEmpty(notes)
                saveNotes(notes) 
                model.saveLastNoteId()   

            elif (commands[num] == "Add"):
                index = model.getNewId()
                notes[index] = model.getNewNote()
                next = "title"

            elif (commands[num] == "Upd"):
                id = view.getNoteId()
                if not checkId(id, notes):
                    continue
                index = id
                next = "title"    

            elif (commands[num] == "Del"):
                id = view.getNoteId()
                if not checkId(id, notes):
                    continue
                del notes[id]

            elif (commands[num] == "List"):
                view.printIfEmpty(notes)
                view.printList(notes) 

            elif (commands[num] == "Read"):
                id = view.getNoteId()
                if not checkId(id, notes):
                    continue
                view.printMsgFull(id, notes[id]["date"], notes[id]["title"], notes[id]["msg"])

            if next == "title":
                msg = view.getTitle()
                if msg != "":
                    notes[index]["title"] = msg 
                notes[index]["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                next = "msg"    
                
            if next == "msg":
                msg = view.getMsg()
                if msg != "":
                    notes[index]["msg"] = msg
                notes[index]["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                next = ""

        except Exception as err:
            print(f"Ошибка: {err}, {type(err)}") 

def checkCommand(num):
    if num < 0 or num > len(commands):
        view.printCommandOutOfRange(num)
        return False
    return True

def checkId(num, notes):
    for i in notes:
        if i == num:
            return True
    view.printIdOutOfRange(num)
    return False

def readNotes(notes):
    new_pb = {}
    try:
        with open('Notes.txt', 'r', encoding='utf-8') as file:
            pb = file.readline()
            pb = file.readline()

            while pb:

                new_temp = {}

                temp = pb.replace('\n','').split(';')

                pb_key = int(temp[0])
                new_temp['date'] = temp[1]
                new_temp['title'] = temp[2]
                new_temp['msg'] = temp[3]
                new_pb[pb_key] = new_temp 

                pb = file.readline()
    except FileNotFoundError:
        pass
    
    for i in notes:
        new_pb[i] = notes[i]

    return new_pb

def saveNotes(notes):  
    if len(notes) == 0:
        return
    
    new_notes = readNotes(notes)

    with open('Notes.txt', 'w', encoding='utf-8') as file:
        file.writelines(f"id;date;title;msg\n")
        for i in new_notes:
            file.writelines(f"{i};{new_notes[i]['date']};{new_notes[i]['title']};{new_notes[i]['msg']}\n")
  