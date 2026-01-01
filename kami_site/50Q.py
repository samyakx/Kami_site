import tkinter as tk
from tkinter import messagebox
import random

class DevOpsQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DevOps 50 Mastery Quiz")
        self.root.geometry("700x500")
        
        # 50 DevOps Questions
        self.all_questions = [
            {"question": "Which tool is used for Infrastructure as Code (IaC)?", "options": ["Ansible", "Terraform", "Docker", "Jenkins"], "answer": "Terraform"},
            {"question": "What does 'CD' in CI/CD stand for?", "options": ["Continuous Design", "Continuous Data", "Continuous Deployment", "Control Delivery"], "answer": "Continuous Deployment"},
            {"question": "Which is a container orchestration platform?", "options": ["Kubernetes", "Prometheus", "GitLab", "Splunk"], "answer": "Kubernetes"},
            {"question": "In Git, which command combines two branches?", "options": ["git pull", "git combine", "git merge", "git push"], "answer": "git merge"},
            {"question": "What is the default port for Jenkins?", "options": ["8080", "9090", "443", "3000"], "answer": "8080"},
            {"question": "Which file is used to define a Docker image?", "options": ["docker.config", "Dockerfile", "docker.yaml", "container.txt"], "answer": "Dockerfile"},
            {"question": "Which tool is popular for monitoring and alerting?", "options": ["Terraform", "Ansible", "Prometheus", "Maven"], "answer": "Prometheus"},
            {"question": "What is the 'brain' of a Kubernetes cluster called?", "options": ["Worker Node", "Control Plane", "Kubelet", "Pod"], "answer": "Control Plane"},
            {"question": "Which command is used to apply Terraform changes?", "options": ["terraform build", "terraform go", "terraform apply", "terraform commit"], "answer": "terraform apply"},
            {"question": "What is a 'Pod' in Kubernetes?", "options": ["A storage unit", "Smallest deployable unit", "A network router", "A database"], "answer": "Smallest deployable unit"},
            {"question": "Which HTTP status code means 'Unauthorized'?", "options": ["200", "404", "401", "500"], "answer": "401"},
            {"question": "What does YAML stand for?", "options": ["Yet Another Markup Language", "Your Apple Multi Layer", "YAML Ain't Markup Language", "Yielding Any Machine Language"], "answer": "YAML Ain't Markup Language"},
            {"question": "Which tool is primarily for configuration management?", "options": ["Terraform", "Ansible", "Docker", "Git"], "answer": "Ansible"},
            {"question": "What is the command to list running Docker containers?", "options": ["docker ls", "docker list", "docker ps", "docker show"], "answer": "docker ps"},
            {"question": "In Git, how do you stage all changes for commit?", "options": ["git add .", "git commit -a", "git stage all", "git push"], "answer": "git add ."},
            {"question": "What is the main purpose of a Reverse Proxy?", "options": ["Speed up internet", "Forward requests to servers", "Delete log files", "Store passwords"], "answer": "Forward requests to servers"},
            {"question": "Which cloud provider owns Azure?", "options": ["Amazon", "Google", "Microsoft", "IBM"], "answer": "Microsoft"},
            {"question": "What is 'Shift Left' in DevOps?", "options": ["Moving tasks to the end", "Testing earlier in the cycle", "Deleting old code", "Moving to the cloud"], "answer": "Testing earlier in the cycle"},
            {"question": "Which command checks the status of a K8s cluster?", "options": ["kube-status", "kubectl get nodes", "k8s check", "docker nodes"], "answer": "kubectl get nodes"},
            {"question": "What is a 'Sidecar' pattern in K8s?", "options": ["A helper container", "A backup cluster", "A type of load balancer", "A security firewall"], "answer": "A helper container"},
            {"question": "Which tool is used for log aggregation?", "options": ["Nagios", "ELK Stack", "Jenkins", "Terraform"], "answer": "ELK Stack"},
            {"question": "What is the standard port for SSH?", "options": ["80", "443", "22", "21"], "answer": "22"},
            {"question": "What does the 'ping' command use?", "options": ["TCP", "UDP", "ICMP", "HTTP"], "answer": "ICMP"},
            {"question": "Which Git command reverts a commit?", "options": ["git delete", "git revert", "git undo", "git back"], "answer": "git revert"},
            {"question": "What is 'Blue-Green' deployment?", "options": ["A color scheme", "Two identical environments", "A testing method", "A security protocol"], "answer": "Two identical environments"},
            {"question": "What is the purpose of 'Vagrant'?", "options": ["Building VM environments", "Monitoring", "Code editing", "Compiling Java"], "answer": "Building VM environments"},
            {"question": "Which is a 'NoSQL' database?", "options": ["MySQL", "PostgreSQL", "MongoDB", "Oracle"], "answer": "MongoDB"},
            {"question": "What is 'Canary Deployment'?", "options": ["Deploying to everyone", "Deploying to a small group", "Using birds to test", "Deleting the server"], "answer": "Deploying to a small group"},
            {"question": "What does 'SRE' stand for?", "options": ["Software Reliability Eng.", "Site Reliability Eng.", "System Repair Expert", "Secure Remote Entry"], "answer": "Site Reliability Eng."},
            {"question": "Which language is Terraform written in?", "options": ["Python", "Java", "Go", "C++"], "answer": "Go"},
            {"question": "In Docker, what is a 'layer'?", "options": ["A UI design", "An instruction in Dockerfile", "A security level", "A network cable"], "answer": "An instruction in Dockerfile"},
            {"question": "What is the use of 'Helm'?", "options": ["Docker GUI", "K8s Package Manager", "Git Hosting", "Cloud Storage"], "answer": "K8s Package Manager"},
            {"question": "What is 'Idempotency' in Ansible?", "options": ["Running once only", "Result is same if run twice", "Speed of execution", "Encryption level"], "answer": "Result is same if run twice"},
            {"question": "Which command removes a Docker container?", "options": ["docker rm", "docker rmi", "docker del", "docker stop"], "answer": "docker rm"},
            {"question": "What is 'GitOps'?", "options": ["Git for Operations", "Using Git as source of truth", "A new version of Git", "Cloud hosting"], "answer": "Using Git as source of truth"},
            {"question": "Which file specifies Terraform providers?", "options": ["main.tf", "provider.tf", "config.xml", "settings.json"], "answer": "main.tf"},
            {"question": "What is a 'DaemonSet' in K8s?", "options": ["A virus", "A pod on every node", "A database backup", "A user role"], "answer": "A pod on every node"},
            {"question": "What is the purpose of 'Nginx'?", "options": ["Database", "Web Server / Proxy", "Compiler", "OS"], "answer": "Web Server / Proxy"},
            {"question": "What does 'TDD' stand for?", "options": ["Test Driven Development", "Total Data Design", "Technical Debt Duty", "Time Delay Delivery"], "answer": "Test Driven Development"},
            {"question": "Which tool is used for Secrets Management?", "options": ["HashiCorp Vault", "Excel", "Notepad", "Docker Hub"], "answer": "HashiCorp Vault"},
            {"question": "What is the default port for HTTPS?", "options": ["80", "8080", "443", "8443"], "answer": "443"},
            {"question": "What command lists all files in Linux including hidden?", "options": ["ls", "ls -a", "ls -l", "list all"], "answer": "ls -a"},
            {"question": "In Linux, how do you change file permissions?", "options": ["chmod", "chown", "permit", "access"], "answer": "chmod"},
            {"question": "What is 'Chaos Engineering'?", "options": ["Testing by breaking things", "Random coding", "Unorganized teams", "Deleting logs"], "answer": "Testing by breaking things"},
            {"question": "Which is an example of 'Serverless'?", "options": ["EC2", "AWS Lambda", "Docker", "VirtualBox"], "answer": "AWS Lambda"},
            {"question": "What is 'Groovy' used for in DevOps?", "options": ["Terraform code", "Jenkins Pipelines", "Docker images", "Python scripts"], "answer": "Jenkins Pipelines"},
            {"question": "What is a 'Namespace' in K8s used for?", "options": ["Naming containers", "Isolating resources", "IP addressing", "Storing passwords"], "answer": "Isolating resources"},
            {"question": "What does 'MTTR' stand for?", "options": ["Mean Time To Recover", "Max Time To Repair", "Minimum Total Rate", "Most Tasks To Resolve"], "answer": "Mean Time To Recover"},
            {"question": "Which tool is often used for 'Service Mesh'?", "options": ["Istio", "Jenkins", "Ansible", "Maven"], "answer": "Istio"},
            {"question": "What is 'Dark Launching'?", "options": ["Launching at night", "Releasing features hidden", "System shutdown", "Illegal deployment"], "answer": "Releasing features hidden"}
        ]
        
        random.shuffle(self.all_questions) # Shuffle to make it interesting
        self.current_question_index = 0
        self.score = 0
        
        # UI Elements
        self.question_label = tk.Label(root, text="", wraplength=600, font=("Arial", 14, "bold"), pady=30)
        self.question_label.pack()
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", width=50, height=2, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=10)
            self.option_buttons.append(btn)
            
        self.progress_label = tk.Label(root, text="", pady=20, font=("Arial", 10))
        self.progress_label.pack()
        
        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.all_questions):
            q_data = self.all_questions[self.current_question_index]
            self.question_label.config(text=f"Q{self.current_question_index + 1}: {q_data['question']}")
            
            # Shuffle options so the correct one isn't always in the same place
            options = q_data['options']
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option)
            
            self.progress_label.config(text=f"Progress: {self.current_question_index + 1} / 50  |  Score: {self.score}")
        else:
            self.show_final_score()

    def check_answer(self, selected_index):
        q_data = self.all_questions[self.current_question_index]
        selected_option = q_data['options'][selected_index]
        correct_option = q_data['answer']
        
        if selected_option == correct_option:
            self.score += 1
            messagebox.showinfo("Correct!", f"Well done! \n\n '{correct_option}' is correct.")
        else:
            messagebox.showerror("Wrong", f"Oops! \n\nThe correct answer was: {correct_option}")
        
        self.current_question_index += 1
        self.load_question()

    def show_final_score(self):
        percentage = (self.score / 50) * 100
        messagebox.showinfo("Result", f"Quiz Complete!\n\nFinal Score: {self.score}/50\nPercentage: {percentage}%")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DevOpsQuizApp(root)
    root.mainloop()