# include <fstream>
# include <string>
# include <cmath>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

// введіть два числа і покажіть їхню сумму в стовпчик

class bird
{
public:
    void words(long int x, long int y)
    {
        c = x + y;
//xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

        for (i=0; i<10; i++)
        {
            v = x/pow(10,i);
            if (v != 0)
                k = i + 1;
        }
        m = 10-k;
        for (i=0; i<m; i++)
            fout << r1;
        fout << x << endl;
        v = 1;
        k = 0;

//yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

        for (i=0; i<10; i++)
        {
            v = y/pow(10,i);
            if (v != 0)
                k = i + 1;
        }
        m = 10-k;
        for (i=0; i<m; i++)
            fout << r1;
        fout << y << endl;
        fout << r2 << endl;
        v = 1;
        k = 0;

//cccccccccccccccccccccccccccccccccccccccccc

        for (i=0; i<10; i++)
        {
            v = c/pow(10,i);
            if (v != 0)
                k = i + 1;
        }
        m = 10-k;
        for (i=0; i<m; i++)
            fout << r1;
        fout << c << endl;

    }

private:
    long int i,c,k = 0, v, m;
    string r1 = " ", r2 = "----------";
};

int main()
{
    long int a,b;
    bird snipe; // аналогія до int a
    fin >> a >> b;
    snipe.words(a,b);
}