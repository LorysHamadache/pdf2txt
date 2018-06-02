from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine



fp = open("../Pdf_test/fichier.pdf", 'rb')


def extract_text_from_pdf(filepath, page_beg, page_end=0):
    if (page_end == 0):
        page_end = page_beg


    parser = PDFParser(filepath)
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
    fichier = open("../data.txt", "w")
    fichier.write(extracted_text)
    fichier.close()
    return extracted_text




extract_text_from_pdf(fp,1)

.
