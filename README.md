# 📷 GraybyteShotnUp 🦾🗿🦾

**GraybyteShotnUp** is an easy-to-use tool for taking screenshots, drawing on them, and uploading them online. It works on Linux and uses **two APIs**—**Imgur** and **Gyazo**—to make sure your uploads always work. If one API is blocked or down, the other takes over.

## 🔥 Features

* **Two APIs for Reliability**:
  * Uploads to Imgur or Gyazo.
  * If Imgur fails, Gyazo works, so you’re never stuck.
* **Screenshot Tool**:
  * Capture any part of your screen.
* **System Tray**:
  * Quick access from your taskbar.
* **Notifications**:
  * Shows the upload link and speed.

## 🤔 What You Need

* **Python 3.6+**
* **Tools**:
* * **scrot** (for Linux screenshots):
* On Ubuntu:


## 💳 Getting API Keys

You need keys for Imgur and Gyazo to upload screenshots. Here’s how to get them:

### Imgur Key

1. **Sign Up**:
* Go to [Imgur API](https://api.imgur.com/oauth2/addclient).
* Log in to Imgur.
* Click **"Add a new application"**.
* Fill in:
  * Name: GraybyteShotnUp
  * Authorization: Anonymous usage
  * Callback URL: `http://localhost` (or leave blank)
  * Email: Your email
  * Description: Screenshot tool
* Click Submit.

2. **Copy Key**:
* Imgur gives you a **Client-ID** (like `a1b2c3d4e5f6g7h`).
* Keep it safe.

### Gyazo Key

1. **Sign Up**:
* Go to [Gyazo API](https://gyazo.com/api).
* Log in to Gyazo.
* Click **"Applications"** > **"Create a new application"**.
* Fill in:
  * Name: GraybyteShotnUp
  * Redirect URL: `http://localhost` (or leave blank)
  * Description: Screenshot tool
* Click Submit.

2. **Copy Key**:
* Gyazo gives you an **Access Token** (like `x9y8z7w6v5u4t3s2r1q0`).
* Keep it safe.

## 🔥⃤ Setting Up Keys

1. **Start the Tool**:


2. **Add Keys**:
* Click **"Set API Keys"** in the toolbar or menu.
* Enter **Imgur Client-ID** in the first box.
* Enter **Gyazo Access Token** in the second box.
* Keys are saved in `config-log/config.ini`.

3. **Choose APIs**:
* Check **"Use Imgur"** and **"Use Gyazo"** to use both (recommended).
* Uncheck one if you want to use only the other.

## 🗿 How to Use

1. **Take a Screenshot**:
* Click **"Capture"** or click the tray icon.
* Drag to select part of the screen.
* The screenshot shows up in the tool.

2. **Draw on It**:
* Pick a tool (Line, Circle, Arrow, Text, etc.) from the dropdown.
* Draw on the screenshot.
* Click **"Clear"** to start over.

3. **Upload It**:
* Click **"Upload"**.
* The tool tries Imgur first, then Gyazo if Imgur doesn’t work.
* You’ll see a notification with the link and upload speed.
* The link is copied to your clipboard.
* Click **"Open URL"** to see the image online.

4. **Save It**:
* Click **"Save"** to save the screenshot and open it.

5. **Tray Menu**:
* Right-click the tray icon for Capture, Open, Set API Keys, or Quit.

## Why Two APIs?

* **Always Works**: If Imgur is blocked or down, Gyazo saves the day.
* **Your Choice**: Turn on/off either API.
* **Fast**: Shows how quick the upload is.

## 🚨 Troubleshooting

* **"scrot not installed"**:
* Install `scrot` (see What You Need).
* **"Icon load failed"**:
* Check the `icons` folder has all files.
* **"Upload failed"**:
* Check your API keys in **"Set API Keys"**.
* **"Can’t copy URL"**:
* Install `xclip` (Linux):


# 📨 FOR MORE INFORMATION AND SUPPORT . ₊˚ ☎︎₊˚✧ ﾟ.

[TELEGRAM](https://t.me/rex_cc) | 
[FACEBOOK](https://www.facebook.com/graybyt3) | 
[X](https://x.com/gray_byte) | 
[INSTAGRAM](https://www.instagram.com/gray_byte)
