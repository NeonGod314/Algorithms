#include<iostream>
#include<string>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);  
    string s;
    register int order=0;
    cin>>s;
    int sum1=0;
    int sum2=0;
    int sum3=0;
    for(int i=0;i<s.size();i++){
        if(s[i]=='a')
            sum1++;
        else if(s[i]=='b')
            sum2++;
        else if(s[i]=='c')
            sum3++;  
        if(s[i]<s[i-1])
            order=1;          
    }
    
    if(sum3==sum1 ||sum3==sum2){ 
        if(order==0) 
            cout<<"YES";
        else
            cout<<"NO";    
        }
    else
        cout<<"NO";    

return 0;
}