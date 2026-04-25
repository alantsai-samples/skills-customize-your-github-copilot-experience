# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful APIs using the FastAPI framework in Python. By the end of this assignment, you will have built a simple API for managing a collection of resources (e.g., books, users, or tasks).

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project

#### Description
Initialize a new FastAPI project and create a basic API endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Use FastAPI and Uvicorn as the server
- Provide a root endpoint (`/`) that returns a JSON welcome message
- Include clear instructions for running the server


### 🛠️ Task 2: Implement CRUD Endpoints

#### Description
Expand your FastAPI app to support Create, Read, Update, and Delete (CRUD) operations for a resource (e.g., books).

#### Requirements
Completed program should:

- Define a Pydantic model for the resource
- Implement endpoints for creating, reading (all and by ID), updating, and deleting resources
- Store resources in an in-memory list or dictionary
- Return appropriate HTTP status codes and error messages


### 🛠️ Task 3: Add Data Validation and Error Handling

#### Description
Enhance your API with input validation and proper error handling.

#### Requirements
Completed program should:

- Validate incoming data using Pydantic models
- Return 404 errors for missing resources
- Return 422 errors for invalid input
- Provide helpful error messages in JSON format

---

**Submission:**
- Include your FastAPI app code and a `requirements.txt` file listing dependencies
- Add instructions for running and testing your API in the README
- (Optional) Add example `curl` commands or screenshots of API responses
