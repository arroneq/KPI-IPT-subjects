# include <fstream>
# include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

class people
{
private:
    int age;
    string name;

public:

    people(string x, int y) //  конструктор з параметром
    {
        boy(x,y);
    }

    void boy(string x, int y)
    {
        age = y;
        name = x;
    }

    ~people() // деструктор, знищує автоматично всі об*єкти класу
    {
        fout << name <<" is going to be dead"<< endl;;
    }

    void out()
    {
        fout << name << " " << age << endl;
    }
};

class pointers
{
public:
    void hello()
    {
        fout << "Well done with pointers!"<<endl;
    }

    pointers()  // конструктор із замовчуванням
    {
        m = 1;
        k = 2;
    }
private:
    int m,k;
};

class somebody    // конструктор копії
{
public:
    somebody(string f)
    {
        nomo = f;
    }

    somebody(const somebody& p) // скопіювали об*єкт // застосування модифікатора const к значенню до повернення перешкоджає
                                                     // написанню дивних виразів подібних до такого X(5) + X(6) = X(7)
    {
        nomo = p.nomo;
    }

    void out3()
    {
        fout << nomo << endl;
    }
private:
    string nomo;
};

int main()
{
    string a;
    int b;
    fin >> a >> b;
//    people nool;   //  це і є конструктор
//    nool.boy(a,b); //  така специфічна функція, яка створює об*єкт класу

    people girl1("Anna",23);
    people girl2("Anton",25);
    girl1.out();
    girl2.out();

    somebody he1("Kolya");
    somebody he2(he1);
    he2.out3();

// приклад доступу до методів класу через вказівники(тобто адреси)

/*    pointers one;
    pointers *p;
    p = &one;
    fout << endl;
    p->hello();*/
}

