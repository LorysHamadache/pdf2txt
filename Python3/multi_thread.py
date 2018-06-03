from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

import os
import shutil
import datetime
import time





def extract_text_from_pdf(filepath, page_beg, page_end=0):
    if (page_end == 0):
        page_end = page_beg

    fp = open(filepath, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()

    parser.set_document(doc)
    doc.set_parser(parser)

    doc.initialize('')

    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    laparams.char_margin = 4.0 # 2.0 by default :  two char whose distance is closer than this value are considered contiguous and get grouped into one.
    laparams.word_margin = 0.3 # 0.1 by default : distance between two words is greater than this value => insert space
    laparams.line_margin = 0.5 # 0.5 by default : Distance between 2 Lines under this value are grouped

    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    extracted_text = ''

    x = list(doc.get_pages())
    for i in range (page_beg-1, page_end):
        page = x[i]
        extracted_text += "EXTRACTION DE LA PAGE " + str(i+1) + "\n\n"
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                extracted_text += lt_obj.get_text()
                extracted_text += "\n"

    return extracted_text

def prep_challenge(n):
    if not os.path.exists("/home/lorys/Documents/targets"):
        os.makedirs("/home/lorys/Documents/targets")

    for i in range(0,n):
        print(i)

        src_dir="../Pdf_test/fichier.pdf"
        dst_dir="/home/lorys/Documents/targets/fichier"+str(i)+".pdf"
        shutil.copy(src_dir,dst_dir)




def folderpdf2foldertxt(path_in,path_out):
    start_time = time.time()
    if not os.path.exists(path_out):
        os.makedirs(path_out)
    i=0
    for f in os.listdir(path_in):
        i= i+1
        print(path_in + "/" +f)
        fichier = open((path_out + "/" + f).replace("pdf","txt"), "w")
        fichier.write(extract_text_from_pdf(path_in + "/" +f, 1))
        fichier.close()
    interval = time.time() - start_time
    print ('Total time in seconds:', interval)






dir = "/home/lorys/Documents/targets"
dirout = "/home/lorys/Documents/targetstxt"
#prep_challenge()
folderpdf2foldertxt(dir, dirout)
