from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

import os
import threading

class SimpleAIApp(App):
    def __init__(self):
        super().__init__()
        self.llm = None
        self.model_loaded = False
        
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        title = Label(
            text='🤖 AI Voice Chat',
            size_hint=(1, 0.2),
            font_size='24sp',
            bold=True
        )
        
        self.status_label = Label(
            text='Ready to load AI model',
            size_hint=(1, 0.2),
            font_size='16sp'
        )
        
        instructions = Label(
            text='1. Place model in: Download/models/\n2. Tap LOAD MODEL\n3. Chat with AI',
            size_hint=(1, 0.3),
            font_size='14sp'
        )
        
        load_btn = Button(
            text='LOAD MODEL',
            size_hint=(1, 0.15),
            background_color=(0.2, 0.8, 0.2, 1)
        )
        load_btn.bind(on_press=self.load_model)
        
        chat_btn = Button(
            text='🎤 CHAT',
            size_hint=(1, 0.15),
            background_color=(0.2, 0.6, 1, 1)
        )
        chat_btn.bind(on_press=self.show_chat)
        
        layout.add_widget(title)
        layout.add_widget(instructions)
        layout.add_widget(self.status_label)
        layout.add_widget(load_btn)
        layout.add_widget(chat_btn)
        
        return layout
    
    def load_model(self, instance):
        def load_thread():
            try:
                Clock.schedule_once(lambda dt: self.update_status("🔄 Loading AI model..."))
                
                # Model paths to check
                model_paths = [
                    "/sdcard/Download/models/qwen2.5-1.5b-instruct-q5_k_m.gguf",
                    "/storage/emulated/0/Download/models/qwen2.5-1.5b-instruct-q5_k_m.gguf",
                ]
                
                model_path = None
                for path in model_paths:
                    if os.path.exists(path):
                        model_path = path
                        break
                
                if not model_path:
                    Clock.schedule_once(lambda dt: self.update_status("❌ Model not found in Download/models/"))
                    return
                
                # Load the model
                from llama_cpp import Llama
                self.llm = Llama(model_path=model_path, n_ctx=1024, n_threads=2)
                self.model_loaded = True
                
                Clock.schedule_once(lambda dt: self.update_status("✅ AI Model Loaded!"))
                
            except Exception as e:
                Clock.schedule_once(lambda dt: self.update_status(f"❌ Error: {str(e)}"))
        
        threading.Thread(target=load_thread, daemon=True).start()
    
    def show_chat(self, instance):
        from kivy.uix.textinput import TextInput
        from kivy.uix.popup import Popup
        
        if not self.model_loaded:
            self.update_status("❌ Please load model first")
            return
            
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        text_input = TextInput(hint_text='Type your message...', size_hint=(1, 0.7))
        
        def send(btn):
            text = text_input.text.strip()
            if text:
                self.chat_with_ai(text)
                popup.dismiss()
        
        send_btn = Button(text='SEND', size_hint=(1, 0.3))
        send_btn.bind(on_press=send)
        
        layout.add_widget(text_input)
        layout.add_widget(send_btn)
        
        popup = Popup(title='Chat with AI', content=layout, size_hint=(0.8, 0.4))
        popup.open()
    
    def chat_with_ai(self, user_input):
        def chat_thread():
            try:
                Clock.schedule_once(lambda dt: self.update_status("🤔 AI is thinking..."))
                
                prompt = f"User: {user_input}\nAssistant:"
                response = self.llm(prompt, max_tokens=100, temperature=0.7)
                ai_text = response['choices'][0]['text'].strip()
                
                Clock.schedule_once(lambda dt: self.update_status(f"✅ AI: {ai_text}"))
                
            except Exception as e:
                Clock.schedule_once(lambda dt: self.update_status(f"❌ Chat error: {str(e)}"))
        
        threading.Thread(target=chat_thread, daemon=True).start()
    
    def update_status(self, message):
        self.status_label.text = message

if __name__ == '__main__':
    SimpleAIApp().run()
