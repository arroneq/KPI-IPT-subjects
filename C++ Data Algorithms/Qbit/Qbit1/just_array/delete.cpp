#include <fstream>
using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

int main ()
{
    int n,b,i,m[1000];
    cin >> n; // кількість елементів масива
    for ( i = 0; i <n ; i++) // ввід статичного масива
	cin >> m[i];
    cin  >> b; // номер елемента, який необхідно видалити
    for ( i=b-1; i<n; i++)
	m[i] = m[i+1];     // зсув вліво всіх елементів (б-1, бо номерується з 0) 
    for ( i=0; i<n-1; i++ )
	cout << m[i] <<" ";
}