import os,PyPDF2
import sys
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
 
for f in os.listdir('.'): 
       if f.endswith('.pdf'):
               try:
                   buffer = open(f,'rb')
                   pdfreader = PyPDF2.PdfFileReader(buffer)
                   text=str(pdfreader.documentInfo['/Title'])
                   os.rename(f,text)
               except:
                       try:
                           parser = PDFParser(buffer)
                           doc = PDFDocument(parser)
                           parser.set_document(doc)
                           rsrcmgr = PDFResourceManager()
                           laparams = LAParams()
                           device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                           interp = PDFPageInterpreter(rsrcmgr, device)

                           pages = PDFPage.create_pages(doc)
                           first_page = next(pages)
                           interp.process_page(first_page)
                           layout = device.get_result()
                           textboxes = [i for i in layout if isinstance(i, LTTextBox)]
                           box_with_tallest_line = max(textboxes, key=lambda x: max(i.height for i in x))
                           text = box_with_tallest_line.get_text()
                           t1=str(re.sub('\s+', ' ', text).strip())
                           os.rename(f,t1)
                       except:
                           try:
                               second_page = next(pages)
                               interp.process_page(first_page)
                               layout = device.get_result()
                               textboxes = [i for i in layout if isinstance(i, LTTextBox)]
                               box_with_tallest_line = max(textboxes, key=lambda x: max(i.height for i in x))
                               text = box_with_tallest_line.get_text()
                               t1=str(re.sub('\s+', ' ', text).strip())
                               os.rename(f,t1)
                           except:
                               print(f,"    Fail    ")
