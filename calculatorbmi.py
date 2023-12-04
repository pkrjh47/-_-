import tkinter as tk

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        # Convert height to meters if it's in centimeters
        if var_height_units.get() == "cm":
            height /= 100

        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place widgets
label_weight = tk.Label(root, text="Weight (kg):")
label_weight.grid(row=0, column=0, padx=10, pady=10)

entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

label_height = tk.Label(root, text="Height:")
label_height.grid(row=1, column=0, padx=10, pady=10)

entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)

var_height_units = tk.StringVar()
var_height_units.set("m")  # Default unit is meters

unit_menu = tk.OptionMenu(root, var_height_units, "m", "cm")
unit_menu.grid(row=1, column=2, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=3, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# Start the main loop
root.mainloop()
