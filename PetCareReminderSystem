# Pet Care Reminder System

# This program helps users set reminders for various tasks related to their pets.
# Users can set reminders for tasks like feeding, grooming, and medication.
# The system will notify the user when it's time to complete a task.

# List to store reminders
reminders = []

# List to store completed tasks
completed_tasks = []

# Function to set a reminder for a specific task and time
def setReminder(petName, task, time):
    """
    This function sets a reminder for a given pet, task, and time.
    The reminder is stored in the 'reminders' list.
    """
    reminder = {"petName": petName, "task": task, "time": time}
    reminders.append(reminder)
    print(f"Reminder set for {petName} to {task} at {time}.")

# Function to send reminders to the user
def sendReminder():
    """
    This function checks if there are any reminders set for the current time.
    If there are, it displays the reminder to the user.
    """
    current_time = "8:00 AM"  # For demonstration purposes, we'll use a fixed time
    for reminder in reminders:
        if reminder["time"] == current_time:
            print(f"It's time to {reminder['task']} {reminder['petName']}!")

# Function to mark a task as completed
def markTaskCompleted(petName, task):
    """
    This function marks a specified task for a given pet as completed.
    The completed task is stored in the 'completed_tasks' list.
    """
    completed_task = {"petName": petName, "task": task}
    completed_tasks.append(completed_task)
    print(f"{task} task for {petName} completed!")

# Function to check for missed reminders
def missedReminderCheck():
    """
    This function checks if there are any reminders that were not marked as completed.
    If there are, it notifies the user about the missed task.
    """
    for reminder in reminders:
        if reminder not in completed_tasks:
            print(f"You missed {reminder['task']} for {reminder['petName']} at {reminder['time']}!")

# Main Program Execution
if __name__ == "__main__":
    # Set up a feeding reminder for Dez
    setReminder("Dez", "Feeding", "8:00 AM")
    
    # Simulate sending the reminder at the specified time
    sendReminder()
    
    # Mark the feeding task for Dez as completed
    markTaskCompleted("Dez", "Feeding")
    
    # Check for any missed reminders
    missedReminderCheck()
