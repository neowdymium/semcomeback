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
    "8 PM - 12:30 AM": "Exam Time",
    "12:30 AM - 2 AM": "Revision/Practice"
}
def generate_feb_to_mar_plan(start_date):
    current_date = start_date
    study_plan = {}
    while current_date <= datetime(2025, 3, 30):
        subjects_today = []
        for priority, sub_list in study_schedule.items():
            for subject in sub_list:
                details = subjects[subject]
                if "current_chapter" not in details:
                    details["current_chapter"] = 1
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
def generate_apr_revision_1(start_date):
    current_date = start_date
    study_plan = {}
    while current_date <= datetime(2025, 4, 15):
        subjects_today = []
        for priority, sub_list in study_schedule.items():
            for subject in sub_list:
                details = subjects[subject]
                if "current_chapter" not in details:
                    details["current_chapter"] = 1
                if details["current_chapter"] <= details["chapters"]:
                    end_chapter = min(details["current_chapter"] + 4, details["chapters"])
                    subjects_today.append({
                        "subject": subject,
                        "chapter": f"Revision 1: Chapters {details['current_chapter']} to {end_chapter}"
                    })
                    details["current_chapter"] = end_chapter + 1
                    if len(subjects_today) == 2:
                        break
            if len(subjects_today) == 2:
                break
        study_plan[current_date] = subjects_today
        current_date += timedelta(days=1)
    return study_plan
def generate_apr_revision_2(start_date):
    current_date = start_date
    study_plan = {}
    while current_date <= datetime(2025, 4, 30):
        subjects_today = []
        for priority, sub_list in study_schedule.items():
            for subject in sub_list:
                details = subjects[subject]
                if "current_chapter" not in details:
                    details["current_chapter"] = 1
                if details["current_chapter"] <= details["chapters"]:
                    end_chapter = min(details["current_chapter"] + 4, details["chapters"])
                    subjects_today.append({
                        "subject": subject,
                        "chapter": f"Revision 2: Chapters {details['current_chapter']} to {end_chapter}"
                    })
                    details["current_chapter"] = end_chapter + 1
                    if len(subjects_today) == 2:
                        break
            if len(subjects_today) == 2:
                break
        study_plan[current_date] = subjects_today
        current_date += timedelta(days=1)
    return study_plan
def generate_may_exams(start_date):
    current_date = start_date
    study_plan = {}
    exam_schedule = [
        "Physics I", "Mathematics I", "Mathematics II", "Mathematics III",
        "Chemistry", "IT Support Services", "Physics II", "Digital Electronics I",
        "Python Development", "Basic Electronics", "Computer Graphics Design II",
        "Social Science"
    ]
    for subject in exam_schedule:
        study_plan[current_date] = [{
            "subject": subject,
            "chapter": "House Exam: Full Book",
            "hours": 4.5
        }]
        current_date += timedelta(days=1)
    return study_plan
def assign_time_slots(subjects_today):
    assigned_slots = {}
    current_time = datetime.strptime("20:00", "%H:%M")
    for subject in subjects_today:
        details = subjects.get(subject["subject"], {"hours_per_day": 2})
        study_time = subject.get("hours", details["hours_per_day"])
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
            details = subjects.get(subject["subject"], {"marks": "N/A", "priority": "N/A"})
            print(f"\n📚 Subject {i}: {subject['subject']}")
            print(f"   - Chapter: {subject['chapter']}")
            print(f"   - Marks: {details['marks']}")
            print(f"   - Study Time: {subject.get('hours', details.get('hours_per_day', 2))} hours")
            print(f"   - Time Slot: {assigned_slots[subject['subject']]['start_time']} to {assigned_slots[subject['subject']]['end_time']}")
        print("\n⏰ Daily Time Slots:")
        for slot, priority in time_slots.items():
            print(f"   - {slot}: {priority}")
    else:
        print(f"\n🎉 No study planned for {date.strftime('%d-%m')}. Take a break or revise sweetheart!")
if __name__ == "__main__":
    print("❤️ ", "Honey, welcome to your personalized study scheduler ❤️")
    date_input = input("Enter the date in dd-mm format (e.g., 15-02): ")
    try:
        day, month = map(int, date_input.split('-'))
        input_date = datetime(2025, month, day)
        if datetime(2025, 2, 7) <= input_date <= datetime(2025, 3, 30):
            study_plan = generate_feb_to_mar_plan(datetime(2025, 2, 7))
        elif datetime(2025, 4, 1) <= input_date <= datetime(2025, 4, 15):
            study_plan = generate_apr_revision_1(datetime(2025, 4, 1))
        elif datetime(2025, 4, 16) <= input_date <= datetime(2025, 4, 30):
            study_plan = generate_apr_revision_2(datetime(2025, 4, 16))
        elif datetime(2025, 5, 1) <= input_date <= datetime(2025, 5, 12):
            study_plan = generate_may_exams(datetime(2025, 5, 1))
        else:
            print("📅 ", "No study plan available for this date. Please enter a date between 07-02-2025 and 12-05-2025.")
            exit()
        display_daily_schedule(input_date, study_plan)
    except ValueError:
        print("Invalid date format. Please enter a valid date in dd-mm format.")
