from unittest import TestCase
from ..build import k_means
from inspect import getfullargspec


class TestK_means(TestCase):
    def test_k_means(self):  # Input parameters tests
        args = getfullargspec(k_means)
        self.assertEqual(len(args[0]), 4, "Expected argument(s) %d, Given %d" % (4, len(args[0])))

    def test_k_means_default(self):  # Input parameters defaults
        args = getfullargspec(k_means)
        self.assertEqual(args[3], (10, 9), "Expected default values do not match given default values")

        # Return type tests
        # Nothing to check here

        # Return value tests
        # Nothing to check here
