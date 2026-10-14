import java.util.Locale;

/**
 * ShopSphere Scalability Audit
 * CSA06 - Design and Analysis of Algorithms, CO1 AT1
 *
 * Counts are theoretical estimates based on the models stated in the question.
 * The program does not access real e-commerce data.
 */
public class ShopSphereScalabilityAudit {
    private static final double OPS_PER_SECOND = 10.0;
    private static final double NIGHTLY_WINDOW_SECONDS = 10.0 * 60.0;

    private static double log2(double n) {
        return Math.log(n) / Math.log(2.0);
    }

    private static String format(double value) {
        return String.format(Locale.US, "%,.2f", value);
    }

    private static String duration(double operations) {
        double seconds = operations / OPS_PER_SECOND;
        if (seconds < 60) return format(seconds) + " seconds";
        if (seconds < 3600) return format(seconds / 60) + " minutes";
        if (seconds < 86400) return format(seconds / 3600) + " hours";
        if (seconds < 365.25 * 86400) return format(seconds / 86400) + " days";
        return format(seconds / (365.25 * 86400)) + " years";
    }

    private static void printEstimate(String module, double operations, String note) {
        System.out.printf("%-25s %18s ops | %18s | %s%n",
                module, format(operations), duration(operations), note);
    }

    public static void main(String[] args) {
        long nCurrent = 100_000L;
        long nFuture = 1_000_000L;
        long nM2Check = 1_024L;

        System.out.println("==============================================================");
        System.out.println("       SHOPSPHERE E-COMMERCE SCALABILITY AUDIT");
        System.out.println(" CSA06 - Design and Analysis of Algorithms | CO1 AT1 | Java");
        System.out.println("==============================================================");
        System.out.println("Assumption: 10 basic operations per second; nightly window = 600 seconds.");
        System.out.println();

        System.out.println("(b) ITERATIVE MODULES");
        double m1Current = (double) nCurrent * (nCurrent - 1) / 2.0;
        double m1Future = (double) nFuture * (nFuture - 1) / 2.0;
        System.out.println("M1 exact comparisons = n(n-1)/2");
        System.out.println("  n = " + nCurrent + ": " + format(m1Current));
        System.out.println("  n = " + nFuture + ": " + format(m1Future));
        System.out.println("  Time: Theta(n^2); auxiliary space: O(1), excluding stored duplicate marks.");
        System.out.println();

        int m2Iterations = (int) Math.ceil(log2(nM2Check));
        long m2CheckCount = (1L << m2Iterations) - 1L;
        int m2FutureIterations = (int) Math.ceil(log2(nFuture));
        long m2FutureCount = (1L << m2FutureIterations) - 1L;
        System.out.println("M2 exact Audit count = 2^ceil(log2(n)) - 1 (for integer n >= 1)");
        System.out.println("  n = " + nM2Check + ": " + m2CheckCount + " Audit operations");
        System.out.println("  n = " + nFuture + ": " + m2FutureCount + " Audit operations");
        System.out.println("  Team claim Theta(n log n): INCORRECT; tight bound is Theta(n).");
        System.out.println();

        System.out.println("(c) RECURSIVE BINARY SEARCH");
        System.out.println("Recurrence: T(n) = T(n/2) + 1, T(1) = 1.");
        System.out.println("Backward substitution: T(n) = T(n/4) + 2");
        System.out.println("  = T(n/8) + 3 = ... = T(n/2^k) + k.");
        System.out.println("Set n/2^k = 1 => k = log2(n); T(n) = 1 + log2(n) for powers of 2.");
        System.out.println("  At n = " + nFuture + ", log2(n) = " + format(log2(nFuture))
                + "; practical comparison estimate is about 20.");
        System.out.println("  Time: Theta(log n); recursive auxiliary stack: Theta(log n).");
        System.out.println("  Iterative binary search auxiliary space: Theta(1).");
        System.out.println();

        System.out.println("(d) MASTER THEOREM RESULTS");
        System.out.println("M4 current: T(n)=4T(n/2)+n; a=4, b=2, f(n)=n, n^(log_b(a))=n^2.");
        System.out.println("  Master Theorem Case 1 => Theta(n^2).");
        System.out.println("M4 redesign: T(n)=2T(n/2)+n; a=2, b=2, f(n)=n, n^(log_b(a))=n.");
        System.out.println("  Master Theorem Case 2 => Theta(n log n).");
        System.out.println("M5: T(n)=2T(n/2)+n log n => extended Case 2 => Theta(n(log n)^2).");
        System.out.println();

        System.out.println("(f) REPORT GENERATOR BOUND");
        System.out.println("f(n)=3n^2+10n log2(n)+50 is Theta(n^2), and is not O(n).");
        System.out.println("For n >= 1, log2(n) <= n, so f(n) <= 3n^2+10n^2+50n^2 = 63n^2.");
        System.out.println("Also f(n) >= 3n^2. Thus c1=3, c2=63, n0=1 prove Theta(n^2).");
        System.out.println("f(n)/n >= 3n grows without bound, so f(n) is not O(n).");
        System.out.println();

        System.out.println("(g) FUTURE CATALOGUE: n = 1,000,000");
        System.out.println("Estimated dominant-operation counts and time at 10 operations/second:");
        double m5Proxy = nFuture * log2(nFuture) * log2(nFuture);
        double m4RedesignProxy = nFuture * log2(nFuture);
        printEstimate("M1 duplicate detector", m1Future, "EXCEEDS 10-minute window");
        printEstimate("M2 rate limiter", m2FutureCount, "EXCEEDS 10-minute window");
        printEstimate("S2 binary search", 20, "WITHIN 10-minute window; about 20 comparisons");
        printEstimate("M4 current (n^2 proxy)", (double) nFuture * nFuture,
                "EXCEEDS 10-minute window; quadratic proxy");
        printEstimate("M4 redesign (n log n)", m4RedesignProxy,
                "EXCEEDS 10-minute window at the stated 10 ops/s");
        printEstimate("M5 analytics (n log^2 n)", m5Proxy,
                "EXCEEDS 10-minute window; asymptotic proxy");
        System.out.println();
        System.out.println("Decision: redesign M1 using hashing/sorting; optimize M2 to process only");
        System.out.println("the required request window; retain indexed binary search for S2.");
        System.out.println("Remove replication in M4, then benchmark and optimize constants/parallelism.");
        System.out.println("For M5, consider more efficient sorting/aggregation and incremental reports.");
        System.out.println("Note: asymptotic proxies estimate growth; real timings require benchmarking.");
        System.out.println("==============================================================");
    }
}

