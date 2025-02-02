"""Unit tests for CHARMM parameter file parser"""

import unittest
import tempfile
import os
from typing import Dict
import pandas as pd
from ..parser import CharmmProcessor

class TestCharmmParser(unittest.TestCase):
    def setUp(self) -> None:
        self.processor = CharmmProcessor()
        self.test_dir = tempfile.mkdtemp()
        
    def test_process_file(self) -> None:
        # Create a minimal test parameter file
        test_content = """ATOMS
MASS 1 H 1.008 ! Hydrogen
MASS 2 C 12.01 ! Carbon

BONDS
H C 340.0 1.09 ! Aliphatic CH
"""
        test_file = os.path.join(self.test_dir, "test.prm")
        with open(test_file, "w") as f:
            f.write(test_content)
            
        result = self.processor.process_file(test_file, self.test_dir)
        
        self.assertIsInstance(result, dict)
        self.assertIn("ATOMS", result)
        self.assertIn("BONDS", result)
        self.assertTrue(isinstance(result["ATOMS"], pd.DataFrame))
        self.assertTrue(isinstance(result["BONDS"], pd.DataFrame))

    def test_search(self) -> None:
        # Setup test data
        self.processor.current_data = {
            "ATOMS": pd.DataFrame({
                "Force Field Type": ["H", "C"],
                "Mass": [1.008, 12.01],
                "Comments": ["Hydrogen", "Carbon"]
            })
        }
        
        # Test search functionality
        results = self.processor.search("Hydrogen")
        self.assertIn("ATOMS", results)
        self.assertEqual(len(results["ATOMS"]), 1)
        self.assertEqual(results["ATOMS"].iloc[0]["Force Field Type"], "H")

    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.test_dir)

if __name__ == '__main__':
    unittest.main()
