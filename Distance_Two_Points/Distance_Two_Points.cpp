/*
DISTANCE BETWEEN TWO POINTS (X, Y, Z)
*/

#include<iostream>
#include<cmath>
using namespace std;

struct Point {
    double X, Y, Z;
};

Point Read(void) {
    Point Coords;
    
    cout << "Indicate X coordinate: " << endl;
    cin >> Coords.X;
    cout << "Indicate Y coordinate: " << endl;
    cin >> Coords.Y;
    cout << "Indicate Z coordinate: " << endl;
    cin >> Coords.Z;
    
    return Coords;
}

double Calculate(const Point &A, const Point &B) {
    
    return sqrt(pow((B.X - A.X), 2) + pow((B.Y - A.Y), 2) + pow((B.Z - A.Z), 2));;
}

void Result(const Point &A, const Point &B) {
    double Res;
    
    Res = Calculate(A, B);
    
    cout<<"The distance between both points is " << Res << " units" << endl << endl;
}

int main(void) {
    Point A, B;
    
    cout << "For the first point: " << endl;
    A = Read();
    system("cls");

    cout << "For the second point: " << endl;
    B = Read();
    system("cls");

    Result(A, B);
    
    system("pause");
    return 1;
}
