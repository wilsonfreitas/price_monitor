# coding:utf-8

# Lib imports
import unittest
import api_connection as api_conn

# ------------------------------------------------------------------------------
class Test_api_connection(unittest.TestCase):
    
    def setUp(self):
        self.url_test = 'http://produto.mercadolivre.com.br/MLB-520190799-playstation-3-super-slim-12gb-hdmi-bivolt-3d-blu-ray-_JM'
        self.api_url_conn = api_conn.public_api_connection(self.url_test)
        
    def test_connection(self):
        self.assertEqual(self.api_url_conn.item_url,self.url_test)
        self.assertEqual(self.api_url_conn.base_api,'https://api.mercadolibre.com/')
        self.assertEqual(self.api_url_conn.item_id,'MLB520190799')
        self.assertEqual(self.api_url_conn.site,'MLB')
        self.assertEqual(self.api_url_conn.item_api_url,'https://api.mercadolibre.com/items/MLB520190799')
        self.assertEqual(self.api_url_conn.public_resources,
            ['users','sites','categories','countries','states',
            'cities','currencies','currency_conversions','items','pictures']
        )
        
    def test_read(self):
        ret = self.api_url_conn.read('https://api.mercadolibre.com/items/MLB520190799')
        self.assertNotEqual(ret, None)
        
    def test_product_id(self):
        ret = self.api_url_conn.product_id(self.url_test)
        self.assertEqual(ret,'MLB520190799')
        
        
if __name__ == '__main__':
	unittest.main()
'''
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_api_connection)
	unittest.TextTestRunner(verbosity=2).run(suite)
#'''