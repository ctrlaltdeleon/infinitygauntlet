#include <SmartInventor.h>

void setup()
{
    SmartInventor.DCMotorUse();
}

void loop()
{
    int leftSensor = analogRead(19);
    int centerSensor = analogRead(20);
    int rightSensor = analogRead(21);

    if (leftSensor < 500)
    {
        // Turn right.
        SmartInventor.DCMotor(M1, CCW, 50);
        SmartInventor.DCMotor(M2, CCW, 50);
    }
    else if (rightSensor < 500)
    {
        // Turn left.
        SmartInventor.DCMotor(M1, CW, 50);
        SmartInventor.DCMotor(M2, CW, 50);
    }
    else if (centerSensor < 500)
    {
        // Turn left.
        SmartInventor.DCMotor(M1, CW, 50);
        SmartInventor.DCMotor(M2, CW, 50);
    }
    else
    {
        // Go forward.
        SmartInventor.DCMotor(M1, CCW, 50);
        SmartInventor.DCMotor(M2, CW, 50);
    }
}
