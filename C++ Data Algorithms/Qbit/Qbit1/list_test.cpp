#include <fstream>

using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

struct  mylist
{
    char value;
    mylist *next;

} a,*mlist = &a;

int main ()
{
    int n;
    cin >> n; // скільки ел списку хочете ввести
    //n = n-1;
    while (n != 0)
    {
        mlist->next = new mylist;
        mlist = mlist->next;
        cin >> mlist->value;
        n--;
    }

    mlist = &a;
    for (mlist = mlist->next; mlist != NULL; mlist = mlist->next)
    {
        cout << mlist->value << endl;
    }
}