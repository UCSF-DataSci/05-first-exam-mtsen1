import random

# function randomly generates base pairs
def generate_dna(length): # length = 1 million base pairs
    sequence = ""
    for i in range(length):
        sequence += random.choice("ATGC") 
    return sequence

# function writes and saves sequence to file
def save_to_file(sequence, filename):
    with open(filename, 'w') as random_seq_file:
        for i in range(0, len(sequence), 80):
            random_seq_file.write(sequence[i : i + 80] + "\n") # next line ever 80 base pairs

# parameters for above functions
def main():
    length = 1000000 # 1 mil base pairs
    rand_sequence = generate_dna(length)
    random_seq_file = 'data/random_sequence.fasta'
    save_to_file(rand_sequence, random_seq_file)
    print("Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta")


if __name__ == "__main__":
    main()