import lexicalbinary as lb
import unittest


class LexicalBinaryTests(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(lb.dumps(0), b'%\x00')
        self.assertEqual(lb.dumps(123), b'%{')
        self.assertEqual(lb.dumps(1000), b'%\x87h')
        self.assertEqual(lb.dumps(-1234567), b'$4R\xf9')

    def test_floats(self):
        self.assertEqual(lb.dumps(0.0), b'#\x80\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(lb.dumps(-0.0), b'#\x7f\xff\xff\xff\xff\xff\xff\xff')
        self.assertEqual(lb.dumps(99.10247), b'#\xc0X\xc6\x8e\xdeT\xb4\x8d')

    def test_string_and_bytes(self):
        self.assertEqual(lb.dumps(b''), b' \x00')
        self.assertEqual(lb.dumps(u''), b'"\x00')
        self.assertEqual(lb.dumps(b'hello'), b' \xb4\x99\xad\xc6\xe3\xbc\x00')
        self.assertEqual(lb.dumps(u'hello'), b'"ifmmp\x00')

    def test_list(self):
        self.assertEqual(lb.dumps([1, b'yes', True, [1]]), b'!%\x01 \xbc\xd9\xae\xb0\x00\x12!%\x01\x01\x01')


if __name__ == '__main__':
    unittest.main()
