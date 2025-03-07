import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Load HR contacts from CSV
csv_file = "cleaned_hr_contacts.csv"
 # Ensure this file is in the same folder
df = pd.read_csv(csv_file)

# Email credentials
sender_email = "thesatwikojha@gmail.com"  # Replace with your email
password = "xxxx xxxx xxxx" # Replace with your App Password

# SMTP setup for Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Attach resume
resume_path = "Satwik_ResumeCSAIML.pdf"  # Replace with the correct filename & path

# Initialize SMTP session
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, password)

# Loop through each HR contact and send a personalized email
for index, row in df.iterrows():
    receiver_email = row["Email"]
    name = row["Name"]
    company = row["Company"]

    # Email subject & body
    subject = f"Application for Associate Software Engineer / Machine learning Engineer at {company}"
    body = f"""
    Dear {name},

    I hope you are doing well. I recently came across {company} and I am highly interested in the Associate Software Engineer role.or role related to Machine 
    Learning Engineer.
    
    I have completed my B.Tech in Computer Science and Engineering from GL Bajaj Institute Of Technology And Management .I have a strong foundation in programming, data structures, algorithms, and problem-solving.
    
    I have experience in AI, Python, and Machine Learning, and I believe my skills align with your requirements and also I have complted my DSA in Java 

    Please find my resume attached. I would love the opportunity to discuss further.

    Best Regards,  
    Satwik Ojha  
    +91 9555371018 
    ojhasatwik@gmail.com 
    """

    # Compose email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Attach Resume
    try:
        with open(resume_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename=resume.pdf")
            msg.attach(part)
    except FileNotFoundError:
        print(f"❌ Resume file not found: {resume_path}")

    # Send email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print(f"✅ Email sent to {name} at {receiver_email}")

# Close SMTP connection
server.quit()
print("🎉 All emails sent successfully!")
