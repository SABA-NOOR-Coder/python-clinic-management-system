from datetime import datetime

class Person:
    def __init__(self, name, phone):
        self.name = name
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    def set_phone(self,new_phone):
        self.__phone = new_phone


class Patient(Person):

    def __init__(self, patient_id, name, age, gender, phone, address):
        super().__init__(name,phone)
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.__address = address


    def get_address(self):
        return self.__address
    
    def set_address(self,new_address):
        self.__address = new_address

    def display_info(self):
        print(f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Phone: {self.get_phone()}, Address: {self.get_address()}") 
    
class Doctor(Person):
    def __init__(self, doctor_id, name, specialization, phone):
        super().__init__(name,phone)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def display_info(self):
            print(f"ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}, Phone: {self.get_phone()}")

class Appointment:
    def __init__(self, appointment_id, patient, doctor):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        now = datetime.now()
        self.date = now.strftime("%d-%m-%Y")
        self.time = now.strftime("%H:%M")

    def display_info(self):
        print(f"ID: {self.appointment_id}, Patient Name: {self.patient.name}, Doctor Name: {self.doctor.name}, Date: {self.date}, Time: {self.time}")

class MedicalRecord:
    def __init__(self, record_id ,patient ,diagnosis ,symptoms ,medicines ,notes):
        self.record_id = record_id
        self.patient = patient
        self.diagnosis = diagnosis
        self.symptoms = symptoms
        self.medicines = medicines
        self.notes = notes

    def display_info(self):
        print(f"ID: {self.record_id}, Patient Name: {self.patient.name}, Diagnosis: {self.diagnosis}, Symptoms: {self.symptoms}, Medicines: {self.medicines}, Notes: {self.notes}")

class Clinic:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.records = []

    def add_patient(self,patient):
        self.patients.append(patient)
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
    def book_appointment(self,appointment):
        self.appointments.append(appointment)
    def add_medical_record(self,medical_record):
        self.records.append(medical_record)

    def display_patients(self):
        for i in self.patients:
            i.display_info()

    def display_doctors(self):
        for i in self.doctors:
            i.display_info()

    def display_appointments(self):
        for i in self.appointments:
            i.display_info()

    def display_records(self):
        for i in self.records:
            i.display_info()

patient1 = Patient("p0001",
        "Ali",
        20,
        "male",
        "03249886608",
        "Johar Town")
patient2 = Patient("p0002",
        "Noor",
        22,
        "Female",
        "0326-0884409",
        "Iqbal Town")
# patient1.display_info()
patient1.set_phone("03000000000")
print(patient1.get_phone())
patient1.set_address("Johar Town Black R")
print(patient1.get_address())
# patient1.display_info()

heart_doctor = Doctor("001",
            "Saad",
            "PHD",
            "03026734823")
# heart_doctor.display_info()
heart_doctor.set_phone("03009000002")
print(heart_doctor.get_phone())
# heart_doctor.display_info()

appointment1 = Appointment("0001",
        patient1, 
        heart_doctor)
# print(appointment1.patient.name)
# appointment1.display_info()

record1 = MedicalRecord( "R001",
    patient1,
    "Flu",
    "Fever, cough, weakness",
    "Paracetamol",
    "Take medicine twice a day")
# print(record1.patient.name)
# print(record1.symptoms)
# record1.display_info()

clinic1 = Clinic("Ali")
clinic2 = Clinic("Noor")
clinic1.add_patient(patient1)
clinic1.add_patient(patient2)
clinic1.add_doctor(heart_doctor)
clinic1.book_appointment(appointment1)
clinic1.add_medical_record(record1)
# clinic1.display_patients()
# clinic1.display_appointments()
# clinic1.display_doctors()
# clinic1.display_records()

people = [patient1, patient2, heart_doctor, appointment1, record1]
for person in people:
    person.display_info()