# Codon Table Generator
# Standard genetic code

codon_table = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",
    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",

    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}

start_codons = {"ATG"}
stop_codons = {"TAA", "TAG", "TGA"}

print("CODON TABLE GENERATOR")
print("1. DNA sequence")
print("2. RNA sequence")

choice = input("Choose 1 or 2: ").strip()

if choice not in {"1", "2"}:
    print("Invalid choice.")
else:
    sequence = input("Enter your sequence: ").upper().strip()
    sequence = "".join(sequence.split())

    if choice == "2":
        sequence = sequence.replace("U", "T")

    if not sequence or any(base not in "ATGC"
                           for base in sequence):
        print("Invalid sequence. Use only A, T, G and C for DNA,")
        print("or A, U, G and C for RNA.")
    else:
        print("\nCODON TABLE")
        for codon, amino_acid in sorted(codon_table.items()):
            print(f"{codon} : {amino_acid}")

        codons = [
            sequence[i:i + 3]
            for i in range(0, len(sequence), 3)
        ]

        print("\nRESULTS")
        print("Codons:", " - ".join(codons))

        amino_acids = []
        for codon in codons:
            if len(codon) < 3:
                amino_acids.append("Incomplete codon")
            else:
                amino_acids.append(codon_table[codon])

        print("Amino acids:", " - ".join(amino_acids))

        starts = [c for c in codons
                  if c in start_codons]
        stops = [c for c in codons
                 if c in stop_codons]

        print("Start codons:", starts if starts else "None")
        print("Stop codons:", stops if stops else "None")

        if len(sequence) % 3 != 0:
            print("Warning: The sequence has an incomplete codon.")