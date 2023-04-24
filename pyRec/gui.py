import tkinter as tk
from tkinter import messagebox
from main import get_movie_recommendations

# Function to get movie recommendations
def get_recommendations():
    user_id = int(user_id_entry.get())
    num_recommendations = int(num_recommendations_entry.get())
    recommended_movies = get_movie_recommendations(user_id, num_recommendations)
    recommended_movies_list = recommended_movies

    recommended_movies_text.delete('1.0', tk.END)
    recommended_movies_text.insert(tk.END, "\n".join(recommended_movies_list))

# Create the main window
root = tk.Tk()
root.title("Movie Recommendation System - By Matt Norris")

# Create user_id input label and entry
user_id_label = tk.Label(root, text="User ID:")
user_id_label.grid(row=0, column=0, padx=10, pady=10)
user_id_entry = tk.Entry(root)
user_id_entry.grid(row=0, column=1, padx=10, pady=10)

# Create num_recommendations input label and entry
num_recommendations_label = tk.Label(root, text="Number of Recommendations:")
num_recommendations_label.grid(row=1, column=0, padx=10, pady=10)
num_recommendations_entry = tk.Entry(root)
num_recommendations_entry.grid(row=1, column=1, padx=10, pady=10)

# Create get recommendations button
get_recommendations_button = tk.Button(root, text="Get Recommendations", command=get_recommendations)
get_recommendations_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create recommended movies text box
recommended_movies_text = tk.Text(root, height=10, width=50)
recommended_movies_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()