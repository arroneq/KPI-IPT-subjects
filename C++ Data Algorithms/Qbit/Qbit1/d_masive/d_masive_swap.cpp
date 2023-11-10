# include <fstream>
# include <algorithm>

using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

// поміняти місцями два рядки


int main ()
{
    int a,r[100][100],p1,p2,n,m,i,j;
    cin >> n;
    cin >> m;
    for (i=0; i<n ; i++)
	for (j=0; j<m; j++)
	    cin >> r[i][j];
    cin >> p1 >> p2;
    for (j=0; j<m; j++)
    {
	swap(r[p1-1][j],r[p2-1][j]); 
    }
    for (i=0; i < n; i++)
    {
	for (j=0; j<m ;j++)
            cout << r[i][j] <<" ";
	cout << endl;
    }

}