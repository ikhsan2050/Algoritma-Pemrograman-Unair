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
public class Cari_Ganjil_Genap {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
    Scanner input = new Scanner(System.in);
    int a;
    System.out.println("Input 4 digit angka");
        a=input.nextInt();
        int bil1=a%10;
        a=(a-bil1)/10;
        int bil2=a%10;
        a=(a-bil2)/10;
        int bil3=a%10;
        a=(a-bil3)/10;
        int bil4=a%10;
        
        int ganjil=0;
        int genap=0;
        
        if(bil1%2==0){
            genap=genap+1;
        }
        else{
            ganjil=ganjil+1;
        }
        if(bil2%2==0){
            genap=genap+1;
        }
        else{
            ganjil=ganjil+1;
        }
        
        if(bil3%2==0){
            genap=genap+1;
        }
        else{
            ganjil=ganjil+1;
        }
        if(bil4%2==0){
            genap=genap+1;
        }
        else{
            ganjil=ganjil+1;
        }
        
        System.out.println("jumlah bilangan ganjil  =   "+ganjil);
        System.out.println("jumlah bilangan genap   =   "+genap);
    }
    
}
