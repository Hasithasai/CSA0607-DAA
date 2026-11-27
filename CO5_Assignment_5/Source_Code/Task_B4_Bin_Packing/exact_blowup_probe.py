"""Shows exact search blow-up: n=28 workloads, demands in [26,49]. Aborts after 60 s."""
import random, time, signal
from bin_packing import exact_min_bins
def h(*a): raise TimeoutError
signal.signal(signal.SIGALRM, h); signal.alarm(60)
rnd = random.Random(28); dem = [rnd.randint(26, 49) for _ in range(28)]
t = time.perf_counter()
try:
    print("optimum =", exact_min_bins(dem, 100), "time", round(time.perf_counter() - t, 2), "s")
except TimeoutError:
    print("n=28: exact branch & bound NOT finished after 60 s (greedy FFD answers in < 1 ms)")
