
def read_json(path_to_file):
    with open(path_to_file, 'r') as json_file:
        file_content = json_file.read()

        for person in file_content["person"]:
            print(person[0]["first_name"])
        # print(file_content)

read_json("people.json")

#def details_of_a_person(first_name,last_name)