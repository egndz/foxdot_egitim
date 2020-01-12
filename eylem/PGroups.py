
PGroups
Basics

Where Patterns are a list of values that are played in sequence, PGroups are groups of values that are played at the same time. Whenever you use a tuple in a Player or a Pattern, it is automatically converted into a PGroup, which, like Patterns, are denoted by the upper-case ‘P’ at its start:
1
2
	
>>> print(P[0, 1, 2, (3, 4, 5)])
P[0, 1, 2, P(3, 4, 5)]

Many Pattern methods can also be applied to PGroups, such as mirror and shuffle. This relationship also extends to ‘lacing’ PGroups; using a list or a Pattern as a value in a PGroup will create a Pattern of PGroups using the sequence of values in turn like so:
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
	
# Lacing a PGroup
>>> print(P(0, 1, [2, 3]))
P[P(0, 1, 2), P(0, 1, 3)]
 
# Lacing a PGroup within a Pattern
>>> print(P[0, 1, P(2, 3, [4, 5])])
P[0, 1, P[P(2, 3, 4), P(2, 3, 5)]]
 
# Lacing a PGroup with multiple lists
>>> print(P(0, [1, 2], [3, 4, 5]))
P[P(0, 1, 3), P(0, 2, 4), P(0, 1, 5), P(0, 2, 3), P(0, 1, 4), P(0, 2, 5)]
Extended PGroups

The are also knows as “PGroup Prime”. By inserting a mathematical operator, such as ‘+’, will activate a type of behaviour when used with in a Player. These usually change the notes from being played simultaneously to spreading them over a period of time. Here are a list of extended PGroups and some example code:
P*(x, y, z, ...)

PGroup-Star: will play the contents of the PGroup spread equally over the Player’s current dur value.
1
2
3
4
5
	
# Plays 3 notes over 2 beats at 2/3 beats duration each
p1 >> pluck(P*(0, 2, 4), dur=2)
 
# Plays the notes in opposite stereo channel every 4 note
p1 >> pluck(dur=1/2, pan=PStep(4, P*(-1, 1)))
P+(x, y, z, ...)

PGroup-Plus: will play the contents of the PGroup spread equally over the Player’s current sus value, regardless of the dur.
1
2
3
4
5
	
# Play 4 notes over a 1 beat sustain
p1 >> pluck(P+(0, 2, 4, 6), dur=PDur(3,8), sus=1)
 
# Vary the sustain to hear the difference
p1 >> pluck([0, 2, P+(0, 2, 4)], dur=PDur(3,8)*2, sus=var([0.75, 1.5, 3]))
P**(x, y, z, ...)

PGroup-DoubleStar: Same as PGroup-Star but randomises the order notes are played in.
1
2
	
# Arpeggiate the chord in a random order
p1 >> pluck(P[0, 1, 2, P**(3, 5, 7, 9)])
P/(x, y, z, ...)

PGroup-Div. Same as PGroup-Start but only delays the notes every other time the group is played.
1
2
	
# Arpeggiate the chord every other loop
p1 >> pluck(P[0, 1, 2, P/(3, 5, 7, 9)])
P^(x, y, z, ..., dur)

PGroup-Pow: Uses the last value of the PGroup to set the delay between each note instead of using a Player’s dur or sus value.
1
2
	
# Force delay of 0.5 beats per note
p1 >> pluck([0, 2, P^(3, 5, 7, 0.5)], dur=1, sus=4)
