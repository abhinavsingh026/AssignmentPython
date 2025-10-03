class Patient:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.patient_id = ""
        self.needs_blood = False
        self.blood_group = None
        self.blood_units = 0.0
        self.blood_cost = 0.0
        self.treatment_type = None
        self.treatment_cost = 0.0
        self.registration_fee = 500.0
        self.discount_amount = 0.0
        self.total_before_discount = 0.0
        self.final_amount = 0.0

        self.blood_rates = {
            "A+": 3000.0,
            "A-": 3200.0,
            "B+": 3100.0,
            "B-": 3300.0,
            "AB+": 3500.0,
            "AB-": 3600.0,
            "O+": 2900.0,
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

    def patient_details(self):
        print('Enter Patient Details: ')
        self.name = input(" Name: ").strip()
        while True:
            try:
                self.age = int(input(" Age: ").strip())
                break
            except ValueError:
                print("Please Enter a Valid integer for age.")
        self.gender = input(" Gender: ").strip()
        self.patient_id = input(" Patient_ID: ").strip()

    def show_patient(self):
        print("\n--- Patient Details ---")
        print(f"Name:       {self.name}")
        print(f"Age:        {self.age}")
        print(f"Gender:     {self.gender}")
        print(f"Patient ID: {self.patient_id}")
        print("---------------------\n")
    
    def blood_need(self):
        ans = input("Does the Patient need Blood? (yes/no): ").strip().lower()
        if ans in ("yes","y"):
            self.needs_blood = True
            while True:
                bg = input("Enter Blood-Group of Patient(A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip().upper()
                if bg in self.blood_rates:
                    self.blood_group = bg
                    break
                else:
                    print("Invalid Blood-Group. Try Again.")
            while True:
                try:
                    units = float(input("Enter No. of Units Required: ").strip())
                    if units<0:
                        raise valueError
                    self.blood_units = units
                    break
                except ValueError:
                    print("Enter a valid non-negative no. for Units.")
            rate = self.blood_rates[self.blood_group]
            self.blood_cost = rate * self.blood_units
            print(f"Calculated Blood Cost: {self.blood_units} units x {rate:.2f} = {self.blood_cost:.2f}")
        else:
            self.needs_blood = False
            self.blood_cost = 0.0
            print("No Blood Required")
    
    def treatment(self):
        print("Select Treatment type from the List Below (Enter Number): ")
        options = list(self.treatment_rates.items())
        for i, (name,rate) in enumerate(options, start=1):
            print(f" {i}.{name} - rate: {rate:.2f}")
        while True:
            try:
                choice = int(input("Your Choice: ").strip())
                if 1 <= choice <= len(options):
                    chosen_name, chosen_rate = options[choice-1]
                    self.treatment_type = chosen_name
                    if "per session" in chosen_name.lower() or "per day" in chosen_name.lower():
                        while True:
                            try:
                                qty = int(input("Enter No. of Days/Sessions: ").strip())
                                if qty<0:
                                    raise ValueError
                                break
                            except ValueError:
                                print("Enter a valid non-negative Integer.")
                        self.treatment_cost = chosen_rate*qty
                    else:
                        self.treatment_cost = chosen_rate
                    print(f"Treatment Selected: {self.treatment_type} - cost: {self.treatment_cost:.2f}")
                    break
                else:
                    print("  Invalid Choice Number. Try Again.")
            except ValueError:
                print("Enter a Valid Integer Choice.")
    
    def discount(self):
        self.total_before_discount = self.registration_fee + self.treatment_cost + self.blood_cost
        if self.age>= 60:
            self.discount_amount = 0.20 * self.total_before_discount
            print(f"\nPatient Qualifies as Senior Citizen -- 20% discount applied on {self.total_before_discount:.2f}")
        else:
            self.discount_amount = 0.0
            print("\nNo Age Based Discount applicable")
    
    def show_bill(self):
        self.final_amount = self.total_before_discount-self.discount_amount
        print("\n ===== Hospital Bill =====")
        print(f"Patient ID:    {self.patient_id}")
        print(f"Name:          {self.name}")
        print(f"Age:           {self.age}")
        print(f"Gender:        {self.gender}")
        print("------------------------------")
        print(f"Registration Fee: {self.registration_fee:.2f}")
        print(f"Treatment: ({self.treatment_type}) : {self.blood_cost:.2f}")
        if self.needs_blood:
            print(f"Blood ({self.blood_group}, {self.blood_units} units) : {self.blood_cost:.2f}")
        else:
            print("Blood           : 0.00")
        print("-----------------------------")
        print(f"Total before Discount: {self.total_before_discount:.2f}")
        print(f"Discount Applied: {self.discount_amount:.2f}")
        print("------------------------------")
        print(f"Amount Payable: {self.final_amount:.2f}")
        print("=============================\n")

if __name__ == "__main__":
    p = Patient()
    p.patient_details()
    p.show_patient()
    p.blood_need()
    p.treatment()
    p.discount()
    p.show_bill()