using System;

class Song
{
    public string title;
    public string artist;
    public int duration;
    // `static` applies to the class itself, not particular to objects.
    public static int songCount = 0;

    public Song(string aTitle, string aArtist, int aDuration)
    {
        title = aTitle;
        artist = aArtist;
        duration = aDuration;
        songCount++;
    }

    public int getSongCount()
    {
        return songCount;
    }
}

class Driver
{
    static void Main(string[] args)
    {
        Console.WriteLine(Song.songCount);

        Song song1 = new Song("Rollercoaster", "Chungha", 420);

        Console.WriteLine(song1.artist);

        Console.WriteLine(Song.songCount);
        Console.WriteLine(song1.getSongCount());

        Console.ReadLine();
    }
}