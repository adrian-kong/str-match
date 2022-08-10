import pytest

from boyer import boyer_moore
from gusfield import z_alg
from naive import naive
import random

STRING_SIZE = 1000
POSSIBLE_CHARS = ['a', 'b', 'c']


@pytest.mark.parametrize('execution_number', range(1_000))
def test_ztable_against_naive(execution_number):
    """
    Naive quadratic algorithm vs linear Z algorithm
    :return: Assertion test for correctness and comparisons
    """

    # Create randomized test string
    text = "".join([random.choice(POSSIBLE_CHARS) for _ in range(STRING_SIZE)])

    # Compute
    naive_z = naive(text)
    gusfield_z = z_alg(text)
    print(f"naive = {naive_z}, z_alg = {gusfield_z}")
    assert gusfield_z == naive_z


@pytest.mark.parametrize('execution_number', range(1_000))
def test_boyer_against_index(execution_number):
    """
    Verify boyer moore correctness
    :return: Assertion test for correctness and comparisons
    """

    # Create randomized test string
    text = "".join([random.choice(POSSIBLE_CHARS) for _ in range(STRING_SIZE)])
    pat = "".join([random.choice(POSSIBLE_CHARS) for _ in range(5)])

    # Compute
    if pat in text:
        true_index = text.index(pat)
        boyer_index = boyer_moore(text, pat)
        print(f"true = {true_index}, boyer = {boyer_index}")
        assert boyer_index == true_index
    else:
        print(f"true = None, boyer = None")
        assert boyer_moore(text, pat) is None
