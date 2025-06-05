from Bio.Seq import Seq # Import Seq class from Biopython

DNA_1 = "CCCCCAAGCGTACAGGGTGCACTTTGTAACGATTTGGGAGTCCAGAGACTCGCTGTTTTCGAAATTTGCCCTCAAGCGCGAGTATTGAACCAGGCTTACG"
DNA_2 = "CCCAAGAACGTAGCAAGCTGACTCAAACAAAATACATTTTGCCCGCGTTACATATGAATCAAGTTGGAAGTTATGGAGCATAGTAACATGTGGACGGCCA"
DNA_3 = "GTGGTGGGTTGCTACACCCCTGCGGCAACGTTGAAGCTCCTGGATTACACTGGCTGGATCTAAGCCGTGACACCCGTCATACTCCATAACCGTCTGTAAC"
DNA_4 = "TCACGGCTTGTTCTGGACTGGATTGCCATTCTCTCAGAGTATTATGCAGGCCGGCGTACGGGTCCCATATAAACCTGTCATAGCTTACCTGACTCTACTT"
DNA_5 = "GGAAATGTGGCTAGGTCTTTGCCCACGCACCTAATCGGTCCTCGTTTGCTTTTTAGGACCCGATGAACTACAGAACACTGCAAGAATCTCTACCTGCTTT"

sequences = [DNA_1, DNA_2, DNA_3, DNA_4, DNA_5] # List of DNA sequences

# Function to calculate GC content and check validity of sequences
def gc_content(seq):
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    return round((gc_count / len(seq)) * 100, 2)

# Function to check if a sequence is valid (contains only A, C, G, T)
def is_valid(seq):
    return all(base in "ACGT" for base in seq.upper()) # Check if all bases are valid

# Main analysis of sequences
for s in sequences: 
    seq_obj = Seq(s.upper()) # Create a Seq object for each sequence
    print(f"Sequence: {s}") # Print the original sequence
    print(f"Length: {len(s)}") # Print the length of the sequence
    print(f"GC Content: {gc_content(s)}%") # Print the GC content
    print(f"Valid: {is_valid(s)}") # Check if the sequence is valid
    print(f"Reverse Complement: {seq_obj.reverse_complement()}") # Print the reverse complement of the sequence
    print("-" * 40) # Print a separator for readability
