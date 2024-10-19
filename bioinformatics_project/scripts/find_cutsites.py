import argparse
import os

# function reads the file with the DNA sequence 
def read_file(filename):
    with open(filename, 'r') as fasta_file:
        sequence = ""
        for line in fasta_file:
            sequence += line.strip() # remove whitespace
    return sequence

# function finds location of cut sites
def find_cut_sites(sequence, cut_site):
    location = []
    start = 0
    while True:
        start = sequence.find(cut_site, start)
        if start == -1:
            break # stop if there are no more
        location.append(start)

        start += 1
    return location

# function finds pairs that are 80 - 120 kp apart
def find_pairs(location):
    pairs = []
    for i in range(len(location)):
        for j in range(i + 1, len(location)):
            distance = location[j] - location[i]
            if 80000 <= distance <= 120000:
                pairs.append((location[i], location[j]))
    return pairs

# argparse parameters
def main():
    parser = argparse.ArgumentParser(description="Find distant cutsites")
    parser.add_argument("filename", type=str)
    parser.add_argument("cut_site", type=str)
    args = parser.parse_args()

    sequence = read_file(args.filename)

    cut_site0 = args.cut_site
    cut_site = args.cut_site.replace('|', '') # remove | in cut site

    location = find_cut_sites(sequence, cut_site)

    cut_site_pairs = find_pairs(location)

    # print summary
    print(f"Analyzing cut site:", cut_site0)
    print(f"Total cut sites found:", len(location))
    print(f"Cut site pairs 80-120 kp apart:", len(cut_site_pairs))
    print(f"First 5 pairs:")
    for i, pair in enumerate(cut_site_pairs[:5]):
        print(f"{i + 1}. {pair[0]} - {pair[1]}")

    # write summary in cutsite_summary.txt
    cutsite_summary = os.path.join("results", "cutsite_summary.txt")
    with open(cutsite_summary, 'w') as cutsite_summary:
        cutsite_summary.write(f"Analyzing cut site: {args.cut_site}\n")
        cutsite_summary.write(f"Total cut sites found: {len(location)}\n")
        cutsite_summary.write(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}\n")
        cutsite_summary.write("First 5 pairs:\n")
        for i, pair in enumerate(cut_site_pairs[:5]):
            cutsite_summary.write(f"{i + 1}. {pair[0]} - {pair[1]}\n")


if __name__ == "__main__":
    main()
