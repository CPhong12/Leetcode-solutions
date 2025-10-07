#include <iostream>

int main()
{
    double PI = 3.14159;

    double radius = 10;
    double circumference = 2 * PI * radius;

    std::cout << circumference << "cm";

    const double PI = 3.14159; // can't change

    return 0;
}