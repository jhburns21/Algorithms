using System.IO;
using System.Collections.Generic;

public class Node
{
  Node* left;
  Node* right;
  int data;
}

public class BST
{

  static void InorderTreeWalk(Node x)
  {
    InorderTreeWalk(x.left);
    Console.WriteLine(x.data);
    InorderTreeWalk(x.right);
  }
}

class program
{
  static void main()
  {

  }
}
