package lab.orders;

public class App {
    record Order(String id, int quantity, long unitPriceCents) {
        long totalCents() {
            return quantity * unitPriceCents;
        }
    }

    public static void main(String[] args) {
        System.out.println("total=" + new Order("o-1", 2, 500).totalCents());
    }
}
