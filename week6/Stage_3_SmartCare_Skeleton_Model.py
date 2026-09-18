from enum import Enum
from datetime import datetime


class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"


class Patient:
    def __init__(self, patient_id: str, name: str):
        self.patient_id = patient_id
        self.name = name

    def validate(self) -> bool:
        return bool(self.patient_id) and bool(self.name)


class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty


class Appointment:
    def __init__(self, appointment_id: str, patient: Patient,
                 practitioner: Practitioner, date_time: datetime):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = AppointmentStatus.SCHEDULED

    def cancel(self) -> None:
        self.status = AppointmentStatus.CANCELLED