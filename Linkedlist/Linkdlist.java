import java.util.Random;

public class Linkdlist {
	
	public static void main(String[] args) {
		
		Node a = new Node(1);
		
		Linkdlist list = new Linkdlist();
		list.initiatingLL(a);
		a.deleteNode(a, 4);
		a = list.removeDuplicates(a);
		
		/**Check**/
		System.out.println(a.data);
		while(a.next!= null){
			System.out.println(a.next.data);
			a = a.next;
		}
	
	}

/** Create the linked list with a given array list **/ 
	public Node initiatingLL(Node head){
		int[] list = {1,2,4,2,3,5,2};
		
		for(int i = 0; i < list.length; i++)
			head.insertAtTail(list[i]);
		
		return head;
	}
	
/**	2.1CTCI - Write code to remove duplicates from an unsorted linked list. 
 			  with no temporary buffer being allowed **/
	public Node removeDuplicates(Node head){
		
		Node ptr1 = head; 
		Node ptr2 = head;
		
		while(ptr1.next != null){
			while(ptr2.next != null){
				if(ptr1.data == ptr2.next.data){
					System.out.println("Duplicate: " + ptr1.data);
					ptr2.next = ptr2.next.next;
				}
				ptr2 = ptr2.next;
			}
			ptr1 = ptr1.next;
		}
		
		
		
		return head;
	}
	
	
	


}
