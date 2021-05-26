public class timeTest {

    public double SimpleTime(Matrix matrix) {
        SquareMult temp = new SquareMult();//Using the standard multiplication method
        /*
        * To get the 2-dimension array which is respond by a 1-dimension array
        * To simplify the method, the array with the same value
        */
        /*
        * To get time used by the standard method
        */
        double startTime=System.currentTimeMillis();
        temp.standardMult(matrix, matrix);
        double endTime=System.currentTimeMillis();
        double n = (endTime - startTime)/1000;//change millisecond to second
        return n;
    }
    public double StrassenTime(Matrix matrix){
        Strassen1 temp1 = new Strassen1();//To use the strassen algorithm multiplication method
        /*
         * To get the time used by the strassen multiplication algorithm
         */
        double startTime = System.currentTimeMillis();
        temp1.Strassen2(matrix, matrix);
        double endTime = System.currentTimeMillis();
        double n = (endTime - startTime)/1000;
        return n;
    }
    public double StrassenTimeBound(Matrix matrix){
        Strassen1 temp1 = new Strassen1();//To use the bounded strassen algorithm multiplication method
        /*
         * To get the time used by the bounded strassen multiplication algorithm
         */
        double startTime = System.currentTimeMillis();
        temp1.StrassenBound(matrix, matrix,128);
        double endTime = System.currentTimeMillis();
        double n = (endTime - startTime)/1000;
        return n;
    }
    public double Adapted(Matrix matrix){
        Adaptive_Multiply temp1 = new Adaptive_Multiply();//To use the bounded strassen algorithm multiplication method
        /*
         * To get the time used by the bounded strassen multiplication algorithm
         */
        double startTime = System.currentTimeMillis();
        temp1.strassen_mult(matrix, matrix);
        double endTime = System.currentTimeMillis();
        double n = (endTime - startTime)/1000;
        return n;
    }
}