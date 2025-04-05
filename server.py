from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/command/check_adb', methods=['GET'])
def check_adb():
    devices = os.popen("adb devices").read()
    if "device" in devices:
        return jsonify({"status": "Phone Connected ✅"})
    return jsonify({"status": "No Device Found ❌"})

@app.route('/command/volume_up', methods=['GET'])
def volume_up():
    os.system("adb shell input keyevent 24")
    return jsonify({"status": "Volume Increased 🔊"})

@app.route('/command/volume_down', methods=['GET'])
def volume_down():
    os.system("adb shell input keyevent 25")
    return jsonify({"status": "Volume Decreased 🔉"})

@app.route('/command/mute', methods=['GET'])
def mute():
    os.system("adb shell input keyevent 164")
    return jsonify({"status": "Muted 🔇"})

@app.route('/command/check_battery', methods=['GET'])
def check_battery():
    battery = os.popen("adb shell dumpsys battery | findstr level").read().strip()
    return jsonify({"status": f"🔋 Battery Level: {battery}"})

@app.route('/command/wifi_on', methods=['GET'])
def wifi_on():
    os.system("adb shell svc wifi enable")
    return jsonify({"status": "WiFi Enabled 📶"})

@app.route('/command/wifi_off', methods=['GET'])
def wifi_off():
    os.system("adb shell svc wifi disable")
    return jsonify({"status": "WiFi Disabled 📴"})

@app.route('/command/screenshot', methods=['GET'])
def take_screenshot():
    os.system("adb shell screencap -p /sdcard/screenshot.png")
    os.system("adb pull /sdcard/screenshot.png .")
    return jsonify({"status": "📸 Screenshot Saved!"})

@app.route('/command/launch_youtube', methods=['GET'])
def launch_youtube():
    os.system("adb shell monkey -p com.google.android.youtube -c android.intent.category.LAUNCHER 1")
    return jsonify({"status": "YouTube Launched ▶️"})

@app.route('/command/launch_playstore', methods=['GET'])
def launch_playstore():
    os.system("adb shell monkey -p com.android.vending -c android.intent.category.LAUNCHER 1")
    return jsonify({"status": "Play Store Launched 🛍️"})

@app.route('/command/launch_spotify', methods=['GET'])
def launch_spotify():
    os.system("adb shell monkey -p com.spotify.music -c android.intent.category.LAUNCHER 1")
    return jsonify({"status": "Spotify Launched 🎵"})

@app.route('/command/open_camera', methods=['GET'])
def open_camera():
    os.system("adb shell am start -a android.media.action.IMAGE_CAPTURE")
    return jsonify({"status": "Camera Opened 📷"})

@app.route('/command/dial_number', methods=['GET'])
def dial_number():
    os.system('adb shell am start -a android.intent.action.DIAL -d tel:9999999999')
    return jsonify({"status": "Dialer Opened 📞"})

@app.route('/command/play_music', methods=['GET'])
def play_music():
    os.system('adb shell am start -a android.intent.action.VIEW -d file:///sdcard/Music/song.mp3 -t audio/mp3')
    return jsonify({"status": "Playing Music 🎶"})

@app.route('/command/open_search', methods=['GET'])
def open_search():
    os.system("adb shell am start -a android.intent.action.WEB_SEARCH --es query 'Hello from my PC'")
    return jsonify({"status": "Google Search Opened 🔍"})

@app.route('/command/screen_on', methods=['GET'])
def screen_on():
    os.system("adb shell input keyevent 26")  
    return jsonify({"status": "Screen ON (Wake) 🔓"})

@app.route('/command/screen_off', methods=['GET'])
def screen_off():
    os.system("adb shell input keyevent 26")  
    return jsonify({"status": "Screen OFF (Lock) 🔒"})

if __name__ == '__main__':
    app.run(debug=True)
