import customtkinter as ctk
import tkinter as tk

# DarkModernBlue
# Global Theme Colors 
THEME_BG_COLOR      = "#1c1d27"  # Background
FRAME_FG_COLOR      = "#242731"  # Frame bg
ENTRY_BG_COLOR      = "#2A2B2E"  # Entry bg
BUTTON_FG_COLOR     = "#3B3F58"  # Button color
BUTTON_HOVER_COLOR  = "#4B4F68"  # Button hover
LABEL_TEXT_COLOR    = "#FFFFFF"  # Label text
PLACEHOLDER_COLOR   = "#AAAAAA"  # Placeholder text
BORDER_COLOR        = "#666666"  # Entry border
PROGRESS_BG_COLOR   = "#2A2B2E"  # Progress bg
PROGRESS_COLOR      = "#3B3F58"  # Progress bar
SLIDER_FG_COLOR     = "#4B4F68"  # Slider track
SLIDER_PROGRESS     = "#7e829d"  # Slider progress

# Custom segmented control
class CustomSegmentedRadio(ctk.CTkSegmentedButton):
    def __init__(self, master, values, default_value=None, command=None, **kwargs):
        super().__init__(master, values=values, command=command, **kwargs)
        if default_value:
            self.set(default_value)

# Custom radio button using a Canvas
class CustomRadioButton(ctk.CTkFrame):
    def __init__(self, master, text, variable, value, circle_size=10, margin=4, outline_width=2, **kwargs):
        kwargs.setdefault("fg_color", FRAME_FG_COLOR)
        super().__init__(master, **kwargs)
        self.variable = variable
        self.value = value
        self.circle_size = circle_size
        self.margin = margin
        self.outline_width = outline_width
        self.selected_color = BUTTON_FG_COLOR
        self.unselected_color = BORDER_COLOR

        canvas_size = circle_size * 2 + margin * 2
        self.canvas = tk.Canvas(self, width=canvas_size, height=canvas_size,
                                highlightthickness=0, bd=0, bg=self.cget("fg_color"))
        self.canvas.pack(side="left", padx=(0, 10))
        self.label = ctk.CTkLabel(self, text=text, text_color=LABEL_TEXT_COLOR, font=("Aptos", 14))
        self.label.pack(side="left")
        self.canvas.bind("<Button-1>", self.on_click)
        self.label.bind("<Button-1>", self.on_click)
        self.bind("<Button-1>", self.on_click)
        self.draw_circle()
        self.variable.trace_add("write", lambda *args: self.draw_circle())

    def draw_circle(self):
        self.canvas.delete("all")
        offset = self.outline_width / 2
        fill = self.selected_color if self.variable.get() == self.value else ""
        self.canvas.create_oval(self.margin + offset, self.margin + offset,
                                self.margin + 2 * self.circle_size - offset, self.margin + 2 * self.circle_size - offset,
                                outline=self.unselected_color, fill=fill, width=self.outline_width)

    def on_click(self, event):
        self.variable.set(self.value)


# Main Application
class DesignShowcase(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("DarkModernBlue")
        self.geometry("600x800")
        self.configure(bg=THEME_BG_COLOR)
        main_frame = ctk.CTkScrollableFrame(self, fg_color=FRAME_FG_COLOR, corner_radius=20)
        main_frame.pack(pady=20, padx=25, fill="both", expand=True)
        main_frame.grid_columnconfigure(0, weight=1)

        header_label = ctk.CTkLabel(main_frame, text="Dark Modern Blue", font=("Inter", 36, "bold"), text_color=LABEL_TEXT_COLOR)
        header_label.grid(row=0, column=0, pady=(20, 10), sticky="n")

        # Username and Password --------------------------------------------------------------------------------------------------------
        username_entry = ctk.CTkEntry(main_frame, placeholder_text="Username", corner_radius=20,
                                      fg_color=ENTRY_BG_COLOR, text_color=LABEL_TEXT_COLOR,
                                      placeholder_text_color=PLACEHOLDER_COLOR, border_width=1, border_color=BORDER_COLOR,
                                      width=400, height=40)
        username_entry.grid(row=1, column=0, pady=(10, 5))
        password_entry = ctk.CTkEntry(main_frame, placeholder_text="Password", corner_radius=20,
                                      fg_color=ENTRY_BG_COLOR, text_color=LABEL_TEXT_COLOR,
                                      placeholder_text_color=PLACEHOLDER_COLOR, border_width=1, border_color=BORDER_COLOR,
                                      show="*", width=400, height=40)
        password_entry.grid(row=2, column=0, pady=(5, 10))

        login_button = ctk.CTkButton(main_frame, text="Login", corner_radius=25, height=30, width=150,
                                     fg_color=BUTTON_FG_COLOR, text_color=LABEL_TEXT_COLOR,
                                     hover_color=BUTTON_HOVER_COLOR, border_width=0, command=self.on_login_click)
        login_button.grid(row=3, column=0, pady=(5, 10))

        forgot_password_label = ctk.CTkLabel(main_frame, text="Forgot password?", font=("Aptos", 12),
                                             text_color=PLACEHOLDER_COLOR, cursor="hand2")
        forgot_password_label.grid(row=4, column=0, pady=(0, 20))
        forgot_password_label.bind("<Button-1>", self.on_forgot_password_click)

        # Textbox with Scrollbar --------------------------------------------------------------------------------------------------------
        textbox_label = ctk.CTkLabel(main_frame, text="Textbox with Scrollbar:", text_color=LABEL_TEXT_COLOR, font=("Aptos", 14))
        textbox_label.grid(row=5, column=0, pady=(10, 5))
        text_area = ctk.CTkTextbox(main_frame, height=100, width=300, fg_color=ENTRY_BG_COLOR, border_color=BORDER_COLOR, border_width=1)
        text_area.grid(row=6, column=0, pady=5)

        # Segmented Control -------------------------------------------------------------------------------------------------------------
        seg_label = ctk.CTkLabel(main_frame, text="Segmented Control:", text_color=LABEL_TEXT_COLOR, font=("Aptos", 14))
        seg_label.grid(row=7, column=0, pady=(20, 5))
        self.segmented_radio = CustomSegmentedRadio(main_frame, values=["Option 1", "Option 2", "Option 3"],
                                                     default_value="Option 1", command=self.on_segment_change,
                                                     width=300, font=("Aptos", 14),
                                                     corner_radius=20)
        self.segmented_radio.grid(row=8, column=0, pady=(5, 20))
        
        # Custom Radio Buttons -----------------------------------------------------------------------------------------------------------
        radio_group_label = ctk.CTkLabel(main_frame, text="Custom Radio Buttons:", text_color=LABEL_TEXT_COLOR, font=("Aptos", 14))
        radio_group_label.grid(row=9, column=0, pady=(20, 5))
        self.radio_var = tk.StringVar(value="Option 1")
        radio1 = CustomRadioButton(main_frame, text="Option 1", variable=self.radio_var, value="Option 1",
                                   circle_size=8, margin=4, outline_width=2, fg_color="#242731")
        radio1.grid(row=10, column=0, pady=(5, 5))
        radio2 = CustomRadioButton(main_frame, text="Option 2", variable=self.radio_var, value="Option 2",
                                   circle_size=8, margin=4, outline_width=2, fg_color="#242731")
        radio2.grid(row=11, column=0, pady=(5, 20))

        self.radio_var.trace_add("write", self.on_radio_change)

        # Dropdown Menu ------------------------------------------------------------------------------------------------------------------
        dropdown_label = ctk.CTkLabel(main_frame, text="Dropdown:", text_color=LABEL_TEXT_COLOR, font=("Aptos", 14))
        dropdown_label.grid(row=12, column=0, pady=(10, 5))
        dropdown = ctk.CTkOptionMenu(main_frame, values=["Option 1", "Option 2", "Option 3"],
                             corner_radius=10, fg_color=ENTRY_BG_COLOR, button_color=BUTTON_FG_COLOR,
                             text_color=LABEL_TEXT_COLOR, dropdown_fg_color=ENTRY_BG_COLOR,
                             command=self.on_dropdown_change)
        dropdown.grid(row=13, column=0, pady=(5, 20))


        # Slider --------------------------------------------------------------------------------------------------------------------------
        slider_label = ctk.CTkLabel(main_frame, text="Volume:", text_color=LABEL_TEXT_COLOR, font=("Aptos", 14))
        slider_label.grid(row=14, column=0, pady=(10, 5))
        volume_slider = ctk.CTkSlider(main_frame, from_=0, to=100, number_of_steps=100,
                                    fg_color=SLIDER_FG_COLOR, progress_color=SLIDER_PROGRESS,
                                    command=self.on_volume_change)
        volume_slider.set(50)
        volume_slider.grid(row=15, column=0, pady=(5, 20), ipadx=100)

        # Progress Bar --------------------------------------------------------------------------------------------------------------------
        progress_label = ctk.CTkLabel(main_frame, text="Progress Bar:", text_color=LABEL_TEXT_COLOR, font=("Aptos", 14))
        progress_label.grid(row=16, column=0, pady=(10, 5))
        progressbar = ctk.CTkProgressBar(main_frame, width=400, fg_color=PROGRESS_BG_COLOR, progress_color=PROGRESS_COLOR)
        progressbar.grid(row=17, column=0, pady=(5, 20))
        progressbar.set(0.5)


    # Callbacks
    def on_login_click(self):
        print("This is the Login button")

    def on_forgot_password_click(self, event):
        print("Forgot password clicked")

    def on_segment_change(self, value):
        print("Segmented control changed to:", value)
        
    def on_radio_change(self, *args):
        print("Radio button selected:", self.radio_var.get())
        
    def on_dropdown_change(self, value):
        print("Dropdown selected:", value)
    
    def on_volume_change(self, value):
        print("Volume set to:", value)
        
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = DesignShowcase()
    app.mainloop()
