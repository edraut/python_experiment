#! /usr/bin/env python

from sys import argv
from classes.file_loader import FileLoader
from classes.data_transformer import DataTransformer
from classes.file_writer import FileWriter

input_filename = argv[1]
output_filename = argv[2]

file_loader = FileLoader(input_filename)
file_loader.load_file()

transformer = DataTransformer(file_loader.file)
transformer.do_transform()

file_loader.close_file()

file_writer = FileWriter(output_filename, transformer.normalized_data)
file_writer.write()
