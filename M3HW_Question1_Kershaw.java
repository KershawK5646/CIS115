import java.awt.Canvas;
import java.awt.Graphics;
import javax.swing.JFrame;
import java.awt.Color;

/** Objectives:
* Create a function that draws a square (DONE)
* Create a function that draws a circle within that square (DONE)
*/

public class M3HW_Question1_Kershaw extends Canvas{
	public static void main(String[] args){
		JFrame frame = new JFrame("My Drawing"); //This is the window that will contain the canvas
		Canvas canvas = new M3HW_Question1_Kershaw();
		canvas.setSize(800,800); // This sets the size of the canvas
		canvas.setBackground(Color.white);
		frame.add(canvas);
		frame.pack(); // This packs the canvas to resize it for the screen
		frame.setVisible(true);
	}
	public void paint(Graphics g){
		g.fillRect(50,50,400,400);
		g.setColor(Color.blue);
		g.fillOval(50,50,400,400);
	}
}