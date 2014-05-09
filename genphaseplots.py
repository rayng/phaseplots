# First let me test out plotting images on python

import numpy as np
import matplotlib.pyplot as plt
import glob

#use glob to list out files that we want in this case:
# This is the main input to the program

def gen_interference_patterns(dir):
#iterate through files
files=glob.glob(dir)
for f in files:
    # parse file name using "/" delimiter
    fsplit=f.split("/")
    # extract last element which is the file name
    fn=fsplit[len(fsplit)-1]
    # load text
    intpattern=np.loadtxt(f)
    arr=intpattern.transpose()
    x,y,z = arr[0], arr[1], arr[2]
    plt.scatter(x, y, c=z, s=50, edgecolor='')
    plt.xlim(min(x), max(x))
    plt.ylim(min(y), max(y))
    plt.ylabel(r"$z$",fontsize=20)
    plt.xlabel(r"$x$",fontsize=20)
    plt.colorbar()
    plt.savefig('./figs/'+fn+'.png')
    plt.clf()
    

tf=0.6595
dir='/home/ngray/ORCA/GPE/SRC/free-exp-data/nr1/*'+str(tf)+'*.dat'

#test this
gen_interference_patterns(dir)






