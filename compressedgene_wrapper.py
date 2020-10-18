#A Gene compressor of str type 
#into an iterable bit sequence

from collections import deque #importing deque from collectons to use a list
#with operations which work on both ends (queue data structure)

class BitSequence:
    def __init__(self,bit_string):
        self._bit_sequence(bit_string) #initializing a private function
        #directly in the BitSequence class whcih accepts a bit_string as argument

    def __getitem__(self,index):
        return self.dq[index] #implementing __getitem__ to be able to return
    #a particular element in the bit sequence

    def __len__(self):
        return len(self.dq) #o be able to use len() on or sequence

    def _bit_sequence(self, bit_string): #defining the bit seq function
        self.dq=deque([]) #creating a deque object
        for i in range(0,bit_string.bit_length()-1,2): #-1 to remove sentinel
            #created in while compressing a gene which will be created in the
            #compressed gene class and 2 steps to always get 2 different bits
            
            self.dq.appendleft(bit_string>>i & 0b11) #shifting the bit_string
            #being worked upon to the right by i and getting exactly to bits
            #by using bitwise & on 11 (& on 11 makes digits replace the 11)
            #appendleft works best cos the bit string is being read from left
            #to right instead how it will be originally created(right to left)
            #with this method there will be no need to reverse the string
            #after decompressing the compressed gene


    def __repr__(self):
        return repr(self.dq) #to display deque will all its elements

class CompressedGene:
    def __init__(self, gene):
        self._compress(gene) #initalizing the private function that compresses
        #the gene directly under __init__

    def _compress(self, gene):
        self.bit_string = 1 #1 as a sentinnel
        for nucleotide in gene.upper():
            self.bit_string <<= 2 #for every necucltide taken, shift bit_string to
            #the left by 2 zeroes to created space for two bits
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide at position\
                                 gene.find(nucleotide): {nucleotide}")
    def decompress(self):
        gene=""
        bit_sequence=BitSequence(self.bit_string) #creating a BitSequence object
        #from the created bit_string from compressed gene
        for bit in bit_sequence: #iterating over the bit_sequence
            if bit == 0b00:
                gene += "A"
            elif bit == 0b01:
                gene += "C"
            elif bit == 0b10:
                gene += "G"
            elif bit == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid bit: {bit}")
        return gene

    def __str__(self):
        return self.decompress() #to display the string that decompress() returns
        
    

if __name__ == "__main__":
    
    from sys import getsizeof
    gene="ACCTGGT"
    print(gene)
    print(getsizeof(gene),"bytes")
    compressed_gene=CompressedGene(gene)
    print(compressed_gene.bit_string)
    print(getsizeof(compressed_gene.bit_string),"bytes")
    print(BitSequence(compressed_gene.bit_string))
    print(compressed_gene.decompress())

























                
