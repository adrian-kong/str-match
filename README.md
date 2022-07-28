# Gusfield Z-algorithm

![Z alg vs Naive](https://github.com/adrian-kong/z-alg/actions/workflows/ci_test.yml/badge.svg)

FIT3155 week 1

Basically just caching string comparisons, identifying the index such that it can refer from previous computations.

Limitations exist where the bound of the interval exceeds or is equal to that of the previous interval.
If the new string interval isn't fully encapsulated within the old interval, we cannot derive from old calculations.

We use this to compute the Z array which corresponds to the Pattern$String we would like to pattern match on.
