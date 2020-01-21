Cheat Sheet

PRINT

--Synthler
print(sorted(SynthDefs))

--Davul samplelari
print(Samples)

--Player metodlari
print(sorted(Player.get_attributes()))

--Gamlar(scales)
print(Scale.names())

PARANTEZLER

--Davul ornekleri icin:
[]: tek vurusta icindeki tum ornekleri calar
(): her dongude sirasiyla icindeki ornegi calar
{}: her dongude rastgele icindeki ornegi calar

--Notalar icin:
(): tum notalari birlikte calar
[]: tum notalari sirasiyla calar

PATERNLER

--Aritmetik operatorler
P[](*,-,+,/) : Icindekilerle operatore gore islem yapar

--Paternler arasi islemler
P[] (*,+,**) P[]: Paternlerin ayni indeksteki elemanlarini carpar/toplar
P[] | P[] : Paternleri birlestirir
P[] & P[] : Paternlerin ayni indeksteki elemanlarini beraber calar

--PGroups 
P*(): sure(dur) niteliginin degerinde hepsini esit aralikla calar(davuldaki []in muadili)
P+(): sus niteliginin degerinde hepsini esit aralikla calar
P**(): sure(dur) niteliginin degerinde hepsini esit aralikla, rastgele calar(davuldaki {}+[] gibi)
P/(): sure(dur) niteliginin degerinde hepsini esit aralikla calar ve delay(gecikme) ekler
P^(): sure(dur) ve sus niteliklerinden bagimsiz olarak verilen son deger kadar delay(gecikme) ekler


