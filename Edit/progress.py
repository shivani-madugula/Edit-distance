from __future__ import print_function
from random import sample, choice
import sys
import string
import datetime as d


def all_edit():
    length_cutoff = int(input("Enter length cutoff:"))
    edit_dis = int(input("enter edit distance:"))

    repeat_file = open("all_repeats_1-6nt.txt","r")

    repeats_out = dict()
    new_motifs = list()
    #motif_fallback = dict()
    #repeat_lengths = []
    out_file1 = open("output_edit1.txt","wt")
    
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
    operation = ['s', 'i', 'd']
    i=0
    #print(rand_indices)
    for repeats in new_motifs:
        rand_indices = sample(list(range(0,length_cutoff)),edit_dis)
        #print(rand_indices)
        for j in range(0,edit_dis):
            op = choice(operation)
            
            if(op == 's'):
               ind = choice(rand_indices)
               #print('s',ind)
               rep = list(repeats)
               alphabet.remove(rep[ind])
               rep[ind]=choice(alphabet)
               repeats = "".join(rep)
               l_repeats = len(repeats)
               alphabet = ['A','T','G','C']
               rand_indices.remove(ind)
            if(op == 'i'):
               ind = choice(rand_indices)
               #print('i',ind)
               alphabet_insert = choice(alphabet)
               rep = list(repeats)
               rep.insert(ind,alphabet_insert)
               repeats = "".join(rep)
               l_repeats = len(repeats)
               rand_indices.remove(ind)
            if(op == 'd'):
                ind = choice(rand_indices)
                #print('d',ind)
                rep = list(repeats)
                if(ind not in range(0,len(rep))):
                   rand_del_ind = sample(list(range(0,len(rep))),1)
                   rep.pop(rand_del_ind[0])
                else:
                    rep.pop(ind)
                repeats = "".join(rep)
                l_repeats = len(repeats)
                rand_indices.remove(ind)
            
        

        

        """
        compare each changed repeat with 
        other repeats in new_motifs except itself
        (use wagner fisher now)
        in this for loop only!
        """
        print("=============",file = out_file1)
        print(new_motifs[i],file = out_file1)
        i=i+1
        print(repeats,file = out_file1)
        print("=============",file = out_file1)
        
        for ext_rep in new_motifs:
            #print(new_motifs[2])
            cal_edit_dis = wagner_fisher(repeats, l_repeats, ext_rep, length_cutoff)
            #print(cal_edit_dis)
            #print(ext_rep,repeats_out[ext_rep]['class'])
            if(edit_dis == cal_edit_dis):
                print(ext_rep,repeats_out[ext_rep]['class'],cal_edit_dis, file = out_file1)
    #print(repeats,l_repeats)
                
            
        
                

        




def wagner_fisher(s1, len_s1, s2, len_s2):
   
    d = {}

    #Make to use O(min(n,m)) space
    #print(s1,s2)
    if len_s1 > len_s2:
        s1, s2 = s2, s1
        len_s1, len_s2 = len_s2, len_s1
    for i in range(-1, len_s1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, len_s2 + 1):
        d[(-1, j)] = j + 1

    for i in range(len_s1):
        for j in range(len_s2):
            if s1[i] == s2[j]:
                d[i, j] = d[i - 1, j - 1]
            else:
                d[(i, j)] = min(
                    d[(i - 1, j)] + 1,  # deletion
                    d[(i, j - 1)] + 1,  # insertion
                    d[(i - 1, j - 1)] + 1,  # substitution
                )
    return d[len_s1 - 1, len_s2 - 1]

        

        
    

   
st = d.datetime.now()    
all_edit()
print(d.datetime.now()-st)

