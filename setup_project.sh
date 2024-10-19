#!/bin/bash

mkdir bioinformatics_project

cd bioinformatics_project

mkdir data scripts results

touch scripts/generate_fasta.py
touch scripts/dna_operations.py
touch scripts/find_cutsites.py
touch results/cutsite_summary.txt
touch data/random_sequence.fasta

# README
cat <<EOT > README.md
# Exam 1

This project is organized into the following structure:

- **data**: contains *random_sequence.fasta* which contains the randomly generated DNA sequence
- **scripts**: contains the following Python scripts:
  - *generate_fasta.py*: generates the DNA sequence
  - *dna_operations.py*: finds the complement and reverse of a DNA sequence
  - *find_cutsites.py*: finds the location of cut sites
- **results**: contains *cutsite_summary.txt* which contains a summary of cut sites found

EOT


echo "Project directory structure created successfully:"
ls -R bioinformatics_project
