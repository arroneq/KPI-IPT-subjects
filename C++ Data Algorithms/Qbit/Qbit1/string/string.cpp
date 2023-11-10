#include <fstream>
#include <string>
using namespace std;

ifstream cin ("input.txt");
ofstream cout("output.txt");

int main ()      //знайти кількість літер та видалити їх з рядка
{
    string s,s1;
    int k=0;
    getline(cin,s);    //введення рядка
    int r = s.length();    //необхідна відповідна бібліотека
    for (int i=0; i<r; i++)
	for (int l=97; l < 123; l++)     //таблиця ASCII
	    if (int(s[i])  == l)
	    {
		k=k+1;
		s.erase(i,1);    //функція видалення
		i=i-1;
    	    }

    cout << k << endl;
    cout << s << endl;   //виведення рядкy
    cout << s1.length();
}