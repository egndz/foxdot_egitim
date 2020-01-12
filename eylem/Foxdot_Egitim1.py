## FoxDot'a Giris Egitimi ##

"""Merhaba! FoxDot egitimine hosgeldiniz. Bu calisma dosyalari, FoxDot'a giris icin hazirlanmistir.
FoxDot, genel olarak bir Python kutuphanesidir, SuperCollider'in etkili ses sentezleme mekanizmasi ile haberleserek canli muzik kodlama deneyimi sunmaktadir.

Bu calisma dosyasinin yetersiz kaldigi ya da daha fazla bilgiye erismek istediginiz noktada, her yazilim dilinde oldugu gibi dokumantasyona erisebilirsiniz! FoxDot'un resmi websitesi:

https://foxdot.org 

Bu dokumantasyon boyunca detayli bir sekilde basitten zora dogru FoxDot kutuphanesinin tum yonlerini ele alacagiz. Eger takildiginiz, cevabini deneyerek bulamadiginiz veya kafa karisikligi yasadiginiz noktalar olursa diger FoxDot kullanicilari ile iletisime gecebileceginiz bir adet forum bulunmaktadir:

https://forum.toplap.org/c/communities/foxdot 

Hadi baslayalim!"""

## 1. BOLUM: TEMEL B?LG?LER ##

"Gozumuzun onune bir adet gitar, piyano ya da benzeri bir enstruman getirelim. Fiziksel dunyada ses yaratmaya yaran bu aletler, dogaldir. Simdi en sevdiginiz enstrumantel parcalardan birini kafanizin icinde calin! Hangi enstruman caliyor? Piyano, gitar, keman, davul... Bu enstrumanlari ayirt etmemizi saglayan sesin bir ozelligi vardir: tini(timbre). Synthesizer, dogada bulunmayan sesleri yaratmamizi saglayan bir donanim/yazilimdir. Yarattigi sese ise #synth demekteyiz. O zaman FoxDot'ta synthleri nasil yaratacagimiza bir bakalim:"

print(SynthDefs)

"Listelenmis synthler, FoxDot'ta kullanabileceginiz synthlerdir. Peki bu synthi nas?l kullaniriz?"

p1 >> gong()

"Duydugunuz ses, C notasidir. Durdurmak icin ise bunu FoxDot'a soylememiz gerekiyor:"

p1 >> gong().stop()

"""Evet, sectigimiz enstruman gong'dan sonra .stop() yazarak synthi durdurabiliriz.
p1 ve >> komutlari, FoxDot'a emir vermemiz icin gerekli komutlard?r. p1(x1,z1,c2.. de yazabilirsiniz) PLAYER olarak adlandirilan bir objedir. PLAYER objesini yazdiktan sonra, aktive etmek icin >> oklarini kullanmamiz gerekmektedir. Bu oklar tipki + gibi bir operasyon belirtmektedir.

Eger player objesinden sonra .stop() yazmak istemezseniz:
p1.stop() yazarak da FoxDot'ta susmani gerektigini belirtebilirsiniz."""

p1.stop()

"Buraya kadar enstruman secmeyi, player objesi ve aktive etmeyi ogrendik. Surekli C notasi duymaktan bunalmis olabilirsiniz, peki enstrumanimizin istedigimiz notalari calmasini nasil saglayabiliriz?"

p1 >> gong(1)

p1.stop()

""" Simdi duydugunuz nota, D(Re) notasidir.
FoxDot, enstrumandan sonra nota belirtmediginiz surece C notasi ile baslamaktadir(Scale ve root konularina geldigimizde bunun nasil degistigini gorecegiz.)
0 = C, 1 = D, 2 = E, 3 = F, 4 = G, 5 = A, 6 = B olarak atanmistir.
Peki Eb ya da G# calmak icin ne yapmali?

Eb --> 1.5
G# --> 4.5

FoxDot, ses sentezlerken frekanslar ile calismaktadir. Ornegin, Piyanonun tam ortas?nda bulunan La tu?u, 440 Hz'dir(Telefon ederken de duydu?unuz biiip sesi, 440 Hz'lik LA notasina esittir!). Eger yarim perde inceltmek ya da kalinlastirmak isterseniz 1/2=0.5 ekleyip cikararak elde edebilirsiniz. Dilerseniz 1.2,1.3,1.4.. yazarak atanmis frekanslari dinleyebilirsiniz.

Simdi asagidaki player objesini calistirmayi deneyelim!"""

p1 >> gong(1,2)

""" Hmmm... FoxDot hata veriyor. Neden acaba?
gong objesi malesef 1'den fazla arguman alamiyor. Peki biz ayni anda ya da sirasiyla farkli notalari nasil calacagiz?"""

p1 >> blip([0,1,2,3])

p1.stop()

""" FoxDot'ta enstrumani ayni anda(akor) ya da farkli sekilde calabilmek icin, enstrumanin icerisinde farkli parantezler kullanmak gerekiyor. 

[] --> soldan saga dogru sirasiyla belirttiginiz notalari calar.
() --> belirttiginiz notalari, ayni anda calar."""

p1 >> blip((0,3,5))
 
p1.stop()

p2 >> blip([0,3,5])

p2.stop()


""" Notalari tekli ya da akor olarak calabiliyoruz... Ancak her bir notanin s?resini(duration) nasil belirleyebiliriz?"""

p1 >> blip([0,3,5], dur = 1/2)

p1 >> blip([0,3,5], dur = [1/2,1/2,1])

p1.stop()

""" ilk player objesinde dur = 1/2, tum notalara uygunlanmaktadir. Eger her bir notanin suresini belirlemek isterseniz, yine koseli parantez kullanarak bunu yapabilirsiniz. Her nota, dur argumani icerisinde yazan deger ile eslestirilmektedir."""

p1 >> blip([0,1,2,3], dur = [1/2,1/2,1])

p1.stop()


""" Nota sayisindan daha az sure(duration) degeri verdigimizde, dur listesi tekrar basa doner ve bir sonraki notaya o sureyi uygular."""

""" Davul ornekleri calabilmek ya da belirli ses ornekleri calabilmek icin bu ise uygun bir enstruman bulunmaktadir: play."""

d1 >> play("x-o-")

d1.stop()

"""Bir davul seti hayal edelim. Kick, trampet, zil ve bircok ekipman bir arada bulunmaktadir. FoxDot'ta bu ekipmanlar klavyedeki bir karaktere atanmistir. Ornegin:

x --> kick
- --> hi-hat
o --> snare(trampet)
* --> clap"""

#TIP: play objesinin icerisinde yer alan cift tirnak isareti space(bosluk) duyarlidir.

d1 >> play("x-o-", sample = 1)

d1.stop()

d1 >> play("  ----", sample = 2, dur = 1, bpm = 60)

d2 >> play("x",dur = 1, bpm = 60)

d_all.stop()

""" Ses ornekleri, FoxDot icerisinde bir dosyada saklanmaktadir. Bakmak isterseniz Help&Settings --> Open Sample Folders'a tiklayabilirsiniz. Davul orneklerini degistirebilmek icin play objesinin icerisine sample=1,2,3... yazabilirsiniz.

Peki dur anahtar argumaninda oldugu gibi sample anahtar argumanina birden fazla deger verirsek ne olur?"""

d1 >> play("----", sample = [0,1,2,3], bpm = 60)

d1 >> play("----", sample = 2, dur = [1/2,1/2,1/4,1/4])

d1.stop()

"""Davul paternlerine biraz ?e?itlilik katmak i?in tipki notalarda oldugu gibi parantezleri kullanabiliriz: """

d1 >> play("x-o[--]", bpm = 60)

d1 >> play("x-o(-o)", bpm = 60)

d1 >> play("x-o{-o*}", bpm = 60)

d1.stop()


#TIP 2: bpm(beat per minute)'i azaltarak davul paterninde nelerin degistigini daha rahat duyabilirsiniz (eger ritim duyarsizi olaniniz var ise, mikemmel bir cozum! :) )


"""Her bir parantez, farkli bir gorevi yerine getirmektedir.

[ ] ---> Tek bir vurusta, icerisinde yer alan butun ornekleri calar
( ) ---> Her seferinde, sirasiyla, icerisinde yer alan ornegi parantez disindaki paterne ekler
{ } ---> Her patern bitisinde, rastgele icerisinde yer alan ornegi ekler.

Bu parantezleri kullanarak degisik davul paternleri elde edebilirsiniz!"""

d1 >> play("x-o(*[--])", bpm = 60)

d1.stop()

d2 >> play("x-o(-[-(-o)])", bpm = 60)

d2.stop()

""" d1,d2,d3... seklinde farkli playlerlara atayarak davul paternleri olusturmak istemeyebilirsiniz. Bunun icin kullanabileceginiz bir operator bulunmaktad?r: <   >"""

d1 >> play("<x-o-><[-x]>", sample = 3, bpm = 120)

d1.stop()

d2 >> play("<xsss><-([ii])>", sample = 4)

d2.stop()

##TIP: sample niteligine liste verdiginizde elemanlara sirasiyla uygulanir. eger elemanin samplei degismesin istiyorsaniz |x2| seklinde oynatici objesi icerisine yazabilirsiniz.

##### AL?ST?RMA:


## 2. BOLUM: PLAYER METODLARI ##

"""Buraya kadar FoxDot'un en temel ozelliklerini gorduk. Nasil enstruman sececegimizi, davul paternlerini nasil olusturabilecegimizi biliyoruz, ancak biraz daha cesnilendirmek istersek ne yapmaliyiz?"""

print(Player.get_attributes())

"""Listede karsimiza cikan bir cok ozellik var! Temel olarak sesimizi manipule etmek istiyorsak oktavini, siddetini, suresini degistirebiliriz. Ancak efekt ekleyerek daha kendine has bir synth elde etmek icin, listede yer alan anahtar argumanlar da kullanilabilir.

Attributes(Ozellikler): degree,oct,dur,scale,amp,amplify,bpm,sample,delay. """

p1 >> gong([0,4,0], dur = [1,1/2,1], oct = [2,3,2])

p1.stop()

p2 >> gong([0,1,2,3])
p2.degree = [0,1,2,3]
p2.dur = 1/2

p2.stop()

"""Buraya kadar dur, bpm, sample ozelliklerini gorduk. Yukaridaki kodda gong enstrumanini alip, derecesini ve notalarin surelerini degistirdik. Ancak organize bir ses toplulugu olan muzik, sesin siddeti(loudness) degistirilmeden olabilir mi?

Hayir. Bu sebepten player objesi icerisinde sesin siddetini ayarlayabilmek icin iki farkl? ozelligimiz bulunmakta: amp ve amplify."""

p1 >> sinepad([0,4,5], amp = [0.1,0.8,1])

p1.stop()


#TIP 3: amp metodunu kullan?rken dikkatli olmak gerek! Genellikle 0 ile 1 arasinda secilen bu degeri 1'in ustunde verdiginizde kulakliklarinizi ve kulaklarinizi hasara ugratabilirsiniz!

"""amp metodu yeterli gibi duruyor, peki o zaman amplify metodu neden var? ileriki bolumde gorecegimiz TimeVar objesi, verilen degerler ile zaman icerisinde muzigin ozelliklerini kontrol etmemizi saglamaktadir. Es zamanli muzik yaparken, ayni anda tum ozellikleri degistiremeyiz; bu yuzden onceden komut vererek istedigimiz zaman istedigimiz ozelligin degismesini saglayabiliriz! amplify metodu ise TimeVar kullanarak player objesinin siddetini zamanla degistirmemizi saglamaktadir. Nasil mi?"""

p1 >> sinepad([0,4,5,2], amp =[0.5,1])
d1 >> play("x ", sample = 2)

p1.amplify = var([1,0.5],[4,4])

p1.stop()

"""Bir de delay metoduna bakalim. Delay, elektronik muzikte sikca kullanilan efektlerden biridir. FoxDot'ta bu metod, denk gelen notanin verilen deger kadar daha gec calinmasini saglamaktadir. root ise player objesi icerisinde gami degistirmeye yarayan bir metoddur. """

Clock.bpm  = 70

p1 >> sinepad([0,1,2], delay = [0,0,0.5], root = var([0,2],3)
d1 >> play("x")

Group(p1,d1).stop()

"""Player objesi icerisinde gami degistirmek istemezseniz, bunu kod icerisinde ya da player icerisinde de yapabileceginiz baska bir yontem daha bulunmaktadir: scale. Daha detayli kullanimi icin dokumantasyona goz atabilirsiniz!"""


## 3. BOLUM: PLAYER EFEKTLER? ##

"""Sesi manipule etmenin en guzel yollarindan biri, efekt eklemektir. Akustik elemanlardan olusan bir grubu canli dinlediginizde, efektler mekanin akustik ozellikleri ve muzisyenlerin fiziksel ozellikleri tarafindan belirlemektedir. Bunu dijital ortamda yapabilmek efektler ile mumkundur."""

print(Player.get_attributes())


""" Listede bulunan efektler, FoxDot icerisinde kullanabileceginiz efektlerdir. Kisaca bu efektleri aciklayabiliriz:


Sustain: Notalarin herbirinin kac vurus uzatilacagini belirler, piyanodaki sustain pedaliyla ayni islevi gormektedir.

Stereo Panning: Sesin cikis yaptigi birden fazla kanal olabilir. FoxDot, su an icin en fazla iki kanaldan cikis vermektedir: sesin iki kanal arasinda gidip gelebilmesi icin bu efekti kullanabilirsiniz.

Frequency Modifier: Cikis kanallarindan birinde, digerine gore frekans degistirmek icin kullanilir. Ornegin, sadece la notasi caliyorsunuz. ?ki kanalda da 440 Hzlik bir frekans duyacaksinizdir. Ancakbirinde degisiklik yapmak isterseniz, diyelim ki fmod = 10 Hz, kanalin birinde duyacaginiz frekans 450 Hz olacaktir. Bu efekt, atonal bir ses saglamaktadir.

Vibrato: Ses perdesini devamli olarak mod?le etmeye yarar.

Slide: Notanin frekansini zaman icerisinde kaydirmaktadir. Eger bu efekti gecikmeli uygulamak isterseniz slidelay degiskenine parametre atayarak yapabilirsiniz. Slide efektinin hangi frekanstan basladigini belirlemek isterseniz slidefrom ile de bunu gerceklestirebilirsiniz.

Pitch bend: Notanin frekansini zaman ile degistiren bu efekt, slidedan farkli olarak baslanan frekansa nota suresi sonunda geri doner.

Buraya kadar belirli efektleri aciklanmis bulunduk, daha fazlasini ogrenmek icin dokumantasyona bakabilir ve bu bolum sonunda istenilen alistirma ile deneyebilirsiniz."""

b1 >> jbass()

b1 >> jbass(chop = 2, delay = [0.5,(0,0.5)])

b1 >> jbass(chop = 2, delay = [0.5,(0,0.5)], fmod = [-3,3])

b1 >> jbass(chop = 2, delay = [0.5,(0,0.5)], fmod = [-3,3], sus = 2, blur = var([1,2],16))

b1.stop()

b2 >> soprano(oct=4)

b2 >> soprano(vib=4,vibdepth=.01)

b2.stop()

b3 >> pluck(dur=4,slide=[-1,1])

b3.stop()

b4 >> pluck(dur=4, slide = [-1,1],slidedelay=.2)
#Baslangici geciktirir.

b4.stop()

b5 >> pluck(dur=4, slidefrom=[-2,-1,0,1,2])

b5.stop()

b6 >> pluck(dur=4, bend=[1,2,3],oct=5)

b6.stop()

p1 >> play("2",dur=8, chop=16)

p1.stop()

p2 >> play("2", dur=8, coarse=16)

p2.stop()

p3 >> keys(dur=8,echo=.2, echotime=8,room=.5)

p3.stop()

p4 >> pads(dur=4,spin=4,sus=16)

p4 >> pads(dur=4,pan=[-1,0,1])

p4.stop()

p5 >> pads(dur=2, cut=linvar([.1,.5,.8,1],2))

p5.stop()

p6 >> pluck(formant=P[:7],oct=4)

p6.stop()

p7 >> pads(dur=4,tremolo=2)

p7.stop()

p8 >> pads(pshift = [0,2,4,5])
p9 >> pads([0,1,2,3])
#semitone

p_all.stop()

p0 >> blip([0,4], dur=4, glide=[7,-7],oct=4)
#semitone, similar to slide




##AL?ST?RMA: En cok size uygun goldugunuz bir synth ile efektleri deneyin. Farkli efektlerin tek basina ve birlikte nasil bir manipulasyon gucune sahip oldugunu gorun. Boylece size en uygun sesi yakalabilirsiniz. Ornegin, klank synthi ile sustain ve blur efektleri birlikte sesin siddetini amp ya da amplify olmadan arttirabiliyor. Bunun gibi degisik gozlemler yapabilirsiniz!

## 1. Synthini bul. 2. Efekt listesinden lpf, chop, fmod gibi efektleri dene. 3. Deneyerek bu efektlerin nasil degisim yarattigini gozlemle.
