//function.cpp
#include "function.h"

using namespace std;

ifstream fin("fin_put.txt");
ofstream fout("autput.txt");

mylist* in(int n) // тип  mylist*, бо будемо повертати вказііник
{
    mylist *zu,*first;
    zu = new mylist;
    first = zu; // зберігаємо вказівник на перший елемент
    while (n != 0)
    {
        fin >> zu->value; 
        if (n>1)     // бо нам непотрібно створювати наперед ще один елемент, коли n=1
        {
            zu->next = new mylist;
            zu = zu->next; 
        }
        else zu->next= NULL;//якщо n=1 - наступна адреса вказує на NULL
        n--;
    }
  return first; //тепер наш вказівник р буде вказувати на перший елемент
}

void out(mylist *p)
{
    // передали функції адресу першого елементу
    for ( ; p != NULL; p = p->next)
    {
        fout << p->value << " ";
    }
    fout << endl; // щоб виводити новий список з нового рядка
}

void add(mylist *p, mylist *t) //з двох списків робимо один
{
    for ( ; p->next!=NULL; p = p->next); //прокручуємо до адреси останнього ненульвого

    p->next = t; //наступна адреса - адреса першого елемента в другому списку
}



void sortex(mylist *p)
{
    mylist *first2;
    int katalizator = 1;
    double uno,dos;
    first2 = p;
    while(katalizator == 1) // Цикл продовжуватиме сортувати, поки буде хоча б один виклик if
    {
        katalizator = 0; 
        for (; p->next != NULL; p = p->next)
        {
            uno = p->value;
            dos = p->next->value;
            if (uno >= dos)
            {
                p->value = dos;
                p->next->value = uno;
                katalizator = 1;
            }
        }
        p = first2;  // Ми ж пропрутили вказівник до останнього елементу, тож мусимо знову повернути на перший елемент
    }
}




