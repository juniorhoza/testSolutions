package org.example;

public class singleSalary {
    public int singlesalary(int[] salaries){
        int uniqueSalary=0;
                for(int i=0;i<salaries.length;i++){
                    for(int j=0;j<salaries.length;j++){
                        if(salaries[i]==salaries[j]){
                            break;

                        }
                        else{
                            uniqueSalary= salaries[i];
                        }
                    }
                }
        return  uniqueSalary;
    }
}
