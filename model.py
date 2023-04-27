import io


note_id_counter = 0

note = {"date": "", "title": "", "msg": ""}
# notes = dict()

def getNewNote():
    global note
    return note.copy()

def getNewId():
    global note_id_counter
    note_id_counter += 1
    return note_id_counter

def getLastNoteId():
    global note_id_counter
    try:
        with open('last_note_id.txt', 'r') as file:
            note_id_counter = int(file.read())
    except FileNotFoundError:
        pass
    except io.UnsupportedOperation:
        pass
    except ValueError:
        pass

def saveLastNoteId():
    global note_id_counter
    with open('last_note_id.txt', 'w') as file:
        file.write(str(note_id_counter))        