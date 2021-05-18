import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Matrix{
    public int row;
    public int column;
    public double[] matrix;

    public Matrix(int a, int b){
        row = a;
        column = b;
        matrix = new double[a * b];
    }//create a nxn matrix and store it value into a one dimension array

    public Matrix(double val){
        row = 1;
        column = 1;
        matrix = new double[1];
        matrix[0] = val;
    }//create a 1x1 matrix

    public Matrix() {
        row = 0;
        column = 0;
        matrix = null;
    }

    public Matrix MatrixAdd(Matrix a,Matrix b){
        Matrix result = new Matrix(a.row,a.column);
        for(int i = 0;i < a.row;i++) {
            for(int j = 0;j < a.column;j++) {
                result.matrix[i * a.column + j] = a.matrix[i * a.column + j] + b.matrix[i * a.column + j];
            }
        }//cij = aij + bij for C = A + B
        return result;
    }

    public Matrix MatrixMin(Matrix a, Matrix b) {
        Matrix result = new Matrix(a.row,a.column);
        for(int i = 0;i < a.row;i++) {
            for(int j = 0;j < a.column;j++) {
                result.matrix[i * a.column + j] = a.matrix[i * a.column + j] - b.matrix[i * a.column + j];
            }
        }//cij = aij - bij for C = A - B
        return result;
    }

    public void setVal(int row,int column,double val) {
        matrix[(row) * this.column + column] = val;
    }

    public double getVal(int row,int column) {
        return matrix[(row) * this.column + column];
    }

    public Matrix BlockMatrix(int startRow,int endRow,int startColumn,int endColumn,Matrix a){
        Matrix result = new Matrix(endRow - startRow + 1,endColumn - startColumn + 1);
        for(int i = startRow;i <= endRow;i++){
            for (int j = startColumn;j <= endColumn;j++){
                result.matrix[(i - startRow) * (endColumn - startColumn + 1) + j - startColumn] = a.matrix[(i - 1) * column + j - 1];
                //block the matrix a into small part result and give its value to new matrix
            }
            //(i - startRow) * (endColumn - startColumn + 1) is the i-th row's position start for matrix result,(j - startColumn) is the j-th one in i-th row in new matrix
            //(i - 1) * column + j - 1 is the position in the matrix we want to split
        }
        return result;
    }
    public Matrix getMatrix(String strFile){
        try {
            BufferedReader reader  = new BufferedReader(new FileReader(strFile));
            String temp = "";
            ArrayList<String> matrix = new ArrayList<String>();
            while((temp = reader.readLine())!=null) {
                matrix.add(temp);
            }
            reader.close();
            String[] matrix_split = matrix.get(0).split(" ");
            Matrix result = new Matrix(matrix.size(),matrix_split.length);
            for(int i = 0;i<matrix.size();i++) {
                matrix_split = matrix.get(i).split(" ");
                for(int j = 0;j<matrix_split.length;j++) {
                    result.setVal(i, j, Double.parseDouble(matrix_split[j]));
                }
            }
            return result;
        }catch(Exception e){
            e.printStackTrace();
            return null;
        }
    }
}