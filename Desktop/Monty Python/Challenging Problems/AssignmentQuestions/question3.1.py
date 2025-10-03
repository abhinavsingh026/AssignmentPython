class Patient:
    def __init__(self,name,age,gender,patient_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.patient_id = patient_id

        self.needs_blood = False
        self.blood_group = None
        self.blood_units = 0.0
        self.blood_cost = 0.0
        self.treatment_cost = 0.0
        self.treatment_type = None
        self.registration_fee = 500.0
        self.discount_amount = 0.0
        self.total_before_discount = 0.0
        self.final_amount = 0.0

        self.blood_rates = {
            "A+": 1200.0,
            "A-": 1400.0,
            "B+": 1600.0,
            "B-": 1800.0,
            "AB+": 2000.0,
            "AB-": 2400.0,
            "O+": 2800.0,
            "O-": 3400.0
        }

        self.treatment_rates = {
            "consultation": 500.0,
            "Medication": 1500.0,
            "Minor Surgery": 25000.0,
            "Major Surgery": 50000.0,
            "Physiotherapy (per session)": 600.0,
            "Observation (per day)": 2000.0
        }

    def show_patient(self):
        print("\n--- Patient Details ---")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")
        print(f"Patient ID : {self.patient_id}")
        print("-----------------------")
    
    def blood_need(self, needs_blood, blood_group=None, units=0):
        if needs_blood:
            self.needs_blood = True
            self.blood_group = blood_group
            self.blood_units = units
            rate = self.blood_rates.get(blood_group, 0.0)
            self.blood_cost = rate * units
        else:
            self.needs_blood = False
            self.blood_cost = 0.0
    
    def treatment(self, treatment_type, quantity=1):
        rate = self.treatment_rates.get(treatment_type, 0.0)
        if treatment_type in ["Physiotherapy", "Observation"]:
            self.treatment_cost = rate * quantity
        else:
            self.treatment_cost = rate
        self.treatment_type = treatment_type
    
    def discount(self):
        self.total_before_discount = self.registration_fee + self.treatment_cost + self.blood_cost
        if self.age >= 60:
            self.discount_amount = 0.20 * self.total_before_discount
        else:
            self.discount_amount = 0.0

    def show_bill(self):
        self.final_amount = self.total_before_discount - self.discount_amount
        print("\n======= HOSPITAL BILL =======")
        print(f"Patient ID        : {self.patient_id}")
        print(f"Name              : {self.name}")
        print(f"Age               : {self.age}")
        print("------------------------------")
        print(f"Registration fee  : {self.registration_fee:.2f}")
        print(f"Treatment ({self.treatment_type}) : {self.treatment_cost:.2f}")
        if self.needs_blood:
            print(f"Blood ({self.blood_group}, {self.blood_units} units) : {self.blood_cost:.2f}")
        else:
            print("Blood             : 0.00")
        print("------------------------------")
        print(f"Total before disc : {self.total_before_discount:.2f}")
        print(f"Discount applied  : -{self.discount_amount:.2f}")
        print("------------------------------")
        print(f"Amount payable    : {self.final_amount:.2f}")
        print("==============================\n")

if __name__ == "__main__":
    p1 = Patient("Rahul Sharma", 65, "Male", "P1234")
    p1.show_patient()
    p1.blood_need(True, "B+", 2)
    p1.treatment("Physiotherapy", quantity=5)
    p1.discount()
    p1.show_bill()