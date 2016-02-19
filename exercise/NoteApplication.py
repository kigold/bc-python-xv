class NotesApplication(object):
	def __init__(self,author):
		self.notes = []
		self.author = author

	def create(self,note_content):
			self.notes.append(note_content)

	def list(self):
		
		for idx in range(1, len(self.notes)+1):
			print "Note ID: ",
			print idx,
			print self.notes[idx-1]
			print "By Author ", self.author
			print ""

	def get(self, note_id):
		return self.notes[note_id]

	def search(self,search_text):
		if search_text in self.note_content:
			print "Showingresultsforsearch ", search_text
			
			for idx in range(1, len(self.note)+1):
				print "Note ID: ",
				print idx,
				print self.notes[idx-1]
				print "By Author ", self.author
				print ""

	def delete(self,note_id):
		self.note_content.remove(self.note_content[note_id])

	def edit(self, note_id, new_contenet):
		self.note_content[note_id] = new_contenet

#Testing
notes = NotesApplication("kingsley")
test = ""
notes.create("Day one at Andela BC")
notes.create("Day two at Andela BC")
notes.create("Day three at Andela BC")
notes.create("Day four at Andela BC")
notes.create("Day five at Andela BC")

notes.list()
notes.get(1)


