# include <fstream>
# include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

//визначити, яке максимальне число можна скласти із цифр чотиризначного числа

class pointers
{
public:
    string maximum(int x)
    {
        za = x/1000;
        zb = (x % 1000)/100;
        zc = (x % 100)/10;
        zd = x % 10;
        int h[4];
        h[0]=za; h[1]=zb; h[2]=zc; h[3]=zd;
        for (int j=0; j<4; j++)
            for (int i=0; i<3; i++)
                if (h[i] <= h[i+1])
                {
                    r=h[i+1];
                    h[i+1]=h[i];
                    h[i]=r;
                }
        m1 = h[0]; m2 = h[1]; m3 = h[2]; m4 = h[3];
        s1 = to_string(m1);
        s2 = to_string(m2);
        s3 = to_string(m3);
        s4 = to_string(m4);
        s = s1+s2+s3+s4;
        return s;
    }

private:
    int za,zb,zc,zd,m1,m2,m3,m4,r,max;
    string s1,s2,s3,s4,s;
};

int main()
{
    int a;
    pointers p;
    fin >> a;
    fout << p.maximum(a);
}