import argparse
from database import Session, engine
from models import Base, Student, Teacher, Group, Subject

session = Session()

def create_teacher(name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    print(f"Teacher {name} created.")

def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"ID: {teacher.id}, Name: {teacher.name}")

def update_teacher(teacher_id, new_name):
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        teacher.name = new_name
        session.commit()
        print(f"Teacher {teacher_id} updated to {new_name}.")
    else:
        print(f"Teacher {teacher_id} not found.")

def delete_teacher(teacher_id):
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher {teacher_id} deleted.")
    else:
        print(f"Teacher {teacher_id} not found.")

def main():
    parser = argparse.ArgumentParser(description="CLI for managing database records.")
    parser.add_argument("-a", "--action", choices=["create", "list", "update", "delete"], required=True, help="CRUD operation")
    parser.add_argument("-m", "--model", choices=["Teacher"], required=True, help="Model to operate on")
    parser.add_argument("--id", type=int, help="Record ID (for update/delete)")
    parser.add_argument("--name", type=str, help="Name (for create/update)")

    args = parser.parse_args()

    if args.model == "Teacher":
        if args.action == "create" and args.name:
            create_teacher(args.name)
        elif args.action == "list":
            list_teachers()
        elif args.action == "update" and args.id and args.name:
            update_teacher(args.id, args.name)
        elif args.action == "delete" and args.id:
            delete_teacher(args.id)
        else:
            print("Invalid arguments for Teacher.")

if __name__ == "__main__":
    main()
