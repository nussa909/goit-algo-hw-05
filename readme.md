 PS E:\Projects\goit\algo\goit-algo-hw-05> python -u "e:\Projects\goit\algo\goit-algo-hw-05\main.py"
  boyer_moore_search |     real pattern(pos=56)     |   стаття 1.txt(12658)   | 0.00004280
 boyer_moore_search |   real pattern(pos=11480)    |   стаття 1.txt(12658)   | 0.00240590
 boyer_moore_search |     fake pattern(pos=-1)     |   стаття 1.txt(12658)   | 0.00168630
 rabin_karp_search  |     real pattern(pos=56)     |   стаття 1.txt(12658)   | 0.00014890
 rabin_karp_search  |   real pattern(pos=11480)    |   стаття 1.txt(12658)   | 0.01657250
 rabin_karp_search  |     fake pattern(pos=-1)     |   стаття 1.txt(12658)   | 0.03050410
     kmp_search     |     real pattern(pos=56)     |   стаття 1.txt(12658)   | 0.00014950
     kmp_search     |   real pattern(pos=11480)    |   стаття 1.txt(12658)   | 0.01390360
     kmp_search     |     fake pattern(pos=-1)     |   стаття 1.txt(12658)   | 0.01524650
	 
 boyer_moore_search |     real pattern(pos=94)     |   стаття 2.txt(17590)   | 0.00012580
 boyer_moore_search |   real pattern(pos=15561)    |   стаття 2.txt(17590)   | 0.00647710
 boyer_moore_search |     fake pattern(pos=-1)     |   стаття 2.txt(17590)   | 0.00462970
 rabin_karp_search  |     real pattern(pos=94)     |   стаття 2.txt(17590)   | 0.00034620
 rabin_karp_search  |   real pattern(pos=15561)    |   стаття 2.txt(17590)   | 0.04190710
 rabin_karp_search  |     fake pattern(pos=-1)     |   стаття 2.txt(17590)   | 0.05157790
     kmp_search     |     real pattern(pos=94)     |   стаття 2.txt(17590)   | 0.00017410
     kmp_search     |   real pattern(pos=15561)    |   стаття 2.txt(17590)   | 0.02151960
     kmp_search     |     fake pattern(pos=-1)     |   стаття 2.txt(17590)   | 0.02401570

Найкращий результат для пошуку в тексті показав алгоритм Бойера-Мура. Найкращий свій результат він видає коли шуканий підрядок знаходиться на початку текста, значно гірший - якщо підрядок відсутній в тексті і найгірший - якщо підрядок присутній в тексті, але ближче до кінця.

Алгоритм Карпа-Рабіна виявився найповільнішим в цьому тесті. Найкращий результат він видає, якщо підрядок знаходиться на початку текста, а найгірший результат - якщо підрядка немає в тексті.

Алгоритм Кнута-Морріса-Пратта видає середні результати (гірше ніж Бойера-Мура, але краще ніж Карпа-Рабіна). Найкращий результат видає - якщо шуканий підрядок знаходиться на початку текта, і гірші результати - якщо підрядок знаходиться в кінці текста або відсутній взагалі(результати приблизно однакові).

Всі алгоритми показали свій кращий результат на тексті "стаття 1.txt"