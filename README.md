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

6. Optimization MultiThread
    Linear : 22.8 sec for 101 files
    MultiThread 21.24 sec for 101 files
    After multiple Tests , it seems MultiThread is slower on average, high volatility of time on multiple tests

    According to an answer on StackOverflow : https://stackoverflow.com/questions/36955638/how-should-i-reduce-the-execution-time-using-threading-in-python

    Your threads are fighting with eachother on one core due to the Global Interpreter Lock. The Global Interpreter Lock prevents more than one python thread from running at a time, even on a multi-core system. Thus, to execute multiple cpu-bound tasks in parallel, it is necessary to use processes (from the multiprocessing module) instead of threads.

7. CREATION of Multi Process program
          Linear : 22.8 sec for 101 files
          MultiThread 21.24 sec for 101 files
          Multi Process 5.4 sec for 101 files

          FROM 44 minutes to 12 Minutes thanks to multiprocessing
