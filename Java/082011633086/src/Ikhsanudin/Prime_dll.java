package Ikhsanudin;
import java.util.Scanner;

public class Prime_dll {

    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int n;
        boolean result = false;
        System.out.print("input bilangan =  ");
        n=input.nextInt();
        isPrime(n, result);
        greatestPrime(n, result);
    }
    public static boolean isPrime (int n, boolean result) {
        int faktor=0;
        
        for (int i=1; i<=n; i++){
            if (n%i==0){
                faktor=faktor+1;
            }
        }
        if (faktor==2){
            result= true;
            //System.out.println("prima");
            return result;
        }
        else {
            result=false;
            //System.out.println("Bukan prima");
            return result;
        } 
    }
    public static int greatestPrime(int n, boolean result){
        boolean max=false;
        int i=n;
        int great=0;
        while(max==false){
            i=i-1;
            max=isPrime(i, result);
            //System.out.println(max);
            great=i;
        }
        
        System.out.println("Prima Terbesar  "+great);
        return great;
        
    }
}