import csv

class Tag:
    def __init__(self, name, start, end) -> None:
        self.name = name
        self.location = (start, end)
    def __repr__(self) -> str:
        return f'{self.name} at {self.location}'

class TagType: # mainly for exporting a set of tag types for use in multiple docs. Use by Tag(str(TagType), start, end)
    def __init__(self, desc) -> None:
        self.desc = desc
    def __repr__(self) -> str:
        return f'{self.desc}'
        
class Record:
    def __init__(self, content) -> None:
        self.content = content
        self.tags = []
        self.tag_types = []
    def add_tag_type(self, tag_type):
        self.tag_types.append(TagType(tag_type))
    def add_tag(self, tag_name, tag_start, tag_end):
        self.tags.append(Tag(tag_name, tag_start, tag_end))
    def add_tag_from_type(self, tag_type,tag_start, tag_end):
        self.tags.append(Tag(str(tag_type)), tag_start, tag_end)
    def read_tags(self):
        return f'{self.name} has tags {self.tags}'
    def __repr__(self) -> str:
        return f'{self.name} is a Record'
    
class ImportedDocument:
    def __init__(self, name, input_doc, index_of_records) -> None:
        self.name = name
        self.list_of_records = []
        for i in input_doc:
            self.list_of_records.append(Record(i[index_of_records]))
    def __repr__(self) -> str:
        return f'{self.name} an imported document of {len(self.list_of_records)} records'    
