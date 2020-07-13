#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int i;
	cin>>i;
	while(true){
	if (i==1)
	break;
	if (i%2==0)
	i/=2;
	else
	i=i*3+1;
	
	}
	cout<<i;
	return 0;
}
