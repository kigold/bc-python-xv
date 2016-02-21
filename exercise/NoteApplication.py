class NotesApplication(object):
	def __init__(self,author = "Guest"):
		self.notes = []
		self.author = author

	def create(self,note_content=None):
		if note_content != None:
			self.notes.append(str(note_content))
		else:
			print "Please Enter the name of the note when creating"
			return "Please Enter the name of the note when creating"

	def list(self):
		
		for idx in range(1, len(self.notes)+1):
			print "Note ID: ",
			print idx,
			print self.notes[idx-1]
			print "By Author ", self.author
			print ""

	def get(self, note_id = 0):
		if note_id and len(self.notes) >= note_id and note_id >= 0:
			return self.notes[abs(note_id-1)]

	def search(self,search_text=None):
		if search_text != None:
			result= "Showing results for search " + "'" + str(search_text) +"'"

					
			for idx in range(1, len(self.notes)+1):
				if search_text.lower() in self.notes[idx-1].lower():
					result +=  "\nNote ID: " + str(idx) + "\n" + str(self.notes[idx-1]) + "\n\n" + "By Author " + str(self.author)
			return result

	def delete(self,note_id=None):
		if note_id != None and len(self.notes) >= note_id:
			self.notes.remove(self.notes[note_id-1])

	def edit(self, note_id, new_contenet):
		self.notes[note_id-1] += " " +new_contenet

#Testing
'''notes = NotesApplication("kingsley")
test = ""


#notes.list()
print notes.get(3)
notes.search("khvk")
#notes.delete(5)

notes.edit(5, "Andela Day 5, Was a great day, Hectic, But we are Greatful to God")

notes.list()

notes = NotesApplication()
notes.create("Day one at Andela BC")
notes.create("Day two at Andela BC")
notes.create("Day three at Andela BC")
notes.create("Day four at Andela BC")
notes.create("Day five at Andela BC")

print len(notes.notes)

notes.search("four")

notes.edit(3,"was also fun")
notes.list()
'''





