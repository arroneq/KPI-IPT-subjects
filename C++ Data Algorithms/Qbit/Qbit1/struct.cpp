#include <fstream>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

int main()
{

    struct student
    {
        string name;
        string pri;
        int BD;
    };

    struct birh
    {
        int day;
        int mounth;
        int year;
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

    cout << p->name +" не достойний "+ p->author + "на " << p->page << "відсотків" ;

}
