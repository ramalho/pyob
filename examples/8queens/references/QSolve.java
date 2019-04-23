import java.awt.*;
import java.applet.*;

class Queen {
		// data fields
	private int row;
	private int column;
	private Queen neighbor;

		// constructor
	Queen (int c, Queen n) {
			// initialize data fields
		row = 1;
		column = c;
		neighbor = n;
		}

	public boolean findSolution() {
		while (neighbor != null && neighbor.canAttach(row, column))
			if (! advance())
				return false;
		return true;
		}

	public boolean advance() {
		if (row < 8) {
			row++;
			return findSolution();
			}
		if (neighbor != null) {
			if (! neighbor.advance())
				return false;
			if (! neighbor.findSolution())
				return false;
			}
		else
			return false;
		row = 1;
		return findSolution();
			
		}

	private boolean canAttach(int testRow, int testColumn) {
		int columnDifference = testColumn - column;
		if ((row == testRow) ||
			(row + columnDifference == testRow) ||
			(row - columnDifference == testRow))
				return true;
		if (neighbor != null)
			return neighbor.canAttach(testRow, testColumn);
		return false;
		}

	public void paint (Graphics g) {
			// first draw neighbor
		if (neighbor != null)
			neighbor.paint(g);
			// then draw ourself
			// x, y is upper left corner
		int x = (row - 1) * 50;
		int y = (column - 1) * 50;
		g.drawLine(x+5, y+45, x+45, y+45);
		g.drawLine(x+5, y+45, x+5, y+5);
		g.drawLine(x+45, y+45, x+45, y+5);
		g.drawLine(x+5, y+35, x+45, y+35);
		g.drawLine(x+5, y+5, x+15, y+20);
		g.drawLine(x+15, y+20, x+25, y+5);
		g.drawLine(x+25, y+5, x+35, y+20);
		g.drawLine(x+35, y+20, x+45, y+5);
		g.drawOval(x+20, y+20, 10, 10);
		}

	public void foo(Queen arg, Graphics g) {
		if (arg.row == 3)
			g.setColor(Color.red);
		}
}

public class QSolve extends Applet {

	private Queen lastQueen;

	public void init() {
		int i;
		lastQueen = null;
		for (i = 1; i <= 8; i++) {
			lastQueen = new Queen(i, lastQueen);
			lastQueen.findSolution();
			}
		}

	public void paint(Graphics g) {
			// draw board
		for (int i = 0; i <= 8; i++) {
			g.drawLine(50 * i, 0, 50*i, 400);
			g.drawLine(0, 50 * i, 400, 50*i);
			}
			// draw queens
		lastQueen.paint(g);
		}

	public boolean mouseDown(java.awt.Event evt, int x, int y) {
		lastQueen.advance();
		repaint();
		return true;
		}

}

