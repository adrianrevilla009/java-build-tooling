package lab.orders;

public class App {
    public static void main(String[] args) {
        System.out.println("total=" + new Order("o-1", 2, 500).totalCents());
    }
}
