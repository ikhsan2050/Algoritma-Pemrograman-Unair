
package Ikhsanudin;
import java.util.Arrays;
import java.util.Scanner;

public class BubbleSort_2 {

    public static void main(String[] args){
        boolean changed = true;
        Scanner input=new Scanner(System.in);
        
        int panjang;
        System.out.println("input panjang array");
        System.out.println("  (dimulai dari 0) ");
            panjang=input.nextInt();
            
        int [] list = new int [panjang];
        for (int i=0; i<list.length; i++){
            System.out.print("input array ["+i+"]  ");
            list[i]=input.nextInt();   
        }
        
        do {
            changed = false;
            for (int j = 0; j < list.length - 1; j++){
                if (list[j] > list[j + 1]) {
                    int x=list[j];
                    list[j]=list[j+1];
                    list[j+1]=x;
                    changed = true;
                }
                }
                
        }
        while (changed);
        System.out.println("data terurut");
        System.out.println(Arrays.toString(list));
    }
}
