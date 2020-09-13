import java.util.*; // include collection(e.g. ArrayList, List, Map, Set, Dequeue, Comparator, Iterator, Queue, Arrays, Stack, Vector, PriorityQueue, )

class Test {
	public static void main(String[] args) {
		// print(String s)
		// print and println
		System.out.print("print s");
		System.out.println("print s in line");

		// double methods
		// abs
		double a = -323.321;
		System.out.print("abs(-323.312) = "+Math.abs(a));
		// power 
		System.out.println("power of 2 is "+Math.pow(2, 3));
		// sqrt
		System.out.println("sqrt of 2 is "+Math.sqrt(2));
		// round
		System.out.println("round(-323.312) = "+Math.round(a));
		// random[0, 1)
		System.out.println("a random number betweem 0 and 1 is "+Math.random());
		// random[0, 1)
		System.out.println("a random number betweem 0 and 100 is "+Math.round(Math.random()*100));
		// e
		System.out.println("e is "+Math.E);
		// PI
		System.out.println("pi is "+Math.PI);

		// type conversion
		System.out.println("Type Conversion");
		int b = Integer.parseInt("1234");
		System.out.println("String -> int"+b); 
		int c = (int) 2131.323;
		System.out.println("float -> int"+c); 
		
		// do-while loop
		System.out.println("test do-while loop");
		int x = 0;
		do {
			 x++;
			 System.out.print(x+" ");
		} while (x < 5);

		//Arrays
		// String array with initialized values
		String[] sarr = {"A", "B", "C", "D", "E", "1", "2", "3"};
		// double array
		double[] darr = new double[3];
		// 2d-int arra 
		int[][] tdarr = new int[3][3];
		System.out.println("2d array is \n"+tdarr);

		// String process
		System.out.println();
		String words = "this is a words";
		char[] carr = {'a', 'b', 'c', 'd', 'e'};
		// charAr : get char from string based on index
		System.out.println("word index 2 is "+words.charAt(2));
		// subString method: get part of the string
		System.out.println("the sub String of words is \""+words.substring(0, words.length() - 1)+"\"");
		// contains: String contains
		System.out.println("string contains part of string "+words.contains("words"));
		// startsWith(boolean) : start with some string
		System.out.println("is words start with \"this\"? "+words.startsWith("this"));
		// endsWith(boolean) : end with some string
		System.out.println("is words end with \"words\"? "+words.endsWith("words"));
		// indexOf(String s): index fo first occurrence of s
		// indexOf(String s, int i) index of occuurrence of s after i
		System.out.println("the index \"this\" in words is "+words.indexOf("this"));
		// concat :String A + String B
		String words2 = new String(carr);
		System.out.println("concat words and carr"+words.concat(words2));
		// compareTo(String s): compare string based on ascii-code
		System.out.println("A is bigger than B ? "+"A".compareTo("B"));
		// toLowerCase(),  toUpperCase(), replace(String a, String b)
		System.out.println("the lower case of A is "+"A".toLowerCase());
		System.out.println("the upper case of b is "+"b".toUpperCase());
		// replace(old_string, new_string)
		System.out.println("we use that to replace this, and result: "+words.replace("this", "that"));
		// trim : delete toside space
		// splite : splite by something, such as " ", return output is String[]
		System.out.println("after splite, we get "+words.split(" "));
	}
}
