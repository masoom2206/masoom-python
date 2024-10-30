import unittest
import mainProgram

class TestMain(unittest.TestCase):
  def setUp(self):
    print("Testing function:", self._testMethodName)
  def test_do_stuff(self):
    test_param = 10
    result = mainProgram.do_stuff(test_param)
    self.assertEqual(result, 15)# Pass
    # self.assertEqual(result, 20)# Failed

  #check the try/except error is working or not.
  def test_do_stuff2(self):
    test_param = "Masoom"
    result = mainProgram.do_stuff(test_param)
    # self.assertTrue(isinstance(result, ValueError))# Pass
    self.assertIsInstance(result, ValueError)# Pass

  def test_do_stuff3(self):
    test_param = None
    result = mainProgram.do_stuff(test_param)
    # self.assertTrue(isinstance(result, ValueError))# Pass
    self.assertEqual(result, "Please enter a number")# Pass

  def test_do_stuff4(self):
    test_param = ""
    result = mainProgram.do_stuff(test_param)
    # self.assertTrue(isinstance(result, ValueError))# Pass
    self.assertEqual(result, "Please enter a number")# Pass

  def test_do_stuff5(self):
    test_param = 0
    result = mainProgram.do_stuff(test_param)
    # self.assertTrue(isinstance(result, ValueError))# Pass
    self.assertEqual(result, "Please enter the number greater than zero(0)")# Pass

  def test_do_stuff_multiply(self):
    test_param = 10
    result = mainProgram.do_stuff_multiply(test_param)
    self.assertEqual(result, 100)# Pass

  def test_do_stuff_true(self):
    result = mainProgram.do_stuff_true()
    self.assertTrue(result)# Pass

  def tearDown(self):
    print("Cleaning up...")

if __name__ == '__main__':
  unittest.main()