# include <fstream>
# include <algorithm>

using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

// вивеси максимальний для кожного стовпця


int main ()
{
    int r[100][100],y,max,min,n,m,i,j;
    cin >> n;
    cin >> m;
    int k[m];
    for (i=0; i<n ; i++)
    for (j=0; j<m; j++)
        cin >> r[i][j];
    for (j=0; j<m; j++)
    {
    max=-1001;
    for (i=0; i<n; i++)
        if (r[i][j] > max)
	{
	    max = r[i][j];
	    k[j] = max;
	}
    }
    for (j=0; j<m; j++)
	cout << k[j] << " ";
}













