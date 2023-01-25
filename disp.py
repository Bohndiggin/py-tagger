from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import csv

from utils import *

class MainWindow:
    def __init__(self, root) -> None:
        self.root = root
    
        self.main_frame = ttk.Frame(root)
        self.main_frame['padding'] = 5
        self.main_frame.grid(column=0, row=0, sticky=NSEW)

        root.option_add('*tearOff', FALSE)
        menubar = Menu(root)
        root['menu'] = menubar
        menu_file = Menu(menubar)
        # menu_edit = Menu(menubar)
        menu_tags = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        # menubar.add_cascade(menu=menu_edit, label='Edit')
        menubar.add_cascade(menu=menu_tags, label='Tag Control')

        # menu_file.add_command(label='New', command=self.placeholder_command)
        menu_file.add_command(label='Open...', command=self.open_csv)
        menu_file.add_command(label='Save', command=self.save_command)
        
        # menu_edit.add_command(label='Add Task', command=self.placeholder_command)
        # menu_edit.add_command(label='Remove Task', command=self.placeholder_command)

        menu_tags.add_command(label='Add Tags', command=self.add_tags_window)
        menu_tags.add_command(label='Load Tag Set', command=self.load_tag_set)
        menu_tags.add_command(label='Save Tag Set', command=self.save_tag_set)

        ## ENTRY
        self.text_frame = ttk.Labelframe(self.main_frame, text='Entry')
        self.text_frame.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=NSEW)
        self.text_box = Text(self.text_frame, height=50, width=90)
        self.text_box.grid(column=0, row=0, sticky=NSEW)

        ## TAGS

        self.tags_frame = ttk.Labelframe(self.main_frame, text='tags')
        self.tags_frame.grid(column=2, row=0, sticky=NSEW)

        ## Controls

        self.controls_frame = ttk.Labelframe(self.main_frame, text='controls')
        self.controls_frame.grid(column=2, row=1, sticky=NSEW)
        self.btn = ttk.Button(self.controls_frame, text='WOAAH', command=self.placeholder_command)
        self.btn.grid(column=0, row=0, sticky=NSEW)
        
    #{"label":"SKILL","pattern":[{"LOWER":"name"}]}
    def update(self):
        pass

    def open_csv(self):
        OpenWindow(self)
        # self.imported_document = None
        # filename = filedialog.askopenfilename(initialfile='job_search.csv', defaultextension=".csv",filetypes=[("All Files","*.*"),("Comma Seperated Values","*.csv")])
        # with open(filename, 'r') as f:
        #     reader_obj = csv.reader(f, delimiter=',')

    def placeholder_command(self):
        pass
    
    def add_tags_window(self):
        TagAddWindow()

    def load_tag_set(self):
        pass

    def save_tag_set(self):
        pass

    def save_command(self):
        pass
    

class LoadWindow:
    def __init__(self) -> None:
        pass

class TagAddWindow:
    def __init__(self) -> None:
        pass

class OpenWindow:
    def __init__(self, parent) -> None:
        self.ow = Toplevel()
        self.ow_frame = ttk.Frame(self.ow)
        self.ow_frame.grid(column=0, row=0, sticky=NSEW)

        self.parent = parent

        self.open_button = Button(self.ow_frame, text='Open', command=self.open_it)
        self.open_button.grid(column=0, row=0, sticky=NSEW)

    def open_it(self):
        pass