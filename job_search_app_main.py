import tkinter as tk
from tkinter import ttk
import requests

# Create the main window
window = tk.Tk()
window.title("Job Search App")
window.geometry("800x500")
window.resizable(False, False)

# Job title input
job_label = ttk.Label(window, text="Job Title:")
job_label.pack(pady=5)

job_entry = ttk.Entry(window, width=40)
job_entry.pack()

# Location input
location_label = ttk.Label(window, text="Location:")
location_label.pack(pady=5)

location_entry = ttk.Entry(window, width=40)
location_entry.pack()

def search_jobs():
    job = job_entry.get()
    location = location_entry.get()

    results_box.delete(1.0, tk.END)

    if not job:
        results_box.insert(tk.END, "Please enter a job title.\n")
        return

    url = "https://remotive.com/api/remote-jobs"
    response = requests.get(url)

    if response.status_code != 200:
        results_box.insert(tk.END, "Error fetching jobs.\n")
        return

    data = response.json()
    jobs = data["jobs"]

    for job_post in jobs:
        title = job_post["title"]
        company = job_post["company_name"]
        job_location = job_post["candidate_required_location"]

        if job.lower() in title.lower() and location.lower() in job_location.lower():
            results_box.insert(
                tk.END,
                f"{title}\nCompany: {company}\nLocation: {job_location}\n\n"
            )

# Search button
search_button = ttk.Button(window, text="Search Jobs", command=search_jobs)
search_button.pack(pady=10)

# Results box
results_box = tk.Text(window, height=15, width=90)
results_box.pack(pady=10)

# Start app
window.mainloop()
