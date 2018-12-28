from __future__ import print_function
from random import sample, choice
from weighted_levenshtein import lev
import numpy as np
import sys
import string
import datetime as d

substitute_costs = np.ones((128, 128), dtype=np.float64)

def all_edit():
    
    #length_cutoff = int(input("Enter length cutoff:"))
    #edit_dis = int(input("enter edit distance:"))
    #filename = input("enter output filename:")
    length_cutoff = int(sys.argv[1])
    edit_dis = int(sys.argv[2])
    filename = str(sys.argv[3])

    repeat_file = open("all_repeats_1-6nt.txt","r")

    repeats_out = dict()
    new_motifs = list()
    #motif_fallback = dict()
    #repeat_lengths = []
    out_file = open(filename,"w+")
    
    motif_lengths = []

    for line in repeat_file:
        motif_dict = dict()
        
        L = line.strip().split('\t')
        motif = L[0]
        motif_length = int(L[2])

        if motif_length not in motif_lengths:
            motif_lengths.append(motif_length)
        i=0
        input_seq_length = motif_length
        while i < motif_length and input_seq_length < length_cutoff:
            motif += motif[i]
            i += 1
            if i >= motif_length:
                i = 0
            input_seq_length = len(motif)
        
        motif_dict['class'] = L[1]
        motif_dict['motif_length'] = motif_length
        motif_dict['strand'] = L[3]
        repeats_out[motif] = motif_dict
        new_motifs.append(motif) #consists of all the motifs of specified length

    """
    accessing the newly formed motifs 
    """

    #print(repeats_out[new_motifs[9]]['class'])
    alphabet = ['A','T','G','C']
    i=-1
    #print(rand_indices)
    for repeats in new_motifs:
        rand_indices = sample(list(range(0,length_cutoff)),edit_dis)
        for ind in rand_indices:
            rep = list(repeats)
            alphabet.remove(rep[ind])
            rep[ind]=choice(alphabet)
            repeats = "".join(rep)
            l_repeats = len(repeats)
            alphabet = ['A','T','G','C']
            #print(rand_indices)
            #print(repeats[ind])
        #print(repeats)
        #print(new_motifs[0])
        #break
        """
        compare each changed repeat with 
        other repeats in new_motifs except itself
        (use wagner fisher now)
        in this for loop only!
        """
        
        i=i+1
        
        for ext_rep in new_motifs:
            #print(new_motifs[2])
            cal_edit_dis = lev(repeats, ext_rep)
            
            #print(cal_edit_dis)
            #print(ext_rep,repeats_out[ext_rep]['class'])
            if(cal_edit_dis <= edit_dis):
                print('{:<20s} {:<20s} {:<20s} {:<10s} {:<10s}'.format(new_motifs[i],repeats,ext_rep,repeats_out[ext_rep]['class'],str(cal_edit_dis)),file = out_file)
                #print(new_motifs[i],'\t',repeats,'\t',ext_rep,'\t',repeats_out[ext_rep]['class'],'\t',cal_edit_dis, file = out_file)
                



st = d.datetime.now()    
all_edit()
print(d.datetime.now()-st)
