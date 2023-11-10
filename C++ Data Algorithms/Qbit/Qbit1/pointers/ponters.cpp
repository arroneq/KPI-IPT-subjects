#include <fstream>
#include <string>

using namespace std;

ifstream cin("input.txt");
ofstream cout ("output.txt");

int main ()
{
/*    int *g = new int [10];    // виділення пам"яті
    for (int i=0; i<10; i++)
    {
	cin >> g[i];
	delete [ ] g;        // видалення адрес
    }

    for (int i=0; i<10; i++)     //а нічого і не виведе, бо видалена адреса масиву
	cout << g[i];


    double a[10];
    double *p;      //створюємо вказівник 

    double *v = &a[10];   //створюємо свій ітератор кінця
    for (p = &a[0] ;p < v ; p++)    // p = &a[0] прив"язуємо вказівник,кажемо,чию адресу він буде зберігати 
                                 //вказівник має бути того ж типу, що й змінна(або масив),
                                // щоб вказівник знав, де є наступна адреса (+ стільки-то байт пам"яті)

*/

// вказівник з масивом, пошук максимального, сортування

    int y[10];
    int *d;
    int *begin = &y[0];    // штучно ствоорені ітератори початку і кінця
    int *end = &y[10];
    for (d = begin; d < end; d++ )
	*d = rand()%100;

    int max = *begin;
    for (d = begin; d < end; d++ )
	if (*d > max)
	    max = *d;

    for (d = begin; d < end; d++)
	    cout << *d << " ";

    cout << "max=" << max << endl;

// вказівник і рядок string

    string ho1,ho2,ho3,ho4,ho5;
    string *p;

    getline(cin,ho1);
    getline(cin,ho2);
    getline(cin,ho3);
    getline(cin,ho4);
    getline(cin,ho5);

    string *up = &ho1;
    string *down = up + 5;

    for (p = up; p < down; p++)
	cout << *p + " o_O " << endl;

// вказівник зі структурою


    struct book
    {
        string name;
        string author;
        int page;
    };

// http://www.asvcorp.ru/tech/soft/c/part6.html


/* ПАМЯТКА: Для доступа к членам структуры при работе с самой структурой
 используется оператор «точка». При обращении к структуре с помощью указателя
 используется оператор «стрелка». */


/* 
 Используя указатель на структуру, можно получить доступ к ее элементам.
 Для этого можно воспользоваться двумя способами.
 Первый способ представляет применение операции разыменования:
1) (*указатель_на_структуру).имя_элемента

 Второй способ предполагает использование операции -> (операция стрелка):
2) указатель_на_структуру -> имя_элемента

*/

    struct book a;
    struct book *p;
    p = &a;

    p->name = "anton";
    p->author = "goblin";
    p->page = 82;


// cin >> a.name >> a.author >> a.page;

    cout << p->name +" не достойний "+ p->author + "на " << p->page << " відсотків" ;

}





























}