import tkinter as tk
from tkinter import messagebox

class DevOpsQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DevOps Mastery Quiz")
        self.root.geometry("600x400")
        
        # Quiz Data: Add your 50 questions here
        self.questions = [
            {
                "question": "Which tool is primarily used for Infrastructure as Code (IaC)?",
                "options": ["Ansible", "Terraform", "Docker", "Jenkins"],
                "answer": "Terraform"
            },
            {
                "question": "What does the 'CD' in CI/CD stand for?",
                "options": ["Continuous Design", "Continuous Data", "Continuous Deployment", "Control Delivery"],
                "answer": "Continuous Deployment"
            },
            {
                "question": "Which of these is a container orchestration platform?",
                "options": ["Kubernetes", "Prometheus", "GitLab", "Splunk"],
                "answer": "Kubernetes"
            },
            # ... Add more questions following this format
        ]
        
        self.current_question_index = 0
        self.score = 0
        
        # UI Elements
        self.question_label = tk.Label(root, text="", wraplength=500, font=("Helvetica", 16, "bold"), pady=20)
        self.question_label.pack()
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", width=40, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.option_buttons.append(btn)
            
        self.status_label = tk.Label(root, text="", pady=20, font=("Helvetica", 12))
        self.status_label.pack()
        
        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            q_data = self.questions[self.current_question_index]
            self.question_label.config(text=f"Q{self.current_question_index + 1}: {q_data['question']}")
            
            for i, option in enumerate(q_data['options']):
                self.option_buttons[i].config(text=option, state="normal", bg="systemButtonFace")
            
            self.status_label.config(text=f"Score: {self.score}/{len(self.questions)}")
        else:
            self.show_final_score()

    def check_answer(self, selected_index):
        q_data = self.questions[self.current_question_index]
        selected_option = q_data['options'][selected_index]
        correct_option = q_data['answer']
        
        if selected_option == correct_option:
            self.score += 1
            messagebox.showinfo("Result", f"Correct! \n\n {correct_option} is the right answer.")
        else:
            messagebox.showerror("Result", f"Wrong! \n\n The correct answer was: {correct_option}")
        
        self.current_question_index += 1
        self.load_question()

    def show_final_score(self):
        messagebox.showinfo("Quiz Over", f"Congratulations! Your final score is {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DevOpsQuizApp(root)
    root.mainloop()