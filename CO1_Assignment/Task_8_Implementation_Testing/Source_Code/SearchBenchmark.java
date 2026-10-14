import java.io.*;
import java.nio.file.*;
import java.util.*;

/**
 * CO1 Assignment: exact student registration-number search benchmark.
 * Run: javac SearchBenchmark.java && java SearchBenchmark [queriesPerSize]
 * The program writes benchmark_results.csv in the working directory.
 */
public class SearchBenchmark {
    static long linearComparisons;
    static long binaryComparisons;

    static int linearSearch(int[] a, int key) {
        for (int i = 0; i < a.length; i++) {
            linearComparisons++;
            if (a[i] == key) return i;
        }
        return -1;
    }

    static int recursiveBinarySearch(int[] a, int key, int low, int high) {
        if (low > high) return -1;
        int mid = low + (high - low) / 2;
        binaryComparisons++;
        if (a[mid] == key) return mid;
        if (key < a[mid]) return recursiveBinarySearch(a, key, low, mid - 1);
        return recursiveBinarySearch(a, key, mid + 1, high);
    }

    static int[] makeData(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = 1_000_000 + i;
        return a;
    }

    static long elapsedNanos(Runnable r) {
        long start = System.nanoTime(); r.run(); return System.nanoTime() - start;
    }

    static String ms(long ns) { return String.format(Locale.US, "%.3f", ns / 1_000_000.0); }

    public static void main(String[] args) throws Exception {
        int q = args.length > 0 ? Integer.parseInt(args[0]) : 1000;
        int[] sizes = {1_000, 10_000, 100_000, 1_000_000};
        Random random = new Random(20261014L);
        Path output = Paths.get("benchmark_results.csv");
        try (PrintWriter out = new PrintWriter(Files.newBufferedWriter(output))) {
            out.println("n,algorithm,preprocessing_ms,lookup_ms,total_ms,queries,comparisons_or_calls,verified");
            for (int n : sizes) {
                int[] data = makeData(n);
                int[] queries = new int[q];
                // Half successful, half unsuccessful; deterministic seed per dataset size.
                Random r = new Random(20261014L + n);
                for (int i = 0; i < q; i++) {
                    queries[i] = (i % 2 == 0) ? data[r.nextInt(n)] : (2_000_000 + r.nextInt(n));
                }

                final boolean[] verified = {true};
                linearComparisons = 0;
                long linearLookup = elapsedNanos(() -> {
                    for (int key : queries) {
                        int found = linearSearch(data, key);
                        if ((found >= 0) != (key >= 1_000_000 && key < 1_000_000 + n)) verified[0] = false;
                    }
                });
                out.printf(Locale.US, "%d,Linear Search,0.000,%s,%s,%d,%d,%s%n", n,
                        ms(linearLookup), ms(linearLookup), q, linearComparisons, verified[0]);

                // Data is already sorted by construction. Include a sorting pass as preprocessing measurement.
                int[] sorted = Arrays.copyOf(data, data.length);
                long binaryPrep = elapsedNanos(() -> Arrays.sort(sorted));
                binaryComparisons = 0; verified[0] = true;
                long binaryLookup = elapsedNanos(() -> {
                    for (int key : queries) {
                        int found = recursiveBinarySearch(sorted, key, 0, sorted.length - 1);
                        if ((found >= 0) != (key >= 1_000_000 && key < 1_000_000 + n)) verified[0] = false;
                    }
                });
                out.printf(Locale.US, "%d,Recursive Binary Search,%s,%s,%s,%d,%d,%s%n", n,
                        ms(binaryPrep), ms(binaryLookup), ms(binaryPrep + binaryLookup), q, binaryComparisons, verified[0]);

                HashSet<Integer> index = new HashSet<>(Math.max(16, (int)(n / 0.75f) + 1));
                long hashPrep = elapsedNanos(() -> { for (int id : data) index.add(id); });
                verified[0] = true;
                long hashLookup = elapsedNanos(() -> {
                    for (int key : queries) {
                        boolean found = index.contains(key);
                        if (found != (key >= 1_000_000 && key < 1_000_000 + n)) verified[0] = false;
                    }
                });
                out.printf(Locale.US, "%d,Hash Table Search,%s,%s,%s,%d,%d,%s%n", n,
                        ms(hashPrep), ms(hashLookup), ms(hashPrep + hashLookup), q, q, verified[0]);
                System.out.printf("n=%d completed; verified=%s%n", n, verified[0]);
            }
        }
        System.out.println("Results written to " + output.toAbsolutePath());
    }
}
