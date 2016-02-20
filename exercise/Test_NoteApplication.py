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

	def test_empty_get(self):
		notes = NotesApplication()
		self.assertEqual(notes.get(), None, msg="List not empty")

	def test_get_negative_index(self):
		notes = NotesApplication()
		self.assertEqual(notes.get(-4), None, msg="Supposed to be out of range or negative")

	def test_get_negative_index1(self):
		notes = NotesApplication()
		self.assertEqual(notes.get(-1004), None, msg="Supposed to be out of range or negative")

	def test_get_negative_index2(self):
		notes = NotesApplication()
		self.assertEqual(notes.get(-100400000000), None, msg="Supposed to be out of range or negative")

	def test_alpha(self):
		notes = NotesApplication()
		self.assertEqual(notes.get('sd'), None, msg="Supposed to be out of alphabee")

	def test_get_boolean_as_index(self):
		notes = NotesApplication()
		self.assertEqual(notes.get(True), None, msg="List not empty")

	def test_search_empty_field(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		self.assertEqual(notes.search(), None, msg="Supposed to be an empty return")

	def test_search(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		self.assertEqual(notes.search("two"), 'Day two at Andela BC', msg="")

	def test_search1(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		self.assertEqual(notes.search("one"), None, msg="")

	def test_search_capitalsed_text(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		self.assertEqual(notes.search("TWO"), None, msg="Supposed to be return same result for 'two'")

	def test_search_missed_case(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		self.assertEqual(notes.search("tWo"), None, msg="Supposed to be return same result for 'two'")

	def test_delete_empty_argument(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		self.assertEqual(notes.delete("tWo"), None, msg="Supposed to be return same result for 'two'")







if __name__ =="__main__":
	unittest.main()