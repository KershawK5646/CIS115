import java.awt.Canvas;
import java.awt.Graphics;
import javax.swing.JFrame;
import java.awt.Color;

/**
Write a method for each of the letters H, E, L, and O.
Each should draw the selected letter using line graphics at the selected X Y coordinates.

Try to keep a 100 sizing/ Spacing if possible.
*/
public class M3HW_Question3_Kershaw extends Canvas{
	// MAIN
	public static void main (String[] args) {
		JFrame frame = new JFrame ("My Drawing");
		Canvas canvas = new M3HW_Question3_Kershaw();
		canvas.setSize(1500,1000);
		frame.add(canvas);
		frame.pack();
		frame.setVisible(true);
	}
	// Calling my functions.
	public void paint(Graphics g) {
		//Call my functions below.
		drawH(g, 100,100);
		drawE(g, 300,100);
		drawL(g, 500,100);
		drawL(g, 700,100);
		drawO(g, 850,100);
	}
	
	//Draw an H from starting coordinates.
	public void drawH (Graphics g, int x, int y){
		g.drawLine(x,y, x,y+200); //Left line of H.
		g.drawLine(x+100,y, x+100,y+200); //Right line of H
		g.drawLine(x,y+100, x+100,y+100); //Middle of H.
	}
	
	//Draw an E from starting coordinates.
	public void drawE (Graphics g, int x, int y){
		g.drawLine(x,y, x, y+200); 		   //Spine of E.
		g.drawLine(x,y, x+100,y);  		   //Top line of E.
		g.drawLine(x,y+100, x+100,y+100);  //Middle line of E.
		g.drawLine(x,y+200, x+100,y+200);  //Bottom line of E.		
	}
	//Draw an L from starting coordinates.
	public void drawL (Graphics g, int x, int y){
		g.drawLine(x,y, x, y+200); //Draws L Spine.
		g.drawLine(x,y+200, x+100,y+200); //Draws bottom of L.
	}
	//Draw an 0 from starting coordinates.
	public void drawO (Graphics g, int x, int y){
		g.drawOval(x,y, 200,200); //Uses the native oval command to draw the O.
	}
}