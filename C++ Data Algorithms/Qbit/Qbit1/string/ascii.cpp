#include <fstream>

using namespace std;

ifstream cin ("input.txt");
ofstream cout("output.txt");

int main ()
{
    for (int i=95; i<123; i++)
	cout<< i << " " << char(i)  << endl;
}