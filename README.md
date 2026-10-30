# Codon Table Generator

## 1. Project Overview

In this project, Python is used to translate the DNA sequences to amino acids and generate a table of codons using the standard genetic code.

## 2. Objective

To write a Python program to accept a DNA or RNA sequence, break it into codons and show which amino acid that each encodes.

## 3. Features

* Has all 64 codons and the amino acids that follow them.
* Accepts DNA and RNA sequences.
* Validates nucleotide input.
* Segments sequences into triplets.
* Translates codons into amino acids.
* Identifies start and stop codons.
* Identify incomplete codons at the end of a sequence.
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
2. Open the folder for your project in VS Code.
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

A codon is a set of three nucleotides that codes for an amino acid or a translation stop signal. The translation of a codon elucidates how genes are expressed into protein.

## 10. Learning Outcomes

This is a showcase of Python dictionaries, loops, conditionals, string handling, input validation, and some simple biological sequence analysis.

## Testing and Validation

The project includes a unit test file named `test_codon_generator.py`.

The six unit tests check:

* Whether all 64 codons are present.
* Whether ATG maps to Methionine.
* Whether TAA, TAG, and TGA are stop codons.
* Whether selected codons map to the correct amino acids, including Phenylalanine, Tryptophan, and Alanine.

### Running the Tests

Run the following command from the project folder:

```bash
python -m unittest test_codon_generator.py
```

The test file uses Python's `ast` module to extract the codon table from the main program without running its interactive input prompts.

**Note:** These tests check the codon table, and the particular codon assignments we've chosen. They do not test all the features of DNA/RNA translation. Run the tests locally to make sure they pass.
