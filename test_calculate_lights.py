import unittest, glob
from main import Calculate_Lights


# initialize an instance of the class
calc = Calculate_Lights()

# get all the files from your local system
file_names = glob.glob('*.txt')
# print(file_names)


class TestCalculateLight(unittest.TestCase):
    """
        Testing for the input file : test.txt
        
        """
    def test_sum_lights_on(self):
        # invoke the function from the Calculate_Lights class
        result = calc.sum_lights_on(file_names[1])
        self.assertEqual(result, 998004)
    
    def test_sum_lights_state(self):
        # file_name = 'test.txt'
        result = calc.sum_lights_state(file_names[1])
        self.assertEqual(result, 1003996)
    
    
        """
        Testing for the input file : coding_challenging_input.txt
        
        """
    def test_sum_lights_on_1(self):
        # invoke the function from the Calculate_Lights class
        result = calc.sum_lights_on(file_names[0])
        # print('RESULT', result)
        self.assertEqual(result, 385705)
        
    
    def test_sum_lights_state_2(self):
        # file_name = 'coding_challenge_input.txt'
        result = calc.sum_lights_state(file_names[0])
        self.assertEqual(result, 1716513)
    

if __name__ == '__main__':
    unittest.main()
    
        