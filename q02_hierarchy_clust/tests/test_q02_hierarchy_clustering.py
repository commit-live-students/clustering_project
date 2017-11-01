from unittest import TestCase
from ..build import hierarchy_clustering
from inspect import getargspec


class TestHierarchy_clustering(TestCase):
    def test_hierarchy_clustering(self):

        # Input parameters tests
        args = getargspec(hierarchy_clustering)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return type tests
        # Nothing to check here

        # Return value tests
        # Nothing to check here
