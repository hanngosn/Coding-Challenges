import java.util.ArrayList;
import java.util.List;

/* Calculate the height of tree after some circulations. 
Default height of the tree is 1. After the first season, 
the height is doubled. After the second season, the height is 
growing 1 more unit. 
Input format includes <1> the number of test samples
		      <2> test sample 1
		      <3> tets sample 2
*/

public class Tree {
	
	
	public Tree(){
	
	}

	
	public static void main(String[] args){
		
		 int[] numbers = {2,3,4};
		 for(int i = 1; i < numbers.length; i++)
			 System.out.println(tree(numbers[i]));
	
	
	public static int tree(int n){
		if (n==0)
			return 1;
		else if(n==1)
			return 2;
		else if(n==2)
			return 3;
		else if(n%2 == 0)
			return tree(n-1)+1;
		return tree(n-1)*2;
	}

}
	

