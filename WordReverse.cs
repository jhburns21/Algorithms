// Sample code to read in test cases:
using System;

class FizzBuzz
{
    static void Main(string[] args)
    {
      string[] lines = System.IO.File.ReadAllLines(@args[0]);
      foreach (string line in lines)
      {
        if(line != "\n")
        {
          string[] words = line.Split(' ');
          string newLine = "";

          foreach (string w in words)
          {
            newLine = w + " " + newLine;
          }
          Console.WriteLine(newLine);
        }
      }
    }
}
