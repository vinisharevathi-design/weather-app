from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        api_key = '1d08519c66403f992fa6cb0c63bb79b2'  # Unga OpenWeather API key-a inga podunga
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error = "City not found! Please check the city name."
            
    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)