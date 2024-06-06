# Tracker Setup and Usage Guide for Beginners and experts.

Welcome to the Tracker Setup and Usage Guide. This guide provides simple, step-by-step instructions for setting up and using the tracker on your Termux environment.

## Quick Start Guide

Follow these steps to set up the tracker:

1. **Update and Upgrade Termux Packages**:
    ```sh
    apt update
    apt upgrade
    ```

2. **Install Git**:
    ```sh
    pkg install git
    ```

3. **Clone the Firebase Deployment Scripts**:
    ```sh
    git clone https://github.com/UnlimitedJokarHacks/UniTrack-.git
    ```

4. **Navigate to the Scripts Directory**:
    ```sh
    cd UniTrack
    ```

5. **Install Node.js**:
    ```sh
    pkg install nodejs
    ```

6. **Install Dependencies**:
    ```sh
    npm install
    ```

7. **Install Python**:
    ```sh
    pkg install python
    ```

8. **Run Deployment Script**:
    ```sh
    ./deploy.sh
    ```

## Creating a Tracking Link

To create a tracking link, follow these steps:

1. **Run the Tracking Script**:
    ```sh
    python create_link.py
    ```
    This script will generate a unique tracking link.

2. **Distribute the Link**:
    Share the generated link with the target user. When they open the link, their location data will be captured.

## Viewing Tracked Locations

To view the tracked locations, use the following steps:

1. **Run the Viewing Script**:
    ```sh
    python view_locations.py
    ```

2. **Access the Locations**:
    The script will display the tracked locations. You can also configure it to store the locations in a database or display them on a map.

## Credits

This project is brought to you by **Jokar Hacks Tech**. 

For support, contact:
- [@jokar_hacks](https://t.me/jokar_hacks) on Telegram
- [@jokar_hack](https://t.me/jokar_hack) on Telegram

Join our channel on Telegram: [@jokarhacks](https://t.me/jokarhacks)

---

Thank you for using our tracker. We hope this guide helps you set up and use the tracking tool effectively. For any further assistance, feel free to reach out to us on Telegram.
