# Generałowie sił powietrznych Bajtocji: Bajtek, Kajtek i Zajtek zamierzają przeprowadzić pierwszą w historii Bajtocji wielką wyprawę kosmiczną. Każdy z nich zgromadził już pewną ilość paliwa rakietowego i właśnie szykują się na zakup modułów, z których złożą rakietę. Bajtockie rakiety są skonstruowane w ten sposób, że w początkowym fragmencie lotu są napędzane tylko przez pierwszy moduł, po zużyciu się paliwa w tym module zostaje on odrzucony i odtąd napędu rakiecie dostarcza drugi moduł itd.

# Każdy z generałów odwiedzi dzisiaj swoją ulubioną fabrykę i zakupi moduł z silnikiem rakietowym o pewnej sprawności; z tych trzech modułów ustawionych w ustalonej kolejności (Bajtek kupuje dolny, Kajtek - środkowy, a Zajtek - górny) zostanie złożona rakieta. Maksymalny zasięg tej rakiety (tj. największa odległość, na jaką może ona dolecieć) będzie równy sumie zasięgów poszczególnych modułów, z których każdy jest wyrażony jako iloczyn sprawności silnika oraz objętości zatankowanego do modułu paliwa.

# Ze względu na wzrastające ceny w fabrykach, generałowie być może nie zakupią modułów o największych sprawnościach. Chcieliby więc poznać liczbę różnych trójek modułów, które mogą zakupić (każdy generał po jednym module ze swojej fabryki), takich że złożona z nich rakieta będzie miała zasięg większy niż połowa zasięgu najlepszej rakiety, jaka mogłaby powstać przy aktualnym asortymencie fabryk, tj. gdyby każdy generał kupił najsprawniejszy moduł. Różne moduły o tych samych sprawnościach są przy zliczaniu uznawane za różne.

# Napisz program, który:

# wczyta ze standardowego wejścia asortymenty fabryk, które odwiedzą generałowie oraz ilości paliwa rakietowego, jakie posiadają,
# obliczy liczbę trójek modułów spełniających wymogi Bajtka, Kajtka i Zajtka,
# wypisze wynik na standardowe wyjście.

import sys
import bisect

b,k,z = map(int,sys.stdin.readline().split())

g1 = int(sys.stdin.readline())
graph1 = list(map(int,sys.stdin.readline().split()))

g2 = int(sys.stdin.readline())
graph2 = list(map(int,sys.stdin.readline().split()))

g3 = int(sys.stdin.readline())
graph3 = list(map(int,sys.stdin.readline().split()))

graph1.sort()
graph2.sort()
graph3.sort()


half = int((graph1[-1]*b+graph2[-1]*k+graph3[-1]*z)/2)

ans = 0

for i in range(g1):
    for j in range(g2):
        t = graph1[i]*b+graph2[j]*k
        
        num = bisect.bisect_right(graph3,(half-t)//z)
        ans += g3-num
print(ans)