#include <fstream>
#include <string>
using namespace std;

ifstream cin ("input.txt");
ofstream cout("output.txt");

int main ()   //замінити місцями всі z на w і навпаки
{
    string s;
    getline(cin,s);    //введення рядка
    int r = s.length();    //необхідна відповідна бібліотека
    for (int i=0; i<r; i++)
    {
        if (int(s[i]) == 122)
	    s[i] = char(119);
	else if (int(s[i]) == 119)
	    s[i] = char(122);
    }
    
    cout << s;

}