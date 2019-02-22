import re
import pdb

class DataRow:
  def __init__(self, line_str):
    raw_columns = line_str.split(',')
    self.columns = map(lambda elem: elem.strip(), raw_columns)
    self.status = 'valid' #optimism!

  def parse_and_validate(self):
    self._parse_line()
    if 'invalid' == self.status: return False
    self._validate_columns()

  def to_dict(self):
    return {
      'color': self.color,
      'firstname': self.first_name,
      'lastname': self.last_name,
      'phonenumber': self.phone,
      'zipcode': self.zipcode
    }

  ################################################################
  ### Line Format Determination and Parsing
  ################################################################
  # future additions to line formats should be handled here
  def _parse_line(self):
    column_count = len(self.columns)
    if 4 == column_count:
      self._parse_four_columns()
    elif 5 == column_count:
      self._parse_five_columns()
    else:
      self.status = 'invalid'
    if 'valid' == self.status:
      self._transform_phone()

  def _parse_four_columns(self):
    full_name, self.color, self.zipcode, self.phone = self.columns
    name_parts = full_name.rsplit(' ',1) #assume middle name/initial will be preserved as part of first name
    if len(name_parts) == 2 :
      self.first_name, self.last_name = name_parts
    else:
      self.status = 'invalid'

  def _parse_five_columns(self):
    if self._is_zip(self.columns[2]):
      self._parse_format_a()
    elif self._is_phone(self.columns[2]):
      self._parse_format_b()
    else:
      self.status = 'invalid'

  def _parse_format_a(self):
    self.first_name, self.last_name, self.zipcode, self.phone, self.color = self.columns

  def _parse_format_b(self):
    self.last_name, self.first_name, self.phone, self.color, self.zipcode = self.columns

  def _transform_phone(self):
    digits_only = re.sub('[^\d]','',self.phone)
    area_code = digits_only[0:3]
    exchange = digits_only[3:6]
    number = digits_only[6:10]
    self.phone = "%(area_code)s-%(exchange)s-%(number)s" % \
      {'area_code': area_code, 'exchange': exchange, 'number': number}

  ################################################################
  ### END Line Format Determination and Parsing
  ################################################################


  ################################################################
  ### Column Validation
  ################################################################
  # future additions to validations should be handled here

  ### NOTE: since the spec does not require a positive length string for names or color
  ### we won't validate that, but this is where we would add such validations if the
  ### requestor changed their mind. The only requirements in the spec
  ### are that phone and zip have their respective formats and be in the right position
  ### in the row, and that there are columns for the string values, even if those
  ### columns are empty strings or spaces. In real life I would simply ask the requestor
  ### about empty names/colors before wrapping this up.
  def _validate_columns(self):
    if not self._is_zip(self.zipcode):
      self.status = 'invalid'
    elif not self._is_phone(self.phone):
      self.status = 'invalid'

  def _is_zip(self, str):
    if re.match('^\d{5}$',str):
      return True
    else:
      return False

  def _is_phone(self,str):
    digits_only = re.sub('[^\d]','',str)
    if 10 == len(digits_only):
      return True
    else:
      return False

  ################################################################
  ### END Column Validation
  ################################################################
