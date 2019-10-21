import unittest
from data_analysis import outlier_val, remove_singleton, stale_val
from pprint import pprint as pp

class dataAnalysis( unittest.TestCase ):

    def test_outlier_val_begin(self):
        data = [ [ '18/10/2017', 1.1 ],
                 [ '17/10/2017', 1.1 ],
                 [ '16/10/2017', 1.1 ],
                 [ '15/10/2017', 1.1 ],
                 [ '14/10/2017', 0   ],
                 [ '13/10/2017', 1.2 ],
                 [ '12/10/2017', 1.2 ], 
                 [ '11/10/2017', 1.2 ],]
        
        clusters = outlier_val( data )
        last_val = clusters[-1]

        # Should contain 3 clusters
        self.assertEqual(last_val[2], 3) 
        # Should have 3 values
        for cluster in clusters:
            self.assertEqual(len(cluster), 3)
    
    def test_outlier_val_middle(self):
        data =  [ [ '13/10/2017', 1.1, ],
                  [ '12/10/2017', 1.1, ],
                  [ '11/10/2017', 1.1, ],  
                  [ '10/10/2017', 2.0, ], # Outlier
                  [ '09/10/2017', 1.2, ],
                  [ '08/10/2017', 1.2, ],
                  [ '07/10/2017', 1.2, ],]
        
        clusters = outlier_val( data )
        
        res = []

        for cluster in clusters:
            if cluster[2] == 2:
                res.append( cluster )
        
        # 1 outlier
        self.assertEqual( len(res), 1 )
        # cluster value 2
        self.assertEqual( res[0][2], 2 )

    def test_remove_singleton_begin(self):
        data =  [ [ '18/10/2017', 1.1, 0 ], #First val Outlier
                  [ '17/10/2017', 1.1, 1 ],
                  [ '16/10/2017', 1.1, 1 ],
                  [ '15/10/2017', 1.1, 1 ],
                  [ '14/10/2017', 0  , 2 ], # Missing
                  [ '13/10/2017', 1.2, 3 ],
                  [ '12/10/2017', 1.2, 3 ], 
                  [ '11/10/2017', 1.2, 3 ],]

        processed = remove_singleton( data )
        outlier = processed[0]
        missing = processed[1]

        self.assertEqual(len(processed), 2)
        self.assertEqual( outlier[2], 'OUTLIER' )
        self.assertEqual( missing[2], 'MISSING' )

    def test_remove_singleton_middle(self):
        data2 = [ [ '13/10/2017', 1.1, 3 ],
                  [ '12/10/2017', 1.1, 3 ],
                  [ '11/10/2017', 1.1, 3 ],  
                  [ '10/10/2017', 2.0, 4 ], # Outlier
                  [ '09/10/2017', 1.2, 5 ],
                  [ '08/10/2017', 1.2, 5 ],
                  [ '07/10/2017', 1.2, 5 ],]
        processed = remove_singleton( data2 )
        outlier = processed[0]
        self.assertEqual(len(processed), 1)
        self.assertEqual(outlier[2], 'OUTLIER')

    def test_stale_val(self):
        data = [ [ '18/10/2017', 1.1 ],
                 [ '17/10/2017', 1.1 ],
                 [ '18/10/2017', 1.1 ],]
        res = stale_val( data )
        self.assertEqual( len(res), 2)

if __name__=="__main__":
    unittest.main()