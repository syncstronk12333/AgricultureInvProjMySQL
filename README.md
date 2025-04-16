# 🌾 Agriculture Inventory System

A console-based inventory management system built using **Python** and **MySQL** for efficiently managing agricultural crop data, profits/losses, and tool inventory.

## 📌 Project Overview

This system provides features for:
- Authenticating users securely via a login portal.
- Managing crop-related information like stock levels, profit/loss tracking.
- Maintaining a simple tool inventory using a CSV file.
- Filtering and viewing data based on user-defined ranges.
- Safely storing user passwords in a **binary file (`password.dat`)** using Python's `pickle` module.

## 🔧 Features

### 🔐 User Authentication
- Password stored in binary format (`password.dat`).
- Secure login with a security question-based password reset.

### 🌱 Crop Data Management
- Add, update, and delete crop records.
- View crops filtered by stock, profit, or loss ranges.
- Automatically handles cases of profit/loss (if one is missing, it's marked as `-`).

### 📊 Profit & Loss Tracking
- View individual crop profit/loss.
- View all crops with profit ≥ AED 2000.

### 🧰 Tool Management
- Tools stored and managed via a CSV file (`toolsss.csv`).
- Add, view, or delete tool records including quantity and condition (EXCELLENT/USABLE/BROKEN).

### 📋 Terminal-Based UI
- User-friendly interface with menu-based navigation.
- Clean output formatting using `tabulate`.

## ⚙️ How to Run

1. Set up MySQL
- Create a database named agri.
- Create the stock table using the query below:
- CREATE TABLE stock (
    Name VARCHAR(50) PRIMARY KEY,
    Stock INT NOT NULL,
    Profit INT,
    Loss INT
);

2. Insert values in database
- use sample query to insert:
- INSERT INTO stock (Name, Stock, Profit, Loss) VALUES
('Wheat', 150, 3200, NULL),
('Rice', 200, 2800, NULL),
('Corn', 180, 2500, NULL),
('Barley', 100, NULL, 900),
('Millet', 90, 1200, NULL),
('Sorghum', 130, NULL, 1100),
('Tomato', 300, 4200, NULL),
('Potato', 250, 3900, NULL),
('Carrot', 220, 3500, NULL),
('Cabbage', 160, NULL, 1400),
('Onion', 280, 3100, NULL),
('Garlic', 70, NULL, 1700),
('Spinach', 90, 1500, NULL),
('Broccoli', 85, NULL, 1300),
('Chili', 95, 1800, NULL),
('Peas', 200, 2100, NULL),
('Lettuce', 140, NULL, 1000),
('Radish', 110, 1600, NULL),
('Cauliflower', 130, 1900, NULL),
('Beans', 175, NULL, 1200);

2. Install Required Modules
- pip install mysql-connector-python tabulate

3. Add Password (optional initial setup)
- To manually set the login password in password.dat:
- import pickle
- with open("password.dat", "wb") as f:
-     pickle.dump("YourPasswordHere", f)
- Or run the program and choose the Reset Password option.

4. Run the Program
- python agri.py
