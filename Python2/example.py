# Python 2.7.6 HOW TO EXTRACT TEXT



from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
# From PDFInterpreter import both PDFResourceManager and PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfdevice import PDFDevice
# To raise exception whenever text extraction from PDF is not allowed

from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator



class pdf_text_extractor:

    def __init__(self, pdf_file_path, password=""):

        self.pdf_file_path = pdf_file_path
        self.password = password

    def getText(self):


        # Open and read the pdf file in binary mode
        with open(self.pdf_file_path, "rb") as fp:

            # Create parser object to parse the pdf content
            parser = PDFParser(fp)

            # Store the parsed content in PDFDocument object
            document = PDFDocument(parser,self.password)
            # Check if document is extractable, if not abort
            if not document.is_extractable:
                raise PDFTextExtractionNotAllowed

            # Create PDFResourceManager object that stores shared resources
            # such as fonts or images
            rsrcmgr = PDFResourceManager()

            # set parameters for analysis
            laparams = LAParams()

            # Create a PDFDevice object which translates interpreted
            # information into desired format
            # Device to connect to resource manager to store shared resources
            # device = PDFDevice(rsrcmgr)
            # Extract the decive to page aggregator to get LT object elements
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)

            # Create interpreter object to process content from PDFDocument
            # Interpreter needs to be connected to resource manager for shared
            # resources and device
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            # Initialize the text
            extracted_text = ""

            # Ok now that we have everything to process a pdf document,
            # lets process it page by page
            for page in PDFPage.create_pages(document):
                # As the interpreter processes the page stored in PDFDocument
                # object
                interpreter.process_page(page)
                # The device renders the layout from interpreter
                layout = device.get_result()
                # Out of the many LT objects within layout, we are interested
                # in LTTextBox and LTTextLine
                for lt_obj in layout:
                    if (isinstance(lt_obj, LTTextBox) or
                            isinstance(lt_obj, LTTextLine)):
                        extracted_text += lt_obj.get_text()


                break;


        return extracted_text.encode("utf-8")

ins = pdf_text_extractor("./Pdf_test/fichier.pdf","")
print(ins.getText())
