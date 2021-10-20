import unittest
import tinhtiendien

# test case phương pháp phân hoạch tương đương
class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        assert(tinhtiendien.caculatePrice('sinh hoat',-1) == 'input error')
        print('output 1:',tinhtiendien.caculatePrice('sinh hoat', -1))
        
    def test_case_2(self):       
        assert(tinhtiendien.caculatePrice('sinh hoat',25) == 37500)
        print('output 2: ', tinhtiendien.caculatePrice('sinh hoat', 25))
    
    def test_case_3(self):       
        assert(tinhtiendien.caculatePrice('sinh hoat',125) == 250000)
        print('output 3: ', tinhtiendien.caculatePrice('sinh hoat', 125))
    
    def test_case_4(self):       
        assert(tinhtiendien.caculatePrice('sinh hoat',250) == 625000)
        print('output 4: ',tinhtiendien.caculatePrice('sinh hoat', 250))

    def test_case_5(self):      
        assert(tinhtiendien.caculatePrice('sinh hoat',500) == 1750000)
        print('output 5: ', tinhtiendien.caculatePrice('sinh hoat', 500))

    def test_case_6(self):        
        assert(tinhtiendien.caculatePrice('kinh doanh',-10) == 'input error')
        print('output 6: ', tinhtiendien.caculatePrice('kinh doanh', -10))

    def test_case_7(self):        
        assert(tinhtiendien.caculatePrice('kinh doanh',60) == 108000)
        print('output 7: ', tinhtiendien.caculatePrice('kinh doanh', 60))

    def test_case_8(self):        
        assert(tinhtiendien.caculatePrice('kinh doanh',250) == 600000)
        print('output 8: ', tinhtiendien.caculatePrice('kinh doanh', 250))

    def test_case_9(self):       
        assert(tinhtiendien.caculatePrice('kinh doanh',380) == 1178000)
        print('output 9: ', tinhtiendien.caculatePrice('kinh doanh', 380))
    
    def test_case_10(self):        
        assert(tinhtiendien.caculatePrice('kinh doanh',600) == 1980000)
        print('output 10: ', tinhtiendien.caculatePrice('kinh doanh', 600))

    def test_case_11(self):
        print('output 11: ', tinhtiendien.caculatePrice('sinh hoat', 200))
        assert(tinhtiendien.caculatePrice('sinh hoat', 200) == 500000)
        


if __name__ == '__main__':
    unittest.main()
