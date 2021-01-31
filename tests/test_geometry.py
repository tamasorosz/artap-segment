from unittest import TestCase
from artapsegment.geometry import Geometry
from artapsegment.objects import Node, Line, CubicBezier


class TestGeometry(TestCase):

    def test_initialization(self):
        geo = Geometry()

        self.assertEqual([], geo.nodes)
        self.assertEqual([], geo.lines)
        self.assertEqual([], geo.cubic_beziers)

    def test_add_nodes_and_line(self):

        geo = Geometry()

        a = Node(1.0, 0.0)
        b = Node(0.5, 0.0)

        l = Line(a, b, id=1, label="test")


        geo.add_node(a)
        geo.add_node(b)
        self.assertEqual(a,geo.nodes[0])

        geo.add_line(l)
        self.assertEqual(l,geo.lines[0])

    def test_add_bezier(self):

        geo = Geometry()

        a = Node(1.0, 0.0)
        b = Node(0.5, 0.0)

        l = Line(a, b, id=1, label="test")

        c1 = Node(0.6, 0.1)
        c2 = Node(0.7, 0.2)

        cb = CubicBezier(a, c1, c2, b, id=1, label="test")

        geo.add_node(a)
        geo.add_node(b)
        geo.add_node(c1)
        geo.add_node(c2)

        self.assertEqual(c1,geo.nodes[2])

        geo.add_cubic_bezier(cb)
        self.assertEqual(cb,geo.cubic_beziers[0])

