from datetime import datetime, timedelta

subjects = {
    "Physics I": {"chapters": 15, "marks": 200, "priority": "high", "hours_per_day": 2},
    "Mathematics I": {"chapters": 15, "marks": 200, "priority": "high", "hours_per_day": 2},
    "Mathematics II": {"chapters": 15, "marks": 200, "priority": "high", "hours_per_day": 2},
    "Mathematics III": {"chapters": 15, "marks": 200, "priority": "high", "hours_per_day": 2},
    "Chemistry": {"chapters": 15, "marks": 200, "priority": "high", "hours_per_day": 1.5},
    "IT Support Services": {"chapters": 12, "marks": 200, "priority": "high", "hours_per_day": 1.5},
    "Physics II": {"chapters": 14, "marks": 200, "priority": "medium", "hours_per_day": 1.5},
    "Digital Electronics I": {"chapters": 10, "marks": 150, "priority": "medium", "hours_per_day": 1},
    "Python Development": {"chapters": 11, "marks": 150, "priority": "medium", "hours_per_day": 1},
    "Basic Electronics": {"chapters": 10, "marks": 150, "priority": "low", "hours_per_day": 1},
    "Computer Graphics Design II": {"chapters": 9, "marks": 50, "priority": "low", "hours_per_day": 0.5},
    "Social Science": {"chapters": 10, "marks": 100, "priority": "low", "hours_per_day": 1},
}

study_schedule = {
    "high": ["Physics I", "Mathematics I", "Mathematics II", "Mathematics III", "Chemistry", "IT Support Services"],
    "medium": ["Physics II", "Digital Electronics I", "Python Development"],
    "low": ["Basic Electronics", "Computer Graphics Design II", "Social Science"]
}

time_slots = {
    "8 PM - 10 PM": "High Priority",
    "10 PM - 11 PM": "Medium Priority",
    "11 PM - 12 AM": "Low Priority",
    "12 AM - 2 AM": "Revision/Practice"
}

def generate_study_plan(start_date):
    current_date = start_date
    study_plan = {}

    while True:
        all_subjects_completed = True
        for priority, sub_list in study_schedule.items():
            for subject in sub_list:
                details = subjects[subject]
                if "current_chapter" not in details:
                    details["current_chapter"] = 1
                if details["current_chapter"] <= details["chapters"]:
                    all_subjects_completed = False

        if all_subjects_completed:
            break

        subjects_today = []
        for priority, sub_list in study_schedule.items():
            for subject in sub_list:
                details = subjects[subject]
                if details["current_chapter"] <= details["chapters"]:
                    subjects_today.append({
                        "subject": subject,
                        "chapter": f"Chapter {details['current_chapter']}"
                    })
                    details["current_chapter"] += 1
                    if len(subjects_today) == 3:
                        break
            if len(subjects_today) == 3:
                break

        study_plan[current_date] = subjects_today
        current_date += timedelta(days=1)

    return study_plan

def assign_time_slots(subjects_today):
    assigned_slots = {}
    current_time = datetime.strptime("20:00", "%H:%M")

    for subject in subjects_today:
        details = subjects[subject["subject"]]
        study_time = details["hours_per_day"]
        end_time = current_time + timedelta(hours=study_time)
        assigned_slots[subject["subject"]] = {
            "start_time": current_time.strftime("%I:%M %p"),
            "end_time": end_time.strftime("%I:%M %p"),
            "chapter": subject["chapter"]
        }
        current_time = end_time

    return assigned_slots

def display_daily_schedule(date, study_plan):
    if date in study_plan:
        print(f"\n📅 Study Plan for {date.strftime('%d-%m')}:")
        subjects_today = study_plan[date][:3]
        assigned_slots = assign_time_slots(subjects_today)

        for i, subject in enumerate(subjects_today, 1):
            details = subjects[subject["subject"]]
            print(f"\n📚 Subject {i}: {subject['subject']}")
            print(f"   - Priority: {details['priority'].capitalize()}")
            print(f"   - Chapter: {subject['chapter']}")
            print(f"   - Marks: {details['marks']}")
            print(f"   - Study Time: {details['hours_per_day']} hours")
            print(f"   - Time Slot: {assigned_slots[subject['subject']]['start_time']} to {assigned_slots[subject['subject']]['end_time']}")

        print("\n⏰ Daily Time Slots:")
        for slot, priority in time_slots.items():
            print(f"   - {slot}: {priority}")
    else:
        print(f"\n🎉 No study planned for {date.strftime('%d-%m')}. Take a break or revise!")

if __name__ == "__main__":
    start_date = datetime(2025, 2, 6)
    study_plan = generate_study_plan(start_date)

    print("Welcome to your personalized study scheduler,")
    date_input = input("Enter the date in dd-mm format (e.g., 15-02): ")
    day, month = map(int, date_input.split('-'))
    input_date = datetime(2025, month, day)

    display_daily_schedule(input_date, study_plan)
