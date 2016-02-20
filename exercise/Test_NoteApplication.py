import unittest
from NoteApplication import NotesApplication
class NoteApplicationTestSuit(unittest.TestCase):
	def test_note_instance(self):
		notes = NotesApplication("kingsLey")
		self.assertIsInstance(notes,NotesApplication,msg="The object must be that of NoteApplication")

	def test_obj_type(self):
		notes = NotesApplication("kingsley")
		self.assertTrue(type(notes) is NotesApplication, msg="The object should be a NotesApplication")

	def test_default_author(self):
		notes = NotesApplication()
		self.assertEqual(notes.author, "Guest", msg="deault name is not set")

	def test_empty_create(self):
		notes = NotesApplication()
		self.assertEqual(notes.create(), "Please Enter the name of the note when creating", msg="create parameter not initialised")

	def test_empty_list(self):
		notes = NotesApplication()
		self.assertEqual(notes.list(), None, msg="List not empty")



if __name__ =="__main__":
	unittest.main()