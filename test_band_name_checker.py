import unittest

from band_name_checker import canonicalize, create_domains, lookup_domain, process_name


class MyTestCase(unittest.TestCase):
    def test_canonicalize(self):
        name = "this is a big ol' honkin' test"
        expected = "thisisabigolhonkintest"

        self.assertEqual(canonicalize(name), expected)

    def test_create_domains(self):
        name = "this is a big ol' honkin' test"
        expected = ["thisisabigolhonkintest.com",
                    "thisisabigolhonkintest.net",
                    "thisisabigolhonkintestband.com",
                    "thisisabigolhonkintestband.net"]

        self.assertEqual(create_domains(name), expected)

    def test_create_domains_with_domain_passed_in(self):
        names = ["testing123.com", "foobarbaz.net"]
        raw_results = map(create_domains, names)
        results = [list[0] for list in raw_results]

        self.assertEqual(results, names)

    def test_lookup_domain(self):
        name = "joeygibson.com"
        domain, result = lookup_domain(name)

        self.assertEqual(name, domain)
        self.assertEqual(name, result['domain_name'].lower())

    def test_process_name(self):
        name = "joey gibson"
        # expected = []
        results = process_name(name)

        print(list(results))



if __name__ == '__main__':
    unittest.main()
