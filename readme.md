#Rolodex

##To run the parser on the command line

`./bin/data_to_json.py <data.in> <output.json>`

Replace data.in with your input source filename.
Replace output.json with your desired output filename.

##To run the tests
`python -m unittest tests.data_row_test tests.data_transformer_test`

##General Considerations

* The DataTransformer is independent of file reading and writing, which makes it easier to reuse it when the input and output come from other sources, like memory or network operations. It also makes it cleaner to test.
* See the note on empty strings and extending the validations in data_row.py in the Validations section.
* The test cases necessary to vet the functionality described in the spec fit nicely into tests for the high-level methods. Naturally if this became more complex, there would need to be more tests for lower level methods as the call stack bacame deeper.