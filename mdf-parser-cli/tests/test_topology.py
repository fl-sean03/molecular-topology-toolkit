import unittest
from parser.topology import extract_topology

class TestTopology(unittest.TestCase):
    def setUp(self):
        self.sample_atoms = {
            "1": {"charge_group": 1, "neighbors": ["2", "3"]},
            "2": {"charge_group": 2, "neighbors": ["1", "3"]},
            "3": {"charge_group": 3, "neighbors": ["1", "2"]}
        }

    def test_extract_topology(self):
        bonds, angles, dihedrals = extract_topology(self.sample_atoms)
        
        # Test bonds
        self.assertIsInstance(bonds, set)
        self.assertEqual(len(bonds), 3)
        
        # Test angles
        self.assertIsInstance(angles, set)
        self.assertEqual(len(angles), 3)
        
        # Test dihedrals
        self.assertIsInstance(dihedrals, set)

if __name__ == '__main__':
    unittest.main()
