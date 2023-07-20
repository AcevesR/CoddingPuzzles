/* In one step, any element of a given array can be either increased or decreased by 1.
Write a function:
class Solution { public int solution (int[] A); } 
that, given an array A of N integers, 
returns the minimum number of steps required to make all elements equal. 

Examples: 
1. Given A = [3, 2, 1, 1, 2, 3, 1], the function should return 5. 
All 1s can be increased by 1 and all 3s can be decreased by 1. 

2. Given A = [4, 1,4, 1], the function should return 6. 
All 4s can be decreased by 1 three times. 

3. Given A = [3,3,3] the function should return 0. 
All elements are already the same. 

Write an efficient algorithm for the following assumptions: 
N is an integer within the range [1..100,000]; 
each element of array A is an integer within the range [1..4].
*/


import java.util.Arrays;

class Solution {
    public int solution(int[] A) {
        int n = A.length;
        Arrays.sort(A); // Sort the array to find the median value

        int median = A[n / 2]; // Median value, as the array is sorted

        int steps = 0;
        for (int i = 0; i < n; i++) {
            steps += Math.abs(A[i] - median); // Calculate the steps needed for each element
        }

        return steps;
    }
}

public class Main {
    public static void main(String[] args) {
        // Test cases
        int[] A1 = {3, 2, 1, 1, 2, 3, 1};
        int[] A2 = {4, 1, 4, 1};
        int[] A3 = {3, 3, 3};

        Solution solution = new Solution();

        int result1 = solution.solution(A1);
        int result2 = solution.solution(A2);
        int result3 = solution.solution(A3);

        System.out.println("Result 1: " + result1); // Output: Result 1: 5
        System.out.println("Result 2: " + result2); // Output: Result 2: 6
        System.out.println("Result 3: " + result3); // Output: Result 3: 0
    }
}
