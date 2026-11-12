# My Academic Projects and Practical Technical Work

This document describes my academic projects, software prototypes, and practical technical experiments. These projects have allowed me to explore different areas of Computer Science, including UI/UX design, mobile application development, database management, artificial intelligence, retrieval-augmented generation, and workflow automation.

# 1. EatEasy – Food Delivery Application Prototype

## Project Overview

EatEasy is a food delivery application prototype that I developed as part of my Human-Computer Interaction (HCI) coursework. The main purpose was to design an interface that allows users to understand and navigate a food ordering process easily.

## My Contribution

I designed nine application screens using Figma. My work included organizing screen layouts, selecting colors, arranging interface components, and maintaining visual consistency throughout the application.

I also created clickable prototype interactions. This allowed me to connect screens and demonstrate how a user could navigate through the application instead of viewing each screen as an isolated design.

## Design Considerations

While working on EatEasy, I focused on:

- Organizing information clearly.
- Maintaining consistency between screens.
- Designing understandable navigation.
- Considering the user's journey through the application.
- Connecting screens through clickable prototype interactions.

## What I Learned

This project helped me understand that UI/UX design is not only about making screens visually attractive. Navigation, usability, consistency, and the sequence of user actions are also important parts of an application.

It also gave me practical experience with Figma and interactive prototyping.

# 2. SkillBridge – Student Skill Exchange Platform

## Project Overview

SkillBridge is a Student Skill Exchange Platform developed as an Advanced Database Management System (ADBMS) project.

The idea is to provide a platform where students can offer skills they already know and request to learn skills from other students.

For example, one student may offer graphic design and want to learn Python, while another student may offer Python and want to learn graphic design. The platform is designed to help students connect through these skill exchange opportunities.

## Database Design

The project focuses on organizing information through a relational database. Its main entities include:

- Users
- Skills
- Offered_Skills
- Wanted_Skills
- Exchange_Request
- Sessions
- Reviews
- Exchange_History

Each entity represents a different part of the platform. Users maintain their profiles, Skills stores available skill information, and Offered_Skills and Wanted_Skills connect users with the skills they offer or want to learn.

Exchange_Request manages requests between students, while Sessions, Reviews, and Exchange_History represent later stages of an exchange.

## My Contribution and Technical Focus

My work has focused on understanding the database requirements, identifying entities, designing relationships, and organizing the information needed by the platform.

I have also explored how relational database concepts can support a practical website rather than simply storing unrelated records.

## What I Learned

SkillBridge helped me understand how to translate a real-world idea into database entities and relationships. It also improved my understanding of relational database design and how different tables work together to support application functionality.


# 2. Exam Integrity System

## Project Overview

My Final Year Project is titled "Exam Integrity System". It focuses on AI-assisted decision support for physical examination hall management. Its purpose is to identify potentially conflicting seating arrangements by evaluating hall-related information while considering uncertainty. The proposed solution is a software-based web prototype rather than a physical examination hall monitoring device.

## Main System Concept

The proposed system has two major interfaces:

### Student Allocation Interface

The student allocation interface provides a pre-examination environment with student lists, subject details, hall capacities, seating arrangement generation controls, a remaining-seats display, and hall allocation information through the browser.

### Teacher or Admin Dashboard

The admin dashboard displays flagged conflicts with relevant hall numbers and explanations of why an arrangement was considered potentially problematic. Unclear cases can be sent for human review.

## Research Direction

My research interest in this project includes uncertainty-aware decision support, explainable evidence, reducing false-positive decisions, and human involvement in ambiguous cases.

## What I Aim to Learn

Through this project, I want to explore how AI can support important decisions without treating every detected pattern as a confirmed conclusion. It also gives me an opportunity to understand the connection between web development, AI-based analysis, and explainable decision-making.

# 4. Cloud Computing – Three-Level RAG Project

## Project Overview

As part of my Cloud Computing coursework, I worked on a project related to Final Year Project (FYP) stress. The project involved working with CSV files, a RAG-based workflow, and the Mistral language model.

The main purpose was to explore how a language model could generate answers with different levels of detail based on the information provided to the system.

## CSV Files and Data Preparation

I created CSV files containing the data required for the project and connected them to the project workflow.

Working with these files gave me practical experience in preparing data in a structured format and making it available to the application.

## Three Answer Generation Levels

I worked with three levels of answer generation:

**Level 1 – Short Answer**

Generated a brief, single-line response to provide a direct answer.

**Level 2 – Expanded Answer**

Generated a longer response with additional sentences and explanation.

**Level 3 – Detailed Answer**

Generated a more detailed response covering the question in greater depth.

I compared the answers produced at these levels to observe how the response changed according to the required level of detail.

## Language Model

I used the Mistral language model for answer generation and explored how it could produce responses with different levels of detail.

## What I Learned

This project gave me practical exposure to working with CSV data, a RAG-based project workflow, and a language model. It also helped me understand the importance of organizing source data and comparing generated responses according to the user's information needs.

# 5. MediConnect – Healthcare Mobile Application

## Project Overview

MediConnect is a healthcare mobile application developed to connect patients and doctors through a shared platform.

The application provides different interfaces and functionality according to the user's role. It includes three main roles: Patient, Doctor, and Admin.

The idea is to make healthcare-related interactions, appointment management, and patient-doctor communication more organized through a mobile application.

## Application Roles and Features

**Patient**

Patients can:

- View available doctors.
- Book appointments.
- Manage their profiles.
- Access medical records.
- Manage payment-related information.

**Doctor**

Doctors can:

- Manage appointments.
- View patient information.
- Update availability.
- Manage their profiles.
- Use the doctor verification process.

**Admin**

The admin interface provides management functionality for:

- Users.
- Appointments.
- Billing.
- Security settings.

## Doctor Verification

An important feature of MediConnect is its doctor verification workflow using PMC identification numbers.

The application includes predefined verified demonstration doctor accounts. For other doctor registrations, an entered PMC number can receive a Pending Verification status.

The intended verification process allows the doctor to use the application while their verification status is awaiting manual checking against the relevant PMC registry.

This feature separates the registration process from the verification status instead of treating every registered doctor as automatically verified.

## Backend and Database

The application uses Supabase as its backend service, with PostgreSQL as the database.

It also uses Supabase Authentication for account management, including email authentication and Google OAuth.

The application has separate access and functionality for patients, doctors, and administrators.

## Technical Debugging and Improvement

During development, a profile update problem occurred because some expected database columns were missing.

The issue involved fields such as blood group and location-related information. The missing columns were added to the database schema after the submitted demonstration video had been recorded.

This resolved the profile-saving issue for both patient and doctor profiles.

## What I Learned

MediConnect helped me explore mobile application development, role-based functionality, authentication, database integration, and backend services.

It also showed me why frontend and backend structures must remain consistent. If an application expects a database field that does not exist, operations such as profile updates can fail.

This project gave me practical exposure to connecting a mobile application with a PostgreSQL-based backend.

# 6. Local Large Language Model Experiment Using LM Studio

## Project Overview

For my Agentic AI Systems and Applications coursework, I completed a practical experiment involving the installation and execution of a language model locally using LM Studio.

I wanted to understand how a language model can run on a personal computer and communicate with a Python application.

## Hardware Considerations

My computer has 8 GB RAM and integrated Intel HD Graphics 5500. Because of these hardware limitations, selecting a smaller model was important.

I used the Llama 3.2 1B Instruct model in Q4_K_M GGUF quantized format.

I also explored a text embedding model as part of my experimentation.

## Python API Integration

After loading the language model in LM Studio, I connected it with Python through a local API.

I created a Python test script to check communication between the application and the local model. The test successfully established communication and received a generated response.

## What I Learned

This experiment introduced me to local LLM execution, quantized models, embeddings, and API-based communication.

It also helped me understand how hardware resources influence the selection of AI models and why smaller models can be useful for local experimentation.

# 7. Workflow Automation Experiment Using n8n

## Project Overview

I have also explored workflow automation using n8n. The purpose of this learning experiment is to understand how different software services can be connected to automate repetitive tasks.

## Tools and Setup

I installed Docker Desktop and configured n8n to run locally.

I also started exploring authentication and service integration for Google Drive and Google Sheets.

This involved learning about Google service accounts, OAuth credentials, and the configuration required for connecting external services.

## What I Learned

This experiment introduced me to workflow automation, local service deployment, Docker-based environments, and API integrations.

I am still developing my understanding of n8n and want to explore more practical automation workflows.

# Overall Skills and Knowledge Gained

Across these projects, I have explored several areas of Computer Science:

- UI/UX design and clickable prototyping through Figma.
- Mobile application development and role-based functionality.
- Relational database design and PostgreSQL integration.
- SQL Server and database security concepts.
- Retrieval-Augmented Generation and language model integration.
- Local LLM execution using LM Studio.
- Python API communication.
- AI-assisted decision support and uncertainty handling.
- Workflow automation using n8n and Docker.

These projects represent my academic and practical learning journey. I do not consider myself an expert in every technology mentioned here. I am continuing to improve my skills through implementation, experimentation, and understanding the technical decisions behind each project.