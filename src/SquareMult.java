/*
 * The class is used to calculate the matrix by a standard way
 */

public class SquareMult {
    public Matrix standardMult(Matrix a,Matrix b) {
        if(a.column != b.row) {
            System.out.println("Error");//Make sure that matrix can be multiplied
            return null;
        }
        Matrix result = new Matrix(a.row,b.column);//Set a new n×n matrix to store result
        double val = 0;
        for(int i = 0;i < a.row;i++) {
            for(int j = 0;j < b.column;j++) {
                val = 0;//val is cij
                for(int k = 0;k < a.column;k++) {
                    val = val + a.getVal(i, k) * b.getVal(k, j);
                }
                result.setVal(i, j, val);
            }//follow the pseudo given
        }
        return result;
    }
}