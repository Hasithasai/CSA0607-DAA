"""Q2: Sequential search for tool records."""
def sequential_search(records, target):
    comparisons=0
    for index,record in enumerate(records):
        comparisons+=1
        if record["tool_id"]==target:
            return record,comparisons,index
    return None,comparisons,-1

def main():
    print("Q2 SEQUENTIAL SEARCH")
    for n in (10,100,1000):
        records=[{"tool_id":f"T-{i:04d}","technician":f"TECH-{i%17:02d}","issue_time":f"2026-11-16 {i%24:02d}:00","bay":f"B-{i%5+1}"} for i in range(n)]
        tests=[("first",records[0]["tool_id"]),("middle",records[n//2]["tool_id"]),("last",records[-1]["tool_id"]),("missing","T-MISSING")]
        for label,target in tests:
            found,c,index=sequential_search(records,target)
            print(f"n={n:4d} case={label:6s} target={target:10s} comparisons={c:4d} result={'FOUND' if found else 'NOT FOUND'}")
if __name__=="__main__": main()
