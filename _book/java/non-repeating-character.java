// Function for java to detect if there's a non-repeating character.

public static char nonRepeatingCharacter(String a)
{
    int repeatCount = 0;
    char [] stringCharArray = a.toCharArray();
    for(int i = 0; i < stringCharArray.length; i++)
    {
        repeatCount = 0;
        for(int j = 0; j < stringCharArray.length; j++)
        {
            if(stringCharArray[i] == stringCharArray[j] && i != j)
            {
                repeatCount = 1;
                break;
            }
        }
        if(repeatCount == 0)
            return stringCharArray[i];
    }
    return 0;
}