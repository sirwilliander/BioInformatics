s ='ATCTTTTGCAAAAATTATTTCTTCGTGAGCTTGCGAATTTAGTGTTTGACAGGCGGATCGATCGCCCGCTTTGGTAGTGTACCTTGCGTTAGCAAGTACACTCGCCGTTCGGTCAAGCACCTTGGCCCTAACCAGGCATGTAAACGAGATTACTCAAAACCCTGGAGACCGCCGACTGGAATTAGAAGGATGCCATGGTCTGGGCTTAGAGAATACCCTAACAGGCGGTGAGAAGCTGGACAAACTCCGTGAGATTATTGTAGAGCGAGGGGAGGTTGCATCGTGTGGTGGCTAATCAAGAAATCTGATAAACGCATCATAGCTGAAAGCCTGCGTCGTAGTCGGTGGAAACCCTGGAATATGGCACGTCGTTCCCGGGGGATGCTGTGGTGAATATGGGAACCACTCTGGCAAGCATAGTCACGCCGGGATGCTCGCCAAGAACATTGTTCTAGTGACAGTCGACAAGTGTTTGCGTCAAAATAATAGAGGGGGTAACCGAACTACCAGTCCATAACTCCGGCCTCGGGATCAATGTGGGCACGAATTACGAAGGCGGGCACAGCATAGCTGTTCAGTTGTCCAAGCCGGCATTACCCCCTTCTCAAAGAATGTTGTCCCCATAGAGAATCGCATGAGATATGGAGCCTGAGGCATGCTTTTCCAGCGCACAGTGAGAGGCAGCTGAGCTGTCTCGCTCCGCAGACTCTGTCAACTAGACGAGTACTCCAAAATCGGTACCAGGTGACTGAGCTCCTTTTTATTCGTAACGAGTAGTAACTGGCTGCCAAATACAAAGGACCCTTACGTAAAATATCAATCCGTGGAGGTGGAGCCAGGTGCCTTGGGGGTGAATAGAGGCTTAGCAAATATTGCAGGATACTAGCAATGTCCATCCTACCTGCTTCATCTGGGGTATTAAGACCTATATCCTCCTATAAAC'

dict={}

dict['A']=0
dict['C']=0
dict['G']=0
dict['T']=0

for i in range(len(s)):
    dict[s[i]]= dict[s[i]]+1

print(dict['A'], dict['C'], dict['G'],dict['T'])