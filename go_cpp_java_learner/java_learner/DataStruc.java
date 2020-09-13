import java.util.*;
import java.util.Arrays;

class Test {
	public static void main(String[] args) {
		/* Arrays */
		// sort and toString
		int [] a = {19, 27, 3, 6, 15, 9, 11, 0, 3, 13, 25};
		Arrays.sort(a); // if you directly print "a", it will get the RAM address
		
		// so we use toString mehtod transfer address --> string
		System.out.println(Arrays.toString(a));
		
		// arrays --> list
		System.out.println("the list of 'a' is " + Arrays.asList(a));
		
		// search(binary search)
        // find the location of goal elements
        System.out.println("use binary search, the index of '27' is "+Arrays.binarySearch(a, 27));
		
		// fill : filliing with somthing(e.g. 1)
		int[] d1 = new int[3];
		Arrays.fill(d1, 1);
		System.out.println(Arrays.toString(d1));




		/* ArrayList */
		// ArrayList (no length limit)
		// build ArrayList in two ways
		ArrayList<Integer> l1 = new ArrayList<Integer>();
		ArrayList<Integer> l2 = new ArrayList<Integer>();
		// add, add(int idx, Obeject c)   remove,  remove(int index, Object o) 
		l1.add(0);l2.add(20);
		l1.add(1);l2.add(30);
		l1.add(2);l2.add(10);
		l1.remove(2);
		System.out.println("the list 'l1' is " + l1);
		
		// set : Replaces the element at the specified position
		l1.set(0, -99);
		System.out.println("replace index 0 element with -99 "+l1);

		//clone: clone ArrayList
		ArrayList<Integer> cl1 = (ArrayList<Integer>)l1.clone();
		
		//addAll(Collection c), addALL(int start, Collection c)
		cl1.addAll(1, l2);
		System.out.println("clone of l1 is "+cl1);
		
		// subList: splite arrayList
		List<Integer> sub = cl1.subList(0, 3);
		ArrayList<Integer> sub2 = new ArrayList<Integer>(sub);
		System.out.println("sub list of cl1 from 0 to 3 is "+sub2);

		// size(): get size of ArrayList
		System.out.println("the size of cl1 is "+cl1.size());

		// isEmpty()
		System.out.println("is cl1 emtpy? "+cl1.isEmpty());

		// contains(object o)
		System.out.println("is cl1 cotain 1? "+cl1.contains(1));

		// get: get element based on index,   indexOf: get index based on element
		System.out.println("get element that index equal to 1, "+cl1.get(1));
		System.out.println("get index that element is 1, "+cl1.indexOf(1));

		// toArray()
		System.out.println("the array of cl1 is "+ Arrays.toString(cl1.toArray()));



		/* Map */
		// create HashMap
		Map<String, Integer> map = new HashMap<String, Integer>();
		
		// put, get, clear: remove all, remove: remove k-v pair
		map.put("no1", 100);
		map.put("no2", 200);
		map.put("no3", 300);
		System.out.println("get key:no1 value is "+map.get("no1"));
		
		// remove
		map.remove("no3");

		// size: check map size
		System.out.println("the size of map is "+map.size());

		// keySet: get key set
		ArrayList<String> kl = new ArrayList<String>(map.keySet());
		System.out.println("the key set is "+kl);
		
		// Values: get values set
		ArrayList<Integer> vl = new ArrayList<Integer>(map.values());
		System.out.println("the value set is "+vl);

		// containsValue / containsKey
		System.out.println("does map include key 'no1'? "+map.containsKey("no1"));
		System.out.println("does map include value 100? "+map.containsValue(100));



		/* HashSet */

		// add, clear, clone, contains, isEmpty, remove, size
		HashSet<Integer> s = new HashSet<Integer>();
		s.add(1);
		s.add(1);
		s.add(2);
		s.add(3);
		System.out.println("the set s is "+s);

		// remove
		s.remove(3);
		System.out.println("the set s is "+s);

	}
}
