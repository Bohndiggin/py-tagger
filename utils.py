import csv
import pandas as pd

class Tag:
    def __init__(self, name, start, end, content) -> None:
        self.name = name
        self.location = (start, end)
        self.content = content
    def __repr__(self) -> str:
        return f'{self.name} at {self.location}'
    def pack(self):
        return ''

class TagType: # mainly for exporting a set of tag types for use in multiple docs. Use by Tag(str(TagType), start, end)
    def __init__(self, desc) -> None:
        self.desc = desc
    def __repr__(self) -> str:
        return f'{self.desc}'
        
class Record:
    def __init__(self, content, name, column_name) -> None:
        self.content = content
        self.name = name
        self.column_name = column_name
        self.tags = []
        self.tag_types = []
    def add_tag_type(self, tag_type):
        self.tag_types.append(TagType(tag_type))
    def add_tag(self, tag_name, tag_start, tag_end, tag_content):
        self.tags.append(Tag(tag_name, tag_start, tag_end, tag_content))
    def add_tag_from_type(self, tag_type  ,tag_start, tag_end, tag_content):
        self.tags.append(Tag(str(tag_type)), tag_start, tag_end, tag_content)
    def read_tags(self):
        return f'{self.name} has tags {self.tags}'
    def __repr__(self) -> str:
        return f'{self.name} is a Record'
    
class ImportedDocument:
    def __init__(self, name, input_doc) -> None:
        self.name = name
        self.list_of_records = []
        for i in input_doc:
            doc_list = []
            for j in i:
                doc_list.append(Record(j))
            self.list_of_records.append(doc_list)
    def __repr__(self) -> str:
        return f'{self.name} an imported document of {len(self.list_of_records)} records'    

def read_in_csv(csv_name, record_column_name):
    dataframe = pd.read_csv(csv_name)
    dataframe['tags'] = ''
    for rownum in range(len(dataframe)):
        dataframe.tags.iloc[rownum] = Record(dataframe[record_column_name].iloc[rownum], f'Record {rownum}', record_column_name)
    return dataframe