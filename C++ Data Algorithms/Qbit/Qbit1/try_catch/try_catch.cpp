#include <fstream>

using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

int main()
{
    int a[6];
    for (int i=0; i < 6; i++)
      cin >> a[i];

        try
        {
            for (int i =0; i<6; i++)
              if (a[i] == 0)
                throw 1;

            for (int l = 47; l<122; l++)
              for (int i = 0; i<6; i++)
                if (int(a[i]) == l)
                  throw 2;
        }

        catch(int i)
        {
            cout << "помилка №" << i << endl;
        }
}