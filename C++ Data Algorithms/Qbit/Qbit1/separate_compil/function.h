//function.h
#pragma once
#include <fstream>
struct  mylist
{
    double value;
    mylist *next;

};

mylist* in(int n);
void out(mylist* p);
void add(mylist *p, mylist *t);
void sortex(mylist *p);
