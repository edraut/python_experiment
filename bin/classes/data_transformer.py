from data_row import DataRow
from operator import itemgetter

class DataTransformer:
  def __init__(self,data):
    self.data = data
    self.entries = []
    self.errors = []

  def do_transform(self):
    self._parse_data()
    self._sort_entries()
    self._generate_output()

  def _parse_data(self):
    line_number = 0
    for line in self.data:
      data_row = DataRow(line)
      data_row.parse_and_validate()
      if 'valid' == data_row.status:
        self._insert_data(data_row)
      else:
        self._insert_error(data_row,line_number)
      line_number += 1

  def _insert_data(self,data_row):
    self.entries.append(data_row.to_dict())

  def _insert_error(self,data_row,line_number):
    self.errors.append(line_number)

  def _sort_entries(self):
    #NOTE: this approach is easy to read, extend, debug, manipulate, etc.
    # there are more performant approaches, but I've opted to avoid premature optimization
    # if a specific performance problem arises or if a metric is added to the spec
    # this could be done more efficiently to meet the new requirement,
    # e.g. concatenating last and first and only sorting once would cut the iterations in half.
    first_pass = sorted(self.entries, key=itemgetter('firstname'))
    self.entries = sorted(first_pass, key=itemgetter('lastname'))

  def _generate_output(self):
    self.normalized_data = {'entries': self.entries, 'errors': self.errors}
