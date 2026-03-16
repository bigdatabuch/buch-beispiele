import java.util.stream.IntStream;

import com.tdunning.math.stats.AVLTreeDigest;
import com.tdunning.math.stats.TDigest;

public class TDigestExample {
	// requires t-digest-x.x.jar in classpath

	public static void main(String[] args) {
		TDigest td = new AVLTreeDigest(10);	

		// add a thousand numbers 
		IntStream.range(0, 1000).forEach(n -> td.add(n));

		// print quantiles
		for (double d = 0; d <= 1; d += 0.05)
			System.out.printf("Quantile %.2f -> %.1f%n", d, td.quantile(d));
		
		// print cumulated distribution function, i.e. what proportion of the data is small than x?
		System.out.println();
		System.out.println("Proportion of data smaller than x? -> " + td.cdf(5));
	}

}
