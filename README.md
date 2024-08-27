# Run app using virtualenv
```bash
./init.sh
```

# Run app using Docker
## build the image
```bash
docker build -t auth .
```
## run it 
```bash
docker run -d -p 5000:5000 auth
```

##############################################
User Stories

    - User Story 1: Doctor Consultation via Chat   
       As a  patient,
       I want   to have a secure and private chat with a doctor through the website,
       so that   I can receive real   time medical advice without needing to visit the clinic in     person.

         Acceptance Criteria:   
        The patient can log in securely and start a chat session with an available doctor.
        The chat interface is easy to use, and messages are delivered promptly.
        The doctor can view the patient's chat history within the session to provide accurate advice.
        The session can be ended by either the doctor or the patient, with a summary available for review.

    - User Story 2: AI  Powered FAQ Assistance   
       As a patient,
       I want    to ask medical   related questions to an AI assistant,
       so that    I can get immediate answers to common health questions but you need to cosulte a doctor.

         Acceptance Criteria:   
        The patient can access the AI chat feature without logging in.
        The AI provides accurate and helpful responses based on the user's input.
        The AI can handle follow  up questions in the same session.
        The patient has the option to escalate the chat to a human doctor if it's not common medical question.

    - User Story 3: AI Powered FAQ Assistance   
       As a patient,
       I want    to ask information related to the website services.

         Acceptance Criteria:   
        The patient can access the AI chat feature without logging in.
        The AI provides accurate and helpful responses based on the user's input.
        The AI can handle follow  up questions in the same session.

    - User Story 4: Payment for Services As a patient,
       I want    to make payments securely for medical consultations and home visits,
       so that    I can easily manage my medical expenses through the website.

         Acceptance Criteria:   
        The patient can view a list of available services and their prices.
        The patient can enter payment details securely and receive a confirmation of the transaction.
        The payment system supports multiple payment methods (e.g., credit card, PayPal).
        The patient receives a receipt via email after a successful transaction.

    - User Story 5: Scheduling a Doctor's Home Visit   
       As a    patient,
       I want    to schedule a doctor's home visit through the website,
       so that    I can receive medical care at home without having to travel.

         Acceptance Criteria:   
        The patient can select an available doctor and view their available time slots.
        The patient can enter their location and preferred time for the visit.
        The system sends a confirmation of the booking and a reminder before the scheduled time.
        The patient can view or cancel the booking through their account.

    - User Story 6: User Authentication and Profile Management   
       As a    patient,
       I want    to securely sign up, log in, and manage my profile,
       so that    I can access the services provided by the website and keep my information up to date.

         Acceptance Criteria:   
        The patient can create an account with a unique username, email, and password.
        The patient can log in and log out securely.
        The patient can update their profile information, such as contact details and payment preferences.
        The system ensures the user's data is protected and complies with privacy regulations.
