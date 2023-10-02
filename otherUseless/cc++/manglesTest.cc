#include <iostream>
using namespace std;
void a(int a, int b)
{
}

void a(float a, float b) // 不会报错
{
}

// void a(int a, int b) {}//这里会报错

int main()
{
    cout << '1';

    return 0;
}