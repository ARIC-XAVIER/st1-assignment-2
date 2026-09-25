class Patient:
    def __init__(self, patient_id: str, name: str):
        self.patient_id = patient_id
        self.name = name

    def validate(self) -> bool:
        if self.name == "":
            return False
        else:
            return True
p1 = Patient("P001", "Aric")
print(p1.validate())