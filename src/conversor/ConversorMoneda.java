package conversor;

public class ConversorMoneda {

    public double convertir(double cantidad, Moneda origen, Moneda destino) {
        if (cantidad < 0) {
            throw new IllegalArgumentException("La cantidad no puede ser negativa.");
        }

        return cantidad * (destino.getTasaCambio() / origen.getTasaCambio());
    }
}
