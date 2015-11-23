/* 
 * File:   main.cpp
 * Author: john
 *
 * Created on November 13, 2015, 2:38 PM
 */

#include <cstdlib>
#include <iostream>
using namespace std;

struct gridTile {
    bool isValid;
    char color;
};

// Determine all valid locations on the grid. 
void calcValid(gridTile (&grid)[299][299]) {
    for(int i = 0; i < 299; i++) {
        for (int j = 0; j < 299; j++) {
            // add the digits in the x and y values
            int sum = 0;
            int curi = i;
            int curj = j;
            
            while(curj != 0) {
                sum = sum + (curj%10);
                curj = curj/10;
            }
            while(curi != 0) {
                sum = sum + (curi%10);
                curi = curi/10;
            }
            
            grid[i][j].color = 'w';
            if(sum > 19){ grid[i][j].isValid = false; }
            else { grid[i][j].isValid = true; }
        
        }
    }
}

// A first attempt at a recursive solution for finding all reachable points

//void traverse(int &r, int i, int j, gridTile (&grid)[200][200]) {
//    // cout << "i: " << i << " j: " << j << endl;
//    if(i == 200 || j == 200 || i < 0 || j < 0){
//        return;
//    }
//    
//    r++;
//    grid[i][j].visited = true;
//    
//    if(grid[i][j+1].isValid && grid[i][j+1].visited == false) {
//        traverse(r, i, j+1, grid);
//    }
//    
//    if(grid[i+1][j].isValid && grid[i+1][j].visited == false) {
//        traverse(r, i+1, j, grid);
//    }
//    
//    if(grid[i][j-1].isValid && grid[i][j-1].visited == false){
//        traverse(r, i, j-1, grid);
//    }
//    
//    if(grid[i-1][j].isValid && grid[i-1][j].visited == false){ 
//        traverse(r, i-1, j, grid);
//    }
//    cout << r << endl;
//}

// Modified version of DFS to find all reachable points in the grid
void DFSVisit(gridTile (&grid)[299][299], int i, int j, int &r) {
    grid[i][j].color = 'g';
    
    // Validity is used in place of an adjacency list to determine where to go.
    if(grid[i][j+1].isValid && (j+1) < 299 && grid[i][j+1].color == 'w'){
        DFSVisit(grid, i, j+1, r);
    }
    if(grid[i+1][j].isValid && (i+1) < 299 && grid[i+1][j].color == 'w'){
        DFSVisit(grid, i+1, j, r);
    }
    if(grid[i][j-1].isValid && (j-1) > 0 && grid[i][j-1].color == 'w'){
        DFSVisit(grid, i, j-1, r);
    }
    if(grid[i-1][j].isValid && (i-1) > 0 && grid[i-1][j].color == 'w'){
        DFSVisit(grid, i-1, j, r);
    }
    grid[i][j].color = 'b';
    r++;
}

// Wrapper for DFSVisit function
int DFS(gridTile (&grid)[299][299]) {
    int reachable = 0;
    DFSVisit(grid, 0, 0, reachable);
    return reachable;
}

// old function that worked with traverse
int countReachable(gridTile (&grid)[299][299]) {
    int reachable = 0;
    //traverse(reachable, 0, 0, grid);
    return reachable;
}

int main(int argc, char** argv) {
    // grid 200x200 since the maximum reachable point in the x and y direction is (299, 0) and (0, 299) respectively
    gridTile grid[299][299];
    
    calcValid(grid);
    int q1 = DFS(grid);
    int total = 4*q1 - (1195); // multiply by 4 and remove any double-counted points
    cout << total;
    return 0;
}
