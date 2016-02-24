class NotesApplication(object):
    ''' This NoteApplication class is used to build and instance of an
    element that emulates the functionality of a note pad .

    Attributes:

            author: this is used to define the authors name
            notes: this is a list where new notes are added
    '''

    def __init__(self,author = "Guest"):

    	''' Initialises the class with an authors name, if not provided, default is "Guest"
        and creats and empty list to save created notes

        args: authors 

        '''

        self.notes = []
        self.author = author
    def create(self,note_content=None):
    	''' Initialises the class with an authors name, if not provided, default is "Guest"
            and creats and empty list to save created notes
            
            args:  
                note_content: this is a string that is appended to the note list
            
        '''

        if note_content != None:
			self.notes.append(str(note_content))
			print "Note Successfully created"
        else:
			print "Please Enter the name of the note when creating"
			return "Please Enter the name of the note when creating"

    def list(self):
    	''' Outlines all the notes in the object, that is all the strings in 
    	the notes list
    	'''
		
        for idx in range(1, len(self.notes)+1):
			print "Note ID: ",
			print idx,
			print self.notes[idx-1]
			print "By Author ", self.author
			print ""

    def get(self, note_id = 0):
    	''' Obtains a particular note from the notes list by index

    	    args:
    	        note_id: this is an int value used to get a string from the list by index

    	    return:
    	        the string in the notes list by the index argumented to it
    	'''
        if note_id <= len(self.notes) and note_id > 0:
			print note_id, " Successfully Retreived "
			print "Note ID: " + str(note_id) + "\n" + str(self.notes[abs(note_id-1)]) + "\n\n" + "By Author " + str(self.author) 
			return self.notes[abs(note_id-1)]


    def search(self,search_text=None):
    	''' Searchs through the notes list for string (notes) that contains the search_text

    	 	args:
    	        search_text: the search parameter, the text to be searched for

    	    returns:
    	        a formated list of all the notes that meets the search criteria
    	'''
        if search_text != None:
            result= "Showing results for search " + "'" + str(search_text) +"'"
					
            for idx in range(1, len(self.notes)+1):
				if search_text.lower() in self.notes[idx-1].lower():
					result +=  "\nNote ID: " + str(idx) + "\n" + str(self.notes[idx-1]) + "\n\n" + "By Author " + str(self.author)
            print result
            return result
	

    def delete(self,note_id=None):
    	''' Deletes an item (note) in the notes list, using its index

    	    args:
    	        note_id: an int value to be used to remove a note from the notes list
    	'''
        if note_id != None and len(self.notes) >= note_id:
			self.notes.remove(self.notes[note_id-1])
			print note_id, "Successfully deleted"

    def edit(self, note_id, new_contenet):
    	''' Edits a note in the notes list identified by the argument "note_id" and 
    	appends the text got from the user in "new_content"

    	    args:
    	        note_id: an int value to be used to select a note from the notes list to be edited
    	'''
        self.notes[note_id-1] += " " +new_contenet
        print "Note Id:" , note_id, "Successfully edited and saved"










