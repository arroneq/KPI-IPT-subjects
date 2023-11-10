#include <fstream>
using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

int main ()
{
    int b,n,i,m[1000];
    cin >> n; // кількість елементів масива
    for (i=0; i<n; i++ )
	cin >> m[i];
    for (int j=0; j<n; j++)
	for (i=0; i<n-1; i++) // отут Н-1 
	    if (m[i] > m[i+1])
	    {
		b=m[i+1];
		m[i+1] = m[i];
		m[i] = b;
	    }
    for (i=0; i<n; i++)
	cout << m[i] << " ";
}

