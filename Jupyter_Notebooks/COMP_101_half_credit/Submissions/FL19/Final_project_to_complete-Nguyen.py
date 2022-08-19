# -*- coding: utf-8 -*-
"""
Spyder Editor

Final Project for COMP 101 

J.A. Klemens

"""
##########
#    
#   Control functions
#
#       This group of functions controls data input and the main 'decision making'
#       of the program. The first function asks us to input a source of DNA
#       the second is a function that is used to import text from file, the third
#       checks our string to make sure it is DNA, and returns a true false answer
#       about whether it is DNA or not, the fourth is a function chooser which 
#       sets up the choices we have as a user of the program
#
#
###########

def input_DNA():                # This function asks the user whether they want
                                # To enter DNA manually or read a file
    
    DNA=""                      # Here we create variables to capture DNA, as string
    filename=""                 # And a filename - also as a string - to use as a variable
    
    input_type = str(input("Get DNA sequence from (F)ile or (U)ser input: \n "))
    input_type = input_type.upper()
    
    if input_type[0] == "U":
        DNA = str(input("Type or paste DNA sequence here: \n "))
        print()
        DNA=DNA.upper()
       
        
        
    elif input_type[0] == "F":
        filename = str(input("Enter file name including .txt extension :"))
        print()
        DNA = import_txt(filename)  
        DNA=DNA.upper()
        return(DNA)
    else:
         print("I didn't understand your choice, sorry!")
         print()
         
        
    is_DNA = is_DNA_checker(DNA)   # this calls the function that checks to see
                                   # if we have real DNA here. This function
                                   # is broken, you'll have to fix it below
    
    if is_DNA == False:
        DNA = ""
        
        return (DNA) 
    if is_DNA == True:       
        
        return (DNA)  
        
def import_txt(file):                 
    openfile = open(file, "r")
    contents = openfile.read()
    openfile.close
    return (contents)

def is_DNA_checker(DNA):
    for i in DNA:
        if i != "A" and i!= "C" and i != "G" and i != "T":
            print("The value " + str(i) + " is not part of a valid DNA sequence.")
            print("Sequences consist of A, C, G or T only.")
            print("Please try a different sequence.")
            print()
            return(False)  
    
    return(True)
    
def function_chooser(DNA):
    print("What would you like to do with this sequence? ")
    print("(P)rint my sequence")
    print("(C)ount the Nucleotides")
    print("Transcribe an (R)NA sequence")
    print("(T)ranslate a polypeptide if possible")
    print("e(X)it")
    function_choice = str(input("Enter your choice: "))
    print()
    function_choice = function_choice.upper()
   
    if function_choice[0] == "P":
        
        print_seq(DNA)
        function_chooser(DNA)

    elif function_choice[0] == "C":
        NucleotideCounter(DNA)
        function_chooser(DNA)
    elif function_choice[0] == "R": 
        transcribe(DNA)
        function_chooser(DNA)
    elif function_choice[0] == "T":  
        translate(DNA)
        function_chooser(DNA)
    elif function_choice[0] == "X":  
        return()
    else:
         print("I didn't understand your choice, sorry!")
         print()
         function_chooser(DNA)     
 
    
##########
#    
#   DNA manipulation functions
#       These are the functions that you choose in the function_chooser()
#       Each of them takes the DNA string we captured as an argument
###########
 
def print_seq(DNA):
    print(DNA)       # What should we print here?
    print()
    return()

def NucleotideCounter(DNA):
    A = C = G = T = 0         # these are variables to "hold" the counts for
                              # each class of nucleotide

    for i in DNA:       # define a for loop that inspects each element
        if i == "A":
            #???????:         # in DNAstring, use an if ... elif ... 
            A += 1
        elif i == "G":
            G += 1
        elif i == "T":
            T += 1
        elif i == "C":
            C += 1
        
        #elif 
        #  ...
        #
        #
        
    print("There are " + str(len(DNA)) + " nucleotides in this sequence")
    print()
    print("Distribution of nucleotides")        
    output_text = "A: " + str(A) + ", C: " + str(C) + ", G: " + str(G) + ", T: " + str(T)
    print(output_text)
    print()
    return()

def transcribe(DNA):
    mRNA = ""
    for i in DNA:          # Use a for loop to walk through the DNA data
                           # Use an if ... elif ... elif ... elif statement
                           # to do different things depending on which 
                           # nucleotide you find there, add mRNA nucleotides
                           # using the string += "X" function
        if i == "A":
            mRNA += "A"
        elif i == "T":
            mRNA += "U"
        elif i == "G":
            mRNA += "G"
        elif i == "C":
            mRNA += "C"
        #elif
        # ...
        
    print ("mRNA sequence: " + mRNA)
    print()
    return(mRNA)    
     
def translate(DNA):
    translation_dict = {'UUU':'Phe', 'UUC':'Phe', 'UUA':'Leu', 'UUG':'Leu', 'UCU':'Ser', 'UCC':'Ser', 'UCA':'Ser', 'UCG':'Ser', 'UAA': 'Stop', 'UAG': 'Stop', 'UAU':'Tyr', 'UAC':'Tyr', 'UGU':'Cys', 'UGC':'Cys', 'UGA': 'Stop', 'UGG':'Trp', 'CUU':'Leu', 'CUC':'Leu', 'CUA':'Leu', 'CUG':'Leu', 'CCU':'Pro', 'CCC':'Pro', 'CCA':'Pro', 'CCG':'Pro', 'CAU':'His', 'CAC':'His', 'CAA':'Gln', 'CAG':'Gln', 'CGU':'Arg', 'CGC':'Arg', 'CGA':'Arg', 'CGG':'Arg', 'AUU':'Ile', 'AUC':'Ile', 'AUA':'Ile', 'AUG':'Met', 'ACU':'Thr', 'ACC':'Thr', 'ACA':'Thr', 'ACG':'Thr', 'AAU':'Asn', 'AAC':'Asn', 'AAA':'Lys', 'AAG':'Lys', 'AGU':'Ser', 'AGC':'Ser', 'AGA':'Arg', 'AGG':'Arg', 'GUU':'Val', 'GUC':'Val', 'GUA':'Val', 'GUG':'Val', 'GCU':'Ala', 'GCC':'Ala', 'GCA':'Ala', 'GCG':'Ala', 'GAU':'Asp', 'GAC':'Asp', 'GAA':'Glu', 'GAG':'Glu', 'GGU':'Gly', 'GGC':'Gly', 'GGA':'Gly','GGG':'Gly'}
   
    polypeptide = ""
    mRNA = ""
    aa = ""
    
    mRNA = transcribe(DNA)
    
    start_index = find_start_codon(mRNA)       # before we can translate, we need to know
                                               # where to start, you'll have to fix
                                               # the function find_start_codon() below
    if start_index == None:
        return()                               # if no start codon, return to function_chooser()
        function_chooser(DNA)
    for i in range(start_index,len(mRNA)-2,3): # the -2 keeps me from translating a partial codon, why?
                                               # the , 3 in range() makes i count by 3s 
       
        aa = translation_dict.get(mRNA[i:i+3]) # finds the AA based on the sequence
                                               # note that mRNA[i:i+3] will be 
                                               # three letters of mRNA
        polypeptide += aa
        if aa == "Stop":
            print("Polypeptide: " + polypeptide)
            print()
            return(polypeptide)

    print("Polypeptide: " + polypeptide)
    print()
    return(polypeptide)    
    
def find_start_codon(mRNA):
    
    for i in range(len(mRNA)):                 # hint for ? below: we want i to be a number
        if mRNA[i:i+3] == "AUG":               # keep the loop going until we find the first
                                               # 3 nucleotide sequence matching "AUG"
            return(i)                        # what should we return here?
        
    print("Sorry, no start codon detected!")   # this happens if no "AUG" found
    print()     
        

##########
#    
#   Main body of program 
#     note that it is very simple
#     basically it directs the user to the input function,
#     and then to the function chooser once "DNA" has been uploaded
#
###########


DNA = ""
while DNA == "":
    DNA = input_DNA()
function_chooser(DNA)