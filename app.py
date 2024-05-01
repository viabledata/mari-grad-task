from route import create_app

FLASK_CFG = "dev"

app = create_app(FLASK_CFG)

if __name__ == '__main__':
    app.run()
