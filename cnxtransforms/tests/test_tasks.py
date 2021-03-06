import unittest

EPUB = None
CALLBACK = None

class MakeEpub(unittest.TestCase):
    @property
    def target(self):
        from ..tasks import make_epub
        return make_epub
    
    def test_target(self):
        with self.assertRaises(NotImplementedError):
            self.target(EPUB,CALLBACK)


class MakePDF(unittest.TestCase):
    @property
    def target(self):
        from ..tasks import make_pdf
        return make_pdf
    
    def test_target(self):
        with self.assertRaises(NotImplementedError):
            self.target(EPUB,CALLBACK)

class MakeZip(unittest.TestCase):
    @property
    def target(self):
        from ..tasks import make_zip
        return make_zip
    
    def test_target(self):
        with self.assertRaises(NotImplementedError):
            self.target(EPUB,CALLBACK)

