/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package Ikhsanudin;
import java.util.Scanner;
/**
 *
 * @author PC
 */
public class H_maks {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        double Vawal;
        double g = 9.8;
        
        System.out.println("Input Vawal");
        Vawal=input.nextDouble();
        
        double h=(Vawal*Vawal)/(2*g);
        
        System.out.println("h maks="+h);
}
}
