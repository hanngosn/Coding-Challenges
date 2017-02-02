String a = "abcd";
String b = "ksleee";		#akbscldeee
int i = 0;
		
String s1 = "";
while(i < a.length() && i < b.length()){
	s1 = s1+ "" + a.charAt(i) + b.charAt(i);
	i++;
}

s1 = s1+ a.substring(i)+ b.substring(i);
		
System.out.println(s1);
