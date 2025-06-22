package conversor;

public enum Moneda {
    EUR("Euro", 0.86),
    COP("Peso colombiano", 4076.50),
    PEN("Sol peruano", 3.60),
    USD("Dolares Estadounidenses", 1.00),
    MXN("Peso Mexicano", 19.17)
    ;

    private final String nombre;
    private final double tasaCambio;

    Moneda(String nombre, double tasaCambio) {
        this.nombre = nombre;
        this.tasaCambio = tasaCambio;
    }

    public String getNombre() {
        return nombre;
    }

    public double getTasaCambio() {
        return tasaCambio;
    }
}
