package org.example;

import java.util.Arrays;
import java.util.List;

public class firstAndLastPosition {

    public int[] firstAndLastPos(Integer[] numbers , int target){
        int[] positions = {-1,-1};

        List<Integer> numbersList= Arrays.asList(numbers);
        if(numbersList.contains(target)){
            positions[0]=numbersList.indexOf(target);
            positions[1]=numbersList.lastIndexOf(target);
        }
            for (int i : positions){
                System.out.println(i);
            }
        return positions;
    }
}
