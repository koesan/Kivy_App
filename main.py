from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.utils import platform
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
import cv2
from model import TensorFlowModel
import os
import numpy as np
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA,Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    
class App(MDApp):

    def build(self):
        self.image = ""
        self.sonuc = ""
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        self.tahmin = 999

        screen = Screen()
        btn_folder = MDFloatingActionButton(icon="file-image", pos_hint={'center_x': 0.7, 'center_y': 0.1}, on_release=self.select_image)
        btn_camera = MDFloatingActionButton(icon="camera", pos_hint={'center_x': 0.3, 'center_y': 0.1}, on_release=self.capture_image)
        btn_analiz = MDFloatingActionButton(icon="select-search", pos_hint={'center_x': 0.5, 'center_y': 0.1}, on_release=self.process_image)

        screen.add_widget(btn_folder)
        screen.add_widget(btn_camera)
        screen.add_widget(btn_analiz)

        return screen

    def dialog_error(self):
        dialog = MDDialog(text="Resim yüklemediniz", size_hint=(0.8, 1),  buttons=[MDFlatButton(text='Kapat', on_release=lambda *args: dialog.dismiss())])
        dialog.open()
    
    def dialog_info(self):
    
        dialog = MDDialog(
            text=self.sonuc,
            size_hint=(0.8, 1),
            buttons=[
                MDFlatButton(text='Kapat', on_release=lambda *args: dialog.dismiss()), 
            ]
        )
        dialog.open()

    def select_image(self, obj):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE])
        from kivy.uix.filechooser import FileChooserIconView
        
        file_chooser = FileChooserIconView(path="/storage/emulated/0/")
        popup = Popup(title='Resim seç', content=file_chooser, size_hint=(0.9, 0.9))
        file_chooser.bind(on_submit=self.on_submit)
        popup.open()
    
    def on_submit(self, instance, selection, touch):
        self.image = instance.selection[0]
        instance.parent.parent.parent.dismiss()

    def capture_image(self, obj):
        camera = Camera(play=True)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(camera)

        popup = Popup(title='Capture Image', content=layout, size_hint=(0.9, 0.9))
        camera.bind(on_touch_down=lambda *args: self.capture(camera, popup))
        popup.open()

    def capture(self, camera, popup):
        camera.export_to_png("capture.png")
        self.image = "capture.png"
        popup.dismiss()

    def process_image(self, obj):
        if self.image != "":
            # Görüntüyü yükle
            img = cv2.imread(self.image)
            model = TensorFlowModel()
            model.load(os.path.join(os.getcwd(), 'model.tflite'))

            # Giriş görüntüsünü işleme
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.resize(img, (32, 32))
            img = img / 255.
            img = img.astype(np.float32)
            img = np.asarray(img)
            img = img.reshape(1, 32, 32, 1)

            output_data = model.pred(img)
            classa = np.argmax(output_data)
            probabilityValue = np.amax(output_data)
            
            traffic_signs = {
            0: "Speed limit (20km/h)",
            1: "Speed limit (30km/h)",
            2: "Speed limit (50km/h)",
            3: "Speed limit (60km/h)",
            4: "Speed limit (70km/h)",
            5: "Speed limit (80km/h)",
            6: "End of speed limit (80km/h)",
            7: "Speed limit (100km/h)",
            8: "Speed limit (120km/h)",
            9: "No passing",
            10: "No passing for vehicles over 3.5 metric tons",
            11: "Right-of-way at the next intersection",
            12: "Priority road",
            13: "Yield",
            14: "Stop",
            15: "No vehicles",
            16: "Vehicles over 3.5 metric tons prohibited",
            17: "No entry",
            18: "General caution",
            19: "Dangerous curve to the left",
            20: "Dangerous curve to the right",
            21: "Double curve",
            22: "Bumpy road",
            23: "Slippery road",
            24: "Road narrows on the right",
            25: "Road work",
            26: "Traffic signals",
            27: "Pedestrians",
            28: "Children crossing",
            29: "Bicycles crossing",
            30: "Beware of ice/snow",
            31: "Wild animals crossing",
            32: "End of all speed and passing limits",
            33: "Turn right ahead",
            34: "Turn left ahead",
            35: "Ahead only",
            36: "Go straight or right",
            37: "Go straight or left",
            38: "Keep right",
            39: "Keep left",
            40: "Roundabout mandatory",
            41: "End of no passing",
            42: "End of no passing by vehicles over 3.5 metric tons"
            }

            self.sonuc  = f"isim: {traffic_signs[classa]} doğruluk: {probabilityValue}"
            self.tahmin = classa
            self.dialog_info()
        else:
            self.dialog_error()

App().run()

