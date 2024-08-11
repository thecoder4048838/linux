import os
import subprocess
import shutil

# User configuration
username = "user"  # Username for the new user
password = "root"  # Password for the new user

# Creating a new user and setting up the environment
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

# Pin and Autostart settings
Pin = 123456  # PIN for Chrome Remote Desktop
Autostart = True  # Whether to set up the script to start automatically

class CRDSetup:
    def __init__(self, user):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.changewall()
        self.installGoogleChrome()
        self.installTelegram()
        self.installQbit()
        self.finish(user)

    @staticmethod
    def installCRD():
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("Chrome Remote Desktop Installed!")

    @staticmethod
    def installDesktopEnvironment():
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("systemctl disable lightdm.service")
        print("XFCE4 Desktop Environment Installed!")

    @staticmethod
    def installGoogleChrome():
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"])
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("Google Chrome Installed!")

    @staticmethod
    def installTelegram():
        subprocess.run(["apt", "install", "--assume-yes", "telegram-desktop"])
        print("Telegram Installed!")

    @staticmethod
    def changewall():
        os.system(f"curl -s -L -k -o xfce-verticals.png https://gitlab.com/chamod12/changewallpaper-win10/-/raw/main/CachedImage_1024_768_POS4.jpg")
        current_directory = os.getcwd()
        custom_wallpaper_path = os.path.join(current_directory, "xfce-verticals.png")
        destination_path = '/usr/share/backgrounds/xfce/'
        shutil.copy(custom_wallpaper_path, destination_path)
        print("Wallpaper Changed!")

    @staticmethod
    def installQbit():
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "qbittorrent"])
        print("Qbittorrent Installed!")

    @staticmethod
    def finish(user):
        if Autostart:
            os.makedirs(f"/home/{user}/.config/autostart", exist_ok=True)
            link = "www.youtube.com/@The_Disala"
            colab_autostart = """[Desktop Entry]
Type=Application
Name=Colab
Exec=sh -c "sensible-browser {}"
Icon=
Comment=Open a predefined notebook at session signin.
X-GNOME-Autostart-enabled=true""".format(link)
            with open(f"/home/{user}/.config/autostart/colab.desktop", "w") as f:
                f.write(colab_autostart)
            os.system(f"chmod +x /home/{user}/.config/autostart/colab.desktop")
            os.system(f"chown {user}:{user} /home/{user}/.config")

        # Add the user to the chrome-remote-desktop group
        os.system(f"adduser {user} chrome-remote-desktop")

        # Hardcoded CRD SSH Code with other parameters to start the CRD service
        command = 'DISPLAY= /opt/google/chrome-remote-desktop/start-host --code="4/0AcvDMrDhvu73SHR1FMS14T17teopoEmZXXmYAQFwuu_FpTKScoI88DVK7tOY7IFr0cr53Q" --redirect-url="https://remotedesktop.google.com/_/oauthredirect" --name=$(hostname) --pin={}'.format(Pin)
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-remote-desktop start")

        print("..........................................................")
        print(".....Brought By The Disala................................")
        print("..........................................................")
        print("......#####...######...####....####...##.......####.......")
        print("......##..##....##....##......##..##..##......##..##......")
        print("......##..##....##.....####...######..##......######......")
        print("......##..##....##........##..##..##..##......##..##......")
        print("......#####...######...####...##..##..######..##..##......")
        print("..........................................................")
        print("..Youtube Video Tutorial - https://youtu.be/xqpCQCJXKxU ..")
        print("..........................................................")
        print(f"Log in PIN: {Pin}")
        print(f"User Name: {user}")
        print(f"User Pass: {password}")
        while True:
            pass

try:
    CRDSetup(username)
except NameError as e:
    print("'username' variable not found. Create a user first")
