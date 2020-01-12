Patern Uretecleri

Biliyoruz ki belirli uzunluktaki paternler bir fonksiyona ba?l? olarak ?retilirler. Ne var ki, bazen sonsuz uzunluktaki paternleri kullanmak i?e yarayabilir, ?rne?in rastgele say?lar ?retmek i?in. Tam bu noktada patern ?reticileri devreye girer. Python ?rete?leri ile t?m de?erlerin haf?zada tutulmamas? konusunda benzerlik g?steren patern ?rete?leri bir sona sahip de?ildir. Haydi gelin ba?lamak i?in PRand patern ?retecine bakal?m, daha sonras?nda kullan?labilir patern ?rete?lerini kodun devam?nda bulabilirsiniz.

PRand ?reteci bize belirledi?imiz de?er aral??? i?erisinde sonsuz say?da rastgele say? ?retir. Paternlerde yapt???m?z gibi objeyi ekrana yazd?ramay?z; bunun sebebi ise sonsuz say?daki de?erlerin hepsi hen?z hesaplanmam??t?r:
1
2
3
	
>>> my_gen = PRand(0, 10)
>>> print(my_gen)
PRand(0, 10)

To see what values are in my_gen we need to access it using indexing or slicing.
1
2
3
4
5
6
	
>>> my_gen[0]
4
>>> my_gen[1]
6
>>> my_gen[:10]
P[4, 6, 1, 8, 3, 8, 8, 8, 0, 1]

PRand? indekslemek bize o indeksteki de?eri; dilimleme i?lemi de de?erlerden olu?an bir patern verir. ?lk iki de?erin nas?l 4 ve 6 oldu?unu fark ettiniz mi? Bir patern ?reteci, verilen indekste neredeyse her zaman ayn? de?eri d?ner. ?sterseniz herhangi bir patern metodunu dilimleme i?leminden sonra elde etti?iniz bir patern objesine uygulayabilirsiniz.


Patern ?rete?leri ile basit aritmetik i?lemleri de ger?ekle?tirebilirsiniz:
1
2
3
4
5
	
>>> my_gen2 = my_gen * 2
>>> print(my_gen2)
PRand(Mul 2)
>>> my_gen2[:10]
P[8, 12, 2, 16, 6, 16, 16, 16, 0, 2]

Yeni PRand? ekrana yazd?rmak bize hakk?nda az bir bilgi vermektedir -- varolan bir PRand objesi oldu?unu ve 2 ile ?arp?ld???n? s?yler. Kendi fonksiyonlar?n?z? paternlere uygulad???n?z gibi patern ?rete?lerine de d?n??t?r?c? metodlar? ile uygulayabilirsiniz. Haydi girdisi tek say? olunca 5, ?ift olunca 3 d?nen bir fonksiyon tan?mlayal?m:
    
1
2
3
4
5
	
>>> def odd_test(num):
...    return 5 if num % 2 == 1 else 3
>>> my_odd_gen = odd_test(PRand(0, 10))
>>> print(my_odd_gen)
3

num % 2 i?lemi bir say? yerine yeni bir PRand d?nmektedir, o halde "bu i?lemin sonucu 1e e?it midir?" diye soruldu?unda False, yani 3 d?nmektedir(True oldu?u halde 5 d?necektir). Patern ?retecimizin i?indeki de?erlere bu fonksiyonu uygulayabilmek i?in transform metodunu uygulamal? ve fonksiyon ile desteklemeliyiz.

1
2
3
4
5
	
>>> my_odd_gen = PRand(0, 10).transform(odd_test)
>>> print(my_odd_gen)
PRand(lambda None)
>>> print(my_odd_gen[:10])
P[3, 3, 3, 5, 3, 3, 5, 3, 5, 3]

Yeni patern ?retecini ekrana bast???m?zda kar??m?za ??kan sonu? yeni PRandin girdi de?eri olmadan d?n??t?r?ld???n? g?stermektedir. Dilimleme yaparak 3 ve 5lerden olu?an, bizim de bekledi?imiz ?zere, bir patern d?nmektedir.

E?er patern ?rete?lerimizi bir de?erde saklamadan ekrana yazd?r?rsak ne olur?

1
2
3
4
	
>>> print(PRand(0, 10)[:10])
P[8, 5, 6, 0, 2, 2, 7, 3, 4, 4]
>>> print(PRand(0, 10)[:10])
P[1, 0, 0, 8, 0, 3, 4, 4, 2, 9]

Farkl? de?erlerden olu?an bir liste kar??m?za ??k?yor. Bunun sebebi ise yeni PRand objesini her seferinde s?f?rlamam?z. A??k?as? bu biraz rahats?z edici, ?zellikle patern objelerini patern ?rete?leri ile destekliyorsan?z ve bir de?i?kene atamadan kullan?yorsan?z. E?er patern ?retecinizden ayn? de?erleri almak istiyorsan?z, seed metodunu kullanarak bilgisayar?n?z?n rastgele say? ?retecini ayn? say? setlerini ?retmesi i?in zorlayabilirsiniz. 

1
2
3
4
	
>>> print(PRand(0, 10, seed=1)[:10])
P[2, 9, 1, 4, 1, 7, 7, 7, 10, 6]
>>> print(PRand(0, 10, seed=1)[:10])
P[2, 9, 1, 4, 1, 7, 7, 7, 10, 6]

Patern Uretec Tipleri

PRand(lo, hi, seed=None) / PRand([values])

PRand k?sacas? lo ve hi aras?nda rastgele tam say?lar ?retmektedir. E?er hi de?eri yok say?l?rsa, de?er verilmezse, de?er aral??? 0 ve lo aras?nda otomatik olarak se?ilir. Bir liste lo ve hi yerine koyulursa PRand ?reteci bu de?erler aras?ndan rastgele se?im yapar.

1
2
3
4
5
6
	
>>> PRand(5, 10)[:10]
P[9, 10, 7, 10, 5, 10, 6, 5, 5, 7]
>>> PRand(5)[:10]
P[5, 4, 5, 5, 4, 1, 5, 5, 2, 0]
>>> PRand([1, 2, 3])[:10]
P[3, 2, 2, 2, 1, 3, 3, 2, 2, 1]
PxRand(lo, hi) / PxRand([values])

PRand ile birebir aynidir ancak elemanlar tekrar etmez.
1
2
3
4
5
6
	
>>> PxRand(5, 10)[:10]
P[6, 10, 8, 6, 9, 6, 9, 6, 10, 7]
>>> PxRand(5)[:10]
P[4, 3, 2, 1, 4, 1, 0, 5, 2, 3]
>>> PxRand([1, 2, 3])[:10]
P[2, 3, 2, 1, 3, 2, 3, 1, 3, 2]
PwRand([values], [weights])

Weights listesini kullanarak values listesindeki ayn? indekse sahip elemanin ne siklikla secilecegine karar verir. Ornegin, 2 degeri verilmis bir weight elemani, ayni indeksteki degeri digerlerine gore 2 kat daha fazla olasilikla sefer.

1
2
3
4
	
>>> PwRand([0, 1], [1, 2])[:10]
P[1, 0, 0, 1, 1, 1, 1, 0, 1, 1]
>>> PwRand([0, 1, 2], [1, 2, 3])[:10]
P[1, 2, 2, 2, 2, 2, 0, 2, 2, 1]
PWhite(lo, hi)

Returns random floating point numbers between lo and hi.
1
2
	
>>> PWhite(0,5)[:10]
P[4.19058560392058, 2.776022501076935, 1.0643923909231003, 1.638195673989835, 0.8591848958936567, 2.461472231869311, 3.3546237751457335, 1.1854918335554943, 1.8310777165408907, 1.1767145868610336]
PChain(mapping_dictionary)

Based on a simple Markov Chain of using equal probabilities. Takes a dictionary of items; states and possible future states. Each future state has an equal probability of being chosen. If a possible future state is not valid, a KeyError will be raised.
1
2
3
4
5
6
7
8
	
>>> markov_chain = {
...    0: [3, 4],
...    3: [0, 4, 5],
...    4: [3, 0],
...    5: [3, 4],
... }
>>> PChain(markov_chain)[:10]
P[3, 0, 4, 0, 4, 3, 5, 4, 3, 5]
PWalk(max = 7, step = 1, start = 0)

Returns a series of integers where each element is step size away from each other and value are in the range +/- the max. The first element can be chosen using start.
1
2
3
4
	
>>> PWalk()[:10]
P[0, 1, 2, 1, 2, 3, 2, 3, 4, 5]
>>> PWalk(20, 5, 5)[:10]
P[5, 10, 15, 20, 15, 20, 15, 20, 15, 20]
PDelta(deltas, start = 0)

Takes a list of deltas (small increments/decrements) and returns the series of numbers generated by adding these values together in sequence. Using a single positive number will create an infinitely increasing series. Set the starting value using start.
1
2
3
4
5
6
	
>>> PDelta([0.1, 0.5, -0.3])[:10]
P[0, 0.1, 0.6, 0.3, 0.4, 0.9, 0.6, 0.7, 1.2, 0.9]
>>> PDelta([0.5])[:10]
P[0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
>>> PDelta([0.5, -0.5], start=1)[:10]
P[1, 1.5, 1.0, 1.5, 1.0, 1.5, 1.0, 1.5, 1.0, 1.5]
PSquare()

Returns the series of square numbers.
1
2
3
4
	
>>> PSquare()[:10]
P[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> PSquare()[10:20] % 7
P[2, 2, 4, 1, 0, 1, 4, 2, 2, 4]
PIndex()

Returns the series of whole numbers.
1
2
	
>>> PIndex()[:10]
P[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
PFibMod()

Returns the Fibonacci sequence.
1
2
	
>>> PFibMod()[:10]
P[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
PZ12(tokens = [0, 1], p = [1, 0.5])

Simple implementation of the Z12 algorithm for pre-determined random numbers. Using an irrational value for p, however, results in a non-determined order of values. Experimental ? only works with 2 values.
1
2
3
4
	
>>> PZ12([0, 1], [1, 0.5])[:15]
P[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
>>> PZ12([0, 1], [1, math.sqrt(2)])[:15]
P[1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1
