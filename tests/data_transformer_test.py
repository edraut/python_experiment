import unittest
from bin.classes.data_transformer import DataTransformer

class DataTransformerTestCase(unittest.TestCase):
  def setUp(self):
    self.test_input_data = [
      "Noah, Moench, 123123121, 232 695 2394, yellow",
      "Ria Tillotson, aqua marine, 97671, 196 910 5548",
      "Annalex, Loftis, 97296, 905 329 2054, blue",
      "Annalee, Loftis, 97296, 905 329 2054, blue",
      "James Johnston, gray, 38410, 628 102 3672",
      "Liptak, Quinton, (653)-889-7235, yellow, 70703",
      "0.547777482345"
    ]
    self.transformer = DataTransformer(self.test_input_data)

class TestParseData(DataTransformerTestCase):
  def runTest(self):
    self.transformer._parse_data()

    self.assertFalse(self._nameExists('Noah','Moench'))
    self.assertTrue(self._nameExists('Ria','Tillotson'))
    self.assertTrue(self._nameExists('Annalex','Loftis'))
    self.assertTrue(self._nameExists('Annalee','Loftis'))
    self.assertTrue(self._nameExists('James','Johnston'))
    self.assertTrue(self._nameExists('Quinton','Liptak'))
    self.assertEqual(5,len(self.transformer.entries))
    self.assertEqual([0,6], self.transformer.errors)

  def _nameExists(self,firstname,lastname):
    found = False
    for entry in self.transformer.entries:
      if firstname == entry['firstname'] and lastname == entry['lastname']:
        found = True
    return found

class TestSortEntries(DataTransformerTestCase):
  def runTest(self):
    self.transformer._parse_data()
    self.transformer._sort_entries()

    self.assertTrue(self._nameAtIndex('James','Johnston',0))
    self.assertTrue(self._nameAtIndex('Quinton','Liptak',1))
    self.assertTrue(self._nameAtIndex('Annalee','Loftis',2))
    self.assertTrue(self._nameAtIndex('Annalex','Loftis',3))
    self.assertTrue(self._nameAtIndex('Ria','Tillotson',4))

  def _nameAtIndex(self,firstname,lastname,index):
    firstname_match = firstname == self.transformer.entries[index]['firstname']
    lastname_match = lastname == self.transformer.entries[index]['lastname']
    return firstname_match and lastname_match

class TestGenerateOutput(DataTransformerTestCase):
  def runTest(self):
    self.transformer._parse_data()
    self.transformer._sort_entries()
    self.transformer._generate_output()

    self.assertEqual(self.transformer.entries, self.transformer.normalized_data['entries'])
    self.assertEqual(self.transformer.errors, self.transformer.normalized_data['errors'])
    