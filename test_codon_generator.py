```python
import runpy
import unittest

project = runpy.run_path("Codon-Table-Generator.py")
CODON_TABLE = project["CODON_TABLE"]


class TestCodonGenerator(unittest.TestCase):

    def test_all_64_codons_exist(self):
        self.assertEqual(len(CODON_TABLE), 64)

    def test_start_codon(self):
        self.assertEqual(CODON_TABLE["ATG"], "Methionine")

    def test_stop_codons(self):
        for codon in ["TAA", "TAG", "TGA"]:
            self.assertEqual(CODON_TABLE[codon], "Stop")

    def test_phenylalanine(self):
        self.assertEqual(CODON_TABLE["TTT"], "Phenylalanine")

    def test_tryptophan(self):
        self.assertEqual(CODON_TABLE["TGG"], "Tryptophan")

    def test_alanine(self):
        self.assertEqual(CODON_TABLE["GCT"], "Alanine")


if __name__ == "__main__":
    unittest.main()
```
