# Medical Buddy

Medical Buddy is an AI-powered virtual assistant designed to provide personalized medical assistance, including checking drug interactions, offering conversational support, and enabling safe, reliable access to medical information. This app integrates various models and tools to ensure that users get accurate and actionable insights for their medical needs.

![WhatsApp Image 2024-09-06 at 02 30 36_7dcd4807](https://github.com/user-attachments/assets/b39d6735-f04e-46f6-8ab0-6c5e3b371110)


## Features

- *Drug Interaction Checker*: Automatically checks for potential drug interactions between two medications using a CSV dataset, ensuring safety and clarity for users.
- *Multi-Model AI Support*: Switches between using Google Gemini and Ollama models depending on internet connectivity, ensuring a seamless experience even offline.
- *Real-Time Python Execution*: Execute Python commands for real-time calculations and data analysis, assisting with medical research or any custom analysis.
- *Contextual Conversations*: Chat history is saved and loaded upon app restart, ensuring the conversation context is maintained, leading to better recommendations and personalized responses.
- *Progressive Interaction*: Uses notifications and progress bars to keep users updated on ongoing operations, creating a smooth and responsive user experience.
- *Chat History & Data Management*: Offers functionality to clear chat history and remove generated data files, giving users control over their data.

## How It Works

### Drug Interaction Checker
Medical Buddy uses a CSV dataset to store known drug interactions. The user can input two drugs, and the system will return any known interaction, ensuring safer medication management.

### Dynamic Model Selection
The app dynamically selects the best model to use based on internet connectivity:
- *Online Mode*: Utilizes Google Gemini for fast, cloud-based responses.
- *Offline Mode*: Switches to Ollama’s model, ensuring the user experience is uninterrupted.

### Conversational Interface
Medical Buddy saves the user’s chat history and ensures continuity in the interaction. It can answer questions, check drug interactions, and even execute Python commands to assist in various medical and computational needs.

## Usage

Simply input your queries or drug names, and Medical Buddy will provide the required information or check for drug interactions. You can also execute Python code or clear previous conversations as needed.

This AI-powered assistant makes managing your healthcare easier and safer by providing quick, accurate, and actionable insights.
