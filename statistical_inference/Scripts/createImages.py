
from PIL import Image
import numpy as np

def order (im_matrix):
    u,index,count = np.unique(im_matrix,return_index=True,return_counts=True, axis=0) #removed axis=0 as it is default anyway and gave an error
    b = np.zeros((np.size(im_matrix,0),np.size(im_matrix,1)),dtype=int)
    c = np.stack((index,count), axis=-1)
    c = c[c[:,1].argsort(kind='mergesort')]
    pointer = np.size(im_matrix,0)-1
    for j in range(np.size(c,0)):
        for conta in range(c[j,1]):
            b [pointer,:] = im_matrix[c[j,0]]
            pointer -= 1
    return b

def delete (n_positions,matrix,freq,positions,pos):
    mask = np.ones(n_positions, dtype=bool)
    mask[positions[0]] = False
    matrix = matrix [:,mask]
    n_positions = matrix.shape[1]
    freq = freq[mask]
    pos = pos[mask]
    return [matrix,n_positions,freq,pos]

def image (path1,path2, S, file_name, NCHROMS, threshold, apply_threshold,row_order,col_order):
    global once
    #we import the file
    file = open(path1 + file_name).readlines()
    #we look for the caracter // inside the file
    find = []
    for i, string in enumerate(file):
        if string == '//\n':
           find.append(i+3)
    #in this for cycle, we take one simulation at time and we produce its image
    for ITER,pointer in enumerate(find):
        #croms è la matrice totale
        n_columns = len(list(file[pointer]))-1
        croms = np.zeros((100, n_columns),dtype=int)
        for j in range(NCHROMS):
            f = list(file[pointer + j])
            del f[-1]
            F = np.array(f,dtype=int)
            croms[j,:]=F
        #n_pos is the number of genomic positions
        n_pos = np.size(croms,1)
        if apply_threshold == True:
           #we calculate the frequency of the derived allele for each position
           freq = croms.sum(axis=0)/NCHROMS
           freq = np.array(freq)
           for i in range(n_pos):
               if freq[i] > 0.5:
                   freq[i] = 1-freq[i]
           #freq is now a vector that contains the minor allele frequency for each position
           #we delete the positions in which the minor allele frequency is <= threshold
           positions = np.where(freq<=threshold)
           croms,n_pos,freq = delete (n_pos,croms,freq,positions)

        if row_order == True:
           #we order rows for descent haplotype frequency
           croms = order(croms)

        if col_order == True:
       #we order columns for descent frequency from left to right
          croms_transpose = croms.transpose()
          croms_transpose = order(croms_transpose)
          croms = croms_transpose.transpose()

       #Black and white image:
       #white (pixel colour coded by 1) --> ancestral allel (that is 0 in the simulation file)
       #black (pixel colour coded by 0) --> derivato (that is 1 in the simulation file)..
       #for this reason...we need to change 0 with 1 and viceversa before producing the image
        all1 = np.ones((NCHROMS,n_pos))
        bw = all1 - croms
        bw_croms_uint8 = np.uint8(bw)
        bw_croms_im = Image.fromarray (bw_croms_uint8*255, mode = 'L')
        dim.append(bw_croms_im.size[0])
        #img..selection_coefficients..NREF..ITER.bmp"
        string = path2 + "img.." + str(S) + ".." + str(ITER+1) + ".bmp"
        #string = path2 + "img..1.." + str(ITER+1)+ "..co.bmp"
        ####changes made by me: note the ..bn!!!!!!
        bw_croms_im.save(string)

#%%
                                        #MAIN
apply_threshold = False
threshold = 0.05
row_order = True
column_order = False
types = ["CR", "EN", "VU", "LC", "TEST"]
NCHROMS = 100
NITER = 1
path_sim = "Simul/"
path_img = "Images/"

global dim
dim = []

for S in types:
        file_name = "msms.." + str(S) + ".txt"
        print(file_name)
        image (path_sim, path_img, S, file_name, NCHROMS, threshold, apply_threshold, row_order, column_order)
print(np.mean(dim))

import os

path_orig = "Images/"
path_resized = "Images_resized/"
path_models = "Models/"

img_rows = 64
img_cols = 64

listing = os.listdir(path_orig)

print(len(listing))

for file in listing:
    im = Image.open(path_orig + file)
    im_resized = im.resize((img_cols, img_rows))
    im_resized.save(path_resized + file)




