
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

***

| Uygulama Resimleri                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------- |
| ![Merged_document (1)](https://github.com/user-attachments/assets/cc93701e-7b69-469b-bef6-65d2d975f8e2) | 


