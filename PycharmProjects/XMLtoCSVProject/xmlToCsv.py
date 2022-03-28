import csv
import xml.etree.ElementTree as ET
import os


def xmlToCsv(file_path, csv_name) -> None:
    tree = ET.parse(file_path)
    root = tree.getroot()

    with open(csv_name, "w") as csv_file:
        writer = csv.writer(csv_file)
        headers = (child.tag for child in root[1])
        writer.writerow(headers)
        num_record = len(root)

        for record in range(num_record):
            rec = (child.text for child in root[record])
            writer.writerow(rec)
            for re in record:
                r = (child.text for child in root[re])
                writer.writerow(r)


if __name__ == '__main__':
    import sys
    import pathlib

    try:
        file_path = sys.argv[1]
        csv_name = sys.argv[2]

    except IndexError:
        sys.exit("Two Args required. One xml path and one save file name")

    with pathlib.Path(file_path) as xml_file:
        if xml_file.is_file():
            for filename in os.listdir(file_path):
                xmlToCsv(file_path, csv_name)

        else:
            sys.exit(f"did not find {file_path}")

'''

def make_csv(folderpath, xmlfilename):
    tree = ET.parse(os.path.join(folderpath, xmlfilename))
    root = tree.getroot()
    filename, _ = xmlfilename.rsplit('.', 1)
    Shot_30AA = open(filename + '.csv', 'w', newline='')
    csvwriter = csv.writer(Shot_30AA)
    head = []

    ShotCode = root.attrib['ShotCode']
    csvwriter.writerow(['ShotCode', ShotCode])
    head.append(ShotCode)

    for member in root.getchildren():
        submembers = member.getchildren()
        keys = submembers[0].attrib.keys()
        csvwriter.writerow("\n")
        csvwriter.writerow(keys)
        for submember in submembers:
            row_data = [submember.attrib[k] for k in keys]
            csvwriter.writerow(row_data)
    Shot_30AA.close()


path = 'C:/Users/pc/PycharmProjects/pythonProject2/XML Files using October 01, 2021/'
for filename in os.listdir(path):
    if filename.endswith('.xml'):
        make_csv(path, filename)
'''

