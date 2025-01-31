"""Unit tests for MDF file parser"""

import unittest
import tempfile
import os
from typing import Dict
from tools.mdf_parser.mdf_parser import parse_mdf_file
from tools.mdf_parser.topology import extract_topology

class TestMDFParser(unittest.TestCase):
    def setUp(self) -> None:
        self.test_dir = tempfile.mkdtemp()
        
    def test_parse_mdf_file(self) -> None:
        # Create a minimal test MDF file
        test_content = """
MOL:1:C1  1  CG1  0.0  1.0  2.0  3.0  0  0  0  0  MOL:1:C2/1
MOL:1:C2  2  CG1  1.0  2.0  3.0  4.0  0  0  0  0  MOL:1:C1/1 MOL:1:C3/1
MOL:1:C3  3  CG2  2.0  3.0  4.0  5.0  0  0  0  0  MOL:1:C2/1
"""
        test_file = os.path.join(self.test_dir, "test.mdf")
        with open(test_file, "w") as f:
            f.write(test_content)
            
        result = parse_mdf_file(test_file)
        
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 3)
        self.assertIn("MOL:1:C1", result)
        self.assertEqual(result["MOL:1:C1"]["charge_group"], "CG1")
        self.assertEqual(result["MOL:1:C1"]["neighbors"], ["MOL:1:C2"])

    def test_extract_topology(self) -> None:
        test_data = {
            "MOL:1:C1": {"charge_group": "CG1", "neighbors": ["MOL:1:C2"]},
            "MOL:1:C2": {"charge_group": "CG1", "neighbors": ["MOL:1:C1", "MOL:1:C3"]},
            "MOL:1:C3": {"charge_group": "CG2", "neighbors": ["MOL:1:C2"]}
        }
        
        bonds, angles, dihedrals = extract_topology(test_data)
        
        self.assertIsInstance(bonds, dict)
        self.assertIsInstance(angles, dict)
        self.assertIsInstance(dihedrals, dict)
        
        # Check bonds
        self.assertEqual(len(bonds), 2)
        self.assertIn(("CG1", "CG1"), bonds)
        self.assertIn(("CG1", "CG2"), bonds)

    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.test_dir)

if __name__ == '__main__':
    unittest.main()
