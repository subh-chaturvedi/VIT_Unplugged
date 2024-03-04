from flask import Flask, request, jsonify
import os  
import openai

app = Flask(__name__)

openai.api_key = "REDACT"

@app.route("/send_mail", methods=["POST"])
def send_mail():
    # """
    # API endpoint to receive mail content, format a prompt, and send mail.
    # """

    # Extract mail content from request data
    mail_content = request.json.get("mail")

    if mail_content is None:
        return jsonify({"error": "Missing mail content in request body"}), 400

    # Replace with your GPT-4 prompt formatting logic here (refer to comments below)
    prompt = format_prompt_for_gpt(mail_content)

    # Replace with your GPT-4 interaction logic here and handle potential errors
    recipients = interact_with_gpt(prompt)

    if recipients is None:
        return jsonify({"error": "Failed to determine recipients from GPT-4"}), 500

    # Send mail to all recipients (replace with your preferred mail sending library)
    send_mail_to_recipients(mail_content, recipients)

    return jsonify({"message": "Mail sent successfully"}), 200

def format_prompt_for_gpt(mail_content):
    # """
    # This function should format the mail content into a prompt suitable for GPT-4.
    # Ensure it follows the prompt structure and entity information provided earlier.
    # """
    # Example implementation (replace with your actual logic):
    entities = "Program Chair: Manages academic programs (schedules, holidays, credits).\nSchool Dean: Decides curriculum for subjects and school.\nVice Chancellor: Top administrator, involved only in critical matters.\nStudent: Belongs to a School and program, has a proctor.\nProctor (Teacher): Handles student leaves and communication.\nController of Examinations: Manages exams and related queries.\nController of Technical Services: IT administrator for student dashboard etc.\nTeacher: Teaches courses, also acts as a proctor.\nChief Warden: Manages hostel-related issues."
    prompt = f"**Entities:**\n{entities}\n**Mail:**\n{mail_content}\n**Question:** Based on the mail content and entity information, who are the appropriate recipients for this email?"
    return prompt

def interact_with_gpt(prompt):
    # """
    # This function should interact with GPT-4 using the provided prompt and return a list of recipient entities.
    # Handle potential errors and return `None` if unsuccessful.
    # """
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # This is the model ID for GPT-4, change if needed
        messages=[{"role": "user", "content": prompt}],
        max_tokens=70
    )

    # recipients = extract_recipients_from_response(response.choices[0].message)
    print(response.choices[0].message.content.strip())
    recipients = extract_recipients_from_response(response.choices[0].message.content.strip())
    print (recipients)


entitiess = ["Program Chair", "School Dean", "Vice Chancellor", "Student", "Proctor", "Controller of Examination", "Controller of Technical Services", "Teacher", "Chief Warden"]
emailDict = {
    "Program Chair": "pc@vitbhopal.ac.in",
    "School Dean": "dean@vitbhopal.ac.in",
    "Vice Chancellor": "vicechancellor@vitbhopal.ac.in",
    "Student": "student@vitbhopal.ac.in",
    "Proctor": "proctor@vitbhopal.ac.in",
    "Controller of Examination": "coe@vitbhopal.ac.in",
    "Controller of Technical Services": "cts@vitbhopal.ac.in",
    "Teacher": "teacher@vitbhopal.ac.in",
    "Chief Warden": "warden@vitbhopal.ac.in"
}



def extract_recipients_from_response(gpt_response):
    # """
    # This function should parse the GPT-4 response and extract the list of recipient entities.
    # Handle potential parsing errors and return an empty list if unsuccessful.
    # """
    # Example implementation (replace with your actual parsing logic):
    # ... (logic to parse GPT-4 response and extract recipient entities)

    # entitiess: ["Program Chair","School Dean","Vice Chancellor","Student","Proctor","Controller of Examination","Controller of Technical Services","Teacher","Chief Warden"]
    # emailDict: {"Program Chair":"pc@vitbhopal.ac.in","School Dean":"dean@vitbhopal.ac.in","Vice Chancellor":"vicechancellor@vitbhopal.ac.in","Student":"student@vitbhopal.ac.in","Proctor":"proctor@vitbhopal.ac.in","Controller of Examination":"coe@vitbhopal.ac.in","Controller of Technical Services":"cts@vitbhopal.ac.in","Teacher":"teacher@vitbhopal.ac.in","Chief Warden":"warden@vitbhopal.ac.in"}

    recipients = []

    for i in entitiess:
        # print("&",i)
        if i in gpt_response:
            recipients.append(emailDict[i])

    return recipients

def send_mail_to_recipients(mail_content, recipients):
    # """
    # This function should send the original mail to all the recipients using your preferred mail sending library.
    # Handle potential sending errors.
    # """
    # Replace with your actual mail sending logic
    # ... (logic to send mail to recipients)

    print(i for i in recipients)


if __name__ == "__main__":
    print("Starting Python Flask Server...")
    # app.run()

    print(interact_with_gpt("Program Chair or Dean or Teacher? Choose one randomly"))

    # print(extract_recipients_from_response("Program Chair and Teacher"))
