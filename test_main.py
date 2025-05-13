import unittest
from main import dfa_equivalence, cyk

class TestAutomata(unittest.TestCase):

    
    # DFA Tests :
    
    def test_dfa_equivalence_true(self):
        dfa1 = {
            'alphabet': ['0', '1'],
            'start': 'q0',
            'accept': ['q1'],
            'transition': {
                'q0': {'0': 'q0', '1': 'q1'},
                'q1': {'0': 'q0', '1': 'q1'}
            }
        }
        dfa2 = {
            'alphabet': ['0', '1'],
            'start': 's0',
            'accept': ['s1'],
            'transition': {
                's0': {'0': 's0', '1': 's1'},
                's1': {'0': 's0', '1': 's1'}
            }
        }
        self.assertTrue(dfa_equivalence(dfa1, dfa2), "Equivalent DFAs failed the test")

    def test_dfa_equivalence_false(self):
        dfa1 = {
            'alphabet': ['0', '1'],
            'start': 'q0',
            'accept': ['q1'],
            'transition': {
                'q0': {'0': 'q0', '1': 'q1'},
                'q1': {'0': 'q1', '1': 'q1'}
            }
        }
        dfa2 = {
            'alphabet': ['0', '1'],
            'start': 's0',
            'accept': ['s0'],
            'transition': {
                's0': {'0': 's0', '1': 's1'},
                's1': {'0': 's0', '1': 's1'}
            }
        }
        self.assertFalse(dfa_equivalence(dfa1, dfa2), "Non-equivalent DFAs passed incorrectly")

    def test_dfa_empty_language(self):
        dfa1 = {
            'alphabet': ['0'],
            'start': 'q0',
            'accept': [],
            'transition': {
                'q0': {'0': 'q0'}
            }
        }
        dfa2 = {
            'alphabet': ['0'],
            'start': 's0',
            'accept': [],
            'transition': {
                's0': {'0': 's0'}
            }
        }
        self.assertTrue(dfa_equivalence(dfa1, dfa2), "Empty-language DFAs should be equivalent")

    
    
    # CYK Tests :

    def test_cyk_valid(self):
        cfg = {
            'S': ['AB', 'BC'],
            'A': ['BA', 'a'],
            'B': ['CC', 'b'],
            'C': ['AB', 'a']
        }
        self.assertTrue(cyk(cfg, "ba"), "Valid string failed CYK")

    def test_cyk_invalid(self):
        cfg = {
            'S': ['AB'],
            'A': ['a'],
            'B': ['b']
        }
        self.assertFalse(cyk(cfg, "aaa"), "Invalid string passed CYK")

    def test_cyk_empty_string_valid(self):
        cfg = {
            'S': ['ε']
        }
        self.assertTrue(cyk(cfg, ""), "Empty string should be accepted if ε in CFG")

    def test_cyk_empty_string_invalid(self):
        cfg = {
            'S': ['AB'],
            'A': ['a'],
            'B': ['b']
        }
        self.assertFalse(cyk(cfg, ""), "Empty string incorrectly accepted")

    def test_cyk_longer_valid_string(self):
        cfg = {
            'S': ['AB'],
            'A': ['a'],
            'B': ['BC', 'b'],
            'C': ['c']
        }
        self.assertTrue(cyk(cfg, "abc"), "Valid long string failed CYK")

if __name__ == "__main__":
    unittest.main()
