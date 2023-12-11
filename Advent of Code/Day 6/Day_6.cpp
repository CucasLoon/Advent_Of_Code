#include <iostream>
#include <vector>
#include <string>

using namespace std;


//This is going to be an interesting test to see if I can remember c++ syntax
int main()
{   
    
    for(int i=0;i<10;i++)
    {
        string word = "Hello";
        for(int j=0;j<i;j++)
        {
            word.append("!");
        }
        cout << word << endl;
    }
    cout << endl;
}