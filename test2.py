# Python 2.7.6
# PdfAdapter.py

""" Reusable library to extract text from pdf file
Uses pdfminer library; For Python 3.x use pdfminer3k module
Below links have useful information on components of the program
https://euske.github.io/pdfminer/programming.html
http://denis.papathanasiou.org/posts/2010.08.04.post.html
"""


from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
# From PDFInterpreter import both PDFResourceManager and PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfdevice import PDFDevice
# To raise exception whenever text extraction from PDF is not allowed
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator




class pdf_text_extractor:
    """ Modules overview:
     - PDFParser: fetches data from pdf file
     - PDFDocument: stores data parsed by PDFParser
     - PDFPageInterpreter: processes page contents from PDFDocument
     - PDFDevice: translates processed information from PDFPageInterpreter
        to whatever you need
     - PDFResourceManager: Stores shared resources such as fonts or images
        used by both PDFPageInterpreter and PDFDevice
     - LAParams: A layout analyzer returns a LTPage object for each page in
         the PDF document
     - PDFPageAggregator: Extract the decive to page aggregator to get LT
         object elements
    """

    def __init__(self, pdf_file_path, password=""):
        """ Class initialization block.
        Pdf_file_path - Full path of pdf including name
        password = If not passed, assumed as none
        """
        self.pdf_file_path = pdf_file_path
        self.password = password

    def getText(self):
        """ Algorithm:
        1) Txr information from PDF file to PDF document object using parser
        2) Open the PDF file
        3) Parse the file using PDFParser object
        4) Assign the parsed content to PDFDocument object
        5) Now the information in this PDFDocumet object has to be processed.
        For this we need PDFPageInterpreter, PDFDevice and PDFResourceManager
        6) Finally process the file page by page
        """

        # Open and read the pdf file in binary mode
        with open(self.pdf_file_path, "rb") as fp:

            # Create parser object to parse the pdf content
            parser = PDFParser(fp)

            # Store the parsed content in PDFDocument object
            document = PDFDocument(parser, self.password)

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


        return extracted_text.encode("utf-8")

ins = pdf_text_extractor("./Pdf_test/fichier.pdf","")
print(ins.getText())
