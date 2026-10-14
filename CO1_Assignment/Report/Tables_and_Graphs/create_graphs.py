import csv, os
import matplotlib.pyplot as plt
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
csv_path=os.path.join(ROOT,'Report','Documentation','supplied_single_run.csv')
rows=list(csv.DictReader(open(csv_path)))
algos=['Linear Search','Recursive Binary Search','Hash Table Search']
sizes=sorted(set(int(r['n']) for r in rows))
# Total-time chart (log scale because magnitudes differ)
for metric, title, ylabel, filename in [
 ('total_ms','Measured total time by dataset size','Total time (ms)','total_time.png'),
 ('count_metric_value','Operation metric by dataset size','Count (note: hash calls are not comparisons)','operation_counts.png')]:
    plt.figure(figsize=(9,5.5))
    for algo in algos:
        subset=[r for r in rows if r['algorithm']==algo]
        vals=[float(next(r[metric] for r in subset if int(r['n'])==n)) for n in sizes]
        plt.plot(sizes, vals, marker='o', label=algo)
    plt.xscale('log'); plt.yscale('log'); plt.xlabel('Number of student records (n)'); plt.ylabel(ylabel); plt.title(title); plt.grid(True, which='both', linestyle='--', alpha=.35); plt.legend(); plt.tight_layout(); plt.savefig(os.path.join(os.path.dirname(__file__),filename),dpi=180); plt.close()
