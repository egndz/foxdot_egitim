"""BOLUM.3: PATERNLER"""

"""BOlUM 3.1: PATERN TEMELLERI"""

'Oynatici objesi icerisine atanan degerlere bir islem uygulamak isteyebiliriz.'

print([2,3,4]*2)

lis = [1,2,3]

print([i*2 for i in lis])

'Ikinci uygulamadaki kodu canli kodlama sirasinda yazmak oldukca zor. Bu yuku almak icin FoxDotta paternler bulunmaktadir.'

p1 >> keys(P[0,1,2,3]*2)

p1.stop()

p2 >> keys(P[:4]*2)

p2.stop()

p3 >> keys(P[0:4] + P[2:6])

p3.stop()

p4 >> keys(P[0:4]  | P[2:6])

p4.stop()

p5 >> keys(P[0:4] ** P[-1:3])

p5.stop()

'Patternler arasinda goruldugu uzere islem yapilabilmektedir. Pattern uzunluklarinin ayni olmasina gerek yoktur.'

print(P[0:4] ** P[-1,0])

Clock.clear()

"""BOLUM 3.2: PATERN METODLARI"""

'Paternler bir obje oldugu icin onlara bagli metodlar ve fonksiyonlar bulunmaktadir. Oynatici objelerine ekledigimiz every metodu burada yerini direk olarak paternlere uyguladigimiz metodlara birakmaktadir.40a yakin patern metodu bulunmaktadir, siklikla kullanilanlara goz atalim:'

##TIP: Isterseniz bu metodlari patern kullanmasaniz bile oynatici objelerinde "every" metodu ile kullanabilirsiniz!

'Paterni uzatip elemanlari rastgele dagitmak mi istiyorsunuz?'

p1 >> keys(P[:4].shuffle(2))

p1.stop()

p2 >> keys(P[:4].shuffle(3),dur = PDur(3,8))

p2.stop()

'Patern patern(PGroups) icinde... Bir varmis bir yokmus!'

p5 >> keys(P[1,[2,3]].shufflets(2))

p6 >> keys(P(1,[2,3]).shufflets(2))

Clock.clear()

p1.stop()

print(P[1,[2,3]].shufflets(2))
print(P(1,[2,3]).shufflets(2))

print(P[:4].shuffle(3))

'Paterni tersine nasil ceviririz?'

p1 >> keys(P[:4].reverse(), dur = 1/2)

p2 >> keys(P[:4].mirror(), dur = 1/2)

p_all.stop()

'mirror ile reverse ayni isi yapiyor gibi duruyor. O halde neden ikisi de var?'

print(P[:4,[5,6]].reverse())
print(P[:4,[5,6]].mirror())

Clock.clear()

'Paternimizin icerisindeki sayilari hizaya nasil getiririz?'

p1 >> blip(P[1,4,2,7,3].sort(reverse = False))

p1.stop()

p2 >> blip(P[(1,3),(7,5,4,3),(4,3,2)].sort())

p2.stop()

Clock.clear()

print(P[(1,3),(7,5,3),(3,1)].sort(key = lambda x: len(x)))

'Ortaligi karistirmaya var misiniz???'

p1 >> pluck(P[0,1,2].stutter(3))

p1.stop()

print(P[0,1,2].stutter([3,4,5]))

Clock.clear()

'Arpeggiattooo!'

p1 >> pluck(P[:4].arp([0,3]))

p1.stop()

print(P[1,2].arp([0,1,2,3]))

Clock.clear()

'Cesnilendirelim mi?'

p1 >> blip(P[1,2,3,4].splice([5,6,7]))

p1.stop()

print(P[1,2,3,4].splice([5,6]))

Clock.clear()

'Toplamali cikarmali reverse.' ##########TEKRAR BAK!

p1 >> blip(P[1,2,[3,4]].invert())

p1 >> blip(P[1,5,9,11].invert())

print(P[1,5,9,11].invert())

'Ross Geller, is that you bruh?'

p1 >> pads(P[1,2,3,4].pivot(2))

p1.stop()

Clock.clear()
'Toplaya toplaya gidek'

p1 >> blip(P[:4].accum())

p1.stop()
print(P[:4].accum(7))

Clock.clear()
'GYM CLASS: CARDIO TIME!'

p1 >> pluck(P[1,2,3,4].stretch(7))

p1.stop()

print(P[:4].stretch(6))

Clock.clear()

'Tras zamani.'

p1 >> keys(P[:5].trim(2))

p1.stop()

Clock.clear()
'Baslangic!'

p1 >> blip(P[1:6].ltrim(1))

p1.stop()

print(P[:6].ltrim(1))

Clock.clear()

'Donguler'

p1 >> pluck(P[:4].loop(4, lambda x:x+2))

p1 >> pluck(P[:4].loop(2) | P[1])

## loop boyle bi' ise yaramiyor gibi duruyor. Hmmm... baska neler yapilabilir?

p1 >> pluck(P[1,3,5].loop(2) | P(1,[2,4],5), dur = var([1/2,1],[4,1]), sus=2, lpf= 800)

##every mi eklesek?

p1 >> pluck(P[1,3,5].loop(2).every(4,"offadd",2).every(2,"arp",[1,2,3,4]) | P(1,[2,3],5), dur= var([1/2,1],[4,1]), sus=2, lpf=800)

p1.stop()

Clock.clear()

'Multiplexer'
#Nested listler dagilmaz.

p1 >> space(P[1,4,6,[3,4]].duplicate(5))

p1.stop()

print(P[1,4,6,[3,4]].duplicate(4))

'Duyarsiz duplicate: iter'

p1 >> blip(P[1,2,[3,4]].iter(4))

p1.stop()

print(P[1,2,[3,4]].iter(2))

Clock.clear()

'Swap' ## TEKRAR BAK

print(P[:6].swap(5))


'Bi d?z bi ters,9.5 sis orgu'

##diyelim ki bir paterne tersini de eklemek istiyorsunuz:
print(P[:5]| P[:5].reverse())

## uzun uzadiya yazmak istemeyebilirsiniz.

print(P[:5].palindrome())
print(P[:5].palindrome(1))

p1 >> pluck(P[:4].every(4,"alt",[4,5,6,7]))

p1.stop()

print(P[:4].alt([0,0,0,0]))

p1 >> pluck(P[:8].norm())

p1.stop()

print(P[:9].norm())

'ciftleri sahneden alalim lutfen'

p1 >> blip(P[1,2,2,2,4,5,5,5].undup())

p1.stop()

print(P[1,2,2,2,3,4,4,4,4].undup())

p1 >> blip(P[1,2,4,5].limit(sum,7))

p1.stop()
print(P[1,2,5,7].limit(sum,7)) ###BUG

p2 >> blip(P[0,1,2,3,4].replace(2,9))

p2.stop()

'Kisa kes'

p3 >> blip(P[0,1,2,3,4].submap({1:8,2:9,4:[9,10]}))

p3.stop()

p4 >> pluck(P[0,1].layer("offadd",[1,9]),dur=2)

p5 >> pluck(P[0,1].layer(lambda x:x+2),dur=2)

p4.stop()

print(P[0,1].layer("offadd",[1,9]))

p1 >> blip(P[1,2,3] | P[0,0,0]).stop()

pat = P[1,2,3]
pat.extend([0,0,0])

p2 >> blip(pat)
p2.stop()

'every ile concat'

p1 >> blip(P[:4].every(4,"concat",[4,5]))

p2 >> blip(P[:4] | [4,5])

'winrar lisans istiyor'

p1 >> pluck(P[0,1,2,3].zip([4,5]))

'kullan ve geciktir'

p1 >> blip(P[:4].offadd([2,3],2))

print(P[:4].offadd([2,3],2))

p2 >> pluck(P[:4].offmul(2,2))

print(P[:4].offmul(2,2))

p3 >> blip(P[:4].offlayer("reverse",2))

d1 >> play("x-hh").every(4,"amen")
d1.stop()

"""BOLUM 3.3: PATERN FONKSIYONLARI"""

"""Metodlar ile karsilastirinca daha az patern fonksiyonu bulunmakta! Bu fonksiyonlar belirli degerlere sahip paternler uretmek icin kullanilabilir.Totalde 11 tane patern fonksiyonu vardir. Daha siklikla kullanilanlar orneklerdeki gibi.
"""

d1 >> play(PStep(4,"-","x"))

d1.stop()

d1 >> play(PStep([2,4],"-","x"))

d1.stop()

p1 >> gong(PRange(10,0,2).palindrome())

p1.stop()

p1 >> gong(PTri(10,0,2), pan = PSine(32))

p1.stop()

print(PRange(10,0,2).palindrome())

print(PTri(10,0,2))

#Triangle(?cgen) ve PRange'e palindrome ekleyince nasil bir benzerlik olusuyor? Bir seyi yapmanin birden fazla yolu olabilir!

print(PEuclid(5,8))

print(PEuclid2(5,8,"v","s"))

print(PStep(5,"v","s"))

d1 >> play(PEuclid2(5,8,"v#","s"))

d1.stop()

#PEuclid2 fonksiyonunu PStep+PEuclid gibi dusunebiliriz. Davul ornekleri calarken isinize yarayabilir!

"""Bu fonksiyonlar arasinda siklikla kullanilan bir baska fonksiyon bulunmaktadir: PDur."""

print(PDur(3,8))
print(PDur(PRange(4,0),4))

#PDur Euclidean ritim diye gecmektedir. Ornegin, (3,8)'de 8 vurusa 3 pulse dagitir.

print(PSine(16))

print(PSq(2,2,3))


"""BOLUM 3.4: PATERN URETECLERI"""

'Paternlere istedigimiz degerleri verebiliriz. Ancak m?zik yaparken raslantisalligi kullanmak isteyecegimiz zamanlar olabilir. Bu gibi durumlarda patern uretecleri isimize yaramaktadir. '

print(PRand(2,10,seed=0)[:10])
print(PRand(2,10,seed=1)[:10])

p1 >> space(PRand(2,10,seed=1)[:5], spin=16)
d1 >>play("[ss] ").spread()

Group(p1,d1).stop()

print(PxRand(1,5)[:10])

p1 >> blip(PxRand(1,5)[:10])

p1.stop()

p2 >> blip(PxRand([1,2,3])[:10])

p2.stop()

Clock.clear()

#print(PwRand([1,2,3],[2,1,1])[:10])

print(PWhite(-1,1)[:5])

p1 >> klank(PWhite(-5,5)[:15],vib=2, vibdepth=.5, shape=sinvar([.1,.5],32),dur=2,oct=[4,3,2,1])
p2 >> space(p1.pitch,dur=4, oct=6)

p_all.stop()

print(PWalk(12,2,0)[:20])

p1 >> keys(PWalk(12,2,0)[:20])

p1.stop()

print(PDelta(.1,2)[:10])

p1 >> pluck(PDelta([.1,1,-.1])[:20]+P*(0,1,2),dur=PDur(var([15,10,5,3,2],4),8)).every(8,"reverse")

p1.stop()


#PSq(a,b,c) ile PSquare benzer calisir. Aradaki fark ilki sirayla giderken ikincisi rastgele diziye dagitir.


"""BOLUM 3.5: PGROUPS: P*+()"""

'PGrouplar ayni anda icerisindeki tum elemanlari calarlar. Tuple yani () kullandiginizda player ya da patern objesi fark etmeksizin hepsi PGroupsa donusturulurler!'

p1 >> pluck(P(0,1,[2,3]))

p1.stop()

Clock.clear()

'Genisletilmis PGROUPS mu?'

p1 >> blip(P*[1,2,3])

p1.stop()

p2 >> blip(P*(0,1,2), amp=.5)
d1 >> play("X ")

Group(p2,d1).stop()

print(P*[1,2,3]) # random calar!

p1 >> pluck(P+(1,2,3), dur=1, sus=var([1,2,3],4))

p1.stop()

p1 >> keys(P+(0,2,4), dur = 1, sus=2).every(2,"arp",[1,2,3,4,5,6])

p1.stop()

p1 >> pluck(P[0,1,P**(3,5,7,9)])
d1 >> play("g ")

Group(p1,d1).stop()

p2 >> pluck(P[0,1,P*(3,5,7,9)])

p_all.stop()

p3 >> pluck(P[0,1,P/(2,4,6,8)])

p3.stop()

p4 >> pluck(P[9,P^(0,1,2,1)],bpm=120)
d4 >> play("x ",bpm=120)

Group(p4,d4).stop()
