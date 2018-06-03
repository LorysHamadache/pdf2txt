from multi_thread import *
from program_linear import *
from multi_process import *

import os
import matplotlib.pyplot as plt


dir = "/home/lorys/Documents/targets2"
dirout = "/home/lorys/Documents/targetstxt2"

y = []
y_m = []
y_p =[]

n = 20

def suppression_folder(dir):
    for the_file in os.listdir(dir):
        file_path = os.path.join(dir, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def graph(n):
    for i in range (0,n):
        suppression_folder(dirout)
        y_m.append(folderpdf2foldertxt_m(dir,dirout))

    for i in range (0,n):
        suppression_folder(dirout)
        y.append(folderpdf2foldertxt(dir,dirout))
    plt.plot(y)
    plt.plot(y_m)
    plt.show()

#suppression_folder(dirout)
