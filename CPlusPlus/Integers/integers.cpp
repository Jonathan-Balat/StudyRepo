#include <iostream>
#include <cstdint>
#include <format>
#include <print>

using namespace std;


void Overflow_Printing(void)
{
    using std::println;
    using std::format;
    using std::string;

    uint8_t bit8UData = 255;            // Overflow to 0
    int8_t bit8Data = 127;              // Overflow to -128
    uint32_t bit32UData = 0xFFFFFFFF;   // Overflow to 0

    for (uint8_t idx = 0; idx < 5; idx++)
    {
        string text = format("{}) Uint8={} int8={} uint32={}", idx, bit8UData, bit8Data, bit32UData);
        cout << text << endl;
        bit8UData++;
        bit8Data++;
        bit32UData++;
    }
}

int main(void)
{
    Overflow_Printing();
    return 0;
}