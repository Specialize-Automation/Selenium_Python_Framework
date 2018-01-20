from unittest import TestLoader, TestSuite, TextTestRunner
from WebAutomation.Test.Scripts.test_MercuryTours_HomePage import MercuryTours_HomePage
from WebAutomation.Test.Scripts.test_MercuryTours_Registration import MercuryTours_Registration
from WebAutomation.Test.Scripts.test_MercuryTours_SignOn import MercuryTours_SignOn

import testtools as testtools


if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(MercuryTours_HomePage),
        loader.loadTestsFromTestCase(MercuryTours_SignOn),
        loader.loadTestsFromTestCase(MercuryTours_Registration)
        ))

#run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)


# #run test parallel using concurrent_suite
    concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    concurrent_suite.run(testtools.StreamResult())