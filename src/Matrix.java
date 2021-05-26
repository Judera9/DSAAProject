import java.io.*;
import java.util.ArrayList;

public class Matrix{
    public int row;
    public int column;
    public double[] matrix;

    public Matrix(int a, int b){
        /*
         * create a nxn matrix and store it value into a one dimension array
         */
        row = a;
        column = b;
        matrix = new double[a * b];
    }

    public Matrix(double val){
        /*
         * create a 1x1 matrix with value is val
         */
        row = 1;
        column = 1;
        matrix = new double[1];
        matrix[0] = val;
    }

    public Matrix() {
        row = 0;
        column = 0;
        matrix = null;
    }

    public int getRow(Matrix a){
        /*
         * find the row of the given square matrix
         */
        double[] b = a.matrix;
        return (int)Math.pow(b.length,0.5);
    }

    public int getColumn(Matrix a){
        /*
         * find the column of the given square matrix
         */
        double[] b = a.matrix;
        return (int)Math.pow(b.length,0.5);
    }

    public Matrix MatrixAdd(Matrix a,Matrix b){
        /*
         * a method for adding two same size matrix
         */
        int row1 = b.getRow(b);
        int column1 = a.getColumn(a);
        Matrix result = new Matrix(row1,column1);
        for(int i = 0;i < row1;i++) {
            for(int j = 0;j < column1;j++) {
                result.matrix[i * column1+ j] = a.matrix[i * column1 + j] + b.matrix[i * column1 + j];
            }
        }//cij = aij + bij for C = A + B
        return result;
    }

    public Matrix MatrixMin(Matrix a, Matrix b) {
        /*
         * a method to minus two same size matrix
         */
        int row1 = b.getRow(b);
        int column1 = a.getColumn(a);
        Matrix result = new Matrix(row1,column1);
        for(int i = 0;i < row1;i++) {
            for(int j = 0;j < column1;j++) {
                result.matrix[i * column1 + j] = a.matrix[i * column1 + j] - b.matrix[i * column1 + j];
            }
        }//cij = aij - bij for C = A - B
        return result;
    }

    public void setVal(int row,int column,double val) {
        /*
         * set val at i-th row and j-th column in the matrix
         */
        matrix[(row) * this.getColumn(this) + column] = val;
    }

    public double getVal(int row,int column) {
        /*
         * get the value at i-th row and j-th column in the matrix
         */
        return matrix[(row) * this.getColumn(this) + column];
    }

    public Matrix BlockMatrix(int startRow,int endRow,int startColumn,int endColumn,Matrix a){
        /*
         * Divide the matrix into four blocks of the same size
         */
        Matrix result = new Matrix(endRow - startRow + 1,endColumn - startColumn + 1);
        for(int i = startRow;i <= endRow;i++){
            for (int j = startColumn;j <= endColumn;j++){
                result.matrix[(i - startRow) * (endColumn - startColumn + 1) + j - startColumn] = a.matrix[(i - 1) * a.getColumn(a) + j - 1];
                //block the matrix a into small part result and give its value to new matrix
            }
            //(i - startRow) * (endColumn - startColumn + 1) is the i-th row's position start for matrix result,(j - startColumn) is the j-th one in i-th row in new matrix
            //(i - 1) * column + j - 1 is the position in the matrix we want to split
        }
        return result;
    }
    public Matrix getMatrix(String strFile){
        /*
         * get the value recorded in the txt file
         * transform it to a matrix and return the matrix
         */
        try {
            BufferedReader reader  = new BufferedReader(new FileReader(strFile));
            String temp = "";
            ArrayList<String> matrix = new ArrayList<String>();
            while((temp = reader.readLine())!=null) {
                matrix.add(temp);
            }
            reader.close();
            String[] matrix_split = matrix.get(0).split("\t");
            Matrix result = new Matrix(matrix.size(),matrix_split.length);
            for(int i = 0;i<matrix.size();i++) {
                matrix_split = matrix.get(i).split("\t");
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
    public void createMatrix(int n){
        /*
         * create a nxn matrix with mij = 1
         * record it to a txt file named Text1
         */
        int[] matrix = new int[(int)Math.pow(n,2)];
        FileWriter fileWriter;
        for (int i = 0;i < Math.pow(n,2);i++){
            matrix[i] = 1;
        }
        try {
            fileWriter = new FileWriter("Text1.txt");//创建文本文件
            for (int i = 0;i < Math.pow(n,2);i++){
                fileWriter.write(matrix[i] + "\t");
            }
            fileWriter.flush();
            fileWriter.close();
        } catch (IOException ex) {
            // TODO Auto-generated catch block
            ex.printStackTrace();
        }


    }

}