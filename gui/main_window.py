import tkinter as tk
from tkinter import ttk, messagebox
from models.process import Process
from simulator import run_simulation
from utils.gantt import show_algorithm_gantt


def create_main_window():
    root = tk.Tk()

    root.title("CPU Scheduling Simulator")
    root.geometry("900x800")
    root.resizable(False, False)


    # Store process data
    process_data = []


    # Main title
    title_label = ttk.Label(root, text="CPU Scheduling Simulator", font=("Arial", 20, "bold"))
    title_label.pack(pady=20)


    # Process input frame
    process_frame = ttk.LabelFrame(root, text="Process Input", padding=15)
    process_frame.pack(padx=30, pady=10,fill="x")


    # PID
    ttk.Label(process_frame, text="PID").grid(
        row=0,
        column=0,
        padx=10,
        pady=5
    )


    pid_entry = ttk.Entry(process_frame, width=15)
    pid_entry.grid(
        row=1,
        column=0,
        padx=10,
        pady=5
    )


    # Arrival Time
    ttk.Label(process_frame,text="Arrival Time").grid(
        row=0,
        column=1,
        padx=10,
        pady=5
    )


    arrival_entry = ttk.Entry(process_frame, width=15)
    arrival_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=5
    )


    # Burst Time
    ttk.Label(process_frame,text="Burst Time").grid(
        row=0,
        column=2,
        padx=10,
        pady=5
    )


    burst_entry = ttk.Entry(process_frame,width=15)
    burst_entry.grid(
        row=1,
        column=2,
        padx=10,
        pady=5
    )


    # Priority
    ttk.Label(process_frame, text="Priority").grid(
        row=0,
        column=3,
        padx=10,
        pady=5
    )


    priority_entry = ttk.Entry(process_frame, width=15)
    priority_entry.grid(
        row=1,
        column=3,
        padx=10,
        pady=5
    )


    # Process table
    process_table = ttk.Treeview(root,columns=("pid","arrival","burst","priority"),show="headings",height=8)

    process_table.heading("pid",text="PID")

    process_table.heading("arrival", text="Arrival Time")

    process_table.heading("burst",text="Burst Time")

    process_table.heading("priority",text="Priority")

    process_table.column("pid",width=150)

    process_table.column("arrival",width=150)

    process_table.column("burst",width=150)

    process_table.column("priority",width=150)

    process_table.pack(padx=30,pady=15)


    # Add Process
    def add_process():
        pid = pid_entry.get().strip()
        arrival_time = arrival_entry.get().strip()
        burst_time = burst_entry.get().strip()
        priority = priority_entry.get().strip()

        # Check PID
        if not pid:
            messagebox.showerror("Invalid Input","PID cannot be empty.")
            return


        # Check Arrival Time
        if not arrival_time:
            messagebox.showerror("Invalid Input","Arrival Time cannot be empty.")
            return


        # Check Burst Time
        if not burst_time:
            messagebox.showerror("Invalid Input","Burst Time cannot be empty.")
            return


        # Check numeric values
        try:
            arrival_time = int(arrival_time)
            burst_time = int(burst_time)

            if priority:
                priority = int(priority)
            else:
                priority = 0

        except ValueError:
            messagebox.showerror("Invalid Input","Arrival Time, Burst Time and Priority must be integers.")
            return


        # Check negative values
        if arrival_time < 0:
            messagebox.showerror("Invalid Input","Arrival Time cannot be negative.")
            return

        if burst_time <= 0:
            messagebox.showerror("Invalid Input","Burst Time must be greater than zero.")
            return

        if priority < 0:
            messagebox.showerror("Invalid Input","Priority cannot be negative.")
            return


        # Check duplicate PID
        for process in process_data:
            if process["pid"] == pid:
                messagebox.showerror("Invalid Input","PID already exists.")
                return


        # Add process to list
        process_data.append(
            {
                "pid": pid,
                "arrival_time": arrival_time,
                "burst_time": burst_time,
                "priority": priority
            }
        )


        # Add process to table
        process_table.insert(
            "",
            "end",
            values=(
                pid,
                arrival_time,
                burst_time,
                priority
            )
        )


        # Clear input fields

        pid_entry.delete(0, tk.END)
        arrival_entry.delete(0, tk.END)
        burst_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)


    # Remove Process
    def remove_process():
        selected_item = process_table.selection()

        if not selected_item:
            messagebox.showwarning("No Selection","Please select a process to remove.")
            return

        for item in selected_item:
            values = process_table.item(item, "values")

            pid = values[0]

            for process in process_data:
                if process["pid"] == pid:
                    process_data.remove(process)
                    break

            process_table.delete(item)


    # Add Process button
    add_button = ttk.Button(process_frame,text="Add Process",command=add_process)
    add_button.grid(
        row=2,
        column=0,
        columnspan=4,
        pady=15
    )


    remove_button = ttk.Button(process_frame, text="Remove Process", command=remove_process)
    remove_button.grid(
        row=3,
        column=0,
        columnspan=4,
        pady=5
    )


    # Algorithm Selection
    algorithm_frame = ttk.LabelFrame(root, text="Scheduling Algorithm", padding=10)
    algorithm_frame.pack(padx=30, pady=10,fill="x")

    ttk.Label(algorithm_frame, text="Algorithm:").pack(side="left",padx=10)


    algorithm_var = tk.StringVar(value="FCFS")

    algorithm_combo = ttk.Combobox(
        algorithm_frame,
        textvariable=algorithm_var,
        values=[
            "FCFS",
            "SJF",
            "Round Robin",
            "SRT",
            "MLFQ"
        ],

        state="readonly",
        width=20
    )


    algorithm_combo.pack(side="left",padx=10)    


    # Run Simulation
    def run_selected_algorithm():
        if not process_data:
            messagebox.showwarning("No Processes","Please add at least one process.")
            return


        processes = []


        for data in process_data:
            process = Process(
                data["pid"],
                data["arrival_time"],
                data["burst_time"],
                data["priority"]
            )

            processes.append(process)

        results = run_simulation(processes)

        selected_algorithm = algorithm_var.get()

        selected_result = results[selected_algorithm]

        average_waiting = selected_result["average_waiting"]
        average_turnaround = selected_result["average_turnaround"]

        selected_algorithm_label.config(text=f"Selected Algorithm: {selected_algorithm}")

        waiting_time_label.config(text=f"Average Waiting Time: {average_waiting:.2f}")

        turnaround_time_label.config(text=f"Average Turnaround Time: {average_turnaround:.2f}")

        show_algorithm_gantt(results,selected_algorithm)


    run_button = ttk.Button(root, text="Run Simulation",command=run_selected_algorithm)
    run_button.pack(pady=15)


    # Results Frame
    results_frame = ttk.LabelFrame(root,text="Results",padding=15)


    results_frame.pack(padx=30,pady=10,fill="x")


    selected_algorithm_label = ttk.Label(results_frame,text="Selected Algorithm: -")


    selected_algorithm_label.pack(anchor="w",pady=5)


    waiting_time_label = ttk.Label(results_frame,text="Average Waiting Time: -")


    waiting_time_label.pack(anchor="w",pady=5)


    turnaround_time_label = ttk.Label(results_frame,text="Average Turnaround Time: -")

    turnaround_time_label.pack(anchor="w",pady=5)
    

    return root    # MISSION 18



if __name__ == "__main__":
    root = create_main_window()
    root.mainloop()