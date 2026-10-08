//номер 2 самостоятельного задания
//Ввод данных 
#include <iostream>
#include <string>
#include <windows.h>
#include <limits>

using namespace std;

int main() {
    SetConsoleOutputCP(CP_UTF8);
    long long number;
    // Валидация ввода
    while (true) {
        cout << "Введите целое число в десятичной системе: ";
        if (cin >> number) {
            break;  // ввод успешен — выходим
        }
        cout << "Ошибка: нужно ввести целое число. Попробуйте снова.\n";
        cin.clear();                    // сбросить флаг ошибки
        cin.ignore(10000, '\n');        // выбросить до 10000 символов до конца строки
    }
    //Вывод в разных системах
    cout << "Десятичное:        " << dec << number << "\n";
    cout << "Двоичное:          ";
    //Вывод битов
    if (number == 0) {
        cout << "0";
    } else {
        bool started = false;
        for (int i = 63; i >= 0; --i) {
            bool bit = (number >> i) & 1LL;
            if (bit) started = true;
            if (started) cout << bit;
        }
    }
    cout << "\nВосьмеричное:      " << oct << number << "\n";
    cout << "Шестнадцатеричное: " << hex << uppercase << number << "\n";
    return 0;
}