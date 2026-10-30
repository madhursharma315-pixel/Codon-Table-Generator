# Codon Table Generator

## 1. Project Overview

This project uses Python to generate a codon table and translate DNA sequences into their corresponding amino acids using the standard genetic code.

## 2. Objective

To create a Python program that accepts a DNA or RNA sequence, divides it into codons, and identifies the corresponding amino acids.

## 3. Features

* Contains all 64 codons and their corresponding amino acids.
* Accepts DNA and RNA sequences.
* Validates nucleotide input.
* Divides sequences into groups of three nucleotides.
* Translates codons into amino acids.
* Identifies start and stop codons.
* Detects incomplete codons at the end of a sequence.
* Displays the complete codon table.

## 4. Technologies Used

* Python 3
* Python dictionaries
* Loops and conditional statements
* String manipulation

## 5. Requirements

Python 3 must be installed on your computer.

## 6. How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the command:

```bash
python Codon-Table-Generator.py
```

## 7. Sample Input

```text
ATGGCTTTTTAA
```

## 8. Expected Output

```text
Codons: ATG - GCT - TTT - TAA
Amino acids: Methionine - Alanine - Phenylalanine - Stop
Start codons: ATG
Stop codons: TAA
```

## 9. Biological Significance

A codon consists of three nucleotides that specify an amino acid or a translation stop signal. Codon translation helps us understand how genetic information is used to produce proteins.

## 10. Learning Outcomes

This project demonstrates Python dictionaries, loops, conditional statements, string manipulation, input validation, and basic biological sequence analysis.
