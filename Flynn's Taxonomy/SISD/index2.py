import math
import time

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def sisd_prime_analysis(start, end):
    primes = []
    prime_sum = 0
    
    for number in range(start, end):   # Tek veri akışı
        if is_prime(number):           # Tek instruction akışı
            primes.append(number)
            prime_sum += number
    
    count = len(primes)
    average = prime_sum / count if count > 0 else 0
    
    return count, prime_sum, average


# Büyük aralık
start_time = time.time()

count, total_sum, avg = sisd_prime_analysis(1, 200000)

end_time = time.time()

print("Toplam asal sayı:", count)
print("Asalların toplamı:", total_sum)
print("Ortalama:", avg)
print("Çalışma süresi:", end_time - start_time, "saniye")

