package de.hsma.bdea;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;

public class CardGenerator {

	public static void main(String[] args) throws FileNotFoundException {
		String[] farben = {"Kreuz", "Pik", "Herz", "Karo"};
		String[] werte = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "As"};
		
		System.setOut(new PrintStream(new FileOutputStream("/tmp//karten.csv")));
		
		for (int i = 0; i < 123294; i++) {
			System.out.println(i + ", " + farben[(int)(Math.random() * 4)] + ", " + werte[(int)(Math.random() * 13)]);
		}

	}

}
