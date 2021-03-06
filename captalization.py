import unittest
import os
import sys

# add srcyr2lat to path so we can test locally
try:
    from srcyr2lat import sr_cyr2lat, CYR_TO_LAT
except ImportError:
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    sys.path.insert(0, ROOT)
    from srcyr2lat import sr_cyr2lat, CYR_TO_LAT


# text from http://www.rastko.rs/knjizevnost/usmena/vkaradzic-price/vkaradzic-price_1.html

class TestCyr2Lat(unittest.TestCase):
    def setUp(self):
        self.src = u'''
Слово иже, али сирца ниже.
Записао калуђер на сирцу (ђе се реже) иже (и): да би познао, ако ђак осијече мало од сирца. Кад калуђер изиђе из собе, онда ђак узме сирац, да осијече мало, а кад види на сирцу иже, онда осијече повелику кришку, па запише опет онако иже, као што је и било. Кад дође калуђер, погледа сирац и узме у руке: "Ва истину слово изе, али сирца низе."'''
        self.src_utf = '''
Слово иже, али сирца ниже.
Записао калуђер на сирцу (ђе се реже) иже (и): да би познао, ако ђак осијече мало од сирца. Кад калуђер изиђе из собе, онда ђак узме сирац, да осијече мало, а кад види на сирцу иже, онда осијече повелику кришку, па запише опет онако иже, као што је и било. Кад дође калуђер, погледа сирац и узме у руке: "Ва истину слово изе, али сирца низе."'''
        self.exp = u'''
Slovo iže, ali sirca niže.
Zapisao kaluđer na sircu (đe se reže) iže (i): da bi poznao, ako đak osiječe malo od sirca. Kad kaluđer iziđe iz sobe, onda đak uzme sirac, da osiječe malo, a kad vidi na sircu iže, onda osiječe poveliku krišku, pa zapiše opet onako iže, kao što je i bilo. Kad dođe kaluđer, pogleda sirac i uzme u ruke: "Va istinu slovo ize, ali sirca nize."'''

    def test_unicode(self):
        self.assertEqual(sr_cyr2lat(self.src), self.exp)

    def test_utf(self):
        self.assertEqual(sr_cyr2lat(self.src_utf), self.exp)

    def test_upper_case(self):
        src = u"ЊЕГОШ није Његош"
        exp = u'NJEGOŠ nije Njegoš'
        self.assertEqual(sr_cyr2lat(src), exp)

    def test_single(self):
        src = u"Њ ЕГОШ није Његош"
        exp = u'NJ EGOŠ nije Njegoš'
        self.assertEqual(sr_cyr2lat(src), exp)
        src = u"њ ЕГОШ није Његош"
        exp = u'nj EGOŠ nije Njegoš'
        self.assertEqual(sr_cyr2lat(src), exp)

    def test_title_case(self):
        src = u"Његош није Његош"
        exp = u'Njegoš nije Njegoš'
        self.assertEqual(sr_cyr2lat(src), exp)

    def test_inv_case(self):
        src = u"ЊеГОШ није Његош"
        exp = u'NjeGOŠ nije Njegoš'
        self.assertEqual(sr_cyr2lat(src), exp)

if __name__ == '__main__':
    unittest.main()
