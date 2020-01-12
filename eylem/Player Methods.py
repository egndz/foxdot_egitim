
Player Methods

As well as manipulating your players by changing their attributes, you can also use methods to change their behaviours. Some methods just apply a “preset” to specific attributes in order to save typing time. For example, the method spread is equivalent to setting a player’s pan to both left and right and offsetting the the pitch, using the pshift attribute, off by 0.125 semitones in each channel:

# Spreading a sound across stereo channels out of phase
d1 >> play("x-o-", pan=(-1, 1), pshift=(0, 0.125))

# This can be done using the "spread" method
d1 >> play("x-o-").spread()

# Instructions are interpreted left-to-right so spread overrides the "pan=[-1, 0, 1]"
d1 >> play("x-o-", pan=[-1, 0, 1]).spread()

# Using "spread" *before* the >> will set panning to [-1, 0, 1] but pshift will still be (0, 0.125)
d1.spread() >> play("x-o-", pan=[-1, 0, 1])

Below is a list of methods that can be used with accompanying example code. This list is incomplete so please bear with me while I update this list with more information.
Class methods
get_attributes()

Returns a list of the possible player attributes that can be changed.

>>> print(Player.get_attributes())
('degree', 'oct', 'freq', 'dur', 'delay', 'blur', 'amplify', 'scale', 'bpm', 'sample', 'sus', 'fmod', 'pan', 'rate', 'amp', 'vib', 'vibdepth', 'slide', 'sus', 'slidedelay', 'slidefrom', 'bend', 'benddelay', 'coarse', 'striate', 'buf', 'rate', 'pshift', 'hpf', 'hpr', 'lpf', 'lpr', 'chop', 'echo', 'decay', 'spin', 'cut', 'room', 'mix', 'formant', 'shape')

help()

Prints the Player class’s docstring to the console.

>>> Player.help()
"FoxDot generates music by creating instances of `Player` and giving them instructions to follow..."

“Magic” methods
__init__(name=None)

Initialises a new player object that you can assign instructions. You can give it a name so that it is easier to identify it when printing the contents of the scheduling clock, for example.

>>> # Creates a new player (name can be different to the variable name)
>>> foo = Player("bar")
>>> foo >> pluck()
>>> # Print contents of clock
>>> print(Clock.playing)
['']

__repr__()

Returns the string representation of the player (called when using print to display information in the console). If it has been given a name it will return the name followed by the synthdef being used. If not it will return information only about the synthdef.

>>> # With a name
>>> p1 = Player("p1")
>>> p1 >> pads()
>>> print(p1)
""
>>> # Without a name
>>> p1 = Player()
>>> p1 >> pads()
>>> print(p1)
"A 'pluck' Player Object

__add__(value)

This adds value to the degree of the Player. If it is using the play synthdef, the value is added to the sample attribute instead.

# The two lines are equivalent
p1 >> pads(P[0, 1, 2, 3] + (0, 4))
p1 >> pads(P[0, 1, 2, 3]) + (0, 4)

# Can be a Pattern, PGroup, var, or single number
p1 >> pads(P[0, 1, 2, 3]) + [0, 0, 4]
p1 >> pads(P[0, 1, 2, 3]) + var([0, -2], 8)

# Using 'play' will alter the sample values such that these lines are equivalent
p2 >> play("x-o-", sample=P[2, 3] + [0, 0, 1])
p2 >> play("x-o-", sample=[2, 3]) + [0, 0, 1]

__getattr__(attr)

The __getattr__ is called when you retrieve an attribute, such as amplitude, from a Player
object using p1.amp. This returns a PlayerKey object, which acts in a similar way to a TimeVar.
__setattr__(attr, value)
__invert__()

Shorthand for the reset method.

# Resets all attributes then updates the player with new 'rate'
p1.reset() >> play("x-o-", rate=2)

# Equivalent to the line above
~p1 >> play("x-o-", rate=2)

Instance methods
stop()

Removes the Player from the scheduling clock such that you cannot hear it any more.

# If a player is running, use .stop() to stop it!
p1 >> pluck()

p1.stop()

# You can add the method to the end of the line too
p1 >> pluck().stop()

reset()

Resets all of the attribute values to their original values. This is zero for all values except oct, rate, and amp, which are 5, 1, and 1 respectively.

# Start a player
p1 >> play("x-o-", dur=1, rate=2, hpf=4000)

# Reset the attributes to defaults
p1.reset()

# Useful for when you don't want to set values to 0 manually e.g.
p2 >> pluck([0, 2, 4, 7], dur=1/4, hpf=500, pan=[-1,1])

# Sets the dur to 1, hpf to 0 and pan to 0
p2.reset() >> pluck([0, 2, 4, 7])

solo(switch=1)

Mutes every other active Player such that this Player is the only one heard. To un-mute an individual Player, just re-evaluate a line of code. To un-mute all Players, call this method with switch set to 0 or False.

# Start a few players
d1 >> play("x-o-")
p1 >> pluck([0,2], dur=PDur(3,8))

# Solo p1
p1.solo()

# Re-add other Players
p1.solo(0)

only()

Stops all other active Players. Unlike solo, this effect cannot be undone using only(0) as the stopping is permanent. You need to manually re-introduce Players.

# Start a few players
d1 >> play("x-o-")
p1 >> pluck([0,2], dur=PDur(3,8))
p2 >> pads([0,3], dur=8, oct=4)

# Stop p1 and p2 using d1.only()
d1.only()

now(attr="degree")

Returns the current value (i.e. the last value played) for a given attribute. By default this is the degree (pitch or sample character) but you can specify the attribute name as a string.

>>> # Start a player
>>> p1 >> pluck([0, 2, 4], dur=[1, 2, 5])

>>> # Print the pitch and duration
>>> print(p1.now(), p1.now("dur"))
0, 1
>>> print(p1.now(), p1.now("dur"))
2, 2
>>> print(p1.now(), p1.now("dur"))
4, 5

every(n, method_name, *args, **kwargs)

Use to call a method every n number of beats. Specify the method name as a string and then the arguments and keyword arguments to supply the method. See Algorithmic Manipulation for more in-depth information on every.

# Start a player
p1 >> pluck([0,1,2,3,4,5,6,7,8])

# Reverse the order every 8 beats
p1.every(8, "reverse")

# Multiple method calls can be chained together
p1 >> pluck([0,2,4,7]).every(4, "reverse").every(8, "rotate")

after(n, method_name, *args, **kwargs)

Similar to every but only calls the method once after n number of beats. This might be useful for only looping a sequence for a certain amount of time, for example:

# Stop a drum loop after 8 beats
d1 >> play("x-o-").after(8, "stop")

stutter(n, *args, **kwargs)

Repeat the last musical event n times. You can specify keyword arguments as you would normally update a Player to control the stutter. The dur keyword changes the duration over which to spread the stuttered events (defaults to the Player’s current duration value).

# Start a player
d1 >> play("x-o-")

# Stutter it once
d1.stutter()

# Stutter it 4 times (3 extra events)
d1.stutter(4)

# Stutter it 8 times over 2 beats and alternate panning
d1.stutter(8, dur=2, pan=[-1,1])

# Very useful when combined with "every"
d1.every(8, "stutter", 4, dur=3)

jump(ahead=1, **kwargs)

Plays the event that’s a number of steps ahead of the player’s current position as specified by the ahead argument. This is best used in conjunction with the every method:

# Plays the snare drum half a beat early after 6.5 beats
d1 >> play("x-o-").every(6.5, "jump", cycle=8)

spread(pshift=0.125)

Sets the panning to both left and right and offsets the pitch by 0.125 semitones by default to get thicker stereo sound.

# Without spread
p1 >> pluck([0, 4], oct=4, dur=PDur(3,8), sus=2)

# With spread
p1 >> pluck([0, 4], oct=4, dur=PDur(3,8), sus=2).spread()

slider(start=0, switch=1)

Creates an alternating slide effect with the player. Set start to 1 to swap the up-down slide order. Use switch=0 to turn the effect off or the reset method.

# Basic player 
p1 >> saw([7, 0, 3, 1, 7, 4, 5, 2], dur=1/4, oct=4)

# With slider added
p1 >> saw([7, 0, 3, 1, 7, 4, 5, 2], dur=1/4, oct=4).slider()

penta(switch=1)

Sets the scale to the pentatonic mode of the default scale. Use switch=0 to revert to the default scale.

# Default scale
p1 >> pluck([0, 1, 2, 3, 4, 5, 6, 7])

# Pentatonic
p1 >> pluck([0, 1, 2, 3, 4, 5, 6, 7]).penta()

degrade(amount=0.5)

Sets the amplitude to be chosen from 1 and 0 at random. The amount argument is the likelihood of the amplitude being 0 as a fraction i.e. a degrade of 0.5 (default) means each event is 50% likely to be a 0 and at 0.1 it is 10% likely to be a 0.

# Start a player
p1 >> pluck()

# Start to decrease the number of events
p1.degrade()

# Can be called repeatedly to degrade by 25% every 8 beats
p1.every(8, "degrade", 0.25)

offbeat(n=1)

Sets the dur to n and delay to n / 2 so that each note is played on the offbeat.

# Use percussion to hear the difference
d1 >> play("x-o-")
p1 >> pluck()

# Set the duration to 1 and offbeat
p1.offbeat()

# Set the duration to 2 and off every 2 beats
p1.offbeat(2)

reverse()

Reverses the order of all the attributes at the current time. This method does not reverse the lists of values but reverses the order in which they are used.

# Player an octave
p1 >> pluck([0, 1, 2, 3, 4, 5, 6, 7])

# Call reverse and the notes start descending
p1.reverse()

# Call using "every" for organic movement up and down
p1.every([6,3], "reverse")

rotate(n=1)

Moves all of the pitch / sample char elements over by n steps such that the new list of data starts is equivalent but starts at the nth item in the original list.

# Start a player
p1 >> pluck([0,1,2,3])

# Rotating [0,1,2,3] changes it to [1,2,3,0]
p1.rotate()

shuffle()

Randomises the order of the pitch / sample character attribute.

# Start a player
p1 >> pluck([0,1,2,3])

# Changes the order once
p1.shuffle()

# Changes the order every 8 beats
p1.every(8, "shuffle")

follow(player)

Follows the pitch of player. It is equivalent to setting the pitch of one player, e.g. p1, to another’s pitch using p2.pitch.

# Start a player
p1 >> pluck([0, 1, 2, 3], dur=2)

# Follow the pitch in p2
p2 >> blip().follow(p1)

# Add values to change the pitch
p2 >> blip().follow(p1) + [0, 2]

accompany(player)

Similar to follow, this method forces the player to play notes that are derived from the pitch of another Player. The pitch will be the closest neighbour to the last pitch used that is the new pitch of the source player plus 0, 2, or 4.

# Start a player
p1 >> pluck([0, 1, 2, 3], dur=2)

# Play accompanying pitches
p2 >> blip().accompany(p1)

# Add values to change the pitch
p2 >> blip().accompany(p1) + [0, 2]

attrmap(key1, key2, mapping)

Undocumented
smap(mapping)

Undocumented
map(player, mapping, attr="degree")

Undocumented
bang(**kwargs)

Undocumented
