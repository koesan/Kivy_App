# Python'da Kivy ile mobil uygulama

Bu projenin temel amacı, Python ile mobil uygulama geliştirmenin nasıl yapılacağını göstermek ve bu mobil uygulamada OpenCV ve TensorFlow kullanımını açıklamaktır.



# Kurulum

# kivy'nin kurulması (Ubuntu)

https://kivy.org/doc/stable/installation/installation-linux.html#ubuntu-11-10-or-newer

sudo apt-get update

sudo apt-get install -y \
    python3-pip \
    python3

sudo apt-get update

# Install build tools, and dependencies to perform a full build (including SDL2 dependencies)
sudo apt-get -y install python3-dev build-essential git make autoconf automake libtool \
      pkg-config cmake ninja-build libasound2-dev libpulse-dev libaudio-dev \
      libjack-dev libsndio-dev libsamplerate0-dev libx11-dev libxext-dev \
      libxrandr-dev libxcursor-dev libxfixes-dev libxi-dev libxss-dev libwayland-dev \
      libxkbcommon-dev libdrm-dev libgbm-dev libgl1-mesa-dev libgles2-mesa-dev \
      libegl1-mesa-dev libdbus-1-dev libibus-1.0-dev libudev-dev fcitx-libs-dev

sudo add-apt-repository ppa:kivy-team/kivy

sudo apt-get update

sudo apt-get install python3-kivy

# Cython kurulumu

 sudo apt-get install git libssl-dev cython3

not: Cython hata verirse

 cd /bin/ && sudo gedit cython

 açılan metin belgesine " cython3 $@ " yaz ve kaydet kapat

 sudo chmod 755 cython

 cd ~

 # Buildozer kurulumu

 sudo git clone https://github.com/kivy/buildozer.git

 sudo apt install -y git zip unzip default-jre default-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev

cd ..

cd buildozer/

sudo python3 setup.py install

# Apk dönüşüm

Python kivy proje dosyanın içine gir ve aşağıdaki kodu çalıştır.

buildozer init

çalıştırdığın kod buildozer.spec dosyası oluşturacak. yapman gereken değişiklikleri (pythonla gelen kütüphane dışındaki kütüphaneleri eklemelisin, ".tflite" gibi dosya uzantılarını eklemelisin ki uygulama bu dosyaları apk ya eklesin vb...)

gereken değişiklikleri yaptıktan sonra aşağıdaki kod ile apk dönüşüm işlemini başlat.

 buildozer --verbose android debug 

not: uygulamayı başarılı bir şekilde apk ya dönüştü. ama bu apk yı telefona yükeldikten sonra, aniden kapanıyorsa, açılmıyorsa, yada işlem başlamıyorsa. bunun gibi hataları çzömek için adb aracını kullana bilrisin bu araç telefonu usb aracılığı ile bilgisayara bğladığında çalıştırdığın uygulamaların çalışma sırasında yapılan işlemleri, kodları, ve hataları terminal ekranında görmeni sağlar. 

# adb kurulumu

sudo apt install adb 
 
# adb çalıştırma

adb logcat -s python

Çalıştırmadan önce kablo ile telefonu bilgisayar bağlayın. sanal makine açıksa bilgisayarınızda adb telefonunuzu algılamıyorsa sanal makineyi kapatıp adb yi tekrar başlatın
