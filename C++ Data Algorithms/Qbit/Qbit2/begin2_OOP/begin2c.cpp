# include <fstream>
# include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

//визначити, скільки слів у слові

class pointers
{
public:
    int maximum(string  x)
    {
        r = x.length();
        for (int i=0; i<r; i++)
            if ((int(x[i]) != 32) && (int(x[i+1]) == 32))
                k = k+1;
        return k;
    }

private:
    int r,k = 1;
};

int main()
{
    string s;
    getline(fin,s);
    pointers p;
    fout << p.maximum(s);
}