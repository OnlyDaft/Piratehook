import requests
import os
import time
import threading

spammer_running = False
stop_spamming = False

def spam(webhook_url, message, num_spams):
    global spammer_running, stop_spamming
    spammer_running = True
    print("Spamming webhook...")
    for i in range(num_spams):
        if stop_spamming:
            break
        payload = {"content": message}
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print(f"Spam {i+1} sent successfully")
        else:
            print(f"Error sending spam {i+1}: {response.status_code}")
    spammer_running = False
    stop_spamming = False
    print("Webhook spammed successfully! Going back to menu...")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("Menu:")
    print("1. Spam the webhook")
    print("2. Delete the webhook")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Enter the webhook URL:")
        webhook_url = input()
        if not webhook_url.startswith("https://discord.com/api/webhooks/"):
            print("Invalid webhook! Going back to menu...")
            time.sleep(3)  # Wait for 3 seconds
            continue  # Return to the menu
        else:
            print("Enter the message to spam:")
            message = input()
            print("Enter the number of times to send the message:")
            num_spams = int(input())

            stop_spamming = False
            threading.Thread(target=spam, args=(webhook_url, message, num_spams)).start()
            while spammer_running:
                print("Spamming webhook...")
                time.sleep(1)

    elif choice == "2":
        print("Enter the webhook URL to delete:")
        webhook_url = input()
        if not webhook_url.startswith("https://discord.com/api/webhooks/"):
            print("Invalid webhook! Going back to menu...")
            time.sleep(3)  # Wait for 3 seconds
            continue  # Return to the menu
        else:
            headers = {"Authorization": "Bot <your_bot_token>"}
            response = requests.delete(webhook_url, headers=headers)
            if response.status_code == 204:
                print("Webhook deleted successfully")
            else:
                print(f"Error deleting webhook: {response.status_code}")
            print("Going back to menu...")
            time.sleep(3)  # Wait for 3 seconds
    else:
        print("Invalid choice. Please try again.")
        time.sleep(3)  # Wait for 3 seconds