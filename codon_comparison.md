# Comparison of Codon Table Generator with the NCBI Standard Genetic Code

## 1. Aim

To check whether the codon-to-amino-acid assignments in the Python Codon Table Generator agree with the NCBI Standard Genetic Code.

## 2. Reference Database

* **Database:** National Center for Biotechnology Information (NCBI)
* **Reference:** Standard Genetic Code, Translation Table 1
* **Purpose:** To verify the amino acid assigned to each codon.

## 3. Methodology

1. A Python dictionary was used to store the 64 possible DNA codons.
2. Each codon was assigned its corresponding amino acid or stop signal.
3. Representative codons were compared with the NCBI Standard Genetic Code.
4. Start and stop codon detection was examined.
5. DNA and RNA input handling was considered.

## 4. Comparison Results

| Parameter                        | Python Codon Table Generator | NCBI Standard Genetic Code    |
| -------------------------------- | ---------------------------- | ----------------------------- |
| Total possible codons            | 64                           | 64                            |
| Amino-acid-coding codons         | 61                           | 61                            |
| Stop codons                      | 3                            | 3                             |
| Start codon used in this project | ATG                          | AUG in RNA notation           |
| DNA stop codons                  | TAA, TAG, TGA                | UAA, UAG, UGA in RNA notation |
| Genetic code                     | Standard genetic code        | Standard genetic code         |

**Note:** The program uses DNA notation, where T is used. RNA sequences contain U instead, which the program converts to T for translation.

## 5. Verification of Representative Codons

| DNA Codon | Expected Assignment | Result |
| --------- | ------------------- | ------ |
| TTT       | Phenylalanine       | Match  |
| ATG       | Methionine          | Match  |
| GCT       | Alanine             | Match  |
| TGG       | Tryptophan          | Match  |
| AAA       | Lysine              | Match  |
| CGT       | Arginine            | Match  |
| TAA       | Stop                | Match  |
| TAG       | Stop                | Match  |
| TGA       | Stop                | Match  |

These representative assignments agree with the NCBI Standard Genetic Code. The complete dictionary should also be checked to confirm all 64 codons.

## 6. Observations

* The standard genetic code contains 64 possible codons.
* Sixty-one codons specify amino acids, while three signal termination.
* Multiple codons can specify the same amino acid.
* The program can group a nucleotide sequence into codons and translate complete codons.
* RNA input can be converted to DNA notation by replacing U with T.
* An incomplete codon at the end of a sequence cannot be translated as a complete codon.

## 7. Limitations

The program identifies ATG as its start codon. Some organisms can use alternative initiation codons, so this feature is a simplified representation of biological translation. The program uses the standard genetic code and does not account for all organism-specific genetic code variations.

## 8. Conclusion

The representative codon assignments checked in this comparison agree with the NCBI Standard Genetic Code. The project demonstrates how Python dictionaries, sequence validation, and codon grouping can be used for basic DNA and RNA translation. Testing all 64 codons would provide a more complete verification.

## 9. Reference

National Center for Biotechnology Information (NCBI). *The Genetic Codes: The Standard Code (Translation Table 1).*
