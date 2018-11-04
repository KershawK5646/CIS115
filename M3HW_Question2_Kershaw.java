import java.awt.Canvas;
import java.awt.Graphics;
import javax.swing.JFrame;
import java.awt.Color;

/**
Write a method for each of the letters H, E, L, and O.
Each should draw the selected letter using line graphics at the selected X Y coordinates.

Try to keep a 100 sizing/ Spacing if possible.
*/
public class M3HW_Question2_Kershaw extends Canvas{
	
	//MAIN
	public static void main (String[] args){
		JFrame frame = new JFrame("My Drawing");
		Canvas canvas = new M3HW_Question2_Kershaw();
		canvas.setSize(1500,1000);
		frame.add(canvas);
		frame.pack();
		frame.setVisible(true);
	}
	public void paint(Graphics g){
		/** Call function here
		*/
		triangle(g, 500, 000); // Top center triangle
		triangle(g, 700, 200); // Bottom left triangle
		triangle(g, 300, 200); // Bottom right triangle
	}
	// Defining the triangle function.
	public void triangle(Graphics g, int x, int y){
		
		// Declaring variables needed.
		int rightBottomX = x+200; //Ending x coordinate for right line (700)
		int rightBottomY = y+200; //Ending y coordinate for right line (200)
		int leftBottomX = x-200; //Ending y coordinate for left line (300) 
		int leftBottomY = y+200; //Ending y coordinate for left line (200)
		
		/**Outputs bottom points for me to plan triforce
		System.out.println("Right bottom X point is...");
		System.out.println(rightBottomX);
		System.out.println("Right bottom Y point is...");
		System.out.println(rightBottomY);
		
		System.out.println("Left bottom X point is...");
		System.out.println(leftBottomX);
		System.out.println("Left bottom Y point is...");
		System.out.println(leftBottomY);
		*/
		
		g.drawLine(x, y, rightBottomX, rightBottomY); // Right line
		g.drawLine(x, y, leftBottomX, leftBottomY); // Left line
		g.drawLine(leftBottomX, leftBottomY, rightBottomX, rightBottomY); //Bottom Line
	}
}