# include <fstream>
# include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

// перевантажуємо + та * на додавання людей та множення магазинів

// перегрузка за допомогою функції-члена класу

class people
{
public:

    string name;  // писати змінні в private не можна, інше operator їх не побачить
    int age;      // operator побачить змінні private лише у випадку використання friend функції

    people(string x,int y)
    {
        name = x;
        age = y;
    }

    void out() 
    {
        fout << name << " " << age;
    }
};

// звичайна функція перевантаження оператора
// """! функція operator поза класом !"""

people operator + (people a, people b)  // функція повертає об*єкт типу people(але вже з новими параметрами)
{
    return people(a.name + b.name, a.age + b.age);
}



// перевантаження за допомогою friend функцій

class shop
{
private:
    string city; // а тут вже можна записати дані у private
    int area;

public:
    shop(string x,int y)
    {
        city = x;
        area = y;
    }

    void out() 
    {
        fout << city << " " << area;
    }

    friend shop operator * (shop a, shop b);
};

// """! функція operator поза класом !"""

shop operator * (shop a, shop b) // а цей оператор вже бачить змінні в private
{
    shop temp(a.city + "_mango_" + b.city, a.area * b.area); // передаю парематри через кому в новий об*єкт
    return temp;
}

int main()
{
    string m;
    int n;
    fin >> m >> n;
    people man1(m,n);
    fin >> m >> n;
    people man2(m,n);
    people man3 = man1 + man2;  // додали дві людини
    man3.out();
    fout << endl;

    fin >> m >> n;
    shop roshen(m,n);
    fin >> m >> n;
    shop avk(m,n);
    shop milenium = roshen * avk;  // перемножили два магазини
    milenium.out();
}





