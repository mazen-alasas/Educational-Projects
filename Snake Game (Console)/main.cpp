#include <iostream>
using namespace std;

char Matrix[3][3] = {{'1','2','3'},
                     {'4','5','6'},
                     {'7','8','9'}};

void PrintMatrix() {
    system("cls");
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            cout << Matrix[i][j] << ' ';
        }
        cout << endl;
    }
}

char Player = 'X';

void SetPlayer() {
    cout << "Who wants to Start (X/O)? <<  ";
    char p;
    cin >> p;
    Player = p;
    cout << "OK, Let's Go ..\n";
}

void PlayMatrix() {
    cout << "Player " << Player << " Choose Your Position  :  ";
    int Position;
    cin >> Position;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(Matrix[i][j] - '0' == Position) {
                Matrix[i][j] = Player;
            }
        }
    }
    if(Player == 'X') {
        Player = 'O';
    } else {
        Player = 'X';
    }
}

string WhoWins() {

    int rowX = 0, rowY = 0;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(Matrix[i][j] == 'X') {
                rowX++;
            } else if(Matrix[i][j] == 'Y') {
                rowY++;
            }
            if(rowX == 3) {
                return "X";
            } else if(rowY == 3) {
                return "O";
            }
        }
    }

    int colX = 0, colY = 0;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(Matrix[j][i] == 'X') {
                colX++;
            } else if(Matrix[j][i] == 'Y') {
                colY++;
            }
            if(colX == 3) {
                return "X";
            } else if(colY == 3) {
                return "O";
            }
        }
    }
    /*
        00 01 02
        10 11 12
        20 21 22
    */
    if((Matrix[0][0] == 'X' && Matrix[1][1] == 'X' && Matrix[2][2] == 'X') ||
       (Matrix[0][2] == 'X' && Matrix[1][1] == 'X' && Matrix[2][0] == 'X')) {
        return "X";
    }
    if((Matrix[0][0] == 'O' && Matrix[1][1] == 'O' && Matrix[2][2] == 'O') ||
       (Matrix[0][2] == 'O' && Matrix[1][1] == 'O' && Matrix[2][0] == 'O')) {
        return "O";
    }

    int ctr = 0;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(Matrix[i][j] != 'X' && Matrix[i][j] != 'O') {
                ctr++;
            }
        }
    }

    if(ctr == 0) {
        return "No Winner";
    }
    return "Continue";
}


int main() {

    SetPlayer();
    while(WhoWins() == "Continue") {
        PrintMatrix();
        PlayMatrix();
    }
    PrintMatrix();
    if(WhoWins() == "No Winner") {
        cout << "There is no Winner ..\n";
    } else {
        if(Player == 'X') {
            Player = 'O';
        } else {
            Player = 'X';
        }
        cout << "Congratulations, Player " << Player;
    }
    return 0;
}
