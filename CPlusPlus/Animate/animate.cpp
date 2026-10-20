#include <iostream>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <string>
#include <thread>


using namespace std;

void AnimationPrinting(const char* vehicle)
{
    using std::string;
    using std::this_thread::sleep_for;

    uint16_t lineWidth = 100;
    uint16_t carWidth = strlen(vehicle);
    uint16_t animationWidth = lineWidth-carWidth;
    uint16_t leftDash = 0;
    uint16_t rightDash = animationWidth;

    for (uint8_t idx = 0; idx <= animationWidth; idx++)
    {
        system("cls");
        leftDash = idx;
        rightDash = animationWidth - idx;
        cout << string(leftDash,'-') << vehicle << string(rightDash,'-') << endl;
        sleep_for(10ms);
    }
}

int main(void)
{
    char policeCar[] = "[[8]]";
    char ambulanceCar[] = "[ + ]]";

    AnimationPrinting(policeCar);
    AnimationPrinting(ambulanceCar);

    return 0;
}