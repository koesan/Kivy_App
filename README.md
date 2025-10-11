<div align="center">

# Python Mobile App Development with Kivy

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Kivy](https://img.shields.io/badge/Kivy-2.x-brightgreen.svg)](https://kivy.org/)
[![TensorFlow Lite](https://img.shields.io/badge/TensorFlow%20Lite-2.x-orange.svg)](https://www.tensorflow.org/lite)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![Android](https://img.shields.io/badge/Platform-Android-3DDC84.svg)](https://www.android.com/)

![App Screenshots](https://github.com/user-attachments/assets/cc93701e-7b69-469b-bef6-65d2d975f8e2)

---

**[English](#english)** | **[Türkçe](#turkish)**

</div>

---

## <a name="english"></a>🇬🇧 English

# Python Mobile App Development with Kivy

The main purpose of this project is to show how to develop mobile applications with Python and explain the use of OpenCV and TensorFlow in this mobile application.

## Installation

### Installing Kivy (Ubuntu)
For detailed information: [Kivy Documentation](https://kivy.org/doc/stable/installation/installation-linux.html#ubuntu-11-10-or-newer)

```bash
sudo apt-get update

sudo apt-get install -y \
    python3-pip \
    python3
```

#### Installing Build Tools and Dependencies (including SDL2)
```bash
sudo apt-get -y install python3-dev build-essential git make autoconf automake libtool \
    pkg-config cmake ninja-build libasound2-dev libpulse-dev libaudio-dev \
    libjack-dev libsndio-dev libsamplerate0-dev libx11-dev libxext-dev \
    libxrandr-dev libxcursor-dev libxfixes-dev libxi-dev libxss-dev libwayland-dev \
    libxkbcommon-dev libdrm-dev libgbm-dev libgl1-mesa-dev libgles2-mesa-dev \
    libegl1-mesa-dev libdbus-1-dev libibus-1.0-dev libudev-dev fcitx-libs-dev
```

#### Add Kivy PPA and Install Kivy:
```bash
sudo add-apt-repository ppa:kivy-team/kivy

sudo apt-get update

sudo apt-get install python3-kivy
```

### Installing Cython
```bash
sudo apt-get install git libssl-dev cython3
```

> **Note**: If you get an error related to Cython, follow these steps:
> 
> ```bash
> cd /bin/ && sudo gedit cython
> ```
> Add this line to the opened file:
> ```
> cython3 $@
> ```
> Then:
> ```bash
> sudo chmod 755 cython
> cd ~
> ```

### Installing Buildozer

```bash
sudo git clone https://github.com/kivy/buildozer.git

sudo apt install -y git zip unzip default-jre default-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev

cd buildozer/

sudo python3 setup.py install
```

## APK Conversion

Enter your Python Kivy project and run the following command:

```bash
buildozer init
```

This command will create the `buildozer.spec` file. Add non-Python libraries (for example, TensorFlow or OpenCV) and file extensions like `.tflite` to this file so that these files are also included when the APK is created.

After making the necessary changes, you can start the APK conversion with this command:

```bash
buildozer --verbose android debug
```

When the process is completed without errors, the generated APK file will be located in the "bin" folder. You can transfer the APK file to your Android phone and then install it.

> **Note**: If the APK is successfully created but the application suddenly closes, does not open, or does not work at all after loading it on the phone, you can use the `adb` tool to solve these errors. This tool allows you to see the operations, codes, and errors performed while the application is running on the terminal screen when you connect the phone to the computer via USB.
>
> [Adb example video](https://www.youtube.com/watch?v=T3rOvpDzEOY&list=WL&index=50&t=717s)

### Installing ADB

```bash
sudo apt install adb
```
USB debugging must be enabled in the developer options on your phone.

### Error Tracking with ADB
Connect the phone to the computer via USB and run the following command:

```bash
adb logcat -s python
```

> **Note**: If you are using a virtual machine and `adb` does not detect your phone, turn off the virtual machine and try the `adb` command again.

You can monitor your application's steps on the terminal screen and view any errors here.

---

## <a name="turkish"></a>🇹🇷 Türkçe

# Python ile Kivy Mobil Uygulama Geliştirme

Bu projenin temel amacı, Python ile mobil uygulama geliştirmenin nasıl yapılacağını göstermek ve bu mobil uygulamada OpenCV ve TensorFlow kullanımını açıklamaktır.

## Kurulum

### Kivy'nin kurulması (Ubuntu)
Detaylı bilgi için: [Kivy Documentation](https://kivy.org/doc/stable/installation/installation-linux.html#ubuntu-11-10-or-newer)

```bash
sudo apt-get update

sudo apt-get install -y \
    python3-pip \
    python3
```

#### Build araçları ve bağımlılıkların kurulumu (SDL2 dahil)
```bash
sudo apt-get -y install python3-dev build-essential git make autoconf automake libtool \
    pkg-config cmake ninja-build libasound2-dev libpulse-dev libaudio-dev \
    libjack-dev libsndio-dev libsamplerate0-dev libx11-dev libxext-dev \
    libxrandr-dev libxcursor-dev libxfixes-dev libxi-dev libxss-dev libwayland-dev \
    libxkbcommon-dev libdrm-dev libgbm-dev libgl1-mesa-dev libgles2-mesa-dev \
    libegl1-mesa-dev libdbus-1-dev libibus-1.0-dev libudev-dev fcitx-libs-dev
```

#### Kivy PPA'sını ekleyin ve Kivy'yi yükleyin:
```bash
sudo add-apt-repository ppa:kivy-team/kivy

sudo apt-get update

sudo apt-get install python3-kivy
```

### Cython kurulumu
```bash
sudo apt-get install git libssl-dev cython3
```

> **Not**: Eğer Cython ile ilgili bir hata alırsanız, aşağıdaki adımları izleyin:
> 
> ```bash
> cd /bin/ && sudo gedit cython
> ```
> Açılan dosyaya şu satırı ekleyin:
> ```
> cython3 $@
> ```
> Ardından:
> ```bash
> sudo chmod 755 cython
> cd ~
> ```

### Buildozer Kurulumu

```bash
sudo git clone https://github.com/kivy/buildozer.git

sudo apt install -y git zip unzip default-jre default-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev

cd buildozer/

sudo python3 setup.py install
```

## APK Dönüşümü

Python Kivy projenizin içine girin ve aşağıdaki komutu çalıştırın:

```bash
buildozer init
```

Bu komut, `buildozer.spec` dosyasını oluşturacaktır. Python dışındaki kütüphaneleri (örneğin, TensorFlow veya OpenCV) ve `.tflite` gibi dosya uzantılarını bu dosyaya ekleyin ki APK oluşturulurken bu dosyalar da eklenmiş olsun.

Gerekli değişiklikleri yaptıktan sonra şu komut ile APK dönüşümüne başlayabilirsiniz:

```bash
buildozer --verbose android debug
```

İşlem hatasız bir şekilde tamamlandığında, oluşturulan APK dosyası "bin" klasörü içinde yer alacaktır. APK dosyasını Android telefonunuza aktarabilir ve ardından kurulumunu gerçekleştirebilirsiniz.

> **Not**: Eğer APK başarılı bir şekilde oluşturulmasına rağmen, telefona yükledikten sonra uygulama aniden kapanıyor, açılmıyor ya da hiç çalışmıyorsa, bu hataları çözmek için `adb` aracını kullanabilirsiniz. Bu araç, telefonu USB ile bilgisayara bağladığınızda, uygulamanın çalışma sırasında yapılan işlemleri, kodları ve hataları terminal ekranında görmenizi sağlar.
>
> [Adb örenk video](https://www.youtube.com/watch?v=T3rOvpDzEOY&list=WL&index=50&t=717s)

### ADB kurulumu

```bash
sudo apt install adb
```
Telefonunuzda geliştirici seçenekleri kısmında usb hata ayıklama açık olmalı.

### ADB ile hata takibi
Telefonu bilgisayara USB ile bağlayın ve aşağıdaki komutu çalıştırın:

```bash
adb logcat -s python
```

> **Not**: Eğer sanal makine kullanıyorsanız ve `adb` telefonunuzu algılamıyorsa, sanal makineyi kapatıp `adb` komutunu tekrar deneyin.

Uygulamanızın adımlarını terminal ekranında izleyebilir ve herhangi bir hata olduğunda burada görüntüleyebilirsiniz.
