# pdf2txt
Project's aim: Extract text from pdfs

Initial Situation : Folder containing over a thousand pdfs

Ending Situation : An other Folder containing a .txt for each pdfs containing the pdf's first page text

1. Research of a Pdf extraction library:
    => PyPDF was working fine on my pdfs but not on the tests one.
    => Self made Library had problem with Encoding
    => pdfMiner (Python2) and pdfMiner3k (Python3) is the library I have been looking format

2. Make an extraction program for 1 pdf.
    By playing with the parameters :
      -> Make sure that encoding is okay for Text
      -> Make sure that each Word are separated by a blank
      -> Create Indentation

3. Creation of the tests folders

4. Creation of the program able to extract all pdfs from a folder.

5. Tests => 10 031 pdfs extracted in 44 minutes (pc in use)

6. Optimization MultiThread???
