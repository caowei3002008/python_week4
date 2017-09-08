import random
class patient(object):
    def __init__(self, id, name, allergies, bed_number = None):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number

class hospital(patient):
    def __init__(self, name_of_hospital, bed_number_all):
        self.patients = []
        self.name_of_hospital = name_of_hospital
        self.bed_number_all = bed_number_all
        self.capacity = len(self.bed_number_all)
        print "The hospital name is:", self.name_of_hospital,", the total capacity of bed is ",self.capacity

    def patient_added_and_bed_number_assigned(self, id, allergies, name, bed_number = None):
        super(hospital, self).__init__(name, bed_number, id, allergies)
        key = ['ID','Name', 'Bed Number', 'Allergies']
        if len(self.bed_number_all) > 0:
            bed_number = self.bed_number_all[0]
            self.bed_number_all.pop(0)
        else:
            print "The hospital is full"
            return self
        patienter = [id, name, bed_number, allergies]
        self.patients.append(dict(zip(key,patienter)))
        return self

    def patient_removed(self, name):
        for index in range(0, len(self.patients)):
            if name is self.patients[index].get('Name'):
                bed_number = self.patients[index].get('Bed Number')
                self.patients.pop(index)
                self.bed_number_all.append(bed_number)
                return self

    def display_current_patient_list(self):
        for item in self.patients:
            print item
        print "The capacity of bed is ",len(self.bed_number_all)
        return self


def create_bed_number(a,b):
    length = random.randint(a, b)
    bed_list = []
    for index in range(0,length):
        bed_list.append(index)
    return bed_list

bed_capacity = create_bed_number(20,28)

hospital1 = hospital('A', bed_capacity)
hospital1.patient_added_and_bed_number_assigned('001','None','Trump A')
hospital1.patient_added_and_bed_number_assigned('002','None','Trump B')
hospital1.patient_added_and_bed_number_assigned('003','None','Trump C')
hospital1.patient_added_and_bed_number_assigned('004','None','Trump D')
hospital1.patient_added_and_bed_number_assigned('005','None','Trump E')
hospital1.patient_added_and_bed_number_assigned('001','None','Trump F')
hospital1.patient_added_and_bed_number_assigned('002','None','Trump G')
hospital1.patient_added_and_bed_number_assigned('003','None','Trump H')
hospital1.patient_added_and_bed_number_assigned('004','None','Trump I')
hospital1.patient_added_and_bed_number_assigned('005','None','Trump J')
hospital1.patient_added_and_bed_number_assigned('001','None','Trump K')
hospital1.patient_added_and_bed_number_assigned('002','None','Trump L')
hospital1.patient_added_and_bed_number_assigned('003','None','Trump M')
hospital1.patient_added_and_bed_number_assigned('004','None','Trump N')
hospital1.patient_added_and_bed_number_assigned('005','None','Trump O')
hospital1.patient_added_and_bed_number_assigned('001','None','Trump P')
hospital1.patient_added_and_bed_number_assigned('002','None','Trump Q')
hospital1.patient_added_and_bed_number_assigned('003','None','Trump R')
hospital1.patient_added_and_bed_number_assigned('004','None','Trump S')
hospital1.display_current_patient_list()
hospital1.patient_removed('Trump N')

hospital1.display_current_patient_list()

