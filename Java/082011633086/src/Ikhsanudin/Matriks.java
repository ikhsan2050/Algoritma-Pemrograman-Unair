package Ikhsanudin;
import java.util.Scanner;

public class Matriks {

    public static void main(String[] args) {
        int data[][]=new int[3][3];
        Scanner input=new Scanner(System.in);
        int frek[]=new int[10];
        int modus;
        
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                System.out.println("input matriks ke"+"["+i+"]"+"["+j+"]");
                data[i][j]=input.nextInt();
            }
        }
        for(int i=0; i<=9; i++){
            frek[i]=0;
        }
        for(int i=0; i<=9; i++){
            for(int j=0; j<=2; j++){
                for(int k=0; k<=2; k++){
                    if(i==data[j][k]){
                        frek[i]=frek[i]+1;
                    }
                }
            }
        }
        modus=frek[0];
        for (int i=1; i<=9; i++){
            if(modus<frek[i]){
                modus=i;
            }
        }
        System.out.println();
        System.out.println("matriks");
        for(int i=0; i<3; i++){
            System.out.print(data[0][i]+"  ");
        }
        System.out.println();
        for(int i=0; i<3; i++){
            System.out.print(data[1][i]+"  ");
        }
        System.out.println();
        for(int i=0; i<3; i++){
            System.out.print(data[2][i]+"  ");
        }
        System.out.println();
        System.out.println();
        System.out.println("modus =  "+modus);
}
    
}
