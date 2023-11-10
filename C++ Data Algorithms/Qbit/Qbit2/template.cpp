# include <fstream>
# include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

// ШАБЛОНИ ФУНКЦІЇ

// перевантаження функції в залежності від вхідних змінних

int sum(int a, int b)
{
    return a + b;
}

double sum(double a, double b)
{
    return a + b;
}

string sum(string a, string b)
{
    return a + b;
}

// шаблон функції sum

template <typename V>     //  template <typename T1, typename T2>  // шаблон для роботи з різними типами даних
V sum (V a, V b)          //  T1 sum (T1 a, T2 b)
{                         //  {
    return a + b;         //      return a + b;
}                         //  }

// замість ключового слова 'typename'(з мови С) можна сміливо писати слово 'class'(з мови С++)
// у випадку такої заміни слово 'class' не має відношення до ООП, функціонал цих слів однаковий

// ШАБЛОНИ КЛАСУ ООП

template <typename A1, typename A2, typename A3>
class people
{
private:
    A1 value1;
    A2 value2;
    A3 value3;

public:
    people(A1 x, A2 y, A3 z)
    {
        value1 = x;
        value2 = y;
        value3 = z;
    }


    ~people() // деструктор
    {
        fout << value1.name << " " << value1.age <<" is going to be dead" << endl;
        fout << value2 <<" is going to be dead" << endl;
        fout << value3 <<" is going to be dead" << endl;
    }

    void out()
    {
        fout << sizeof(value1) << " байти"  << endl;
        fout << sizeof(value2) << " байти" << endl;
        fout << sizeof(value3) << " байти" << endl;
    }
};

class birth
{
public:
    void hello()
    {
        fout << "Well done with a birth! " <<  endl;
    }

    birth()  // конструктор із замовчуванням
    {
        age = 0.75;
        name = "Anton";
    }

//private:
    string name;
//private:
    double age;

};

int main()
{
// робота з перевантаженою функцієї і її шаблоном

/*  int x,y;
    double x,y;
    string x,y;
    fin >> x >> y;
    fout << sum(x,y); */

// робота з шаблоном класy

    string b = "Rabit";
    double c = 35.45;
    birth a;
    people<birth,string,double> abba(a,b,c);
    abba.out();
}



