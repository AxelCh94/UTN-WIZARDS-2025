
package ar.com.system2023.mundopc;


public class Orden {
    private final int idOrden;
    private Computadora computadora[]; // Arreglo de objetos
    private static int computadorOrdenes;
    private static final int MAX_COMPUTADORAS = 10;
    private int contadorComputadora; 
    
    // Contrucotor vacio
    public Orden(){
        this.idOrden = ++Orden.computadorOrdenes;
        this.computadora = new conputadoras[Orden.MAX_COMPUTADORAS];
        
    }
    
    // Metodo para agregar una nueva computadora al arreglo
    public void agregarComputadora(Computadora computadora){
        if (this.contadorComputadora < Orden.MAX_COMPUTADORAS){
            this.computadora[this.contadorComputadora++] = computadora;
        }
    }
}
