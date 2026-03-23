import time
import math

print("=" * 60)
print("CPU CLOCK SPEED SİMÜLATÖRÜ")
print("=" * 60)

def simulate_cpu(clock_speed_ghz, num_operations):
    cycles_per_second = clock_speed_ghz * 1_000_000_000
    return num_operations / cycles_per_second

def measure_real_performance(num_operations):
    start = time.perf_counter()
    for i in range(1, num_operations + 1):
        math.sqrt(i)
    return time.perf_counter() - start

def format_time(seconds):
    if seconds < 1e-6:
        return f"{seconds * 1e9:.4f} ns"
    elif seconds < 1e-3:
        return f"{seconds * 1e6:.4f} µs"
    elif seconds < 1:
        return f"{seconds * 1e3:.4f} ms"
    else:
        return f"{seconds:.4f} s"

# 1) Teorik süre analizi
print("\n📊 1) Teorik Süre Analizi (1 Milyon İşlem)")
print("-" * 60)
operations = 1_000_000
clock_speeds = [1.0, 2.4, 3.6, 4.8, 5.5]
print(f"{'Clock Speed (GHz)':<22} {'Tahmini Süre':<20} {'İşlem/Saniye'}")
print("-" * 60)
for ghz in clock_speeds:
    est_time = simulate_cpu(ghz, operations)
    ops_per_sec = operations / est_time
    print(f"{ghz:<22} {format_time(est_time):<20} {ops_per_sec:,.0f}")

# 2) Gerçek Python performansı
print("\n⚡ 2) Gerçek Python Performans Ölçümü")
print("-" * 60)
for size in [10_000, 100_000, 1_000_000, 5_000_000]:
    elapsed = measure_real_performance(size)
    print(f"{size:>12,} işlem  →  Süre: {format_time(elapsed):<15}  Verim: {size/elapsed:>15,.0f} işlem/sn")

# 3) Hız karşılaştırması
print("\n🔁 3) Clock Speed Arttıkça Ne Olur?")
print("-" * 60)
base_time = simulate_cpu(1.0, operations)
for ghz in clock_speeds:
    speedup = base_time / simulate_cpu(ghz, operations)
    bar = "█" * int(speedup * 5)
    print(f"{ghz} GHz  →  {speedup:5.1f}x hız  {bar}")

# 4) Moore Yasası
print("\n📈 4) Moore Yasası Simülasyonu (Her 2 Yılda 2x Transistör)")
print("-" * 60)
base_transistors = 2_300
base_year = 1971
print(f"{'Yıl':<8} {'Transistör Sayısı':<25} {'Görsel'}")
print("-" * 60)
for i in range(0, 13):
    year = base_year + i * 2
    t = base_transistors * (2 ** i)
    bar = "▮" * min(i + 1, 20)
    if t >= 1_000_000_000:
        label = f"{t/1_000_000_000:.1f} Milyar"
    elif t >= 1_000_000:
        label = f"{t/1_000_000:.1f} Milyon"
    elif t >= 1_000:
        label = f"{t/1_000:.1f} Bin"
    else:
        label = f"{t}"
    print(f"{year:<8} {label:<25} {bar}")

# 5) Özet
print("\n" + "=" * 60)
print("📌 ÖZET")
print("=" * 60)
print("""
  • Clock Speed (GHz): İşlemcinin 1 saniyede kaç cycle
    tamamladığını gösterir.

  • 1 GHz = 1 milyar cycle/saniye

  • Clock speed arttıkça → daha fazla işlem/saniye
    → daha iyi performans

  • Moore Yasası: Her ~2 yılda transistör sayısı 2 katına
    çıkar → daha hızlı ve güçlü işlemciler

  • Parallel Programming ile bağlantı:
    Tek çekirdek yerine çok çekirdek kullanarak
    clock speed sınırını aşmak mümkündür!
""")
print("=" * 60)