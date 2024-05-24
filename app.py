from config import Config
from app import create_app

app = create_app(Config)

# run on port 8000 to avoid conflicts with mac stuff
if __name__ == "__main__":
    app.run(debug=True, port=8000)
