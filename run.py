from app import api as application

if __name__ == '__main__':
    application.app.run(debug=True, host='0.0.0.0', port=5000)
