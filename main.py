from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# .\env\Scripts\Activate