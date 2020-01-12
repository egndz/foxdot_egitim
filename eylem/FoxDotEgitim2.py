"""BOLUM 2.1.: PLAYER METODLARI"""

'Nitelikler ile oynatici objelerini degistirebilirsiniz, bunun baska bir yolu ise player metodlarini kullanmaktir. Zaman kazanmak bu metodlar oldukca kullanislidir.'

d1 >> play("V ", pan=(-1,1), pshift=(0,.5))

d1 >> play("V ").spread()

d1.spread() >> play("V ", pan=[-1,0,1])

d1.stop()

'Player objesinin ismini kendiniz belirleyebilirsiniz.'

foo = Player("bar")

foo >> keys()

foo.stop()

'Oynatici objesinin derecesini degistirebilirsiniz.'

p1 >> pads(P[:4]+(0,[1,2,3,4]))

p1.stop()

print(P[:4]+(0,[1,2,3,4]))

d1 >> play("xxxx", sample=[2,3,0,1])
d2 >> play("[--]")

d_all.stop()

'Player objesi icerisinde kullandiginiz degerleri sifirlayabilirsiniz.'

p1.rate =2

p1.reset() >> play("x(-[--])o-")

p1.stop()

'Assolisti sahneye alabilirsiniz.'

p1 >> pluck(PWalk(5,2,0)[:10].arp([1,2,3,4,5,6]).stutter([2,3,4,5]), dur=var([1,PDur(4,8)],[8,4]),coarse=3, sus=2)
p2 >> ambi(p1.pitch, dur=4, oct=[5,4,3])

for i in range(1,5):
    if Clock.beat_dur == i*2:
        p1.solo(1)
    else:
        p1.solo(0)

p_all.stop()

Clock.clear()

#Eger sona yaklasiyor ve digerlerini tamamen susturmak istiyorsan?z solo() yerine only() kullanin!

'every metodu ile otomatik manipulasyon!'

'Tek tek mi ugrasalim yani?'

p2 >> marimba([0,2,4,5])

p2.stutter(8, dur=2)

p2.every(4,"stutter",8,dur=2)

Clock.clear()

'JUMP MF** JUMP!'

d1 >> play("x-o-").every(6.5,"jump",cycle=8)

d1.stop()

'Slide'

p1 >> saw(PRand(0,5)[:10] | PTri(0,8,1),oct=3).slider()

p1.stop()

p2 >> blip().degrade()

p2.stop()

'diley diley ve beat'

d1 >> play("x-o-").offbeat(.4)

d1.stop()

'ondeki arabayi takip et'

p1 >> pluck([1,2,3])

p2 >> pads(p1.pitch ,amp=.6) #p1.pitch+var([.])...

p3 >> keys().follow(p1) #+var([2,3,4],4)

p_all.stop()





