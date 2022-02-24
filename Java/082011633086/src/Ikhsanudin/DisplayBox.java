package Ikhsanudin;
import javax.swing.JOptionPane;

public class DisplayBox {

    public static void main(String[] args) {
        
        ClassDisplays x = new ClassDisplays();
        
        String a = "";
        
        JOptionPane.showMessageDialog(null, x.Cont(a)+x.Content(a), x.Disp(a), JOptionPane.INFORMATION_MESSAGE);
    }
    
}
