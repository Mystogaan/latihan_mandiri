import model.Vehicle;
import model.Maintenance;
import model.Motorcycle;
import model.Car;

import java.time.LocalDate;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // Membuat objek Vehicle
        Car car = new Car("Toyota", "Camry", 2022, 4);
        Motorcycle motorcycle = new Motorcycle("Yamaha", "NMAX", 2021, true);

        // Menampilkan info kendaraan
        System.out.println("=== Vehicle Information ===");
        System.out.println("Car: " + car.getBrand() + " " + car.getModel() + " (" + car.getYear() + ")");
        System.out.println("Motorcycle: " + motorcycle.getBrand() + " " + motorcycle.getModel() + " (" + motorcycle.getYear() + ")");

        // Menambahkan riwayat perawatan
        Maintenance maintenance1 = new Maintenance(LocalDate.of(2023, 5, 10), "Oil Change", 30.0);
        Maintenance maintenance2 = new Maintenance(LocalDate.of(2023, 7, 15), "Brake Check", 50.0);

        // Simpan riwayat perawatan ke dalam ArrayList
        ArrayList<Maintenance> maintenanceList = new ArrayList<>();
        maintenanceList.add(maintenance1);
        maintenanceList.add(maintenance2);

        // Menampilkan riwayat perawatan
        System.out.println("\n=== Maintenance History ===");
        for (Maintenance m : maintenanceList) {
            m.displayInfo();
            System.out.println();
        }
    }
}
