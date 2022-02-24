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
public class Modulo_Devisi {
    public static void main(String[] args) {
        int a,b;
        
        Scanner input = new Scanner(System.in);
        
        System.out.println("input a");
        a=input.nextInt();
        
        System.out.println("input b");
        b=input.nextInt();
        
        int n=a;
        int mod=0;
        int dev=0;
        
        if(a>b){
        while(n-b>=0 && n!=0){
            mod=n-b;
            dev=dev+1;
            n=n-b;
        }
        }
        
        System.out.println(a+" dev "+b+" = "+dev);
        System.out.println(a+" mod "+b+" = "+mod);
    }
}
