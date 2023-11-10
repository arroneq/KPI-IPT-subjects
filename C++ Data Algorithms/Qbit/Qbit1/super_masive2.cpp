#include <fstream>
using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

// спроби зрозуміти, як можна зліпити два масиви в один для 8 лабораторної

int main()
{
  int k=5,m=4,g,i,j,h,z;
  g=k+m;

    int *a = new int[k];
    int *b = new int[m];
    int *c = new int[g];

    for (i=0; i<k;i++)
      cin >> a[i];
    for (j=0; j<m;j++)
      cin >> b[j];

    i=0;j=0;

    for (h=0; h<k;h++)
    {
        c[h] = a[i];
        i++;
    }
    for (h=k; h<g;h++)
    {
        c[h] = b[j];
        j++;
    }

    for (i=0; i<h; i++)
        for (j=i; j<h; j++)
            if (c[i] >= c[j])
            {
                z = c[i];
                c[i] = c[j];
                c[j] = z;
            }

    for (h=0; h<g; h++)
      cout << c[h] << " ";



}