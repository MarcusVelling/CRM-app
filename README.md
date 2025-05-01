# Vue.js + FastAPI Project

This project consists of a Vue.js frontend and a FastAPI backend.

## Project Structure
```
.
├── backend/           # FastAPI backend
│   └── main.py       # Main FastAPI application
├── frontend/         # Vue.js frontend
└── requirements.txt  # Python dependencies
```

## Backend Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the backend server:
```bash
cd backend
uvicorn main:app --reload
```

The backend will be available at http://localhost:8000

## Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:5173

## API Documentation

Once the backend is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 