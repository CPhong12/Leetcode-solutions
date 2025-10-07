#include <iostream>

namespace first
{
    int x = 1;
}

int main()
{
    // Solution preventing name conflicts
    using namespace first;

    // using std::cout;
    // using std::string;
    int x = 0;

    // string name = "Bro";
    //  std::cout << first::x;

    return 0;
}