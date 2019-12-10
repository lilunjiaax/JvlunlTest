import java.util.Scanner;
public class JD {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int a  = input.nextInt();
        int [][]map = new int[a][2];
        for (int i = 0; i < a; i++) {
            map[i][0] = input.nextInt();
            map[i][1] = i+1;
        }
        int temp1,temp2;
        for (int i = 0; i <a-1 ; i++) {
            for (int j = i+1; j < a; j++) {
                if(map[i][0]>map[j][0])
                {
                    temp1 = map[i][0];
                    temp2 = map[i][1];
                    map[i][0] = map[j][0];
                    map[i][1] = map[j][1];
                    map[j][0] = temp1;
                    map[j][1]= temp2;
                }
            }
        }
        int count =1;
        for (int i = 0; i < a-1; i++) {
            if(Math.abs(map[i][1]-map[i+1][1])==1)
            {
                if(map[i+1][1]-map[i][1]==1)
                {
                    count++;
                }
                continue;
            }
            else count++;
        }
        System.out.println(count);


    }
}