#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double a;
    double b;
    double c;
    double x;
    double x1;
    double discr;
    cin >> a;
    cin >> b;
    cin >> c;
    discr = (b*b - 4*a*c);
    if (a == 0 && b ==0)
    {
        cout << " " << endl;
    }
    else if (a == 0)
    {
        x = ((c) / (b));
        cout << "X1:" << x << endl;
    }
    else if(discr > 0)
    {
        x = ( -1*b + sqrt(b*b - 4*a*c) ) / (2 * a);
        x1 = ( -1*b - sqrt(b*b - 4*a*c) ) / (2 * a);
        cout << "X1:" << x << " X2:" << x1 << endl;
    }
    else if (discr == 0)
    {
        x = (-1*b) / (2*a);
        cout << "X1:" << x << endl;
    } 
}
