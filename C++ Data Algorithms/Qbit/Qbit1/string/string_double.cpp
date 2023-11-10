#include <fstream>
#include <string>
using namespace std;

ifstream cin ("input.txt");
ofstream cout("output.txt");

int main ()         //подвоїти всі літери в рядку
{
    string s,s1;
    int k=0;
    getline(cin,s);    //введення рядка
    int r = s.length();    //необхідна відповідна бібліотека
    for (int i=0; i<r; i++)
	for (int l=65; l < 123; l++)   //таблиця ASCII
	    if (int(s[i]) == l)
	    {
		s.insert(i,1,s[i]);   //функція вставки 
		i=i+1;
		r=r+1;
	    }
    cout << s;

}