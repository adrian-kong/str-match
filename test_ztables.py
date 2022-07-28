import pytest
from z_alg import z_alg
from naive import naive
import random

STRING_SIZE = 1000
POSSIBLE_CHARS = ['a', 'b', 'c']


@pytest.mark.parametrize('execution_number', range(1_000))
def test_z_alg_vs_naive(execution_number):
    """
    Naive quadratic algorithm vs linear Z algorithm
    :return: Assertion test for correctness and comparisons
    """

    # Create randomized test string
    text = "".join([random.choice(POSSIBLE_CHARS) for _ in range(STRING_SIZE)])

    # Compute
    naive_z, naive_comps = naive(text)
    gusfield_z, gusfield_comps = z_alg(text)
    print(f"naive = {naive_z}, z_alg = {gusfield_z}")
    assert gusfield_z == naive_z
    assert naive_z >= gusfield_z
