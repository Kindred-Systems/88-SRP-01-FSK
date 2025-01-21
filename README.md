# Open Adventure Engine: Flask Server

The Open Adventure Engine Flask Server powers a single game instance, handling core gameplay logic, user authentication, and dynamic world updates. This server is designed to integrate seamlessly with a Flutter frontend, which serves as the primary interface for players across web, Android, and iOS platforms.

## Features

- **Single Game Instance**: This server hosts and manages a single game world.
- **Native Authentication**: User accounts and sessions are managed natively within the server.
- **Flutter Integration**: Supports interaction through a Flutter frontend for web and mobile platforms.
- **Scalable Deployment**: Can be containerized for multiple instances in future web session deployments.
- **Future Expansion**: Ready for integration with a centralized registry and scalable frontend hosting.

## Installation

### Prerequisites

- Docker and Docker Compose installed.
- Python 3.10+ for local development (optional).

### Steps

1. Clone the repository (SSH):

    ```bash
    git clone git@github.com:Kindred-Systems/88-SRP-01-FSK.git
    cd open-adventure-engine-flask
    ```

2. Configure the database:

    ```python
    from app import db, create_app
    app = create_app()
    with app.app_context():
        db.create_all()
    exit()
    ```

3. Start the server with Docker:

    ```bash
    docker-compose up
    ```

4. Configure environment variables:

    Create a file named `.env` in the root of the project directory (same level as `docker-compose.yml`). Below is an example structure with placeholder values:

    ```plaintext
    # Flask app variables
    SECRET_KEY=your_secret_key

    # PostgreSQL database variables
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=yourpassword
    POSTGRES_DB=game_instance
    DATABASE_URI=postgresql://postgres:yourpassword@db:5432/game_instance
    ```

    - `SECRET_KEY`: A secret key for Flask application security. Use a long, random string in production.
    - `POSTGRES_USER`: The username for the PostgreSQL database.
    - `POSTGRES_PASSWORD`: The password for the PostgreSQL user.
    - `POSTGRES_DB`: The name of the PostgreSQL database.
    - `DATABASE_URI`: The URI connection string for SQLAlchemy to connect to the database.

5. Access the server API:
    The server runs on [http://localhost:5000](http://localhost:5000).

## Interaction via Flutter

This server is designed to be used with the Flutter frontend, which serves as the player interface. The Flutter app:

- **Web Sessions**: Will eventually be containerized for seamless on-demand session deployment.
- **Mobile Platforms**: Supports Android and iOS apps, providing a unified experience across devices.

## API Endpoints

### Authentication

| Endpoint  | Method | Description           |
|-----------|--------|-----------------------|
| /register | POST   | Register a new user.  |
| /login    | POST   | Login an existing user.|
| /logout   | POST   | Logout the current user.|

### Game

| Endpoint | Method | Description                      |
|----------|--------|----------------------------------|
| /status  | GET    | Get server status (authenticated).|

## Directory Structure

```plaintext
88-SRP-01-FSK/
├── gsrv/                    # Flask app directory
│   ├── __init__.py          # App factory
│   ├── auth.py              # Authentication routes
│   ├── config.py            # Configuration
│   ├── game_logic.py        # Game logic
│   ├── models.py            # Database models
│   ├── routes.py            # General routes
│   ├── Dockerfile           # Dockerfile for Flask app
├── psql/                    # PostgreSQL directory
│   ├── init.sql             # SQL initialization script
│   └── Dockerfile           # Dockerfile for PostgreSQL
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Orchestration for Flask and PostgreSQL
└── README.md                # Documentation
└── LICENSE                  # License
```

## Roadmap

- **Hex Map Mechanics**: Expand endpoints to support dynamic hex map generation and management.
- **AI Behavior**: Introduce APIs for AI principal decision-making and interactions.
- **Web Session Frontend**: Deploy the Flutter web app in containerized environments for scalable player sessions.
- **Mobile App Integration**: Support native Android and iOS applications with backend API.

## License

This project is licensed under the MIT License.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch:

    ```bash
    git checkout -b feature/my-feature
    ```

3. Commit your changes:

    ```bash
    git commit -m "Add my feature"
    ```

4. Push your branch:

    ```bash
    git push origin feature/my-feature
    ```

5. Open a pull request.

## Contact

Questions? Reach out via GitHub Issues or Discussions.
