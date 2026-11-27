"""Task 4 - WordBreak forensics: faulty algorithm vs minimal repair."""

def word_break(text, dictionary, fixed, verbose=False):
    n = len(text)
    dp = [False] * (n + 1); dp[0] = True
    for i in range(1, n + 1):
        dp[i] = False
        for j in range(0, i):
            word = text[j:i]
            ok = (word in dictionary) and (dp[j] if fixed else True)   # the single-line repair: AND dp[j]
            if verbose: print(f"   i={i} j={j} substring='{word}' in dict={word in dictionary} dp[j]={dp[j]} -> {ok}")
            if ok:
                dp[i] = True; break
    return dp[n], dp

def demo(text, d):
    print(f"\nText='{text}', Dictionary={sorted(d)}")
    print(" Original:"); r1, dp1 = word_break(text, d, False, True); print("  dp =", dp1, "->", r1)
    print(" Repaired:"); r2, dp2 = word_break(text, d, True, True); print("  dp =", dp2, "->", r2)
    return r1, r2

if __name__ == "__main__":
    r1, r2 = demo("abcd", {"cd"})            # failing input: truth is FALSE
    assert r1 is True and r2 is False
    r1, r2 = demo("applepie", {"apple", "pie"})   # regression: truth is TRUE
    assert r1 is True and r2 is True
    r1, r2 = demo("abc", {"x"})              # regression: truth is FALSE
    assert r1 is False and r2 is False
    print("\nAll Task 4 tests passed.")
