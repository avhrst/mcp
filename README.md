# Python Project

This is a Python project template with a basic structure.

## Project Structure

```
.
├── README.md
├── requirements.txt
├── src/
│   └── main.py
└── .gitignore
```

## Setup

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

To run the project:
```bash
python src/main.py
```

## Development

- Add your Python code in the `src` directory
- Add new dependencies to `requirements.txt`
- Update this README as needed

# MCP Server with Oracle Database Integration

This is a Message Control Protocol (MCP) server implementation that provides a REST API for message handling with Oracle Database integration using ODBC.

## Prerequisites

- Python 3.8 or higher
- Oracle Client installed and configured
- ODBC Driver for Oracle installed

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the database connection:
   - Update the database settings in `config.py`
   - Make sure your Oracle ODBC driver is properly configured

## Database Setup

Create the messages table in your Oracle database:

```sql
CREATE TABLE messages (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    content VARCHAR2(4000) NOT NULL,
    priority NUMBER DEFAULT 1,
    metadata VARCHAR2(4000),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Running the Server

Start the server with:
```bash
python main.py
```

The server will start on http://localhost:8000 by default.

## API Endpoints

- `POST /messages/` - Create a new message
- `GET /messages/` - Retrieve all messages
- `GET /health` - Health check endpoint

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Example Usage

Create a new message:
```bash
curl -X POST "http://localhost:8000/messages/" \
     -H "Content-Type: application/json" \
     -d '{"content": "Test message", "priority": 1, "metadata": {"key": "value"}}'
```

Get all messages:
```bash
curl "http://localhost:8000/messages/"
```

## Error Handling

The server includes comprehensive error handling for:
- Database connection issues
- Query execution errors
- Invalid input data
- Server health monitoring

## Security Considerations

- Update the default configuration in `config.py` with your secure credentials
- Consider implementing authentication and authorization
- Use HTTPS in production
- Implement rate limiting for production use