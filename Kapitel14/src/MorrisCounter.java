public class MorrisCounter {
	// Count to large numbers with fewer bits (non-deterministic!)

	public static void main(String[] args) {
		byte x = 0;		// the actual variable for the Morris way of counting
		
		for (int c = 0; c < 1000; c++) {
			
			double inc = Math.random() * Math.pow(2, x);
			if (inc <= 1)
				x++;

			System.out.println(c + " -> estimated number: " + (int)(Math.pow(2, x) - 1) + "; x = " + x);
		}
				
	}

}
