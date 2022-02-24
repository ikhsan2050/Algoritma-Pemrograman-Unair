
package Ikhsanudin;
import java.util.Arrays;
import java.util.Scanner;

public class DesimalToBiner {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int desimal;
        System.out.println("masukkan bilangan");
        desimal = input.nextInt();
        int des=desimal;
        int []biner = new int [desimal];
        
        int i=0;
        double Bil=0;
        //biner[0]=0;
        
        while (desimal!=0){
            biner[i]=desimal%2;
            desimal=desimal/2;
            i++;
        }
        //System.out.println(Arrays.toString(biner));
        
        //System.out.print("Biner");
        if(des==0){
            System.out.print("Biner =  "+0);
            System.out.println();
        }
        else {
            System.out.print("Biner =  ");
            for(int j=i-1; j>=0; j--){
            System.out.print(""+biner[j]);
        }
        }
        System.out.println();
    }
}
