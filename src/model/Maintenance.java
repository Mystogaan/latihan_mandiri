package model;

import java.time.LocalDate;

public class Maintenance {
    private LocalDate date;
    private String description;
    private double cost;

    public Maintenance(LocalDate date, String description, double cost) {
        this.date = date;
        this.description = description;
        this.cost = cost;
    }

    public LocalDate getDate() {return date;}
    public void setDate(LocalDate date) {this.date = date;}
    public String getDescription() {return description;}
    public void setDescription(String description) {this.description = description;}
    public double getCost() {return cost;}
    public void setCost(double cost) {this.cost = cost;}

    public void displayInfo() {
        System.out.println("Date: " + date + ", Description: " + description + ", Cost: " + cost);
    }
    

}
