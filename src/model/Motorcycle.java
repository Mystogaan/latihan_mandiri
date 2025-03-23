package model;

public class Motorcycle extends Vehicle {
    private boolean hasSideCar;

    public Motorcycle(String brand, String model, int year, boolean hasSideCar) {
        super(brand, model, year);
        this.hasSideCar = hasSideCar;
    }

    public boolean gethasSideCar() {
        return hasSideCar;
    }

    public void setType(boolean hasSideCar) {
        this.hasSideCar = hasSideCar;
    }

    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Has Side Car: " + hasSideCar);
    }
    
}