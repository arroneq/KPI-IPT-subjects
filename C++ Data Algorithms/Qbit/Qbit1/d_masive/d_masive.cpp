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
    int k[n];
    int ki[n];
    cin >> m;
    for (i=0; i<n ; i++)
	for (j=0; j<m; j++)
	    cin >> r[i][j];
    for (i=0; i<n; i++)
    {
	max=-1001;
	for (j=0; j<m; j++)
	    if (r[i][j] > max)
	    {
		max = r[i][j];
		k[i]=max;
	    }
    }

    int z=k[0],g=0;
    for (i=0; i<n; i++)
	if (k[i] > z)
	{
	    z = k[i];
	    g=i;
	}

//

    for (i=0; i<n; i++)
    {
    min=1001;
    for (j=0; j<m; j++)
        if (r[i][j] < min)
	{
	    min = r[i][j];
	    ki[i]=min;
	}
    }

    int zi=ki[0],gi=0;
    for (i=0; i<n; i++)
    if (ki[i] < zi)
    {
        zi = ki[i];
        gi=i;
    }

// 

/*    cout <<"max= "<< g << " min= " << gi << endl;*/

    for (j=0; j<m; j++)
	swap(r[g][j],r[gi][j]);

//


    for (i =0; i<n; i++)
    {
	for (j=0; j<m; j++)
	    cout << r[i][j] << " ";
	cout << endl;
    }
}







