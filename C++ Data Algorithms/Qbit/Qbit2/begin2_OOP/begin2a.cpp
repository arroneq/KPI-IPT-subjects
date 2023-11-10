# include <fstream>
# include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

// ввести кількість масивів та елементів в них та дослідити чи є в масиві два сусідні елементи одного знаку

class pointers
{
public:
    string znak(int *x, int y)
    {
        for (run2 = x; run2 < x+y; run2++)
        {
            if ((run2 != x+y-1) && ((*run2)*(*(run2+1)) > 0))
            {
                h = "YES";
                run2 = x+y;
            }
            else h = "NO";
            //fout << h << endl;;
        }
        return h;
    }

private:
    int *run2;
    string  h;
};

int main()
{
    int k,n;
    pointers p;
    fin >> k;;
    for (int i=0; i<k; i++)
    {
        fin >> n;
        int *a = new int [n];
        int *run1;
        for (run1 = a; run1 < a+n; run1++)
        {
            fin >> *run1;
        }
        fout << p.znak(a,n) << endl;
    }
}



