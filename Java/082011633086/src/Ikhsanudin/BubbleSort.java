
package Ikhsanudin;

import java.util.Arrays;

public class BubbleSort {

    public static void main(String[] args) {
        boolean changed = true;
        double [] list = {6.0, 4.4, 1.9, 2.9, 3.4, 2.9, 3.5};
        
        do {
            changed = false;
            for (int j = 0; j < list.length - 1; j++){
                if (list[j] > list[j + 1]) {
                    double x = list[j];
                    list[j] = list[j+1];
                    list[j+1] = x;
                    changed = true;
                }
            }
                
        }
        while (changed);
        System.out.println("data terurut");
        System.out.println(Arrays.toString(list));
    }
    
}
