# test_chordomen.py
"""
Tests for ChordOmen module.
"""

import unittest
from chordomen import ChordOmen

class TestChordOmen(unittest.TestCase):
    """Test cases for ChordOmen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChordOmen()
        self.assertIsInstance(instance, ChordOmen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChordOmen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
