
package Ikhsanudin;
import java.util.Arrays;
import java.util.Scanner;
        
public class FibonaciModify {

    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        int a;                   // a  adalah panjang array deret Fibonaci
        System.out.println("input panjang deret Fibonaci");
        a = input.nextInt();
        
        int []fibo = new int[a]; // []fibo adalah array deret fibonaci
        int x;                   // x  adalah suku yang dikurangi
        int y;                   // y  adalah bilangan pengurang 
        
        System.out.println("input suku pertama");
        fibo[0] = input.nextInt();
        
        System.out.println("input suku kedua");
        fibo[1] = input.nextInt();
        
        System.out.println("input suku dan kelipatan yang dikurangi");
        x = input.nextInt();
        
        System.out.println("input bilangan pengurang");
        y = input.nextInt();
        
        int z = x;               // z adalah kelipatan suku yang dikurangi
        
        //Langkah (1) mengisi array deret fibonaci
        for (int i=2; i<a; i++)
            fibo[i] = fibo[i-1]+fibo[i-2];
        //System.out.print("Deret Fibonaci awal =  ");
        //System.out.println(Arrays.toString(fibo));
        
        //Langkah (2) mengurangi suku ke-z dengan bilangan pengurang
        //Langkah (3) mengisi data setelah suku ke-z yang baru
        while (z<=a){
            fibo[z-1] = fibo[z-1] - y;
            for (int i=z; i<a; i++){
            fibo[i] = fibo[i-1]+fibo[i-2];
            }
            z = z+x;
        }
        
        //Langkah (4) menampilkan array deret fibonaci baru
        System.out.print("Deret Fibonaci      =  ");
        System.out.println(Arrays.toString(fibo));
    }
}
