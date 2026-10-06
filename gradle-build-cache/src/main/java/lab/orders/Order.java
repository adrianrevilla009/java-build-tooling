package lab.orders;

public record Order(String id, int quantity, long unitPriceCents) {
    public long totalCents() {
        return quantity * unitPriceCents;
    }
}
