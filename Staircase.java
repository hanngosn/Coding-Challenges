//Input value: n = 6
//Output should be:
//     #
//    ##
//   ###
//  ####
// #####
//######


int n = 6;
String hash = "";
for(int i = 1; i <= n; i++){
	String sp = "";
	for (int k = 1; k <= n-i; k++){
	sp = " " + sp;
	}
	hash = "#" + hash ;
	System.out.println(sp + hash);
}
