#include <cstdio>

using namespace std;

int main()
{
    FILE *f = fopen( "abra.txt" , "rb" );  // rb - read binary
    int n=6,a[n],*d;
    fread(a, sizeof(int), 6, f);   //тепер а - це вказівник :: fread(адреса ел, в який зчитуємо, розмір елементів, кількість елементів, файл, з якого читаємо )

    FILE *fs = fopen("file.txt", "w");   //файловая переменная f связана с файлом file.txt на диске, w - спецификатор доступа к файлу, файл открыт для записи}
    
    for ( d=a; d < a+5; d++)
	fprintf(fs,"%d ",*d);

    fclose(fs); //Закрыть файл и освободить память}
    fclose(f);

}