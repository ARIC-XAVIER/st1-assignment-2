from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"


class Appointment:
    def __init__(self, appointment_id, date_time, patient, practitioner):
        self.appointment_id = appointment_id
        self.date_time = date_time
        self.patient = patient
        self.practitioner = practitioner
        self.status = AppointmentStatus.SCHEDULED

    def create(self):
        pass

    def cancel(self):
        if self.status == AppointmentStatus.SCHEDULED:
            self.status = AppointmentStatus.CANCELLED
        else:
            print("Cannot cancel this appointment")

    def confirm(self):
        if self.status == AppointmentStatus.SCHEDULED:
            self.status = AppointmentStatus.COMPLETED
        else:
            print("Cannot confirm this appointment")

a1 = Appointment("A001", "2026-10-01 10:00", "some patient", "some practitioner")
print(a1.status)

a1.cancel()
print(a1.status)
a1.cancel()