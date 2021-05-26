import java.io.FileWriter;
import java.io.IOException;

public class Strassen1 {
    public Matrix Strassen(Matrix a, Matrix b){//this method is for the matrix's dimension with power of 2

        if(a.column == 1 && a.row == 1) {
            return new Matrix(a.matrix[0] * b.matrix[0]);
        }
        Matrix temp = new Matrix();
        Matrix result = new Matrix(a.getRow(a),b.getColumn(b));
        //int halfSize = a.row * b.column / 2;
        Matrix A = a.BlockMatrix(1,a.getRow(a) / 2,1,a.getColumn(a) / 2,a);
        Matrix B = a.BlockMatrix(1,a.getRow(a) / 2,(a.getColumn(a) / 2) + 1,a.getColumn(a),a);
        Matrix C = a.BlockMatrix((a.getRow(a) / 2) + 1,a.getRow(a),1,a.getColumn(a) / 2,a);
        Matrix D = a.BlockMatrix((a.getRow(a) / 2) + 1,a.getRow(a),(a.getColumn(a) / 2) + 1,a.getColumn(a),a);
        //matrix A,B,C,D is block a into four matrix with same large
        Matrix E = b.BlockMatrix(1,b.getRow(b) / 2,1,b.getColumn(b) / 2,b);
        Matrix F = b.BlockMatrix(1,b.getRow(b) / 2,(b.getColumn(b) / 2) + 1,b.getColumn(b),b);
        Matrix G = b.BlockMatrix((b.getRow(b) / 2) + 1,b.getRow(b),1,b.getColumn(b) / 2,b);
        Matrix H = b.BlockMatrix((b.getRow(b) / 2) + 1,b.getRow(b),(b.getColumn(b) / 2) + 1,b.getColumn(b),b);
        //matrix E,F,G,H is block a into four matrix with same large

        /*
        * create 10 matrix which is defined by
        */
        Matrix S1 = temp.MatrixMin(F,H);//S1=B12−B22
        Matrix S2 = temp.MatrixAdd(A,B);//S2=A11+A12
        Matrix S3 = temp.MatrixAdd(C,D);//S3=A21+A22
        Matrix S4 = temp.MatrixMin(G,E);//S4=B21−B11
        Matrix S5 = temp.MatrixAdd(A,D);//S5=A11+A22
        Matrix S6 = temp.MatrixAdd(E,H);//S6=B11+B22
        Matrix S7 = temp.MatrixMin(B,D);//S7=A12−A22
        Matrix S8 = temp.MatrixAdd(G,H);//S8=B21+B22
        Matrix S9 = temp.MatrixMin(A,C);//S9=A11−A21
        Matrix S10 = temp.MatrixAdd(E,F);//S10=B11+B12
        /*
         * divide and conquer follow pseudo
         */
        Matrix P1 = Strassen(A,S1);//P1=Strassen(A11,B12 − B22)
        Matrix P2 = Strassen(S2,H);//P2=Strassen(A11 + A12,B22)
        Matrix P3 = Strassen(S3,E);//P3=Strassen(A21 + A22,B11)
        Matrix P4 = Strassen(D,S4); //P4=Strassen(A22,B21 − B11)
        Matrix P5 = Strassen(S5,S6);//P5=Strassen(A11 + A22,B11 + B22)
        Matrix P6 = Strassen(S7,S8);//P6=Strassen(A12 − A22,B21 + B22)
        Matrix P7 = Strassen(S9,S10);//P7=Strassen(A11 − A21,B11 + B12)

        Matrix C11 = temp.MatrixMin(temp.MatrixAdd(P5, P4),temp.MatrixMin(P2, P6));
        Matrix C12 = temp.MatrixAdd(P1, P2);
        Matrix C21 = temp.MatrixAdd(P3, P4);
        Matrix C22 = temp.MatrixMin(temp.MatrixAdd(P5, P1), temp.MatrixAdd(P3, P7));
        //follow pseudo

        for(int i = 0;i < result.getRow(result);i++) {
            for(int j = 0; j < result.getColumn(result);j++) {
                if(i < C11.getRow(C11)) {
                    if(j < C11.getColumn(C11)) {
                        result.setVal(i, j, C11.getVal(i, j));
                    }else {
                        result.setVal(i, j, C12.getVal(i, j-C12.getColumn(C12)));
                    }
                }else {
                    if(j < C11.getColumn(C11)) {
                        result.setVal(i, j, C21.getVal(i-C11.getRow(C11), j));
                    }else {
                        result.setVal(i, j, C22.getVal(i-C11.getRow(C11),j-C22.getColumn(C22)));
                    }
                }
            }
        }
        return result;
    }

    public Matrix Merge(Matrix a,Matrix b,Matrix c,Matrix d){
        int n = a.getColumn(a) + c.getColumn(c);
        Matrix result = new Matrix(n,n);
        for(int i = 0;i < result.getRow(result);i++) {
            for(int j = 0; j < result.getColumn(result);j++) {
                if(i < a.getRow(a)) {
                    if(j < a.getColumn(a)) {
                        result.setVal(i, j, a.getVal(i, j));
                    }else {
                        result.setVal(i, j, b.getVal(i, j - b.getColumn(b)));
                    }
                }else {
                    if(j < a.getColumn(a)) {
                        result.setVal(i, j, c.getVal(i - c.getRow(c), j));
                    }else {
                        result.setVal(i, j, d.getVal(i-a.getRow(a),j-d.getColumn(d)));
                    }
                }
            }
        }
        return result;
    }

    public Matrix StrassenBound(Matrix a,Matrix b,int n){
        Matrix temp = new Matrix();
        SquareMult squareMult = new SquareMult();
        Strassen1 strassen1 = new Strassen1();
        if (n < a.getColumn(a)){
            int m = 0;//find m satisfy that 2^m - c = n, and 2^m>n>2^(m-1)
            for (int i = 0;i < a.getRow(a);i++){
                if(Math.pow(2,i) == a.getRow(a)){
                    m = i;
                    break;
                }
                if (Math.pow(2,i) > a.getRow(a)){
                    m = i;
                    break;
                }
            }
            //System.out.println(m);
            if (a.getColumn(a) % Math.pow(2,m) != 0) {
                Matrix A1 = new Matrix((int) Math.pow(2, m), (int) Math.pow(2, m));
                for (int i = 0; i < A1.getRow(A1); i++) {
                    for (int j = 0; j < A1.getColumn(A1); j++) {
                        if (i < a.getRow(a)) {
                            if (j < a.getColumn(a)) {
                                A1.setVal(i, j, a.getVal(i, j));
                            } else {
                                A1.setVal(i, j, 0);
                            }
                        } else {
                            A1.setVal(i, j, 0);
                        }
                    }
                }//use 0 to fill bigger matrix A1
                Matrix B1 = new Matrix((int) Math.pow(2, m), (int) Math.pow(2, m));
                for (int i = 0; i < B1.getRow(B1); i++) {
                    for (int j = 0; j < B1.getColumn(B1); j++) {
                        if (i < b.getRow(b)) {
                            if (j < b.getColumn(b)) {
                                B1.setVal(i, j, b.getVal(i, j));
                            } else {
                                B1.setVal(i, j, 0);
                            }
                        } else {
                            B1.setVal(i, j, 0);
                        }
                    }
                }//use 0 to fill the bigger matrix B1
        /*for(int i = 0; i < Math.pow(A1.row,2); i++){
            System.out.print(A1.matrix[i] + " ");
        }*/
                //int halfSize = a.row * b.column / 2;
                Matrix A = A1.BlockMatrix(1, A1.getRow(A1) / 2, 1, A1.getColumn(A1) / 2, A1);
                Matrix B = A1.BlockMatrix(1, A1.getRow(A1) / 2, (A1.getColumn(A1) / 2) + 1, a.getColumn(A1), A1);
                Matrix C = A1.BlockMatrix((A1.getRow(A1) / 2) + 1, A1.getRow(A1), 1, A1.getColumn(A1) / 2, A1);
                Matrix D = A1.BlockMatrix((A1.getRow(A1) / 2) + 1, A1.getRow(A1), (A1.getColumn(A1) / 2) + 1, A1.getColumn(A1), A1);
                //matrix A,B,C,D is block a into four matrix with same large
                Matrix E = B1.BlockMatrix(1, B1.getRow(B1) / 2, 1, B1.getColumn(B1) / 2, B1);
                Matrix F = B1.BlockMatrix(1, B1.getRow(B1) / 2, (B1.getColumn(B1) / 2) + 1, b.getColumn(B1), B1);
                Matrix G = B1.BlockMatrix((B1.getRow(B1) / 2) + 1, B1.getRow(B1), 1, B1.getColumn(B1) / 2, B1);
                Matrix H = B1.BlockMatrix((B1.getRow(B1) / 2) + 1, B1.getRow(B1), (B1.getColumn(B1) / 2) + 1, B1.getColumn(B1), B1);
                //matrix E,F,G,H is block a into four matrix with same large

                /*
                 * create 10 matrix which is defined by
                 */
                Matrix S1 = temp.MatrixMin(F, H);//S1=B12−B22
                Matrix S2 = temp.MatrixAdd(A, B);//S2=A11+A12
                Matrix S3 = temp.MatrixAdd(C, D);//S3=A21+A22
                Matrix S4 = temp.MatrixMin(G, E);//S4=B21−B11
                Matrix S5 = temp.MatrixAdd(A, D);//S5=A11+A22
                Matrix S6 = temp.MatrixAdd(E, H);//S6=B11+B22
                Matrix S7 = temp.MatrixMin(B, D);//S7=A12−A22
                Matrix S8 = temp.MatrixAdd(G, H);//S8=B21+B22
                Matrix S9 = temp.MatrixMin(A, C);//S9=A11−A21
                Matrix S10 = temp.MatrixAdd(E, F);//S10=B11+B12
                /*
                 * divide and conquer follow pseudo
                 */
                Matrix P1 = StrassenBound(A, S1, n);//P1=Strassen(A11,B12 − B22)
                Matrix P2 = StrassenBound(S2, H, n);//P2=Strassen(A11 + A12,B22)
                Matrix P3 = StrassenBound(S3, E, n);//P3=Strassen(A21 + A22,B11)
                Matrix P4 = StrassenBound(D, S4, n); //P4=Strassen(A22,B21 − B11)
                Matrix P5 = StrassenBound(S5, S6, n);//P5=Strassen(A11 + A22,B11 + B22)
                Matrix P6 = StrassenBound(S7, S8, n);//P6=Strassen(A12 − A22,B21 + B22)
                Matrix P7 = StrassenBound(S9, S10, n);//P7=Strassen(A11 − A21,B11 + B12)

                Matrix C11 = temp.MatrixMin(temp.MatrixAdd(P5, P4), temp.MatrixMin(P2, P6));
                Matrix C12 = temp.MatrixAdd(P1, P2);
                Matrix C21 = temp.MatrixAdd(P3, P4);
                Matrix C22 = temp.MatrixMin(temp.MatrixAdd(P5, P1), temp.MatrixAdd(P3, P7));
                return strassen1.Merge(C11, C12, C21, C22);
            }
            else {
                Matrix A = a.BlockMatrix(1,a.getRow(a) / 2,1,a.getColumn(a) / 2,a);
                Matrix B = a.BlockMatrix(1,a.getRow(a) / 2,(a.getColumn(a) / 2) + 1,a.getColumn(a),a);
                Matrix C = a.BlockMatrix((a.getRow(a) / 2) + 1,a.getRow(a),1,a.getColumn(a) / 2,a);
                Matrix D = a.BlockMatrix((a.getRow(a) / 2) + 1,a.getRow(a),(a.getColumn(a) / 2) + 1,a.getColumn(a),a);
                //matrix A,B,C,D is block a into four matrix with same large
                Matrix E = b.BlockMatrix(1,b.getRow(b) / 2,1,b.getColumn(b) / 2,b);
                Matrix F = b.BlockMatrix(1,b.getRow(b) / 2,(b.getColumn(b) / 2) + 1,b.getColumn(b),b);
                Matrix G = b.BlockMatrix((b.getRow(b) / 2) + 1,b.getRow(b),1,b.getColumn(b) / 2,b);
                Matrix H = b.BlockMatrix((b.getRow(b) / 2) + 1,b.getRow(b),(b.getColumn(b) / 2) + 1,b.getColumn(b),b);
                //matrix E,F,G,H is block a into four matrix with same large

                /*
                 * create 10 matrix which is defined by
                 */
                Matrix S1 = temp.MatrixMin(F,H);//S1=B12−B22
                Matrix S2 = temp.MatrixAdd(A,B);//S2=A11+A12
                Matrix S3 = temp.MatrixAdd(C,D);//S3=A21+A22
                Matrix S4 = temp.MatrixMin(G,E);//S4=B21−B11
                Matrix S5 = temp.MatrixAdd(A,D);//S5=A11+A22
                Matrix S6 = temp.MatrixAdd(E,H);//S6=B11+B22
                Matrix S7 = temp.MatrixMin(B,D);//S7=A12−A22
                Matrix S8 = temp.MatrixAdd(G,H);//S8=B21+B22
                Matrix S9 = temp.MatrixMin(A,C);//S9=A11−A21
                Matrix S10 = temp.MatrixAdd(E,F);//S10=B11+B12
                /*
                 * divide and conquer follow pseudo
                 */
                Matrix P1 = StrassenBound(A,S1,n);//P1=Strassen(A11,B12 − B22)
                Matrix P2 = StrassenBound(S2,H,n);//P2=Strassen(A11 + A12,B22)
                Matrix P3 = StrassenBound(S3,E,n);//P3=Strassen(A21 + A22,B11)
                Matrix P4 = StrassenBound(D,S4,n); //P4=Strassen(A22,B21 − B11)
                Matrix P5 = StrassenBound(S5,S6,n);//P5=Strassen(A11 + A22,B11 + B22)
                Matrix P6 = StrassenBound(S7,S8,n);//P6=Strassen(A12 − A22,B21 + B22)
                Matrix P7 = StrassenBound(S9,S10,n);//P7=Strassen(A11 − A21,B11 + B12)

                Matrix C11 = temp.MatrixMin(temp.MatrixAdd(P5, P4),temp.MatrixMin(P2, P6));
                Matrix C12 = temp.MatrixAdd(P1, P2);
                Matrix C21 = temp.MatrixAdd(P3, P4);
                Matrix C22 = temp.MatrixMin(temp.MatrixAdd(P5, P1), temp.MatrixAdd(P3, P7));
                return strassen1.Merge(C11, C12, C21, C22);
            }
        }
        else{
            return squareMult.standardMult(a,b);
        }
    }

    public Matrix Strassen2(Matrix a,Matrix b){//this method is to calculate matrix multiply with any value of n
        if(a.getColumn(a) == 1 && a.getRow(a) == 1) {
            return new Matrix(a.matrix[0] * b.matrix[0]);
        }
        int m = 0;//find m satisfy that 2^m - c = n, and 2^m>n>2^(m-1)
        for (int i = 0;i < a.getRow(a);i++){
            if (Math.pow(2,i) > a.getRow(a)){
                m = i;
                break;
            }
        }
        Matrix A1 = new Matrix((int) Math.pow(2,m),(int)Math.pow(2,m));
        for(int i = 0;i < A1.getRow(A1);i++) {
            for(int j = 0; j < A1.getColumn(A1);j++) {
                if(i < a.getRow(a)) {
                    if(j < a.getColumn(a)) {
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
        for(int i = 0;i < B1.getRow(B1);i++) {
            for(int j = 0;j < B1.getColumn(B1);j++) {
                if(i < b.getRow(b)) {
                    if(j < b.getColumn(b)) {
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
        Matrix result = new Matrix(a.getRow(a),b.getColumn(b));
        /*for(int i = 0; i < Math.pow(A1.row,2); i++){
            System.out.print(A1.matrix[i] + " ");
        }*/
        Matrix temp = Strassen(A1,B1);//use Strassen method to calculate bigger matrix A1 and B1
        for(int i = 0;i < temp.getRow(temp);i++) {
            for(int j = 0; j < temp.getColumn(temp);j++) {
                if(i < result.getRow(result)) {
                    if(j < result.getColumn(result)) {
                        result.setVal(i, j, temp.getVal(i, j));
                    }
                }
            }
        }//turn the result back to nxn matrix
        return result;
    }


    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Matrix temp1 = new Matrix();
        Adaptive_Multiply temp3 = new Adaptive_Multiply();
        timeTest temp2 = new timeTest();
        int n = 1000;

        //temp1.createMatrix(n);
        //temp3.writeThreshold();

        Matrix matrixA = temp1.getMatrix("Text1.txt");
        Matrix matrixB = temp1.getMatrix("Text1.txt");
        double a = temp2.SimpleTime(matrixA);
        //double b = temp2.StrassenTime(matrixA);
        double c = temp2.StrassenTimeBound(matrixA);

        //if (Math.pow(n, 2) >= 0) System.arraycopy(matrixA.matrix, 0, matrixB.matrix, 0, (int)Math.pow(n, 2));
        Strassen1 temp = new Strassen1();
        //temp.recordAdaptedTime(n);
        //temp.recordStandardTime(n);//this is to record some dimension n with its runtime in standard method with blocked n by 50
        //temp.recordStrassenBound32Time(n);//this is to record some dimension n with its runtime in better Strassen method with blocked n by 50
        //temp.recordStrassenTime(n);//this is to record some dimension n with its runtime in strassen method with blocked n by 50
        //temp.recordStrassenBoundTime(n);//this is to record some dimension n with its runtime in better Strassen method with blocked n by 500
        //temp.recordStandardTimeWith500(n);//this is to record some dimension n with its runtime in standard method with blocked n by 500
        //System.out.println(a);
        //System.out.println(b);
        //System.out.println(c);
        //Matrix result = temp.StrassenBound(matrixB,matrixA,32);
        //for(int i = 0; i < Math.pow(n,2); i++){
        //    System.out.print(result.matrix[i] + " ");
        //}
        System.out.println("\n" + " 标准矩阵乘法时间："+ a + "s"+ "\n" + "Strassen矩阵乘法时间：" + c + "s");
        //for(int i = 0; i < Math.pow(n,2); i++){
         //   System.out.print(matrixB.matrix[i] + " ");
        //}
    }
    public Strassen1() {
    }
    public void recordStrassenTime(int n) {
        /*
        this method is for record the time that for each n in ms
        which the first column record
         */
        Matrix temp1 = new Matrix();
        timeTest temp2 = new timeTest();
        double[] a = new double[n / 50 + 1];

        double[] b = new double[n / 50 + 1];
        for (int i = 1; i < n / 50 + 1; i++) {
            temp1.createMatrix((i-1) * 50 + 1);
            Matrix matrixA = temp1.getMatrix("Text1.txt");
            Matrix matrixB = temp1.getMatrix("Text1.txt");
            a[i] = temp2.SimpleTime(matrixA);
            b[i] = temp2.StrassenTime(matrixA);
        }
        FileWriter fileWriter;

        try {
            fileWriter = new FileWriter("间隔50 Strassen.txt");//创建文本文件
            fileWriter.write(n / 50 + " " + "0" + "\n");//0 denotes Strassen ，1 denotes standard, 2 denotes adapted
            fileWriter.write("1");
            for (int i = 51; i <= n; i += 50) {
                fileWriter.write(" " + i);
            }
            fileWriter.write("\n" + b[1]);
            for (int i = 2; i < n / 50 + 1; i++) {
                fileWriter.write(" " + b[i]);
            }
            fileWriter.flush();
            fileWriter.close();
        } catch (IOException ex) {
            // TODO Auto-generated catch block
            ex.printStackTrace();
        }
    }
    public void recordStandardTime(int n) {
        /*
        this method is for record the time that for each n in ms
        which the first column record
         */
        Matrix temp1 = new Matrix();
        timeTest temp2 = new timeTest();
        double[] a = new double[n / 100 + 1];
        double[] b = new double[n / 100 + 1];
        for (int i = 1; i < n / 100 + 1; i++) {
            temp1.createMatrix(i * 100);
            Matrix matrixA = temp1.getMatrix("Text1.txt");
            Matrix matrixB = temp1.getMatrix("Text1.txt");
            a[i] = temp2.SimpleTime(matrixA);
            b[i] = temp2.StrassenTime(matrixA);
        }
        FileWriter fileWriter;

        try {
            fileWriter = new FileWriter("TextStandard(50).txt");//创建文本文件
            fileWriter.write(n / 100 + " " + "1" + "\n");//0 denotes Strassen ，1 denotes standard, 2 denotes adapted
            fileWriter.write("1");
            for (int i = 100; i <= n; i += 100) {
                fileWriter.write(" " + i);
            }
            fileWriter.write("\n" + a[1]);
            for (int i = 2; i < n / 100 + 1; i++) {
                fileWriter.write(" " + a[i]);
            }
            fileWriter.flush();
            fileWriter.close();
        } catch (IOException ex) {
            // TODO Auto-generated catch block
            ex.printStackTrace();
        }
    }
    public void recordStrassenBound32Time(int n){
        /*
        this method is for record the time that for each n in ms
        which the first column record
         */
        Matrix temp1 = new Matrix();
        timeTest temp2 = new timeTest();
        double []a = new double[n/100 + 1];
        double [] b = new double[n/100 + 1];
        for (int i = 1;i < n/100 + 1;i++) {
            temp1.createMatrix(i *100 + 1);
            Matrix matrixA = temp1.getMatrix("Text1.txt");
            a[i] = temp2.SimpleTime(matrixA);
            b[i] = temp2.StrassenTimeBound(matrixA);
        }
        FileWriter fileWriter;

        try {
            fileWriter = new FileWriter("下界128 间隔100.txt");//创建文本文件
            fileWriter.write(n/100+" "+"2"+"\n");//0 denotes Strassen ，1 denotes standard, 2 denotes adapted
            //fileWriter.write("1");
            for (int i = 100;i <= n;i += 100) {
                fileWriter.write(" " + i);
            }
            fileWriter.write("\n" + b[1]);
            for (int i = 2;i < n/100 + 1; i++) {
                fileWriter.write(" " + b[i]);
            }
            fileWriter.flush();
            fileWriter.close();
        } catch (IOException ex) {
            // TODO Auto-generated catch block
            ex.printStackTrace();
        }
    }
    public void recordStrassenBoundTime(int n){
        /*
        this method is for record the time that for each n in ms
        which the first column record
         */
        Matrix temp1 = new Matrix();
        timeTest temp2 = new timeTest();
        double []a = new double[n/500 + 1];
        double [] b = new double[n/500 + 1];
        for (int i = 1;i < n/500 + 1;i++) {
            temp1.createMatrix((i-1) * 500 + 1);
            Matrix matrixA = temp1.getMatrix("Text1.txt");
            Matrix matrixB = temp1.getMatrix("Text1.txt");
            a[i] = temp2.SimpleTime(matrixA);
            b[i] = temp2.StrassenTimeBound(matrixA);
        }
        FileWriter fileWriter;

        try {
            fileWriter = new FileWriter("TextBounded128 with 间隔500.txt");//创建文本文件
            fileWriter.write(n/500+" "+"2"+"\n");//0 denotes Strassen ，1 denotes standard, 2 denotes adapted
            fileWriter.write("1");
            for (int i = 501;i <= n;i += 500) {
                fileWriter.write(" " + i);
            }
            fileWriter.write("\n" + b[1]);
            for (int i = 2;i < n/500 + 1; i++) {
                fileWriter.write(" " + b[i]);
            }
            fileWriter.flush();
            fileWriter.close();
        } catch (IOException ex) {
            // TODO Auto-generated catch block
            ex.printStackTrace();
        }
    }
    public void recordStandardTimeWith500(int n) {
        /*
        this method is for record the time that for each n in ms
        which the first column record
         */
        Matrix temp1 = new Matrix();
        timeTest temp2 = new timeTest();
        double[] a = new double[n / 500 + 1];

        double[] b = new double[n / 500 + 1];
        for (int i = 1; i < n / 500 + 1; i++) {
            temp1.createMatrix((i-1) * 500 + 1);
            Matrix matrixA = temp1.getMatrix("Text1.txt");
            Matrix matrixB = temp1.getMatrix("Text1.txt");
            a[i] = temp2.SimpleTime(matrixA);
            b[i] = temp2.StrassenTime(matrixA);
        }
        FileWriter fileWriter;

        try {
            fileWriter = new FileWriter("TextStandard(间隔500).txt");//创建文本文件
            fileWriter.write(n / 500 + " " + "1" + "\n");//0 denotes Strassen ，1 denotes standard, 2 denotes adapted
            fileWriter.write("1");
            for (int i = 501; i <= n; i += 500) {
                fileWriter.write(" " + i);
            }
            fileWriter.write("\n" + a[1]);
            for (int i = 2; i < n / 500 + 1; i++) {
                fileWriter.write(" " + a[i]);
            }
            fileWriter.flush();
            fileWriter.close();
        } catch (IOException ex) {
            // TODO Auto-generated catch block
            ex.printStackTrace();
        }
    }
    public void recordAdaptedTime(int n){
         /*
        this method is for record the time that for each n in ms
        which the first column record
         */
        Matrix temp1 = new Matrix();
        timeTest temp2 = new timeTest();
        double[] a = new double[n / 100 + 1];
        double[] b = new double[n / 100 + 1];
        for (int i = 1; i < n / 100 + 1; i++) {
            temp1.createMatrix(i * 100 + 1);
            Matrix matrixA = temp1.getMatrix("Text1.txt");
            Matrix matrixB = temp1.getMatrix("Text1.txt");
            a[i] = temp2.SimpleTime(matrixA);
            b[i] = temp2.Adapted(matrixA);
        }
        FileWriter fileWriter;

        try {
            fileWriter = new FileWriter("TextAdapt(间隔100).txt");//创建文本文件
            fileWriter.write(n / 100 + " " + "1" + "\n");//0 denotes Strassen ，1 denotes standard, 2 denotes adapted
            fileWriter.write("1");
            for (int i = 100; i <= n; i += 100) {
                fileWriter.write(" " + i);
            }
            fileWriter.write("\n" + a[1]);
            for (int i = 2; i < n / 100 + 1; i++) {
                fileWriter.write(" " + a[i]);
            }
            fileWriter.flush();
            fileWriter.close();
        } catch (IOException ex) {
            // TODO Auto-generated catch block
            ex.printStackTrace();
        }
    }
}

