import java.util.*;

class InsertSort {
	public static int[] sort(int[] l) {
		if (l == null)
			return 0;
		for (int i = 0; i < l.length; i++) {
			int min = i;
			for (int j = i+1; j < l.length; j++) {
				if (l[j] < l[min]) {
					min = j; // find index of minimum value
				}
			}
			int temp = l[i];
			l[i] = l[min];
			l[min] = temp;
		}
		return l;
	}
	public static void main(String[] args) {
		int[] l = {6, 5, 4, 3, 2, 1, 9};
		l = sort(l);
		System.out.println(Arrays.toString(l));
	}
}
