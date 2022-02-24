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
public class Membalik_Bilangan {
    public static void main(String[] args) {
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
        
        int angka=bil1*1000+bil2*100+bil3*10+bil4;
        
        System.out.println(angka);
    }
}