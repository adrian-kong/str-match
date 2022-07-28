import unittest
from z_alg import z_alg
from naive import naive


class ZTable(unittest.TestCase):

    def setUp(self) -> None:
        self.texts = []
        with open("test_texts.txt") as f:
            for i in f:
                if not i.startswith("#"):
                    self.texts.append(i)

    def test_z_alg_vs_naive(self):
        """
        Naive quadratic algorithm vs linear Z algorithm
        :return: Assertion test for correctness
        """

        for text in self.texts:
            naive_z, naive_comps = naive(text)
            gusfield_z, gusfield_comps = z_alg(text)
            print(f"naive = {naive_z}, z_alg = {gusfield_z}")
            self.assertEqual(gusfield_z, naive_z, f"error comparing {text}")
            self.assertGreaterEqual(naive_z, gusfield_z)


if __name__ == '__main__':
    unittest.main()
