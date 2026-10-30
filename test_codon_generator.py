import ast
import unittest
from pathlib import Path

source_file = Path(__file__).with_name("Codon-Table-Generator.py")
source = source_file.read_text(encoding="utf-8")
tree = ast.parse(source)

codon_table_node = next(
    node for node in tree.body
    if isinstance(node, ast.Assign)
    and any(
        isinstance(target, ast.Name)
        and target.id == "codon_table"
        for target in node.targets
    )
)

namespace = {}
exec(
    compile(
        ast.Module(body=[codon_table_node], type_ignores=[]),
        str(source_file),
        "exec"
    ),
    namespace
)

CODON_TABLE = namespace["codon_table"]


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
