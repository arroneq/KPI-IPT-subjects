// Використовуючи роздфльну компіляцію вводимо два списки, на виході з уих двох списків маємо один відсортований

main.cpp

#include "function.h"

using namespace std;

ifstream cin ("cin_put.txt");
ofstream cout ("autput.txt");

int main ()
{
    mylist *L2 = NULL,*L2 =NULL;
    int n,m,b;
    cout << "Введіть два числа : кількість елементів в першому і другому списку" << endl;
    cin >> n >> m;
    cout << "Яку операцію ви хочете зробити?" << endl;
    cin >> b;
    switch (b)
    {
        case 1 : // Ввести та вивести два списки
            L1 = in(n);
            L2 = in(m);
            out(L1);
            out(L2); break;
        case 2 : // Зробити з двох списків один і вивести
            L1 = in(n);
            L2 = in(m);
            add(L1,L2);
            out(L1); break;
        case 3 : // Вiдсортувати список
            L1 = in(n);
            L2 = in(m);
            add(L1,L2);
            sortex(L1);
            out(L1); break;
        default :
            cout << "Операції з таким номером немає!";
    }
}



function.h

#pragma once

#include <fstream>

struct  mylist
{
    double value;
    mylist *next;

};

mylist* in(int n);
void out(mylist* L1);
void add(mylist *L1, mylist *L2);
void sortex(mylist *L1);



function.cpp

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
        else zu->next= NULL;// якщо n=1 - наступна адреса вказує на NULL
        n--;
    }
  return first; //тепер наш вказівник р буде вказувати на перший елемент
}



void out(mylist *L1)
{
    // передали функції адресу першого елементу
    for ( ; L1 != NULL; L1 = L1->next)
    {
        fout << L1->value << " ";
    }
    fout << endl; // щоб виводити новий список з нового рядка
}

void add(mylist *L1, mylist *L2) //з двох списків робимо один
{
    for ( ; L1->next!=NULL; L1 = L1->next); //прокручуємо до адреси останнього ненульвого

    L1->next = L2; //наступна адреса - адреса першого елемента в другому списку
}


void sortex(mylist *L1)
{
    mylist *first2;
    int katalizator = 1;
    double uno,dos;
    first2 = L1; // Зберігаємо вказівник на перший елемент
    While (katalizator == 1) // Цикл продовжуватиме сортувати, поки буде хоча б один 	виклик if
    {
        katalizator = 0; 
        for (; L1->next != NULL; L1 = L1->next)
        {
            uno = L1->value; 
            dos = L1->next->value;
            if (uno >= dos)
            {
                L1->value = dos;
                L1->next->value = uno;
                katalizator = 1;
            }
        }
        L1 = first2;  // Ми ж прокрутили вказівник до останнього елементу, тож мусимо знову повернути на перший елемент
    }
}
