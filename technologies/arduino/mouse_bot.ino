#include <SmartInventor.h>

void setup()
{
    Serial.begin(9600);
    SmartInventor.DCMotorUse();
    randomSeed(analogRead(0));
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
        SmartInventor.DCMotor(M1, CW, 50);
        SmartInventor.DCMotor(M2, CCW, 50);
        delay(1000);
        long randomTurn = random(100);
        Serial.println(randomTurn);
        if (randomTurn > 50)
        {
            // Turn left.
            SmartInventor.DCMotor(M1, CW, 50);
            SmartInventor.DCMotor(M2, CW, 50);
        }
        else if (randomTurn <= 50)
        {
            // Turn right.
            SmartInventor.DCMotor(M1, CCW, 50);
            SmartInventor.DCMotor(M2, CCW, 50);
        }
        delay(250);
    }
    else
    {
        // Go forward.
        SmartInventor.DCMotor(M1, CCW, 50);
        SmartInventor.DCMotor(M2, CW, 50);
    }
}

// 33 left
// 2 left
// 41 left
// 77 right
// 78 right
// 55 right
// 50 right
// 97 right
// 5 left
// 16 left
// 2 left
// 60 right
// 88 right
