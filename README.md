# String matching

![Test](https://github.com/adrian-kong/z-alg/actions/workflows/ci_test.yml/badge.svg)

FIT3155 week 1 + 2

## Z table

```
move the txt index left or right and compare to original string one by one.
doing this naively:

let txt=aaaaa
aaaaa txt
 aaaa 4 first loop
  aaa 3 ...
   aa 2 ...
    a 1 ...

skip first index as it will always be the entire pattern so we get:
z table = [4,3,2,1]

let txt=abaab
abaab txt
 abaa 0 first loop
  aba 1 ...
   ab 2 ...
    a 0 ...

z table = [0,1,2,0]
```

## Gusfield

Basically just caching string comparisons, identifying the index such that it can refer from previous computations.

Limitations exist where the bound of the interval exceeds or is equal to that of the previous interval.
If the new string interval isn't fully encapsulated within the old interval, we cannot derive from old calculations.

We use this to compute the Z array which corresponds to the Pattern$String we would like to pattern match on.

```
gusfield will allow skips in z table i.e.

let txt=aabaaaab
a a b a a a a b         txt
 [a]a               1 first loop
    a               0
     [a a]b         2
     [ [a]a]b       2 using bound from last loop => only need to check out of bound chars    
       [ [a]a b]    3 same as above

left most   [ = old l_tmp bound
inner       ] = old r_tmp bound
inner       [ = new l_tmp bound
right most  ] = new r_tmp bound
```


## Boyer Moore

Rather than checking left to right, we begin by comparing the rightmost value of the pattern and moving leftwards.

Preprocess on pattern

If there is a mismatch, will jump the entire pattern rightwards such that the mismatch character is the next along the pattern
```
skip on mismatch logic:

txt="abcEabcFabc"
pat="abcFabc"
        xooo
mismatch on E,
attempt to find E in pat, => does not exist so we skip the unchecked portion of pat

txt="abcEabcFabc"
pat="    abcFabc" => spaces are the skipped chars
         ooooooo
since we don't have a 2D array to store all previous chars in pattern when we preprocess it,
we can only use on the ones before the index we are checking otherwise we can only skip by 1
```

```
skip on matched patterns

if we have
txt="abcEabcFabc"
pat="abcFabc"
        xooo

can see abc is already matched, and we also know there exists abc in the pattern,
can reuse this logic to form good suffix splits, 
perform preprocessing on the string, create Z-table (reversed so right to left)

we get z table:
003000

compute good suffix by iterating over Z array
gs[|pat| - z] = i
since |pat| - z would be the position of the matched suffix
store i-th index as the position of the matched suffix
override with biggest i-th values (would be the safest/smallest jump)

i.e. we get from that z table:
00002005
checking kth character, k+1 would correspond to the position of suffix in pat
```