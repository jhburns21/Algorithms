// Sample code to read in test cases:
using System;
using System.IO;
using System.Collections.Generic;

class FizzBuzz
{
    static void Main(string[] args)
    {
      int d1, d2, cnt;
      string[] lines = System.IO.File.ReadAllLines(@args[0]);
      foreach (string line in lines)
      {
        string[] nums = line.Split(' ');
        Int32.TryParse(nums[0], out d1);
        Int32.TryParse(nums[1], out d2);
        Int32.TryParse(nums[2], out cnt);

        for(int i = 1; i <= cnt; i++)
        {
          string fb = "";
          fb += (i % d1) == 0 ? "F" : "";
          fb += (i % d2) == 0 ? "B" : "";
          Console.Write(fb.Length == 0 ? i.ToString() : fb);
          Console.Write( i < cnt ? " " : "");
        }
        Console.Write("\n");
      }
    }
}
