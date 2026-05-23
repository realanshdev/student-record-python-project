import json

with open("data.json", "r") as f:
    students = json.load(f)

menu = {
    1: "Add Student",
    2: "View Students",
    3: "Search Student",
    4: "Update Student",
    5: "Delete Student",
    6: "Exit",
}

while True:
    for x in menu:
        print(x, "-", menu[x])

    x = int(input("Enter the number"))

    match x:
        case 1:
            roll = input("enter roll no")
            name = input("enter name")
            age = int(input("enter age"))
            branch = input("enter branch")

            student = {"roll no": roll, "Name": name, "age": age, "branch": branch}

            students.append(student)

            with open("data.json", "w") as f:
                json.dump(students, f)

            print("succesfully added")

        case 2:
            for x in students:
                print("Roll no", x["roll no"])
                print("Name", x["Name"])
                print("Age", x["age"])
                print("Branch", x["branch"])

        case 3:
            s = input("Enter roll no")
            found = False

            for x in students:
                if x["roll no"] == s:
                    print("Name:", x["Name"])
                    print("age:", x["age"])
                    print("Branch:", x["branch"])
                    found = True

            if not found:
                print("fle not found")

        case 4:
            x = input("Enter the roll no of student")

            print("What you want to change:\n")

            k = int(
                input("Enter: 1-Change Name \n" "2-Change age \n" "3-change branch \n")
            )

            found = False

            for t in students:
                if t["roll no"] == x:
                    found = True

                    match k:
                        case 1:
                            nme = input("Enter the name to change with")
                            t["Name"] = nme

                        case 2:
                            nme = int(input("Enter age to change with"))
                            t["age"] = nme

                        case 3:
                            nme = input("Enter branch to change with")
                            t["branch"] = nme

                        case _:
                            print("Invalid number")
            if not found:
                print("Roll no not found")
            else:
                with open("data.json", "w") as f:
                    json.dump(students, f)
                    print("Operation done sucessfully")

        case 5:
            ki = input("Enter the roll no of student to delete")
            found = False
            for a in students:
                if a["roll no"] == ki:
                    students.remove(a)
                    found = True
            if found:
                with open("data.json", "w") as f:
                    json.dump(students, f)
                    print("Operation done sucessfully")
            else:
                print("ROll no not found")

        case 6:
            break
