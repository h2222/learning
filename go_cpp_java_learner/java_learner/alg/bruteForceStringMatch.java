class BruteForceStringMatch {
	public static int match(String s, String target) {
		int n = s.length();
		int m = target.length();
		for (int i = 0; i < n - m; i++) {
			int j = 0;
			while (j < m && target.charAt(j) == s.charAt(i+j)) {
				j += 1;
			}
			if (j == m) {
				return i;
			}
		}
		return -1;
	}

	public static void main(String[] args) {
		String s = "It is never to late to study and improve yourself.";
		String target = "yourself";
		System.out.println(match(s, target));

	}
}
