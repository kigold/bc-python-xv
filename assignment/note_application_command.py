from NoteApplication import NotesApplication
print "~~~~~~~~~~~~~~~NoteApplication Command Interface~~~~~~~~~~~~~~~~~~~~~~"
print  "~~~~~~~~~~~~~~Enter 'Exit' at any time to quit~~~~~~~~~~~~~~~~~~~~~~~"
prompt = ""
author = raw_input("Enter your name")
note = NotesApplication("author")
while prompt != "quit":	
	#prompt = raw_input("Enter the content of your note")
	#note.create(prompt)
	prompt = raw_input("type\n * 'Quit' to quit\n * 'Create' to create new note\n * 'List' to list all your notes\n *'Get' to get a saved note based on its id\n * 'Search' to look for notes with contain your specified search strind \n* 'Edit' to edit and change an already saved note\n * 'Delete' to delete and note")
	print "WTF"
	if prompt.lower() == "create":
		prompt = raw_input("Enter the note you want to create")
		note.create(prompt)
	elif prompt.lower() =="list":
		note.list()
	elif prompt.lower() =="get":
		note.list()
		prompt = raw_input("Enter the ID of the note you want to get for")
		note.get(int(prompt))
	elif prompt.lower() =="search":
		prompt = raw_input("Type in the text you are looking for")
		note.search(prompt)
	elif prompt.lower() == "edit":
		note.list()
		id = raw_input("enter the 'ID' of the note you want to edit")
		prompt = raw_input("enter text here")
		note.edit(id,prompt)
	elif prompt.lower() =='delete':
		note.list()
		prompt = raw_input("Enter the 'ID' of the note you want to delete")
		note.delete(id)
	else:
		continue
