from unittest import TestCase
from artap_segment.objects import Node

class TestNodeOperations(TestCase):

    def test_node_init(self):
        self.assertEqual( (1., 1.),Node(1., 1.).as_tuple())