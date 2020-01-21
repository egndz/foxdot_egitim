Clock.bpm = 142

print(sorted(SynthDefs))

p1 >> snick([(0,2),(4,3)],oct=5,amp=linvar([0.4,0.8],8),fmod= [-50,50],slide=2).spread()
#ambi glass gong growl keys klank marimba prophet scatter scratch snick space

#          DO RE MI FA SOL LA SI
#CMajor = [C, D, E, F, G,  A, B] 


#c k l m p s v G Q X 
d1 >> play("XV[xX]V[mX]{Vx{XV}}",dur=1/2,sample=[1,2,3,4],amp=p1.amp)


p2 >> feel(p1.pitch,amp=sinvar([0.4,1.8],8),pan=linvar([-1,1],4h)).every(2,"stutter").spread()


#mi sol si mi si sol
g1 >> blip(P[1,2,3,4], vib=2, amp=p1.amp)















@nextBar
def update():
    Root.scale="major"
