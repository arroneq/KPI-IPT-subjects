#include <cstdio>

int main() 
{
    // https://proginfo.ru/binary-file/
    FILE *f = fopen ("abra.txt", "wb"); // wb - write binary

    int n=6, a[n];
    for (int i=0; i<n; i++)
	a[i]=i+1;

    fwrite(a, sizeof(int), 6, f);

    fclose(f);
}
