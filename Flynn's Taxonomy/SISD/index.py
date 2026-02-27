# SISD örneği: Sequential (tek akış) hesaplama

def sisd_sum(data):
    total = 0
    for value in data:   # Tek veri akışı
        total += value   # Tek instruction akışı
    return total

# Veri kümesi
numbers = list(range(1, 10_000_001))
# Hesaplama
result = sisd_sum(numbers)

print("Toplam:", result)
