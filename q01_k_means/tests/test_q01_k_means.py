from unittest import TestCase
from ..build import k_means
from inspect import getfullargspec


class TestK_means(TestCase):
    def test_k_means(self):

        # Input parameters tests
        args = getfullargspec(k_means).args
        args_default = getfullargspec(k_means).defaults
        self.assertEqual(len(args), 4, "Expected argument(s) %d, Given %d" % (4, len(args)))
        self.assertEqual(args_default, (10, 9), "Expected default values do not match given default values")

        # Return type tests
        # Nothing to check here

        # Return value tests
        # Nothing to check here
