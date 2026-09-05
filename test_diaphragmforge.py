# test_diaphragmforge.py
"""
Tests for DiaphragmForge module.
"""

import unittest
from diaphragmforge import DiaphragmForge

class TestDiaphragmForge(unittest.TestCase):
    """Test cases for DiaphragmForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DiaphragmForge()
        self.assertIsInstance(instance, DiaphragmForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DiaphragmForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
