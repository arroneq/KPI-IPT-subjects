# include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

class bird
{
public:
    void words(int x,int y)
    {
        p = 2*(x+y);
        s = x*y;
        fout << "The perimeter of the rectangle with sides " << x << " and " << y << " is " << p << "." << endl;
        fout << "The area of the rectangle with sides " << x << " and " << y << " is " << s << ".";
    }
private:
    int p,s;
};

int main()
{
    int a,b;
    bird snipe;
    fin >> a >> b;
    snipe.words(a,b);
}