import argparse

# function returns complement of DNA sequence
def complement(sequence):
    complement_dict = { # dictionary mapping base pair complements
        'A' : 'T',
        'T' : 'A',
        'G' : 'C',
        'C' : 'G',
        'a' : 't',
        't' : 'a',
        'c' : 'g',
        'g' : 'c'
    }
    return ''.join(complement_dict[base] for base in sequence if base in complement_dict)

# functions returns the reverse of DNA sequence
def reverse(sequence):
    return sequence[::-1]

# function returns the reverse of the complement DNA sequence
def reverse_complement(sequence):
    return reverse(complement(sequence))

# argparse parameters
def main():
    parser = argparse.ArgumentParser(description="Find complement and reverse of DNA sequence")
    parser.add_argument("sequence", type=str)
    args = parser.parse_args()
    sequence = args.sequence
    
    print("Original sequence:", sequence)
    print("Complement", complement(sequence))
    print("Reverse", reverse(sequence))
    print("Reverse complement", reverse_complement(sequence))

if __name__ == "__main__":
    main()