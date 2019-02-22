import unittest
from bin.classes.data_row import DataRow

class TestHappyParseAndValidate(unittest.TestCase):
  def runTest(self):
    self.row_format_a = DataRow("Lastname, Firstname, (703)-742-0996, Blue, 10013")
    self.row_format_b = DataRow("Firstname1 Lastname1, Red, 11237, 703.955.0373")
    self.row_format_c = DataRow("Firstname2, Lastname2, 10014, 646 111 0101, Green")

    self.row_format_a.parse_and_validate()
    self.row_format_b.parse_and_validate()
    self.row_format_c.parse_and_validate()

    self.assertEqual('valid',self.row_format_a.status)
    self.assertEqual('valid',self.row_format_b.status)
    self.assertEqual('valid',self.row_format_c.status)

    self._assertRowValues('Blue','Firstname','Lastname','703-742-0996','10013',self.row_format_a)
    self._assertRowValues('Red','Firstname1','Lastname1','703-955-0373','11237',self.row_format_b)
    self._assertRowValues('Green','Firstname2','Lastname2','646-111-0101','10014',self.row_format_c)

  def _assertRowValues(self,color,firstname,lastname,phone,zipcode,data_row):
    color_match = color == data_row.color
    if not color_match:
      self.fail("color mismatch")
    fn_match = firstname == data_row.first_name
    if not fn_match:
      self.fail("first name mismatch")
    ln_match = lastname == data_row.last_name
    if not ln_match:
      self.fail("last name mismatch")
    phone_match = phone == data_row.phone
    if not phone_match:
      self.fail("phone number mismatch")
    zip_match = zipcode == data_row.zipcode
    if not zip_match:
      self.fail("zip mismatch")
    return True

class TestInvalidRows(unittest.TestCase):
  def runTest(self):
    self.row_bad_format = DataRow("Lastname Firstname, (703)-742-0996, Blue, 10013")
    self.row_bad_format_2 = DataRow("Lastname, Firstname, (703)-742-0996, 10013, Blue")
    self.row_bad_format_3 = DataRow("Lastname, Firstname, Blue, (703)-742-0996, 10013")
    self.row_bad_format_4 = DataRow("Lastname, Firstname, Blue, (703)-742-0996, 10013, Guitar Strings")
    self.row_bad_format_5 = DataRow("Lastname, Color, (703)-742-0996, 10013")
    self.row_bad_phone = DataRow("Firstname1 Lastname1, Red, 11237, 03 955 0373")
    self.row_bad_zip = DataRow("Firstname2, Lastname2, 10014234, 646 111 0101, Green")

    self.row_bad_format.parse_and_validate()
    self.row_bad_format_2.parse_and_validate()
    self.row_bad_format_3.parse_and_validate()
    self.row_bad_format_4.parse_and_validate()
    self.row_bad_format_5.parse_and_validate()
    self.row_bad_phone.parse_and_validate()
    self.row_bad_zip.parse_and_validate()

    self.assertEqual('invalid',self.row_bad_format.status)
    self.assertEqual('invalid',self.row_bad_format_2.status)
    self.assertEqual('invalid',self.row_bad_format_3.status)
    self.assertEqual('invalid',self.row_bad_format_4.status)
    self.assertEqual('invalid',self.row_bad_format_5.status)
    self.assertEqual('invalid',self.row_bad_phone.status)
    self.assertEqual('invalid',self.row_bad_zip.status)

class TestToDict(unittest.TestCase):
  def runTest(self):
    self.row_format_a = DataRow("Lastname, Firstname, (703)-742-0996, Blue, 10013")
    self.row_format_b = DataRow("Firstname1 Lastname1, Red, 11237, 703 955 0373")
    self.row_format_c = DataRow("Firstname2, Lastname2, 10014, 646 111 0101, Green")

    self.row_format_a.parse_and_validate()
    self.row_format_b.parse_and_validate()
    self.row_format_c.parse_and_validate()

    self.assertEqual({
      'color': 'Blue',
      'firstname': 'Firstname',
      'lastname': 'Lastname',
      'phonenumber': '703-742-0996',
      'zipcode': '10013'
    },self.row_format_a.to_dict())

    self.assertEqual({
      'color': 'Red',
      'firstname': 'Firstname1',
      'lastname': 'Lastname1',
      'phonenumber': '703-955-0373',
      'zipcode': '11237'
    },self.row_format_b.to_dict())

    self.assertEqual({
      'color': 'Green',
      'firstname': 'Firstname2',
      'lastname': 'Lastname2',
      'phonenumber': '646-111-0101',
      'zipcode': '10014'
    },self.row_format_c.to_dict())
