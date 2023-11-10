#include <fstream>
#include <vector>
#include <algorithm>       //обов"язково додати бібліотеку алгоритмів та вектор
using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int main ()
{
    int a,max,z,min,i;
    vector <int> abra;
    out << "записуємо вектор, доки не побачимо 0" << endl;
    for (i=0 ; i<10000 ;i++)
    {
	in >> a;
	abra.push_back(a);   // запис в вектор чисел
	if (abra[i]  == 0)
	    break;
    }
// пошук максимального
    max=abra[0];
    for (i=0; i<abra.size(); i++)
	if (abra[i] > max)
	    max=abra[i];
    out <<"максимальне число масиву - "<< max << endl;

// пошук мінімального

    min=abra[0];
    for (i=0; i<abra.size(); i++)
	if (abra[i] < min)
	    min=abra[i];
    out << "мінімальний елемент масиву - " <<  min << endl;

//сортування вектора (зростання)

    for (i=0 ;i<abra.size(); i++)
	for (int j=i; j<abra.size(); j++)
	{
	    if (abra[i] > abra[j])
		swap( abra[i], abra[j]);  //алгоритм заміни місцями елементів
	}

//виведення вектора

    out << "відсортований по зростанню масив";
    z=abra.size();
    for (i=0; i < z ; i++)
	out << abra[i] << " ";

// сортування 2 спосіб з вбодованим алгоритмом 

    sort(abra.begin(), abra.end());
    for(i(0); i < z; i++)
	out << abra[i] << " ";


// insert

    int k=5,c=20;            // нехай додаємо елемент c на k-те  місце
    for (i = z ;i >  k ; i--)
	abra[i+1] = abra[i];
    abra[k]=c;
    for (i=0; i< z+1 ;i++)
	out << abra[i] << " ";

// delete
                             // нехай видаляємо k-ий елемнт
    out << "видаляємо 5-ий елемент масиву";
    for (i = k ;i < z-1 ;i++)
	abra[i] = abra[i=1];
    for (i=0; i < z-1 ;i++)
	out << abra[i] << " ";


}
