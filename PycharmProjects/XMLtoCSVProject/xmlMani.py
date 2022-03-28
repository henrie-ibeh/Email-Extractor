import xml.etree.ElementTree as ET
import csv



tree = ET.parse(
    "C:/Users/pc/PycharmProjects/XMLtoCSVProject/NDR To Excel Project"
    "/02-10-2020/IHVN_b8wSBkFN6qj_5_021020_FCT90800003.xml")
root = tree.getroot()

# this part prints only tags of all elements

"""
for child in root:
    for element in child.iter('ProgramAreaCode'):
        print(element.tag, element.text)
"""
print(root.findtext(''))

# Putting all the elements of XML tree into a dictionary 'elements'
def xmltodict(xml_tree_root):
    elements = {}
    for root in xml_tree_root:
        elements[root.tag] = root.text

        for child in root:
            elements[child.tag] = child.text

            for element in child:
                elements[element.tag] = element.text

                for children in element:
                    elements[children.tag] = children.text

                    for grand in children:
                        elements[grand.tag] = grand.text

                        for great in grand:
                            elements[great.tag] = great.text

                            for greater in great:
                                elements[greater.tag] = greater.text
    return elements


dictionary = xmltodict(root.findtext('ARTStartDate'))

variables = ['State', 'LGA', 'DatimCode', 'FacilityName', 'PatientUniqueID', 'PatientHospitalNo', 'ANCNoIdentifier',
             'ANCNoConceptID', 'HTSNo', 'Sex', 'AgeAtStartOfARTYears', 'AgeAtStartOfARTMonths', 'CareEntryPoint',
             'DateTransferredIn',
             'TransferInStatus', 'ARTStartDate', 'LastPickupDate', 'LastVisitDate', 'DaysOfARVRefil',
             'CurrentRegimenLine',
             'CurrentRegimen', 'PregnancyStatus', 'PregnancyStatusDate', 'CurrentViralLoad(c/ml)',
             'ViralLoadEncounterDate', 'ViralLoadSampleCollectionDate',
             'ViralLoadReportedDate', 'ViralLoadIndication', 'PatientOutcome', 'PatientOutcomeDate', 'CurrentARTStatus',
             'DateReturnedToCare', 'DateOfTermination', 'CurrentAgeYears', 'CurrentAgeMonths', 'DateOfBirth',
             'BiometricCaptured', 'BiometricCaptureDate', 'ValidCapture', 'CurrentWeight(Kg)', 'CurrentWeightDate',
             'TBStatus',
             'TBStatusDate', 'EnrollmentDate']
"""
for x in variables:
    try:
        print(dictionary[x])
    except KeyError:
        continue

with open('output.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in dictionary.items():
        writer.writerow([key, value])
"""
# this part should print the child elements but it isn't
"""
for i in root.findall('IndividualReport'):
    Id = i.find('PatientIdentifier')
    print(Id.text)
"""

"""
DateOfBirth = i.find('FacilityName').text
print(DateOfBirth)
"""
"""
if __name__ == '__main__':
    try:
        for x in elements:
            xmltodict(root, 'State')
    except KeyError:
            print(f"{1} not found.", xmltodict()[2])


"""
