//
//	Eight Queens puzzle written in Java
//	Written by Tim Budd, January 1996
//	revised for 1.3 event model July 2001
//

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

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
		int x = (row - 1) * 50 + 10;
		int y = (column - 1) * 50 + 40;
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

public class QueenSolver extends JFrame {

	public static void main(String [ ] args) {
		QueenSolver world = new QueenSolver();
		world.show();
	}

	private Queen lastQueen = null;

	public QueenSolver() {
		setTitle("8 queens");
		setSize(600, 500);
		for (int i = 1; i <= 8; i++) {
			lastQueen = new Queen(i, lastQueen);
			lastQueen.findSolution();
			}
		addMouseListener(new MouseKeeper());
		addWindowListener(new CloseQuit());
		}

	public void paint(Graphics g) {
		super.paint(g);
			// draw board
		for (int i = 0; i <= 8; i++) {
			g.drawLine(50 * i + 10, 40, 50*i + 10, 440);
			g.drawLine(10, 50 * i + 40, 410, 50*i + 40);
		}
		g.drawString("Click Mouse for Next Solution", 20, 470);
			// draw queens
		lastQueen.paint(g);
		}

	private class CloseQuit extends WindowAdapter {
		public void windowClosing (WindowEvent e) {
			System.exit(0);
		}
	}

	private class MouseKeeper extends MouseAdapter {
		public void mousePressed (MouseEvent e) {
			lastQueen.advance();
			repaint();
		}
	}
}

