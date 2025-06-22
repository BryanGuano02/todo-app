package conversor;

import javax.swing.*;
import java.awt.*;

public class ConversorSwing extends JFrame {

    private final JTextField txtCantidad;
    private final JComboBox<Moneda> comboOrigen;
    private final JComboBox<Moneda> comboDestino;
    private final JLabel lblResultado;
    private final ConversorMoneda conversor;

    public ConversorSwing() {
        setTitle("Conversor de Monedas");
        setSize(400, 250);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new GridLayout(5, 1));

        txtCantidad = new JTextField(10);
        comboOrigen = new JComboBox<>(Moneda.values());
        comboDestino = new JComboBox<>(Moneda.values());
        lblResultado = new JLabel("Resultado: ");
        conversor = new ConversorMoneda();

        add(crearPanelCantidad());
        add(crearPanelSeleccion("De:", comboOrigen));
        add(crearPanelSeleccion("A:", comboDestino));
        add(crearBotonConvertir());
        add(crearPanelResultado());
    }

    private JPanel crearPanelCantidad() {
        JPanel panel = new JPanel();
        panel.add(new JLabel("Cantidad:"));
        panel.add(txtCantidad);
        return panel;
    }

    private JPanel crearPanelSeleccion(String label, JComboBox<Moneda> combo) {
        JPanel panel = new JPanel();
        panel.add(new JLabel(label));
        panel.add(combo);
        return panel;
    }

    private JButton crearBotonConvertir() {
        JButton boton = new JButton("Convertir");
        boton.addActionListener(e -> realizarConversion());
        return boton;
    }

    private JPanel crearPanelResultado() {
        JPanel panel = new JPanel();
        lblResultado.setHorizontalAlignment(SwingConstants.CENTER);
        panel.add(lblResultado);
        return panel;
    }

    private void realizarConversion() {
        try {
            double cantidad = Double.parseDouble(txtCantidad.getText());
            Moneda origen = (Moneda) comboOrigen.getSelectedItem();
            Moneda destino = (Moneda) comboDestino.getSelectedItem();

            if (origen == destino) {
                lblResultado.setText(String.format("Resultado: %.2f %s", cantidad, destino.name()));
                return;
            }

            double resultado = conversor.convertir(cantidad, origen, destino);
            lblResultado.setText(String.format("Resultado: %.2f %s", resultado, destino.name()));

        } catch (NumberFormatException ex) {
            mostrarError("Ingrese una cantidad válida.");
        } catch (IllegalArgumentException ex) {
            mostrarError(ex.getMessage());
        }
    }

    private void mostrarError(String mensaje) {
        JOptionPane.showMessageDialog(this, mensaje, "Error", JOptionPane.ERROR_MESSAGE);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ConversorSwing().setVisible(true));
    }
}


