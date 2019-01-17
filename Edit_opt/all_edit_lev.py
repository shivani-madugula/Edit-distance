from __future__ import print_function
from random import sample, choice
from Levenshtein import distance
import sys
import string
import datetime as d

#@jit
def all_edit():
    
    length_cutoff = int(sys.argv[1])
    edit_dis = int(sys.argv[2])
    filename = sys.argv[3]

    repeat_file = open("all_repeats_1-6nt.txt","r")

    repeats_out = dict()
    new_motifs = list()
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

    alphabet = ['A','T','G','C']
    i=-1

    for repeats in new_motifs:
        rand_indices = sample(list(range(0,length_cutoff)),edit_dis)
        for ind in rand_indices:
            rep = list(repeats)
            alphabet.remove(rep[ind])
            rep[ind]=choice(alphabet)
            repeats = "".join(rep)
            #l_repeats = len(repeats)
            alphabet = ['A','T','G','C']
        """
        compare each changed repeat with 
        other repeats in new_motifs except itself
        in this for loop only!
        """
        
        i=i+1
        
        for ext_rep in new_motifs:
            cal_edit_dis = distance(repeats, ext_rep)
            if(cal_edit_dis <= edit_dis):
                print('{:<20s} {:<20s} {:<20s} {:<10s} {:<10s}'.format(new_motifs[i],repeats,ext_rep,repeats_out[ext_rep]['class'],str(cal_edit_dis)),file = out_file)
                

st = d.datetime.now()    
all_edit()
print(d.datetime.now()-st)
