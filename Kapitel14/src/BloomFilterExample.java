import com.google.common.hash.BloomFilter;
import com.google.common.hash.Funnels;

public class BloomFilterExample {

	public static void main(String[] args) {
		// requires guava-x.x.jar in classpath
		
		// we plan to insert 1000 values with 1 percent error probability (for false positives)
		BloomFilter<Integer> bf = BloomFilter.create(Funnels.integerFunnel(), 1000, 0.01);
		
		bf.put(4);
		bf.put(7);

		System.out.println("contains 0? " + bf.mightContain(0));
		System.out.println("contains 1? " + bf.mightContain(1));
		System.out.println("contains 4? " + bf.mightContain(4));
		System.out.println("contains 7? " + bf.mightContain(7));
		System.out.println("contains 42? " + bf.mightContain(42));	
	}

}
