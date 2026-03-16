import java.util.stream.LongStream;

import com.google.common.hash.HashFunction;
import com.google.common.hash.Hashing;

import net.agkn.hll.HLL;

public class HyperLogLogExample {
	// requires hll-x.x.x.jar, guava-x.x-jre.jar, and fastutil-x.x.x.jar in classpath

	public static void main(String[] args) {
		HashFunction hf = Hashing.murmur3_128();
		HLL hll = new HLL(14, 5);

		LongStream
			.range(0, 1000000)
			.forEach(n -> hll.addRaw(hf.newHasher().putLong(n).hash().asLong()));

		System.out.println("Estimated Cardinality by HyperLogLog: " + hll.cardinality());
	}

}
