import java.util.Scanner;

public class Strassen1 {
    public Matrix Strassen(Matrix a, Matrix b){//this method is for the matrix's dimension with power of 2
        if(a.column == 1 && a.row == 1) {
            return new Matrix(a.matrix[0] * b.matrix[0]);
        }
        Matrix temp = new Matrix();
        Matrix result = new Matrix(a.row,b.column);
        //int halfSize = a.row * b.column / 2;
        Matrix A = a.BlockMatrix(1,a.row / 2,1,a.column / 2,a);
        Matrix B = a.BlockMatrix(1,a.row / 2,(a.column / 2) + 1,a.column,a);
        Matrix C = a.BlockMatrix((a.row / 2) + 1,a.row,1,a.column / 2,a);
        Matrix D = a.BlockMatrix((a.row / 2) + 1,a.row,(a.column / 2) + 1,a.column,a);
        //matrix A,B,C,D is block a into four matrix with same large
        Matrix E = b.BlockMatrix(1,b.row / 2,1,b.column / 2,b);
        Matrix F = b.BlockMatrix(1,b.row / 2,(b.column / 2) + 1,b.column,b);
        Matrix G = b.BlockMatrix((b.row / 2) + 1,b.row,1,b.column / 2,b);
        Matrix H = b.BlockMatrix((b.row / 2) + 1,b.row,(b.column / 2) + 1,b.column,b);
        //matrix E,F,G,H is block a into four matrix with same large

        Matrix S1 = temp.MatrixMin(F,H);
        Matrix S2 = temp.MatrixAdd(A,B);
        Matrix S3 = temp.MatrixAdd(C,D);
        Matrix S4 = temp.MatrixMin(G,E);
        Matrix S5 = temp.MatrixAdd(A,D);
        Matrix S6 = temp.MatrixAdd(E,H);
        Matrix S7 = temp.MatrixMin(B,D);
        Matrix S8 = temp.MatrixAdd(G,H);
        Matrix S9 = temp.MatrixMin(A,C);
        Matrix S10 = temp.MatrixAdd(E,F);
        /*
         * divide and conquer follow pseudo
         */
        Matrix P1 = Strassen(A,S1);
        Matrix P2 = Strassen(S2,H);
        Matrix P3 = Strassen(S3,E);
        Matrix P4 = Strassen(D,S4);
        Matrix P5 = Strassen(S5,S6);
        Matrix P6 = Strassen(S7,S8);
        Matrix P7 = Strassen(S9,S10);

        Matrix C11 = temp.MatrixMin(temp.MatrixAdd(P5, P4),temp.MatrixMin(P2, P6));
        Matrix C12 = temp.MatrixAdd(P1, P2);
        Matrix C21 = temp.MatrixAdd(P3, P4);
        Matrix C22 = temp.MatrixMin(temp.MatrixAdd(P5, P1), temp.MatrixAdd(P3, P7));
        //follow pseudo

        for(int i = 0;i < result.row;i++) {
            for(int j = 0; j < result.column;j++) {
                if(i < C11.row) {
                    if(j < C11.column) {
                        result.setVal(i, j, C11.getVal(i, j));
                    }else {
                        result.setVal(i, j, C12.getVal(i, j-C12.column));
                    }
                }else {
                    if(j < C11.column) {
                        result.setVal(i, j, C21.getVal(i-C11.row, j));
                    }else {
                        result.setVal(i, j, C22.getVal(i-C11.row,j-C22.column));
                    }
                }
            }
        }
        return result;
    }
    public Matrix Strassen2(Matrix a,Matrix b){//this method is to calculate matrix multiply with any value of n
        if(a.column == 1 && a.row == 1) {
            return new Matrix(a.matrix[0] * b.matrix[0]);
        }
        int m = 0;//find m satisfy that 2^m - c = n, and 2^m>n>2^(m-1)
        for (int i = 0;i < a.row;i++){
            if (Math.pow(2,i) > a.row){
                m = i;
                break;
            }
        }
        Matrix A1 = new Matrix((int) Math.pow(2,m),(int)Math.pow(2,m));
        for(int i = 0;i < A1.row;i++) {
            for(int j = 0; j < A1.column;j++) {
                if(i < a.row) {
                    if(j < a.column) {
                        A1.setVal(i, j, a.getVal(i, j));
                    }else {
                        A1.setVal(i, j, 0);
                    }
                }
                else {
                A1.setVal(i,j,0);
                }
            }
        }//use 0 to fill bigger matrix A1
        Matrix B1 = new Matrix((int) Math.pow(2,m),(int)Math.pow(2,m));
        for(int i = 0;i < B1.row;i++) {
            for(int j = 0;j < B1.column;j++) {
                if(i < b.row) {
                    if(j < b.column) {
                        B1.setVal(i, j, b.getVal(i, j));
                    }else {
                        B1.setVal(i, j, 0);
                    }
                }
                else {
                    B1.setVal(i,j,0);
                }
            }
        }//use 0 to fill the bigger matrix B1
        Matrix result = new Matrix(a.row,b.column);
        /*for(int i = 0; i < Math.pow(A1.row,2); i++){
            System.out.print(A1.matrix[i] + " ");
        }*/
        Matrix temp = Strassen(A1,B1);
        for(int i = 0;i < temp.row;i++) {
            for(int j = 0; j < temp.column;j++) {
                if(i < result.row) {
                    if(j < result.column) {
                        result.setVal(i, j, temp.getVal(i, j));
                    }
                }
            }
        }
        return result;
    }
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner input = new Scanner(System.in);
        Strassen1 temp = new Strassen1();
        while(input.hasNext()){
            int n = input.nextInt();
            Matrix matrixA = new Matrix(n,n);
            Matrix matrixB = new Matrix(n,n);
            for(int i = 0; i < Math.pow(n,2); i++)
                    matrixA.matrix[i]= input.nextInt();
            for(int i = 0; i < Math.pow(n,2); i++)
                    matrixB.matrix[i] = input.nextInt();
            Matrix result = temp.Strassen2(matrixA,matrixB);
            for(int i = 0; i < Math.pow(n,2); i++){
                System.out.print(result.matrix[i] + " ");
            }
        }
    }
    public Strassen1() {
    }
}