from __future__ import print_function
from random import sample, choice
from Levenshtein import distance
from Bio import SeqIO
import sys
import string
import datetime as d


#@jit
def all_edit():
    
    length_cutoff = int(sys.argv[1])
    edit_dis = int(sys.argv[2])
    seq_file = sys.argv[3]
    filename = sys.argv[4]

    repeat_file = open("all_repeats_1-6nt.txt","r")

    records = SeqIO.parse(seq_file,"fasta")


    repeats_out = dict()
    new_motifs = set()
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
        repeats_out['rep_lengths'] = [length_cutoff]
        new_motifs.add(motif) #consists of all the motifs of specified length

    """
    accessing the newly formed motifs 
    """

    #alphabet = ['A','T','G','C']
    #i=-1

    repeat_lengths = repeats_out['rep_lengths'] # All possible length cutoffs
    
    for record in records:

        input_seq = str(record.seq).upper()
        print(input_seq)

        input_seq_length = len(input_seq)
        for length_cutoff in repeat_lengths:
            #fallback = length_cutoff - 1
            sub_start = 0  # substring start
            sub_stop = sub_start + repeat_lengths[-1]  # substring stop
            while sub_stop <= input_seq_length:
            
                subseq = input_seq[sub_start:sub_stop]

                if subseq not in new_motifs:
                    
                    for ext_rep in new_motifs:
                        #i = i+1
                        cal_edit_dis = distance(subseq, ext_rep)
                        if(cal_edit_dis <= edit_dis):
                            print('{:<20s} {:<20s} {:<20s} {:<20s} {:<20s} {:<10s} {:<10s}'.format(record.id,str(sub_start),str(sub_stop),subseq,ext_rep,repeats_out[ext_rep]['class'],str(cal_edit_dis)),file = out_file)
                            #print(record.id,str(sub_start),str(sub_stop),subseq,ext_rep,repeats_out[ext_rep]['class'],str(cal_edit_dis),sep='\t',file = out_file)
                    sub_start += 1
                    sub_stop = sub_start + length_cutoff

                else:
                    sub_start += length_cutoff
                    sub_stop = sub_start + length_cutoff
                

st = d.datetime.now()    
all_edit()
print(d.datetime.now()-st)
