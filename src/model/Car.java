package model;

public class Car extends Vehicle {
    private int numDoors;

    public Car(String brand, String model, int year, int numDoors) {
        super(brand, model, year);
        this.numDoors = numDoors;
    }

    public int getNumDoors() {
        return numDoors;
    }

    public void setNumDoors(int numDoors) {
        if (numDoors > 0) {
            this.numDoors = numDoors;
        }
        else {
            System.out.println("Number of doors must be greater than 0");
        }
    }

    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Number of doors: " + numDoors);
    }
    
}
