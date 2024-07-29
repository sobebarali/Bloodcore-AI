# Bloodcore Crew

Welcome to the Bloodcore Crew project, powered by [crewAI](https://crewai.com). This project aims to set up a crew of agents using the CrewAI framework to analyze blood test reports, search for relevant health articles, make personalized recommendations, and securely share the analysis and recommendations with users via email.

## Project Goals

- Take a sample blood test report in PDF format
- Understand and analyze the report's content
- Search the internet for articles that fit the person's needs
- Make health recommendations based on the findings
- Develop a secure POST API to share the analysis and recommendations with the user via email

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:

```bash
poetry lock
```

```bash
poetry install
```

### Customizing

- Add your `OPENAI_API_KEY` into the `.env` file
- Modify `src/bloodcore/config/agents.yaml` to define your agents
- Modify `src/bloodcore/config/tasks.yaml` to define your tasks
- Modify `src/bloodcore/crew.py` to add your own logic, tools and specific args
- Modify `src/bloodcore/main.py` to add custom inputs for your agents and tasks

## Configuration

In addition to the standard configuration files, make sure to set up the following:

- Mailtrap API credentials for email functionality in `.env`:
  ```
  SMTP_USERNAME="username"
  SMTP_PASSWORD="password"
  SMTP_SERVER="sandbox.smtp.mailtrap.io"
  SMTP_PORT="2525"
  SMTP_FROM_EMAIL="email"
  ```

- Supabase API credentials for authentication in `.env`:
  ```
  SUPABASE_URL=your_supabase_url
  SUPABASE_KEY=your_supabase_api_key
  ```

- OpenAI API key for the Article Searcher agent in `.env`:
  ```
  OPENAI_API_KEY=your_openai_api_key
  ```

- Serper API key for the Article Searcher agent in `.env`:
  ```
  SERPER_API_KEY=your_serper_api_key
  ```    

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run bloodcore
```

This command initializes the Bloodcore Crew, assembling the agents and assigning them tasks as defined in your configuration. This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The Bloodcore Crew consists of multiple AI agents collaborating to achieve the project goals:

- Blood Test Analyzer: Interprets and analyzes the PDF blood test report
- Article Searcher: Searches the internet for relevant health articles based on the analysis
- Recommendation Maker: Generates personalized health recommendations
- Email Sender: Integrates with Mailtrap to send the analysis and recommendations via email
- API Developer: Creates a secure POST API endpoint for receiving reports and sending emails

## APIs

### Blood Test Report Analysis API

- Endpoint: `/blood-report/analyze-report`
- Method: POST
- Request Body:
  - `report`: PDF file of the blood test report
  - `email`: User's email address for receiving the analysis and recommendations
- Response:
  - `status`: Success status of the analysis
  - `message`: Additional information about the analysis process

### User Authentication API

- Endpoint: `auth/signup`
- Method: POST
- Request Body:
  - `email`: User's email address
  - `password`: User's password
- Response:
  - `user`: User's Object

- Endpoint: `auth/login`
- Method: POST
- Request Body:
  - `email`: User's email address
  - `password`: User's password
- Response:
  - `message`: Additional information about the analysis process

- Endpoint: `auth/me`
- Method: GET
- Response:
  - `user`: User's Object

- Endpoint: `auth/logout`
- Method: GET
- Response:
  - `message`: Additional information about the analysis process  


### Email Sender API

- Endpoint: `email/send`
- Method: POST
- Request Body:
  - `email`: User's email address
  - `subject`: Email subject
  - `message`: Email body
  - `attachment`: PDF file of the blood test report
- Response:
  - `status`: Success status of the email sending process
  - `message`: Additional information about the email sending process