-- Create Departments Table
CREATE TABLE Departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Create Doctors Table
CREATE TABLE Doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- Create Patients Table
CREATE TABLE Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    dob DATE
);

-- Create Doctor_Specializations Table (M-M)
CREATE TABLE Doctor_Specializations (
    doctor_id INT,
    specialization VARCHAR(100),
    PRIMARY KEY (doctor_id, specialization),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Create Appointments Table
CREATE TABLE Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    reason TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Insert Sample Data
INSERT INTO Departments (name) VALUES ('Cardiology'), ('Neurology'), ('Pediatrics');

INSERT INTO Doctors (name, email, phone, department_id)
VALUES 
('Dr. Alice Kim', 'alice.kim@clinic.com', '0712345678', 1),
('Dr. John Doe', 'john.doe@clinic.com', '0798765432', 2);

INSERT INTO Patients (name, email, phone, dob)
VALUES 
('Jane Smith', 'jane.smith@email.com', '0711122233', '1990-03-14'),
('Mark Otieno', 'mark.otieno@email.com', '0799988776', '1985-11-02');

INSERT INTO Doctor_Specializations (doctor_id, specialization)
VALUES 
(1, 'Heart Surgery'),
(1, 'General Medicine'),
(2, 'Brain Surgery');

INSERT INTO Appointments (patient_id, doctor_id, appointment_date, reason)
VALUES 
(1, 1, '2025-05-01 10:00:00', 'Chest pain consultation'),
(2, 2, '2025-05-02 14:00:00', 'Frequent headaches');
