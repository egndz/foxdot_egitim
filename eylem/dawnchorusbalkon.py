Clock.bpm = var([140,130],[6,4])
Root.default = 0

Clock.clear()

print(SynthDefs)

p1 >> sinepad(G34 | D34 | B23 | D34, oct = 4, room=1, mix=.3, amp = var([.6,.7,.8,.9],8), sus=1.5, echo=.25, dist = .5)

p2 >> keys(p1.pitch, oct = 3, lpf =1500, sus=3, amp =var([.4,.5,.6,.3],8))

b1 >> jbass(p1.pitch, lpf = var([200,400],8), oct = 5, amp = .5).stop()

p3 >> sinepad(B4F5 | B4E5 | A4F5 | A4G5 | B4G5 | B4F5_4 | A4F5 | A4E5  | B4F5 | B4E5 | A4F5 | A4G5 | B4G5 | B4F5_4 | A4F5 | A4E5, oct=3, amp = var([.6,.7,.8,.9],16), sus=2, pan = PWhite(-1,1)).stop()
p4 >> klank(p1.pitch, lpf = 5000, dur = 4, oct=4, amp = 1, chop = 16).stop()



p1 >> dbass(F34 | E34_9 | B23_8 | E34_9 | F34, oct = 5, amp =.8, room=1,mix=sinvar([.4,.6],16),coarse=2, sus=1, lpf = var([800,1200],4),spin = 16, formant= [0,1])

p1 >> soprano(F34 | E34_9 | B23_8 | E34_9 | F34 ,oct=4, coarse=sinvar([4,16],32)).every(4,"stutter",2)

p2 >> keys(p1.pitch, lpf = 1000, amp = .5).stop()

p3 >> jbass(P[-21] | A4E5_4 | A4D5 | P[-21] | G4D5 | G4C5 | P[-21] | B4A5 | P[-21] | G4D5 | G4E5 | P[-21] | A4E5_4 | P[[(12,16)]] |  B4F5_4, oct = 4, amp = var([.3,.2,.1,.5],16), sus =1.5,room =1,mix=.2)

p4 >> keys(PSine(256), dur = 0.1, vibdepth = var([0.5,1,2,0,0],8), vib = 3, amp = 1, room = 1, mix = 0.8)

##Left Hand Chords
"""Verse 1"""
G34 = P[[(4,11)]].loop(4) | P[[(4,11)]].loop(2)
D34 = P[[(1,8)]].loop(4) | P[[(1,8)]].loop(2)
B23 = P[[(-1,6)]].loop(4) | P[[(-1,6)]].loop(2)

"""Verse 2"""
F34 = P[[(3.5,-4.5)]].loop(4) | P[[(3.5,-4.5)]]
E34_9 = P[[(-5,2)]].loop(4) | P[[(2,-5)]]
B23_8 = P[[(-1,-8)]].loop(4) ## It is only 8 beats in the original song

#Right Hand Chords
"""Verse 1"""
B4F5 = P[0] | P[[(13,17.5)]].loop(3) | P [[(13,17.5)]] 
B4G5 = P[0] | P[[(13,18)]].loop(3) | P[[(13,18)]]
A4F5 = P[0] | P[[(12,17.5)]].loop(3) | P[[(12,17.5)]]
B4E5 = P[[(13,16)]].loop(3)
A4G5 = P[[(12,18)]].loop(3)
A4E5 = P[[(12,16)]].loop(3)
B4F5_4 = P[[(13,17.5)]].loop(3)

"""Verse 2"""
A4D5 = P[[(12,15)]].loop(3)
G4D5 = P[[(11,15)]].loop(3) | P[[(11,15)]]
G4C5 = P[[(11,14.5)]].loop(2) | P[[(11,14.5)]] | P[13]
B4A5 = P[[(13,19)]].loop(3) | P[[(13,19)]].loop(2) | P[[(13,19)]]
G4E5 = P[[(11,16)]].loop(2) | P[[(11,16)]]
A4E5_4 = P[[(12,16)]].loop(3)
B4F5_4 = P[[(13,17.5)]].loop(3)

p1 >> warsav()
