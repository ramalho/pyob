//	eight queens puzzle in C++
//	written by Tim  Budd, Oregon State University, 1996
//

# include <iostream>
# define bool int // not all compilers yet support booleans

class queen {
public:
		// constructor
	queen (int, queen *);
	
		// find and print solutions
	bool findSolution();
	bool advance();
	void print();

private:
		// data fields
	int row;
	const int column;
	queen * neighbor;
	
		// internal method
	bool canAttack (int, int);
};

queen::queen(int col, queen * ngh)
	: column(col), neighbor(ngh)
{
	row = 1;
}

bool queen::canAttack (int testRow, int testColumn)
{
		// test rows
	if (row == testRow)
		return true;
		
		// test diagonals
	int columnDifference = testColumn - column;
	if ((row + columnDifference == testRow) ||
		(row - columnDifference == testRow))
			return true;
			
		// try neighbor
	return neighbor && neighbor->canAttack(testRow, testColumn);
}

bool queen::findSolution()
{
		// test position against neighbors
	while (neighbor && neighbor->canAttack (row, column)) 
		if (! advance())
			return false;
			
			// found a solution
	return true;
}

bool queen::advance()
{
	if (row < 8) {
		row++;
		return findSolution();
		}
		
	if (neighbor && ! neighbor->advance())
		return false;
		
	row = 1;
	return findSolution();
}

void queen::print()
{
	if (neighbor)
		neighbor->print();
	cout << "column " << column << " row " << row << '\n';
}

void main() {
	queen * lastQueen = 0;
	
	for (int i = 1; i <= 8; i++) {
		lastQueen = new queen(i, lastQueen);
		if (! lastQueen->findSolution())
			cout << "no solution\n";
		}
		
	lastQueen->print();
}