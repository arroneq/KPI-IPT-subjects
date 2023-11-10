# include <fstream>
# include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

class employee
{
protected:  // private -> protected
    int age;
    string name;
    float salary;

public:
    employee(string x, int y, float z) //  конструктор
    {
        age = y;
        name = x;
        salary = z;
    }

    void out1()
    {
        fout << name << " " << age << " " << salary;
    }
};

class manager : virtual employee  // в звичайному наслідування можна писати і public
{
protected:
    string mark;
    int rank;
    int bonus;

public:
    manager(string x, int y, float z, string m, int n, int k) : employee(x,y,z) //  конструктор
    {
        mark = m;
        rank = n;
        bonus = k;
    }

    void out2()
    {
        out1();
        fout << " " << mark << " " << rank << " " << bonus;
    }
};

/* ТИПИ СПАДКУВАННЯ 
   (1) --private--
       a) нащадок перетворить на private:(public й protected) батька
          й у своєму public зможе змінювати дані батька (бо працює з ним як із своїми даними private)
          але, відповідно, об*єкт нащадка ззовні(в main) ніяк не зможе змінити дані батька
          Тобто таким наслідуванням можна лише всередині нащадка оперувати даними батька
       b) """! за жодних обставин унаслідувати секцію private неможливо !"""
       c) public-наслідуваний "онук" ніяк не отримає доступ(не зможе унаслідувати) до даних "діда"(див. пункт b))
   (2) --спадкування protected-- 
       a) нащадок перетворить на protected:(public й private) батька
       b) ситуація у всьому аналогічна до private, але єдина відмінність в тому, що
       b) public-наслідуваний "онук" зможе унаслідувати дані від "діда"
   (3) --public--
       a) а тут все прекрасно наслідується переходом public->pulic, protected->protected

  ДЖЕРЕЛО "https://foxford.ru/wiki/informatika/tipy-nasledovaniya-public-private-i-protected-v-s" */

// МНОЖИННЕ СПАДКУВАННЯ

class cleaner : virtual employee, virtual manager // а також треба змінити наслідування manager на virtual
{
private:
    char coronavirus;

public:
    cleaner(string x, int y, float z, string m, int n, int k, char h) : employee(x,y,z), manager(x,y,z,m,n,k)
    {
        coronavirus = h;
    }
    void out3()
    {
        out2(); // вся інформація і так вже є в manager, викликати out1() не потрібно, хоча кокструктор cleaner вимагає саме такого запису
        fout << " " << coronavirus;
    }

};

int main()
{
    string a, m;
    int b,n,k;
    float c;
    char h;
    fin >> a >> b >> c;
    employee worker1(a,b,c);  //конструктор батька
    worker1.out1();
    fout << endl;

    fin >> a >> b >> c >> m >> n >> k;
    manager boss(a,b,c,m,n,k); // конструктор нащадка
    boss.out2();
    fout << endl;

    fin >> a >> b >> c >> m >> n >> k >> h;
    cleaner Vasya(a,b,c,m,n,k,h);
    Vasya.out3();

}


