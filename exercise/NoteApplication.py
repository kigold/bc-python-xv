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
		return self.notes[note_id-1]

	def search(self,search_text):
		print "Showing results for search ", "'",search_text,"'"
			
		for idx in range(1, len(self.notes)+1):
			if search_text in self.notes[idx-1]:
				print "Note ID: ",
				print idx,
				print self.notes[idx-1]
				print "By Author ", self.author
				print ""
		
	def delete(self,note_id):
		self.notes.remove(self.notes[note_id-1])

	def edit(self, note_id, new_contenet):
		self.notes[note_id-1] = new_contenet

#Testing
'''notes = NotesApplication("kingsley")
test = ""
notes.create("Day one at Andela BC")
notes.create("Day two at Andela BC")
notes.create("Day three at Andela BC")
notes.create("Day four at Andela BC")
notes.create("Day five at Andela BC")

#notes.list()
print notes.get(3)
notes.search("khvk")
#notes.delete(5)

notes.edit(5, "Andela Day 5, Was a great day, Hectic, But we are Greatful to God")

notes.list()
'''

