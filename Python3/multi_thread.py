from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

import os
import shutil
import datetime
import time
from threading import Thread,RLock

lock = RLock()

class extraction(Thread):

    def __init__(self,filepath_in,filepath_out,f,page_beg,page_end = 0):
        Thread.__init__(self)
        self.filepath_in = filepath_in
        self.filepath_out = filepath_out
        self.nom_fichier = f
        self.page_beg = page_beg
        self.page_end = page_end


    def extract_text_from_pdf(self):
        if (self.page_end == 0):
            self.page_end = self.page_beg

        fp = open(self.filepath_in + '/' + self.nom_fichier, 'rb')
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
        for i in range (self.page_beg-1, self.page_end):
            page = x[i]
            extracted_text += "EXTRACTION DE LA PAGE " + str(i+1) + "\n\n"
            interpreter.process_page(page)
            layout = device.get_result()
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                    extracted_text += lt_obj.get_text()
                    extracted_text += "\n"

        return extracted_text

    def text_to_fichier(self):
        fichier = open((self.filepath_out + "/" + self.nom_fichier).replace("pdf","txt"), "w")
        fichier.write(self.extract_text_from_pdf())
        fichier.close()

    def run(self):
        with lock:
            self.text_to_fichier()






def prep_challenge(dir,n):
    if not os.path.exists(dir):
        os.makedirs(dir)
    for i in range(0,n):
        print(i)
        src_dir="../Pdf_test/fichier.pdf"
        dst_dir=dir +"/fichier"+str(i)+".pdf"
        shutil.copy(src_dir,dst_dir)





def folderpdf2foldertxt(path_in,path_out):
    start_time = time.time()
    if not os.path.exists(path_out):
        os.makedirs(path_out)
    l=[]
    for f in os.listdir(path_in):
        l.append(extraction(path_in,path_out,f,1))

    for x in l:
        x.start()
        
    for x in l:
        x.join()

    interval = time.time() - start_time
    print ('Total time in seconds:', interval)






dir = "/home/lorys/Documents/targets2"
dirout = "/home/lorys/Documents/targetstxt2"

folderpdf2foldertxt(dir, dirout) #EXECUTED IN 44Minutes for 10 031 pdfs ( Pc was in use)
