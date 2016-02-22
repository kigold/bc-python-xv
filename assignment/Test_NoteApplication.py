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

	def test_define_author(self):
		notes = NotesApplication("kingsley")
		self.assertEqual(notes.author, "kingsley")

	def test_author_as_number(self):
		notes = NotesApplication(23)
		self.assertEqual(notes.author, 23, msg="deault name is not set")	

	def test_empty_create(self):
		notes = NotesApplication()
		self.assertEqual(notes.create(), "Please Enter the name of the note when creating", msg="create parameter not initialised")

	def test_create_number_as_arg(self):
		notes = NotesApplication()
		self.assertEqual(notes.create(23), None, msg="create not successful")

	def test_create_number_as_arg(self):
		notes = NotesApplication("kigold")
		notes.create("this is y am Hot")
		self.assertEqual(len(notes.notes),1)

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
		self.assertEqual(notes.search("two"), "Showing results for search 'two'\nNote ID: 2\nDay two at Andela BC\n\nBy Author Guest", msg="")

	def test_search1(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		self.assertEqual(notes.search("one"), "Showing results for search 'one'\nNote ID: 1\nDay one at Andela BC\n\nBy Author Guest", msg="")

	def test_search_capitalised1(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		self.assertEqual(notes.search("ONE"), "Showing results for search 'ONE'\nNote ID: 1\nDay one at Andela BC\n\nBy Author Guest", msg="")

	def test_search_capitalsed_text(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		self.assertEqual(notes.search("TWO"), "Showing results for search 'TWO'\nNote ID: 2\nDay two at Andela BC\n\nBy Author Guest", msg="Supposed to be return same result for 'two'")

	def test_search_mixed_case(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		self.assertEqual(notes.search("tWo"), "Showing results for search 'tWo'\nNote ID: 2\nDay two at Andela BC\n\nBy Author Guest", msg="Supposed to be return same result for 'two'")

	def test_delete_empty_argument(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		notes.delete()
		self.assertListEqual(notes.notes,["Day one at Andela BC","Day two at Andela BC"], msg="List supposed to be unchange since delet didnt affect anything")

	def test_delete(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		notes.delete(1)
		self.assertNotEqual(len(notes.notes),2, msg="List should not be the same length since delete was successful")

	def test_delete_all(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		notes.delete(1)
		notes.delete(1)
		self.assertEqual(len(notes.notes),0, msg="List should not be the same length since delete was successful")

	def test_delete_empty_list(self):
		notes = NotesApplication()
		notes.delete(1)
		notes.delete(1)
		self.assertEqual(len(notes.notes),0, msg="List should not be the same length since delete was successful")

	def test_eidt(self):
		notes = NotesApplication()
		notes.create("Day one at Andela BC")
		notes.create("Day two at Andela BC")
		notes.edit(2, "it was fun")
		self.assertEqual(notes.get(2),"Day two at Andela BC it was fun")





if __name__ =="__main__":
	unittest.main()