class Patient:
    def __init__(self):
        self.needs_blood = False
        self.blood_group = None
        self.blood_units = 0.0
        self.blood_cost = 0.0
        self.treatment_cost = 0.0
        self.treatment_type = None
        self.treatment_quantity = 0.0
        self.registration_fee = 500.0
        self.discount_amount = 0.0
        self.total_before_discount = 0.0
        self.final_amount = 0.0

        self.blood_rates = {
            "A+": 500.0,
            "A-": 800.0,
            "B+": 1100.0,
            "B-": 1300.0,
            "AB+": 2000.0,
            "AB-": 2400.0,
            "O+": 3000.0,
            "O-": 3500.0
        }

        self.treatment_rates = {
            "consultation": 700.0,
            "Medication": 1000.0,
            "Minor Surgery": 15000.0,
            "Major Surgery": 30000.0,
            "Physiotherapy": 800.0,
            "Observation": 1800.0
        }
    def Patientdetails(self,name,age,gender,patient_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.patient_id = patient_id

    def ShowPatient(self):
        print("\n----Patient Details----")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")
        print(f"Patient ID : {self.patient_id}")
    
    def Bloodneed(self,needs_blood,blood_group=None,units=0):
        if needs_blood:
            self.needs_blood = True
            self.blood_group = blood_group
            self.blood_units = units
            rate = self.blood_rates.get(blood_group, 0.0)
            self.blood_cost = rate * units
        else:
            self.needs_blood = False
            self.blood_cost = 0.0
    
    def Treatment(self,treatment_type,treatment_quantity=0):
        rate = self.treatment_rates.get(treatment_type, 0.0)
        if treatment_type in ["Physiotherapy", "Observation"]:
            self.treatment_quantity = treatment_quantity
            self.treatment_cost = rate * treatment_quantity
            self.treatment_type = treatment_type
        else:
            self.treatment_cost = rate
            self.treatment_type = treatment_type
    
    def Discount(self):
        self.total_before_discount = self.registration_fee + self.treatment_cost + self.blood_cost
        if self.age >= 60:
            self.discount_amount = 0.20 * self.total_before_discount
        else:
            self.discount_amount = 0.0

    def showBill(self):
        self.final_amount = self.total_before_discount - self.discount_amount
        print("\n-------HOSPITAL BILL-------")
        print(f"Registration fee  : {self.registration_fee:.2f}")
        if self.treatment_type in ["Physiotherapy", "Observation"]:
            print(f"Treatment:({self.treatment_type}) - Rate(Per day):{self.treatment_rates.get(self.treatment_type, 0.0)}")
            print(f"No. of Days - {self.treatment_quantity}")
            print(f"Total Treatment Cost: {self.treatment_cost:.2f}")
        else:    
            print(f"Treatment:({self.treatment_type}) : {self.treatment_cost:.2f}")
        if self.needs_blood:
            print(f"BloodType:({self.blood_group}) Units:({self.blood_units}) x Rate:{self.blood_rates.get(self.blood_group, 0.0)}")
            print(f"Total Blood Cost: {self.blood_cost:.2f}")
        else:
            print("Blood             : 0.00")
        print("------------------------------")
        print(f"Total before Discount : {self.total_before_discount:.2f}")
        print(f"Discount applied  : -{self.discount_amount:.2f}")
        print("------------------------------")
        print(f"Amount payable    : {self.final_amount:.2f}")
        print("==============================\n")

pobj = Patient()
pobj.Patientdetails("Donald Trump",82,"Male","TRP07")
pobj.ShowPatient()
pobj.Treatment("Physiotherapy",5)
pobj.Bloodneed(True,"O-",5)
pobj.Discount()
pobj.showBill()