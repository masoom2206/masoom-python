import unittest
import gameProgram

class TestGame(unittest.TestCase):
  def setUp(self):
    print("Testing function:", self._testMethodName)
  
  def test_input(self):
    result = gameProgram.runGame(5, 5)
    self.assertTrue(result)

  def test_input_wrong_guess(self):
    result = gameProgram.runGame(0, 5)
    self.assertFalse(result)

  def test_input_wrong_number(self):
    result = gameProgram.runGame(11, 5)
    self.assertFalse(result)

  def test_input_wrong_type(self):
    result = gameProgram.runGame('11', 5)
    self.assertFalse(result)


  def tearDown(self):
    print("Cleaning up...")

if __name__ == '__main__':
  unittest.main()