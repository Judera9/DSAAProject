/*
 * The class is used to calculate the matrix by a standard way
 */

public class SquareMult {
    public SquareMult(){
    }
    public Matrix standardMult(Matrix a,Matrix b) {
        /*
         *
         */
        if(a.getColumn(a) != b.getRow(b)) {
            System.out.println("Error");//Make sure that matrix can be multiplied
            return null;
        }
        Matrix result = new Matrix(a.getRow(a),b.getColumn(b));//Set a new n×n matrix to store result
        double val = 0;
        for(int i = 0;i < a.getRow(a);i++) {
            for(int j = 0;j < b.getColumn(b);j++) {
                val = 0;//val is cij
                for(int k = 0;k < a.getColumn(a);k++) {
                    val = val + a.getVal(i, k) * b.getVal(k, j);
                }
                result.setVal(i, j, val);
            }//follow the pseudo given
        }
        return result;
    }
}