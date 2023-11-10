#include "mag.h"

ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
    int c,x,y,m;
    fin >> x >> y;
    c = summa(x,y);
    m = dob(x,y);
    fout << "ивести суму " << c << "добуток " <<m;
}