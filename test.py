import unittest
import tests.Menu_unittest as Menu_test

if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = [
        loader.loadTestsFromModule(Menu_test)
    ]
    suite = unittest.TestSuite()
    suite.addTests(tests)
    
    runner = unittest.TextTestRunner(verbosity=3)
    results = runner.run(suite)