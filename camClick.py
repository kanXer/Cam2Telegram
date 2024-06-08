import cv2
import asyncio
from telegram import Bot

# Set your Telegram Bot token
# 6406984942:AAGj3xzbZbe2Hqb9SBupEoRUtZQF54FZSqc
TELEGRAM_BOT_TOKEN = '6406984942:AAGj3xzbZbe2Hqb9SBupEoRUtZQF54FZSqc'
# Set your chat ID (you can get it by messaging the bot and checking the updates API)
TELEGRAM_CHAT_ID = '6178776536'

# Initialize the Telegram Bot
# Initialize the Telegram Bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Initialize the camera
cap = cv2.VideoCapture(0)

async def send_photo():
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection (you might need to fine-tune parameters)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If faces are detected, send a notification
    if len(faces) > 0:
        message = "Someone is in front of the camera!"
# Optionally, you can send a photo from the camera
        _, img_encoded = cv2.imencode('.jpg', frame)
        await bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=img_encoded.tobytes(), caption=message)

# Main event loop
async def main():
    while True:
        await send_photo()
        await asyncio.sleep(1)

# Run the event loop
if __name__ == '__main__':
    asyncio.run(main())
    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()