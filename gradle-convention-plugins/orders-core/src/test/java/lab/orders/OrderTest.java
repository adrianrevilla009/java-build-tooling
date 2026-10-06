package lab.orders;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class OrderTest {
    @Test
    void totalMultipliesQuantityByPrice() {
        assertEquals(750, new Order("o-1", 3, 250).totalCents());
    }
}
