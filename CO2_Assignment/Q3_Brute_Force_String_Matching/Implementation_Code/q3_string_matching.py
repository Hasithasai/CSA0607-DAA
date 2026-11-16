"""Q3: Brute-force exact string matching."""
def brute_force_match(text, pattern):
    n,m=len(text),len(pattern); comparisons=0; matches=[]
    if m==0: return [0],0
    for shift in range(n-m+1):
        j=0
        while j<m:
            comparisons+=1
            if text[shift+j]!=pattern[j]: break
            j+=1
        if j==m: matches.append(shift)
    return matches,comparisons

def main():
    cases=[
      ("Early mismatch","ABCDEFGHIJKLMNOPQRSTUVWXYZ","ZXY"),
      ("Repeated-prefix worst case","A"*30+"B","A"*14+"C"),
      ("Multiple matches","ABABABABABAB","ABAB")
    ]
    print("Q3 BRUTE-FORCE STRING MATCHING")
    for name,t,p in cases:
        hits,c=brute_force_match(t,p)
        print(f"{name}: n={len(t)} m={len(p)} matches={hits} character_comparisons={c}")
if __name__=="__main__": main()
