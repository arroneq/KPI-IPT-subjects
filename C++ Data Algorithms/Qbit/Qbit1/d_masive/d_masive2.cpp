# include <fstream>
# include <algorithm>

using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

// пошук найбільшого серед усіх найбільших та номер рядка з ним в двовимірному масиві


int main ()
{
    int r[100][100],y,max,min,n,m,i,j;
    cin >> n;
    cin >> m;
    int k[m];
    int ki[m];
    for (i=0; i<n ; i++)
    for (j=0; j<m; j++)
        cin >> r[i][j];
    for (j=0; j<m; j++)
    {
    max=-1000;
    for (i=0; i<n; i++)
        if (r[i][j] > max)
        {
	max = r[i][j];
	k[j]=max;
        }
    }

    int z=k[0],g=0;
    for (j=0; j<m; j++)
    if (k[j] > z)
    {
        z = k[j];
        g=j;
    }

//

    for (j=0; j<m; j++)
    {
    min=1000;
    for (i=0; i<n; i++)
        if (r[i][j] < min)
    {
        min = r[i][j];
        ki[j]=min;
    }
    }

    int zi=ki[0],gi=0;
    for (j=0; j<m; j++)
    if (ki[j] < zi)
    {
        zi = ki[j];
        gi=j;
    }

// 
/*    cout << "max= " << g << "min=  " << gi << endl; */

    for (i=0; i<n; i++)
    swap(r[i][g],r[i][gi]);

//


    for (i =0; i<n; i++)
    {
    for (j=0; j<m; j++)
        cout << r[i][j] << " ";
    cout << endl;
    }
}