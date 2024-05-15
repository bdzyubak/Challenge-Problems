from collections import namedtuple


def merge(*records):
    """
    :param records: (varargs list of namedtuple) The patient details.
    :returns: (namedtuple) named Patient, containing details from all records, in entry order.
    """
    record_fields = dict()
    for record in records:
        for field in record._fields:
            record_fields[field] = getattr(record, field)

    Patient = namedtuple('Patient', record_fields.keys())
    patient = Patient(**record_fields)
    return patient


PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth='06-04-1972')

Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color='Blue', hair_color='Black')

print(merge(personal_details, complexion))