### It might feel heavy for just opening a file, but I like my main methods to read cleanly
### and this will encapsulate things like filename validations as needed
class FileLoader:
  def __init__(self,input_filename):
    self.input_filename = input_filename

  def load_file(self):
    self.file = open(self.input_filename,'r')

  def close_file(self):
    self.file.close()
