# include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

class bird
{
public:
    int words(int a, int b)
    {
        return a+b;
    }
};

int main()
{
    int a,b;
    bird snipe; // аналогія до int a
    fin >> a >> b;
    fout << snipe.words(a,b);
}

