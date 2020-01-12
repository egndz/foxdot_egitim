
Pattern Functions

There are several functions that generate a Pattern of values for us for achieving useful things in FoxDot, such as rhythms and melodies. This page is a list of Pattern functions accompanied by descriptions and examples.

Used as input arguments for Foxdot players, these can be treated as patterns themselves and their methods can be applied directly e.g. PDur(3, 8).reverse(). You can also substitute any input argument with a Pattern or TimeVar to create an extended pattern or Pvar. Let’s look at some examples:
1
2
3
4
5
6
7
8
9
10
11
12
	
>>> # Basic pattern function
>>> PDur(3, 8)
P[0.75, 0.75, 0.5]
 
>>> # Use a list/Pattern to join together two patterns using the same function
>>> PDur([3, 2], [8, 4])
P[0.75, 0.75, 0.5, 0.5, 0.5]
 
>>> # Use a TimeVar to create a Pvar
>>> PDur(var([3, 5]), 8)
P[0.75, 0.75, 0.5]             # Equal to PDur(3,8)
P[0.5, 0.25, 0.5, 0.25, 0.5]   # Equal to PDur(5,8) after 4 beats
PStep(n, value, default=0)

Creates a Pattern of length n with the last element set to value. All other values are set to default.
1
2
3
4
	
>>> PStep(5, 4)
P[0, 0, 0, 0, 4]
>>> PStep(4, "o", "x")
P["x", "x", "x", "o"]
PSum(n, total, lim=0.125)

Returns a Pattern of length n whose sum is equal to total and each value is roughly equal. All values are divisible by lim, which is also the smallest possible value for each element.
1
2
3
4
	
>>> PSum(5, 4)
P[1.0, 0.75, 0.75, 0.75, 0.75]
>>> PSum(3, 2)
P[0.75, 0.75, 0.5]
PRange(start, stop=None, step=None)

Returns a Pattern filled with the series from start to stop (non inclusive) with increments of step (defaults to 1). If stop is omitted then the series starts at 0 and ends at start.
1
2
3
4
5
6
	
>>> PRange(5)
P[0, 1, 2, 3, 4]
>>> PRange(2, 7)
P[2, 3, 4, 5, 6]
>>> PRange(4, 14, 2)
P[4, 6, 8, 10, 12]
PTri(start, stop=None, step=None)

Returns a Pattern filled with the series from start to stop and back again (non inclusive) with increments of step (defaults to 1). If stop is omitted then the series starts at 0 and peaks at start.
1
2
3
4
5
6
	
>>> PTri(5)
P[0, 1, 2, 3, 4, 3, 2, 1]
>>> PTri(2, 7)
P[2, 3, 4, 5, 6, 5, 4, 3]
>>> PTri(4, 14, 2)
P[4, 6, 8, 10, 12, 10, 8, 6]
PSine(n=16)

Returns a Pattern with n values taken from a basic sine wave function equal distances apart.
1
2
	
>>> PSine(16)
P[0.0, 0.3826834323650898, 0.7071067811865476, 0.9238795325112867, 1.0, 0.9238795325112867, 0.7071067811865476, 0.3826834323650899, 1.2246467991473532e-16, -0.38268343236508967, -0.7071067811865475, -0.9238795325112865, -1.0, -0.9238795325112866, -0.7071067811865477, -0.3826834323650904]
PEuclid(n, k)

Uses the Euclidean Algorithm to create a Pattern of length k with n number of pulses spread as equally as possible throughout the set. Pulses are represented as a 1.
1
2
	
>>> PEuclid(3, 8)
P[1, 0, 0, 1, 0, 0, 1, 0]
PEuclid2(n, k, lo, hi)

Same function as PEuclid but replaces the 1’s with hi and 0’s with lo.
1
2
	
>>> PEuclid2(3, 8, "x", "o")
P["o", "x", "x", "o", "x", "x", "o", "x"]
PDur(n, k, start=0, dur=0.25)

Returns the output of PEuclid as a series of durations where each element is a step of duration dur. The start keyword specifies the starting index of the Pattern.
1
2
3
4
5
6
	
>>> PDur(3, 8)
P[0.75, 0.75, 0.5]
>>> PDur(3, 8, 1)
P[0.75, 0.5, 0.75]
>>> PDur(3, 8, 1, 0.5)
P[1.5, 1.0, 1.5]
PBern(size=16, ratio=0.5)

Returns a Pattern of length size filled with a random selection of 1s and 0s based on the ratio value, known as a Bernoulli Sequence.
1
2
3
4
	
>>> PBern(6)
P[1, 0, 0, 1, 1, 0]
>>> PBern(6, 0.75)
P[0, 1, 1, 1, 1, 0]
PBeat(string, start=0, dur=0.5)

Returns a Pattern of durations based on an input string where non-whitespace denote a pulse.
1
2
3
4
	
>>> PBeat("x xxx x")
P[1, 0.5, 0.5, 1, 0.5]
>>> PBeat("x xxx x", start=1, dur=1/4)
P[0.25, 0.25, 0.5, 0.25, 0.5]
PSq(a=1, b=2, c=3)

Returns a Pattern of square numbers in the range a to (a + c) - 1.
1
2
3
4
	
>>> PSq(1, 2, 3)
P[1, 4, 9]
>>> PSq(2, 2, 5)
P[4, 9, 16, 25, 36]
