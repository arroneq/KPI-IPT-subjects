# include <fstream>
# include <string>
# include <cmath>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
// передача масивв у функцію через вказівник

class bird
{
public:
    void words(int *f)
    {
        begin = f;
        end = f + 9;
        for (h = begin; h < end; h++)
            fout << *h << endl;
    }

private:
    int i,c,k = 0,v,m,*h,*begin,*end;
    string r1 = " ", r2 = "|";
};

int main()
{
    int a[10],*p,*za;
    za = &a[0];
    bird snipe;
    for (p = za; p < za + 9; p++)
        fin >> *p;
    snipe.words(za);
}