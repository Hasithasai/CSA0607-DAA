"""Task 1 - Repaired LoadVehicle algorithm (Fractional Knapsack, greedy by value/weight)."""

def load_vehicle(packages, capacity):
    # packages: list of (id, weight, value); returns (total_value, loads, remaining)
    items = [p for p in packages if p[1] > 0 and p[2] >= 0]
    items.sort(key=lambda p: p[2] / p[1], reverse=True)     # greedy-choice rule
    remaining, total, loads = capacity, 0.0, []
    print(f"Capacity = {capacity}")
    print("Order by value/weight:", [(p[0], round(p[2] / p[1], 2)) for p in items])
    for pid, w, v in items:
        if remaining <= 0:
            break                                            # vehicle full
        if w <= remaining:                                   # whole package fits
            frac = 1.0
        else:                                                # only a fraction fits
            frac = remaining / w
        gain = frac * v
        loads.append((pid, frac, frac * w, gain))
        remaining -= frac * w
        total += gain
        print(f"  take {pid}: fraction={frac:.3f} weight={frac*w:.1f} gain={gain:.1f} remaining={remaining:.1f}")
    return total, loads, remaining

def run(name, packages, capacity):
    print(f"\n=== {name} ===")
    total, loads, rem = load_vehicle(packages, capacity)
    print(f"Total value = {total:.2f}, unused capacity = {rem:.1f}")
    return total

if __name__ == "__main__":
    pk = [("P1", 10, 60), ("P2", 20, 100), ("P3", 30, 120)]
    assert abs(run("Main test", pk, 50) - 240) < 1e-9
    assert run("Capacity 0", pk, 0) == 0
    assert abs(run("Capacity exceeds total weight", pk, 100) - 280) < 1e-9
    assert abs(run("Single package, fractional", [("X", 8, 40)], 2) - 10) < 1e-9
    print("\nAll Task 1 tests passed.")
