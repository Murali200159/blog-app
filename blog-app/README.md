Blog App
A full-stack blog application with user authentication and CRUD operations for blog posts.
Features

User registration and login with JWT authentication.
Create, read, update, and delete blog posts (CRUD).
Protected routes: only post owners can edit/delete their posts.
Responsive UI with Tailwind CSS.
Pagination and search for posts.
Toasts for success/error messages.
Confirm dialog for post deletion.

Tech Stack

Backend: Node.js, Express, MongoDB, JWT, bcrypt
Frontend: React, Tailwind CSS, Axios
Database: MongoDB

Setup Instructions
Prerequisites

Node.js (v16+)
MongoDB (local or MongoDB Atlas)
Git

Backend Setup

Navigate to the server directory:cd server


Install dependencies:npm install


Create a .env file based on .env.example:cp .env.example .env

Update MONGO_URI, JWT_SECRET, and CLIENT_URL.
Run the server in development:npm start

Server runs on http://localhost:5000.

Frontend Setup

Navigate to the client directory:cd client


Install dependencies:npm install


Create a .env file based on .env.example:cp .env.example .env

Update REACT_APP_API_URL to point to your backend.
Run the frontend in development:npm start

Frontend runs on http://localhost:3000.

Production Deployment

Backend: Use a platform like Render or Heroku. Set environment variables in the platform's dashboard.
Frontend: Build with npm run build and deploy to Netlify or Vercel.

API Documentation
Auth Routes

POST /api/auth/register
Payload: { "username": "string", "email": "string", "password": "string" }
Response: { "message": "User registered" }


POST /api/auth/login
Payload: { "email": "string", "password": "string" }
Response: { "token": "jwt_token" }



Post Routes

GET /api/posts?search=&page=&limit=
Query: search (title/username), page, limit
Response: [{ _id, title, imageURL, content, username, createdAt }]


GET /api/posts/:id
Response: { _id, title, imageURL, content, username, createdAt }


POST /api/posts (auth required)
Payload: { "title": "string", "imageURL": "string", "content": "string" }
Response: { _id, title, imageURL, content, username, createdAt }


PUT /api/posts/:id (auth, owner)
Payload: { "title": "string", "imageURL": "string", "content": "string" }
Response: Updated post


DELETE /api/posts/:id (auth, owner)
Response: { "message": "Post deleted" }



Screenshots

Home Feed: [Insert screenshot or GIF]
Post Detail: [Insert screenshot]
Profile Page: [Insert screenshot]

Bonus

Postman collection: [Link to collection or include JSON in repo]
Seed script: Run npm run seed in server to populate sample data (implement as needed).
