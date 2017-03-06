
public class Node {

	Node next = null; 
	int data; 
	
	public Node(int d){
		data = d;
	}
	
	public void insertAtTail(int val){
		Node tmp = new Node(val);
		Node n = this;
		while(n.next != null)
			n = n.next;
		n.next = tmp;
	}
	
	public Node deleteNode(Node head, int val){
		Node ptr = head;
		
		//moved head
		if(ptr.data == val)
			return head.next;
		
		while(ptr.next != null){
			if(ptr.next.data == val){
				ptr.next = ptr.next.next;
				return head;
			}
			ptr = ptr.next;
		}
		
		return head;
		
	}
		
}
