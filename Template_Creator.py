from __future__ import print_function
from pydoc import doc
from mailmerge import MailMerge
from datetime import date
import os
import csv
template = 'Document Transmittal.docx'

def Word_import(out_file):
    Tables=[*csv.DictReader(open(out_file))]
    print(Tables)
    document = MailMerge(template)
    print("Fields included in {}: {}".format(template, document.get_merge_fields()))

    document.merge_rows('Filename',  Tables)
    document.write('Transmittal Note.docx')
    print("See "+ os.getcwd() + "/Transmittal Note.docx")


