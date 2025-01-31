# test_charmm_parser.py - Unit tests for CHARMM parser

import unittest
from tools.charmm_parser.parser import CharmmProcessor
from tools.charmm_parser.parsers import parse_charmm_parameter_file

class TestCharmmParser(unittest.TestCase):
    def setUp(self):
        self.processor = CharmmProcessor()
        
    def test_process_file(self):
        pass

    def test_search(self):
        pass

if __name__ == '__main__':
    unittest.main()
