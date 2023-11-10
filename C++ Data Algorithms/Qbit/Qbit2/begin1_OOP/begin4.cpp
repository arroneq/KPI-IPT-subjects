# include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

class bird
{
public:
    long int words(long int n)
    {
        return ((1+n)*n)/2;
    }
};

int main()
{
    long int n;
    bird snipe; // аналогія до int a
    fin >> n;
    fout << snipe.words(n);
}