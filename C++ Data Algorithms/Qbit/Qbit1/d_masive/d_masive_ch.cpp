# include <fstream>
# include <algorithm>

using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

// визначити номера стовпців(та вивести їхгю кількість), де парних ел більше, ніж непарних


int main ()
{
    int a,r[100][100],p,ne,n,m,i,j;
    bool b;
    cin >> n;
    cin >> m;
    int z=0,g[m];
    for (i=0; i<n ; i++)
	for (j=0; j<m; j++)
	    cin >> r[i][j];
    for (j=0; j<m; j++)
    {
	p=0;ne=0;
	for (i=0; i<n; i++)
	{
	    a = (r[i][j])%2;
	    b = (a==0);
	    if (b == true)
		p = p+1;
	    else
		ne = ne+1;
	}
	
	/*cout << p << " " << ne << endl;*/
	
	if (p > ne)
	{
	    z = z+1;
	    g[j] = 5;
	}
    }


    cout << z << endl;

    for (j=0; j < m; j++)
	if (g[j] == 5)
	    cout << j+1 <<" ";









}