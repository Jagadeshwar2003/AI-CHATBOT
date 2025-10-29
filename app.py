from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai, os
from google.genai import Client

# Load environment variables
load_dotenv()
app = Flask(__name__)

# Get your key from .env file
openai.api_key = os.getenv("GEMINI_API_KEY")

client = Client(api_key=os.getenv("GEMINI_API_KEY"))
@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json["message"]
        print("💬 User said:", user_message)
        response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_message
        )
        bot_reply = response.text
        print("🤖 Bot replied:", bot_reply)

        return jsonify({"reply": bot_reply})
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"reply": "Sorry, something went wrong on the server."})
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True,host="localhost")

