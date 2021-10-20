import unittest
import tinhtiendien

# test case phương pháp bảng quyết định
class MyTestCase(unittest.TestCase):

    def test_case_1(self):
        print('output 1:',tinhtiendien.caculatePrice('sinh hoat', -1))
        assert(tinhtiendien.caculatePrice('sinh hoat',-1) == 'input error')
        
    def test_case_2(self):
        print('output 2:',tinhtiendien.caculatePrice('sinh hoat', 30))
        assert(tinhtiendien.caculatePrice('sinh hoat',30) == 45000)
    
    def test_case_3(self):
        print('output 3:',tinhtiendien.caculatePrice('sinh hoat', 160))
        assert(tinhtiendien.caculatePrice('sinh hoat',160) == 320000)
    
    def test_case_4(self):
        print('output 4:',tinhtiendien.caculatePrice('sinh hoat', 320))
        assert(tinhtiendien.caculatePrice('sinh hoat',320) == 800000)

    def test_case_5(self):
        print('output 5:',tinhtiendien.caculatePrice('sinh hoat', 600))
        assert(tinhtiendien.caculatePrice('sinh hoat',600) == 2100000)

    def test_case_6(self):        
        assert(tinhtiendien.caculatePrice('kinh doanh',-10) == 'input error')
        print('output 6: ', tinhtiendien.caculatePrice('kinh doanh', -10))

    def test_case_7(self):        
        assert(tinhtiendien.caculatePrice('kinh doanh',85) == 153000)
        print('output 7: ', tinhtiendien.caculatePrice('kinh doanh', 85))

    def test_case_8(self):        
        assert(tinhtiendien.caculatePrice('kinh doanh',270) == 648000)
        print('output 8: ', tinhtiendien.caculatePrice('kinh doanh', 270))

    def test_case_9(self):       
        assert(tinhtiendien.caculatePrice('kinh doanh',385) == 1193500)
        print('output 9: ', tinhtiendien.caculatePrice('kinh doanh', 385))
    
    def test_case_10(self):        
        assert(tinhtiendien.caculatePrice('kinh doanh',675) == 2227500)
        print('output 10: ', tinhtiendien.caculatePrice('kinh doanh', 675))

    def test_case_11(self):
            print('output 11: ', tinhtiendien.caculatePrice('sinh hoat', 200))
            assert(tinhtiendien.caculatePrice('sinh hoat', 200) == 500000)
    
        


if __name__ == '__main__':
    unittest.main()
