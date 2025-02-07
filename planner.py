from datetime import datetime, timedelta

subjects = {
    "Physics I": {"chapters": 15, "marks": 200, "priority": "high", "study_days": 4, "hours_per_day": 2},
    "Mathematics I": {"chapters": 15, "marks": 200, "priority": "high", "study_days": 5, "hours_per_day": 2.5},
    "Mathematics II": {"chapters": 15, "marks": 200, "priority": "high", "study_days": 5, "hours_per_day": 2.5},
    "Mathematics III": {"chapters": 15, "marks": 200, "priority": "high", "study_days": 5, "hours_per_day": 2.5},
    "Chemistry": {"chapters": 15, "marks": 200, "priority": "high", "study_days": 3, "hours_per_day": 1.5},
    "IT Support Services": {"chapters": 12, "marks": 200, "priority": "high", "study_days": 3, "hours_per_day": 1.5},
    "Physics II": {"chapters": 14, "marks": 200, "priority": "medium", "study_days": 3, "hours_per_day": 1.5},
    "Digital Electronics I": {"chapters": 10, "marks": 150, "priority": "medium", "study_days": 3, "hours_per_day": 1},
    "Python Development": {"chapters": 11, "marks": 150, "priority": "medium", "study_days": 3, "hours_per_day": 1},
    "Basic Electronics": {"chapters": 10, "marks": 150, "priority": "low", "study_days": 2, "hours_per_day": 1},
    "Computer Graphics Design II": {"chapters": 9, "marks": 50, "priority": "low", "study_days": 2, "hours_per_day": 0.5},
    "Social Science": {"chapters": 10, "marks": 100, "priority": "low", "study_days": 2, "hours_per_day": 1},
}

study_schedule = {
    "high": [],
    "medium": [],
    "low": []
}

for subject, details in subjects.items():
    study_schedule[details["priority"]].append(subject)

time_slots = {
    "8 PM - 10 PM": "High Priority",
    "10 PM - 11 PM": "Medium Priority",
    "11 PM - 12 AM": "Low Priority",
    "12 AM - 2 AM": "Revision/Practice"
}

def generate_study_plan(start_date):
    current_date = start_date
    study_plan = {}

    for priority, sub_list in study_schedule.items():
        for subject in sub_list:
            details = subjects[subject]
            for _ in range(details["study_days"]):
                if current_date not in study_plan:
                    study_plan[current_date] = []
                study_plan[current_date].append(subject)
                current_date += timedelta(days=1)

    return study_plan

def assign_time_slots(subjects_today):
    assigned_slots = {}
    current_time = datetime.strptime("20:00", "%H:%M")

    for subject in subjects_today:
        details = subjects[subject]
        study_time = details["hours_per_day"]
        end_time = current_time + timedelta(hours=study_time)
        assigned_slots[subject] = {
            "start_time": current_time.strftime("%I:%M %p"),
            "end_time": end_time.strftime("%I:%M %p")
        }
        current_time = end_time

    return assigned_slots

def display_daily_schedule(date, study_plan):
    if date in study_plan:
        print(f"\n📅 Study Plan for {date.strftime('%d-%m')}:")
        subjects_today = study_plan[date][:3]
        assigned_slots = assign_time_slots(subjects_today)

        for i, subject in enumerate(subjects_today, 1):
            details = subjects[subject]
            print(f"\n📚 Subject {i}: {subject}")
            print(f"   - Priority: {details['priority'].capitalize()}")
            print(f"   - Chapters: {details['chapters']}")
            print(f"   - Marks: {details['marks']}")
            print(f"   - Study Time: {details['hours_per_day']} hours")
            print(f"   - Time Slot: {assigned_slots[subject]['start_time']} to {assigned_slots[subject]['end_time']}")

        print("\n⏰ Daily Time Slots:")
        for slot, priority in time_slots.items():
            print(f"   - {slot}: {priority}")
    else:
        print(f"\n🎉 No study planned for {date.strftime('%d-%m')}. Take a break or revise!")

if __name__ == "__main__":
    start_date = datetime(2025, 2, 6)
    study_plan = generate_study_plan(start_date)

    print("❤️ Welcome to your personalized study scheduler my dear! ❤️")
    date_input = input("Enter the date in dd-mm format (e.g., 15-02): ")
    day, month = map(int, date_input.split('-'))
    input_date = datetime(2025, month, day)

    display_daily_schedule(input_date, study_plan)