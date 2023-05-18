import java.util.*;
class maxi_pair{




   public static long MaximumPair(int[] num_arr){
        int size=num_arr.length;
        long result=0;
        for(int i=0;i<size-1;i++){
            for(int j=i+1;j<size;j++){
                if((long)(num_arr[i]*num_arr[j])>result){
                    result=(long)(num_arr[i]*num_arr[j]);
                }

            }
        }
        return result;


    }
    public static void main(String[] args){
        Scanner ob = new Scanner(System.in); 
            int a=ob.nextInt();
            int [] arr=new int[a];
            for(int i=0;i<a;i++)
            arr[i]=ob.nextInt();
            long result=MaximumPair(arr);
            System.out.println(result);
            


        }

        
    }
