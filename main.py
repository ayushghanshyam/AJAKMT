from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.uix.image import AsyncImage
import webbrowser
from kivy.uix.modalview import ModalView
from kivymd.uix.button import MDFillRoundFlatIconButton  
from kivymd.uix.pickers import MDDatePicker
from kivy.metrics import dp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.floatlayout import FloatLayout,MDFloatLayout
import json
from kivymd.uix.label import MDLabel
from bs4 import BeautifulSoup
import os
from kivy.core.clipboard import Clipboard
import requests
from kivymd.uix.button import MDIconButton
from kivymd.toast import toast
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.bottomnavigation import MDBottomNavigationItem,MDBottomNavigation
class CustomMDInputField(MDTextField):
    def __init__(self, **kwargs):
        super(CustomMDInputField, self).__init__(**kwargs)
        self.bind(on_text_validate=self.on_enter)
    def on_enter(self, instance):
        if phone_input.text == '':
            phone_input.text = '91XXXXXXXX'
        if not 'ji' in name_input.text.lower():
            name_input.text+=' Ji'
        if name_input.text == '' or payment_input.text == '':
            toast('fill requirements')
        else:
            t1.add_row([str(len(t1.row_data) + 1), name_input.text, payment_input.text, phone_input.text])
        name_input.text = ''
        payment_input.text = ''
        phone_input.text = ''
class AJAKKMT(MDApp):
    dialog = None
    date_picker = None
    selected_date = None
    used_del=False
    used_del_2=False
    def build(self):
        self.picked=False
        global tb,t2,name_t2,pay_t2,sp_nm,bkwidget
        layout=FloatLayout()
        homewidget=MDBoxLayout(orientation='vertical', size_hint=(1, 1), height='800dp')
        settingwidget=FloatLayout(size_hint=(1, 1), height='800dp')
        tb=MDBottomNavigation(panel_color= (1, 1, 1, 1))
        home=MDBottomNavigationItem(name= 'home',text= 'Home',icon= 'home')
        st=MDBottomNavigationItem(name='settings',text='Settings',icon='cog')
        sl=MDBottomNavigationItem(name='purchase',text='Purchase',icon='currency-usd')
        slwidget=MDBoxLayout(orientation='vertical',size_hint=(1,1))
        sl.add_widget(slwidget)
        t2=MDDataTable(column_data=[('Id', dp(30)), ('Product Name', dp(50)), ('PayMent', dp(60)), ('Shop Name', dp(60))], check=True,rows_num=999)
        slwidget.add_widget(t2)
        tools_for_t2=MDBoxLayout(orientation='horizontal', size_hint=(1, None), height=dp(48))
        clear_t2=MDIconButton(icon='eraser')
        clear_t2.on_press=self.clear_fun_t2
        load_t2=MDIconButton(icon='arrow-up')
        load_t2.on_press=self.load_t2_func
        sv_img_t2=MDIconButton(icon='image')
        sv_img_t2.on_press=self.sv_img_t2_func
        edit_t2=MDIconButton(icon='pencil')
        edit_t2.on_press=self.edit_func_t2
        del_btn_t2=MDIconButton(icon='delete')
        del_btn_t2.on_press=self.delete_func_t2
        r_link_t2=MDIconButton(icon='link')
        r_link_t2.on_press=self.r_link_t2_func
        tools_for_t2.add_widget(clear_t2)
        tools_for_t2.add_widget(load_t2)
        tools_for_t2.add_widget(sv_img_t2)
        tools_for_t2.add_widget(edit_t2)
        tools_for_t2.add_widget(del_btn_t2)
        tools_for_t2.add_widget(r_link_t2)
        h_link_2=MDIconButton(icon='database-edit')
        h_link_2.on_press=self.h_link_func_2
        tools_for_t2.add_widget(h_link_2)
        slwidget.add_widget(tools_for_t2)
        input_layout_t2=MDBoxLayout(orientation='horizontal', size_hint=(1, None), height=dp(48))
        name_t2=MDTextField(hint_text='Product_Name',mode='rectangle')
        pay_t2=MDTextField(hint_text='PayMent',mode='rectangle')
        sp_nm=MDTextField(hint_text='Shop_Name',mode='rectangle')
        ld_to_t2=MDIconButton(icon='arrow-up')
        ld_to_t2.on_press=self.ld_t2_func
        input_layout_t2.add_widget(name_t2)
        input_layout_t2.add_widget(pay_t2)
        input_layout_t2.add_widget(sp_nm)
        input_layout_t2.add_widget(ld_to_t2)
        slwidget.add_widget(input_layout_t2)
        bk=MDBottomNavigationItem(name='gallery',text='Gallery',icon='book')
        bkwidget=MDBoxLayout(orientation='vertical')
        bk.add_widget(bkwidget)
        self.image_scroll_view = ScrollView(do_scroll_x=False, do_scroll_y=True, bar_color=(0, 0.8, 0, 1))
        self.image_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(10),
            size_hint_y=None,
            height=dp(900)
        )
        self.image_scroll_view.add_widget(self.image_layout)
        bkwidget.add_widget(self.image_scroll_view)
        load_button = MDRaisedButton(text="Load Images", on_release=self.load_images,pos_hint={'center_x':.5})
        bkwidget.add_widget(load_button)
        upload_btn=MDRaisedButton(text='Upload Image',on_release=self.upload_btn_func)
        bkwidget.add_widget(upload_btn)
        clear=MDIconButton(icon='eraser')
        load=MDIconButton(icon='arrow-up')
        load.on_press=self.ckdtload
        edit=MDIconButton(icon='pencil')
        edit.on_press=self.edit_func
        clear.on_press=self.clearfun
        sv_img=MDIconButton(icon='image')
        r_link=MDIconButton(icon='link')
        delete=MDIconButton(icon="delete")
        delete.on_press=self.delete_func
        sv_img.on_press=self.sv_img_fun
        r_link.on_press=self.r_link_fun
        h_link=MDIconButton(icon='database-edit')
        h_link.on_press=self.h_link_func
        save_button = MDFillRoundFlatIconButton(text="Save", icon="content-save", pos_hint={'center_x': 0.9})
        save_button.bind(on_release=self.save_data)
        homewidget.add_widget(save_button)
        global t1, name1, ph1, pay1, program,name_input,phone_input,payment_input
        self.date = MDTextField(size_hint=(None, None), hint_text='Date', readonly=True)
        program = MDTextField(size_hint=(None, None), hint_text='ProGram')
        t1 = MDDataTable(column_data=[('Id', dp(30)), ('Name', dp(50)), ('PayMent', dp(60)), ('Phone', dp(60))], check=True,rows_num=999)
        name_input = CustomMDInputField(hint_text='Name')
        payment_input = CustomMDInputField(hint_text='Payment')
        phone_input = CustomMDInputField(hint_text='Phone')
        input_layout = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height=dp(48))
        tools_for_t1=MDBoxLayout(orientation='horizontal', size_hint=(1, None), height=dp(48))
        input_layout.add_widget(name_input)
        input_layout.add_widget(payment_input)
        input_layout.add_widget(phone_input)
        tb.add_widget(home)
        tb.add_widget(sl)
        tb.add_widget(st)
        tb.add_widget(bk)
        tools_for_t1.add_widget(clear)
        tools_for_t1.add_widget(sv_img)
        tools_for_t1.add_widget(r_link)
        tools_for_t1.add_widget(edit)
        tools_for_t1.add_widget(load)
        tools_for_t1.add_widget(delete)
        tools_for_t1.add_widget(h_link)
        st.add_widget(settingwidget)
        def toggle_dark_theme(instance):
            if self.theme_cls.theme_style == "Light":
                self.theme_cls.theme_style = "Dark"
            else:
                self.theme_cls.theme_style = "Light"
        dark_theme_button = MDFillRoundFlatIconButton(text="Toggle Dark Theme", icon="theme-light-dark", pos_hint={'center_x': 0.5,'center_y':.9})
        dark_theme_button.bind(on_release=toggle_dark_theme)
        rearrange_id=MDFillRoundFlatIconButton(text='Rearrange-Id',icon="sort",pos_hint={'center_x': 0.5,'center_y':.7})
        rearrange_id.on_press=self.r_id
        total_chk=MDFillRoundFlatIconButton(text='Find Saving',icon="table",pos_hint={'center_x': 0.5,'center_y':.5})
        total_chk.on_press=self.total_chk_func
        rearrange_id_t2=MDFillRoundFlatIconButton(text='Reaarange-Id-T2',icon='table',pos_hint={'center_x':.5,'center_y':.3})
        rearrange_id_t2.on_press=self.r_id_t2
        settingwidget.add_widget(dark_theme_button)
        settingwidget.add_widget(rearrange_id)
        settingwidget.add_widget(total_chk)
        settingwidget.add_widget(rearrange_id_t2)
        date_button = MDFillRoundFlatIconButton(text="Select Date", icon="calendar", pos_hint={'center_x': 0.5})
        date_button.bind(on_release=self.open_date_picker)
        homewidget.add_widget(date_button)
        homewidget.add_widget(program)
        homewidget.add_widget(t1)
        homewidget.add_widget(tools_for_t1)
        homewidget.add_widget(input_layout)
        layout.add_widget(tb)
        home.add_widget(homewidget)
        return layout
    def apply_btn_func_t2(self):
        t2.row_data=t3_data_t2
        self.win_check_t2.dismiss()
    def check_for_updates_t2(self):
        global t3_data_t2

        url3_t2="https://ajakmt.000webhostapp.com/h_link_host/status.php"
        parmas_2_t2={
        'file_url':f"https://ajakmt.000webhostapp.com/h_link_host/uploads_h_link/done_{self.selected_date.strftime('%Y-%m-%d')}_{program.text}_t2.json.txt"
        }
        response_2_t2 = requests.get(url3_t2, params=parmas_2_t2,timeout=50)
        if response_2_t2.status_code == 200:
            if "done" in response_2_t2.text:
                global t3_data
                win_layout_t2 = MDBoxLayout(orientation='vertical')
                fileurl_t2=parmas_1_t2.get('file_url')
                fileraw_t2 = requests.get(fileurl_t2)
                json_data_t2=fileraw_t2.text
                self.win_check_t2.clear_widgets()
                self.win_check_t2.add_widget(win_layout_t2)
                t3_t2=MDDataTable(column_data=[('Id', dp(30)), ('Name', dp(50)), ('PayMent', dp(60)), ('Phone', dp(60))], check=True,rows_num=999)
                win_layout_t2.add_widget(t3_t2)
                t3_data_t2=json.loads(json_data_t2)
                t3_t2.row_data=t3_data_t2
                apply_btn=MDRaisedButton(text='Apply To T2')
                apply_btn.on_press=self.apply_btn_func_t2
                win_layout_t2.add_widget(apply_btn)
            else:
                toast('Pending...')
    def h_link_func_2(self):
        global parmas_1_t2
        url_t2 = 'https://ajakmt.000webhostapp.com/h_link_host/upload.php'
        files_t2 = {'json_file': (f"./{self.selected_date.strftime('%Y-%m-%d')}_{program.text}_t2.json", open(f"./{self.selected_date.strftime('%Y-%m-%d')}_{program.text}_t2.json", 'rb'))}
        response_t2 = requests.post(url_t2, files=files_t2,timeout=50)
        if response_t2.status_code == 200:
            toast('File uploaded successfully.')
        else:
            toast('File upload failed with status code:'+str( response_t2.status_code))
            toast('Response content:'+str(response_t2.content))
        url_2_t2="https://ajakmt.000webhostapp.com/h_link_host/dt2.php"
        parmas_1_t2={
    'file_url':"https://ajakmt.000webhostapp.com/h_link_host/uploads_h_link/2023-08-30_retirement_t2.json"
        }
        response_1_t2 = requests.get(url_2_t2, params=parmas_1_t2,timeout=50)
        if response_1_t2.status_code == 200:  
            if "<td>" in response_1_t2.text:
                Clipboard.copy(str(url_2_t2+"?"+"file_url="+parmas_1_t2.get('file_url')))
        else:
            toast('Request failed with status code:'+str(response_1_t2.status_code))
            toast('Error message:'+str(response_1_t2.text))
        self.win_check_t2 = ModalView(size_hint=(None, None), size=(500, 500),auto_dismiss=False)
        self.win_layout_t2 = MDBoxLayout(orientation='vertical')
        check_button_t2 = MDRaisedButton(
            text="Check For Request",
            pos_hint={'center_x': 0.5, 'center_y': 0.1}
        )
        check_button_t2.on_press=self.check_for_updates_t2
        self.win_layout_t2.add_widget(check_button_t2)
        self.win_check_t2.add_widget(self.win_layout_t2)
        self.win_check_t2.open()
        toast('Link Copied To ClipBoard')
    def h_link_func(self):
        global parmas_1
        url = 'https://ajakmt.000webhostapp.com/h_link_host/upload.php'
        files = {'json_file': (f"./{self.selected_date.strftime('%Y-%m-%d')}_{program.text}.json", open(f"./{self.selected_date.strftime('%Y-%m-%d')}_{program.text}.json", 'rb'))}
        response = requests.post(url, files=files,timeout=50)
        if response.status_code == 200:
            toast('File uploaded successfully.')
        else:
            toast('File upload failed with status code:'+str(response.status_code))
        toast('Response content:'+str(response.content))
        url_2="https://ajakmt.000webhostapp.com/h_link_host/dt2.php"
        parmas_1={
            'file_url':f"https://ajakmt.000webhostapp.com/h_link_host/uploads_h_link/{self.selected_date.strftime('%Y-%m-%d')}_{program.text}.json"
        }
        response_1 = requests.get(url_2, params=parmas_1,timeout=50)
        if response_1.status_code == 200:
            if "<td>" in response_1.text:
                Clipboard.copy(str(url_2+"?"+"file_url="+parmas_1.get('file_url')))
        else:
            toast('Request failed with status code:'+str(response_1.status_code))
            toast('Error message:'+str(response_1.text))
        self.win_check = ModalView(size_hint=(None, None), size=(500, 500),auto_dismiss=False)
        self.win_layout = MDBoxLayout(orientation='vertical')
        check_button = MDRaisedButton(
            text="Check For Request",
            pos_hint={'center_x': 0.5, 'center_y': 0.1}
        )
        check_button.on_press=self.check_for_updates
        self.win_layout.add_widget(check_button)
        self.win_check.add_widget(self.win_layout)
        self.win_check.open()
        toast('Link Copied To ClipBoard')
    def apply_btn_func(self):
        t1.row_data=t3_data
        self.win_check.dismiss()
    def check_for_updates(self):
        url3="https://ajakmt.000webhostapp.com/h_link_host/status.php"
        parmas_2={
        'file_url':f"https://ajakmt.000webhostapp.com/h_link_host/uploads_h_link/done_{self.selected_date.strftime('%Y-%m-%d')}_{program.text}.json.txt"
        }
        response_2 = requests.get(url3, params=parmas_2,timeout=50)
        if response_2.status_code == 200:
            if "done" in response_2.text:
                global t3_data
                win_layout = MDBoxLayout(orientation='vertical')
                fileurl=parmas_1.get('file_url')
                fileraw = requests.get(fileurl)
                json_data=fileraw.text
                self.win_check.clear_widgets()
                self.win_check.add_widget(win_layout)
                t3=MDDataTable(column_data=[('Id', dp(30)), ('Name', dp(50)), ('PayMent', dp(60)), ('Phone', dp(60))], check=True,rows_num=999)
                win_layout.add_widget(t3)
                t3_data=json.loads(json_data)
                t3.row_data=t3_data
                apply_btn=MDRaisedButton(text='Apply To T1')
                apply_btn.on_press=self.apply_btn_func
                win_layout.add_widget(apply_btn)
            else:
                toast('Pending...')
    def upload_btn_func(self,instance):
        webbrowser.open("https://imgcloud.systumm443.repl.co/")
    def load_images(self,instance):
        self.image_layout.clear_widgets()
        try:
            response = requests.get("https://imgcloud.systumm443.repl.co/display_dt.php", timeout=50)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                image_urls = []
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href:
                        image_urls.append(href)
                for image_url in image_urls:
                    image = AsyncImage(
                        source="https://imgcloud.systumm443.repl.co/"+image_url,
                        size_hint=(None, None),
                        size=(dp(450), dp(550)),
                        pos_hint={'center_x':.5}
                    )
                    self.image_layout.add_widget(image)
            else:
                self.image_layout.add_widget(MDLabel(text="Failed to fetch images"))
        except Exception as e:
            self.image_layout.add_widget(MDLabel(text=f"Error: {str(e)}"))
    def save_edit_t2(self):
        t2.update_row(row_t2,[row_t2[0],n_name_t2.text,n_pay_t2.text,n_phone_t2.text])
        window_t2.dismiss()
    def edit_func_t2(self):
        global n_name_t2,n_pay_t2,n_phone_t2,row_t2,window_t2,winlayout_t2
        row_t2=t2.get_row_checks()[0]
        window_t2=ModalView(size_hint=(None, None), size=(400, 400),auto_dismiss=False)
        winlayout_t2=MDFloatLayout(md_bg_color=(1,1,1,1),radius=(5,5,5,5))
        n_name_t2=MDTextField(hint_text="Product Name",pos_hint={'center_x':.5,'center_y':.9},mode="rectangle")
        n_pay_t2=MDTextField(hint_text="New Payment",pos_hint={'center_x':.5,'center_y':.7},mode="rectangle")
        n_phone_t2=MDTextField(hint_text="Shop Name",pos_hint={'center_x':.5,'center_y':.5},mode="rectangle")
        save_btn_edit_t2=MDIconButton(icon='content-save',pos_hint={'center_x':.5,'center_y':.3})
        save_btn_edit_t2.on_press=self.save_edit_t2
        winlayout_t2.add_widget(save_btn_edit_t2)
        winlayout_t2.add_widget(n_phone_t2)
        winlayout_t2.add_widget(n_pay_t2)
        winlayout_t2.add_widget(n_name_t2)
        window_t2.add_widget(winlayout_t2)
        window_t2.open()
    def sv_img_t2_func(self):
        if self.picked and not program.text=="":
            t2.export_to_png(f"{self.selected_date.strftime('%Y-%m-%d')}_{program.text}_t2.png")
        else:
            toast("Please Fill Date And Program")
    def total_chk_func(self):
        t1_payment_total=0
        t2_payment_total=0
        for t1_dt in t1.row_data:
           t1_payment_total+=int(t1_dt[2])
        for t2_dt in t2.row_data:
            t2_payment_total+=int(t2_dt[2])
        total=t1_payment_total-t2_payment_total
        toast(str(total))
    def load_t2_func(self):
        with open(f"{os.getcwd()}\\{self.selected_date.strftime('%Y-%m-%d')}_{program.text}_t2.json","r") as f:
            t2.row_data=json.load(f)
    def ld_t2_func(self):
        index_t2=str(len(t2.row_data) + 1)
        sp_nm_text=sp_nm.text
        if sp_nm.text=="":
            sp_nm_text="Shop-XXX"
        t2.add_row([index_t2,name_t2.text,pay_t2.text,sp_nm_text])
        name_t2.text=""
        pay_t2.text=""
        sp_nm.text=""
    def r_id_t2(self):
        if self.used_del_2:
            new_data_t2=[]
            row_list_t2=t2.get_row_checks()
            row_to_delete_t2=len(row_list_t2[0])
            for data in t2.row_data:
                    data[0]=str(row_to_delete_t2-int(data[0]))
                    new_data_t2.append(data)
            t2.row_data=[]
            t2.row_data=new_data_t2
        else:
            toast('Only Can Be Used After Del Func!!')
    def r_id(self):
        if self.used_del:
            new_data=[]
            row_list=t1.get_row_checks()
            row_to_delete=len(row_list[0])
            for data in t1.row_data:
                    data[0]=str(row_to_delete-int(data[0]))
                    new_data.append(data)
            t1.row_data=[]
            t1.row_data=new_data
        else:
            toast('Only Can Be Used After Del Func!!')
    def delete_func_t2(self):
        row_list=t2.get_row_checks()
        for row in  row_list:
            t2.remove_row(row)
        self.used_del_2=True
    def clear_fun_t2(self):
        t2.row_data=[]
    def delete_func(self):
        row_list=t1.get_row_checks()
        for row in  row_list:
            t1.remove_row(row)
        self.used_del=True
    def save_edit(self):
        t1.update_row(row,[row[0],n_name.text,n_pay.text,n_phone.text])
        window.dismiss()
    def edit_func(self):
        global n_name,n_pay,n_phone,row,window
        row=t1.get_row_checks()[0]
        window=ModalView(size_hint=(None, None), size=(400, 400),auto_dismiss=False)
        winlayout=MDFloatLayout(md_bg_color=(1,1,1,1),radius=(5,5,5,5))
        n_name=MDTextField(hint_text="New Name",pos_hint={'center_x':.5,'center_y':.9},mode="rectangle")
        n_pay=MDTextField(hint_text="New Payment",pos_hint={'center_x':.5,'center_y':.7},mode="rectangle")
        n_phone=MDTextField(hint_text="New Phone No.",pos_hint={'center_x':.5,'center_y':.5},mode="rectangle")
        save_btn_edit=MDIconButton(icon='content-save',pos_hint={'center_x':.5,'center_y':.3})
        save_btn_edit.on_press=self.save_edit
        winlayout.add_widget(save_btn_edit)
        winlayout.add_widget(n_phone)
        winlayout.add_widget(n_pay)
        winlayout.add_widget(n_name)
        window.add_widget(winlayout)
        window.open()
    def r_link_t2_func(self):
       url="https://ajakmt.000webhostapp.com/upload.php"
       path=f"{os.getcwd()}\\{self.selected_date.strftime('%Y-%m-%d')}_{program.text}_t2.json"
       files = {"file_upload": open(path, "rb")}
       response = requests.post(url, files=files,timeout=20)
       if response.ok:
            baseurl="https://ajakmt.000webhostapp.com/uploads/"
            filename=f"{self.selected_date.strftime('%Y-%m-%d')}_{program.text}_t2_table.php"
            Clipboard.copy(baseurl+filename)
            toast('Link Copied To ClipBoard!!')
       else:
            toast("File upload failed.")
    def r_link_fun(self):
       url="https://ajakmt.000webhostapp.com/upload.php"
       path=f"{os.getcwd()}\\{self.selected_date.strftime('%Y-%m-%d')}_{program.text}.json"
       files = {"file_upload": open(path, "rb")}
       response = requests.post(url, files=files,timeout=20)
       if response.ok:
            baseurl="https://ajakmt.000webhostapp.com/uploads/"
            filename=f"{self.selected_date.strftime('%Y-%m-%d')}_{program.text}_table.php"
            Clipboard.copy(baseurl+filename)
            toast('Link Copied To ClipBoard!!')
       else:
            toast("File upload failed.")
    def sv_img_fun(self):
        if self.picked and not program.text=="":
            t1.export_to_png(f"{self.selected_date.strftime('%Y-%m-%d')}_{program.text}.png")
        else:
            toast("Please Fill Date And Program")
    def clearfun(self):
        t1.row_data=[]
        program.text=""
    def ckdtload(self):
        if self.picked and not program.text=="" and not  program.focus:
            if os.path.exists(f'{os.getcwd()}/{self.selected_date.strftime("%Y-%m-%d")}_{program.text}.json'):
                with open(f'{os.getcwd()}/{self.selected_date.strftime("%Y-%m-%d")}_{program.text}.json', 'r') as json_file:
                    data = json.load(json_file)
                    t1.row_data=data
    def save_data(self, instance):
        try:
            data_t1=t1.row_data
            data_t2=t2.row_data
            filename_t1 = f"{self.selected_date.strftime('%Y-%m-%d')}_{program.text}.json"
            filename_t2 =  f"{self.selected_date.strftime('%Y-%m-%d')}_{program.text}_t2.json"
            if self.picked and program.text and t2.row_data and t1.row_data:
                with open(filename_t1,"w") as f:
                    json.dump(data_t1,f)
                toast("T1-Data saved to:"+filename_t1)
                with open(filename_t2,"w") as f:
                    json.dump(data_t2,f)
                toast("T2-Data saved to:"+filename_t2)
            if self.picked and program.text and t1.row_data:
                with open(filename_t1, "w") as f:
                    json.dump(data_t1, f)
                toast("Data saved to:"+filename_t1)
            else:
                toast('Error!! May Not Filled RequireMent.',background=[1,0,0,1])
        except:
            toast('Error!! May Not Filled RequireMent.',background=[1,0,0,1])
    def open_date_picker(self, instance):
        if not self.date_picker:
            self.date_picker = MDDatePicker()
            self.date_picker.bind(on_save=self.on_date_selected)
        self.date_picker.open()
    def on_date_selected(self, instance, value, date_range):
        self.selected_date = value
        self.date.text = value.strftime('%Y-%m-%d')
        self.date_picker.dismiss()
        toast("Selected Date:"+str(self.date.text))
        self.picked=True
AJAKKMT().run()