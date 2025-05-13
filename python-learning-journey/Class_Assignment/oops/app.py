# Hospital Management System
# Doctor Management Module  ++ add -- remove 
# Paitent Management Module ++ add -- remove


# Hospital Management System
class Hospital():
    # Constructor
    def __init__(self, name, location):
        # Class Attributes
        self.hospital_name = name
        self.hospital_location = location
        # Empty List to Store Doctors
        self.doctors = []
        # Empty List to Store Patients
        self.patients = []


    # Method to Add Doctor
    def add_doctor(self, new_doctor):
        return self.doctors.append(new_doctor) # new_doctor ko doctors list ma add karega
    # Method to remove Doctor
    def remove_doctor(self, remove_doctor):
        return self.doctors.remove(remove_doctor) # remove_doctor ko doctor list sa remove kara ga
    # Method All Doctors
    def get_doctors(self):
        return self.doctors # sara doctors ka naam a jaya ga
    

    # Method to Add Remove
    def add_patient(self, new_patient):
        return self.patients.append(new_patient) # new_patient ko patients list ma add karega
    # Method to remove Patient
    def remove_patient(self, remove_patient):
        return self.patients.remove(remove_patient) # remove_patient ko patient list sa remove kara ga
    # Method All Patients
    def get_patients(self):
        return self.patients # sara patients ka naam a jaya ga
    
# Creating Hospital Object
hospital = Hospital("The city Hospital", "Karachi")
print(hospital)
# Calling one by one parameters
print(hospital.hospital_name)       # The city Hospital
print(hospital.hospital_location)   # Karachi





# Doctor Management
class Doctor():
    # Constructor
    def __init__(self, name, specialization, availability):
        # Class Attributes
        self.doctor_name = name
        self.doctor_specialization = specialization
        self.doctor_availability = availability
        
# Creating Doctor Object
doctor = Doctor ("Dr.Laiba", "Dermatologist", False)
print(doctor)
# Calling one by one parameters
print(doctor.doctor_name)  # Dr.Laiba
print(doctor.doctor_specialization)  # Dermatologist
print(doctor.doctor_availability) # False


# Creating more Doctor Objects
# 🧠 Neurologist Doctor Object
doctor1 = Doctor("Dr.Ahmed", "Neurologist", True)
# ❤️ Cardiologist Doctor Object
doctor2 = Doctor("Dr.Imran", "Cardiologist", False)
# 🦴 Orthopedic Surgeon
doctor3 = Doctor("Dr Kamran", "Orthopedic", True)
# 🍔 Gastroenterologist
doctor4 = Doctor("Dr.Bisma", "Gastroentelogist", True)
# 🫁 Psychiatrist
doctor5 = Doctor("Dr.Fatima", "Psychiatrist", False)





# Patient Management
class Patient():
    # Constructor
    def __init__(self, name, age, disease):
        # Class Attributes
        self.patient_name = name
        self.patient_age = age
        self.patient_disease = disease

# Patient Object
patient = Patient("Misbah", 35, "Over Thinking")
print(patient)
# Calling one by one parameters
print(patient.patient_name)  # Misbah
print(patient.patient_age)   # 35
print(patient.patient_disease)  # over thinking

# Creating more Patient Objects
patient1 = Patient("Kiran", 23, "Migraine")                # Neurologist
patient2 = Patient("Irfan", 25, "Heart Attack")            # Cardiologist
patient3 = Patient("Ayesha", 45, "Blood Pressure")         # Cardiologist
patient4 = Patient("Hina", 18, "Fracture")                 # Orthopedic
patient5 = Patient("Shoaib", 38, "Arthritis")              # Orthopedic
patient6 = Patient("Misbah", 35, "Over Thinking")          # Psychiatrist
patient7 = Patient("Sana", 30, "Anxiety")                  # Psychiatrist
patient8 = Patient("Neha", 27, "Skin Allergy")             # Dermatologist
patient9 = Patient("Rida", 40, "Acidity & Digestion")      # Gastroenterologist
patient10 = Patient("Ali", 50, "IBS (Irritable Bowel)")    # Gastroenterologist




# Create Hospital Instance
hospital = Hospital("City Care Hospital", "Karachi")
print(hospital)
# Calling one by one parameters
print(hospital.hospital_name)       # City Care Hospital
print(hospital.hospital_location)   # Karachi

# Adding Doctors
hospital.add_doctor(doctor)
hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)
hospital.add_doctor(doctor3)
hospital.add_doctor(doctor4)
hospital.add_doctor(doctor5)

# Adding Patients
hospital.add_patient(patient1)
hospital.add_patient(patient2)
hospital.add_patient(patient3)
hospital.add_patient(patient4)
hospital.add_patient(patient5)
hospital.add_patient(patient6)
hospital.add_patient(patient7)
hospital.add_patient(patient8)
hospital.add_patient(patient9)
hospital.add_patient(patient10)

# ✅ Removing One Doctor and One Patient
hospital.remove_doctor(doctor2)     # Removing Dr.Imran
hospital.remove_patient(patient3)   # Removing Ayesha

# Confirm Output
print("Doctors in hospital:")
for d in hospital.get_doctors():
    print(f"{d.doctor_name} ({d.doctor_specialization})")

print("\nPatients in hospital:")
for p in hospital.get_patients():
    print(f"{p.patient_name}, Age: {p.patient_age}, Disease: {p.patient_disease}")