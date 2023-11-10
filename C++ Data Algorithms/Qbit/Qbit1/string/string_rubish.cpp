#include <fstream>
#include <string>
using namespace std;

ifstream cin ("input.txt");
ofstream cout("output.txt");

int main ()
{
    string s,s1=" ";
    int n,m;
    getline(cin,s);    //введення рядка
/*    cin >> n;
    cin >> m;
    int r = s.length();
	s.erase(n-1,m-n+1);*/
    n=s.find(s1)+1;
    cout << n;
}