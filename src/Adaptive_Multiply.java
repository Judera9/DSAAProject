import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Adaptive_Multiply {
    public Matrix standard_mult (Matrix a, Matrix b){
        /*
         * this method is copied from the class SquareMult
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
    public Matrix strassen_mult(Matrix a,Matrix b){
        /*
         * this method run the strassen method after setting bound to get out of it
         */
        Strassen1 strassen1 = new Strassen1();
        return strassen1.StrassenBound(a,b,128);
    }
    public int set_threshold(){
        /*
        * in this method, we use for statement to find a threshold such that choose a method to use
        * the threshold should be the first n that standard method spend more time than Strassen method
        * Then we create a txt file to store this threshold
         */
        int threshold = 0;
        for (int i = 850;i < 4000;i += 10) {
            Matrix temp1 = new Matrix();
            temp1.createMatrix(i);
            Matrix a = temp1.getMatrix("Text1.txt");
            timeTest temp = new timeTest();
            double time1 = temp.SimpleTime(a);
            double time2 = temp.StrassenTimeBound(a);
            if (time1 > time2){
                threshold = i;
                System.out.println(threshold);
                break;
            }
        }

        return threshold;
    }
    public void writeThreshold(){
        Adaptive_Multiply temp = new Adaptive_Multiply();
        int threshold = temp.set_threshold();
        FileWriter fileWriter;
        try {
            fileWriter = new FileWriter("Threshold.txt");//创建文本文件
            fileWriter.write(""+threshold);
            fileWriter.flush();
            fileWriter.close();
        } catch (IOException ex) {
            // TODO Auto-generated catch block
            ex.printStackTrace();
        }
    }
    public int getThreshold(String strfile){
        try {
            BufferedReader reader  = new BufferedReader(new FileReader(strfile));
            String temp = "";
            temp = reader.readLine();
            int n = Integer.parseInt(temp);
            return n;
        }catch(Exception e){
            e.printStackTrace();
            return 0;
        }
    }

    public Matrix adaptive_multiply(Matrix a, Matrix b){
        int n = a.getColumn(a);
        Adaptive_Multiply temp = new Adaptive_Multiply();
        int threshold = temp.getThreshold("Threshold.txt");
        if (threshold >= n){
            return standard_mult(a,b);
        }
        else {
            return strassen_mult(a,b);
        }
    }
    public Adaptive_Multiply(){
    }
}
