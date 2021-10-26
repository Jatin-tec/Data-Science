#include <iostream>

using namespace std;

int main(){

    int Array[2][2][3] = { 
                        {
                            {2, 4, 6},
                            {1, 2, 3}
                        },
                        {
                            {3, 6, 9},
                            {1, 2, 3}
                        }
                    };

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < 3; k++)
            {
                cout<<Array[i][j][k]<<" ";
            }
            
        }
        
    }
                         
}