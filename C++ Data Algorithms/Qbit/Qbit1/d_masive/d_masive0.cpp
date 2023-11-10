# include <fstream>

using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

// замінити діагональ на 0, верхній тр на 1, нижній на 2


int main ()
{
    int r[100][100],y,max,min,n,m,i,j;
    cin >> n;
    cin >> m;
    for (i=0; i<n ; i++)
	for (j=0; j<m; j++)
    	    cin >> r[i][j];
    for (i=0; i<n; i++)
        for (j=0; j<m; j++)
	{
	    if (i==j)
		r[i][j] = 0;
	    if (i < j)
		r[i][j] = 1;
	    if (i > j)
		r[i][j] = 2;
	}

    for (i=0; i<n ; i++)
    {
	for (j=0; j<m; j++)
	    cout << r[i][j] << " ";
	cout << endl;
    }
}