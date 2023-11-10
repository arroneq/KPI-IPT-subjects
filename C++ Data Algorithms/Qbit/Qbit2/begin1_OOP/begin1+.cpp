# include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

class bird
{
public:
    void words()
    {
        fout << "Hello World!" << endl;
    }
};

class pointers
{
public:
    void hello()
    {
        fout << "Well done with pointers!";
    }
};

int main()
{
    bird snipe; // аналогія до int a
    snipe.words();

    pointers a;
    pointers *p;
    p = &a;
    p->hello();
}