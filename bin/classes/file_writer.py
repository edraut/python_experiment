import json

class FileWriter:
  def __init__(self,output_filename,data):
    self.output_filename = output_filename
    self.data = data

  def write(self):
    outfile = open(self.output_filename,'w')
    json.dump(self.data,outfile,indent=2)
    outfile.close()
