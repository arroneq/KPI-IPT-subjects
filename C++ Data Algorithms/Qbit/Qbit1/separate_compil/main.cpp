//main.cpp
#include "function.h"

using namespace std;

ifstream cin ("cin_put.txt");
ofstream cout ("autput.txt");

int main ()
{
    mylist *p = NULL,*t =NULL;
    int n,m,b;
    //cout << "Введіть два числа : кількість елементів в першому і другому списку" << endl;
    cin >> n >> m;
    //cout << "Яку операцію ви хочете зробити?" << endl;
    cin >> b;
    switch (b)
    {
        case 1 : // Ввести та вивести  два списки
            p = in(n);
            t = in(m);
            out(p);
            out(t); break;
        case 2 : // Зробити з двох списків один і вивести
            p = in(n);
            t = in(m);
            add(p,t);
            out(p); break;
        case 3 : // ВІдсортувати список
            p = in(n);
            t = in(m);
            add(p,t);
            sortex(p);
            out(p); break;
        default :
            cout << "Операції з таким номером немає!";
    }
}