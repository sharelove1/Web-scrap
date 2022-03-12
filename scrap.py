from kivy.lang import Builder
from kivymd_extensions.akivymd import*
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
import requests
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.image import Image
from kivymd.uix.swiper import MDSwiper,MDSwiperItem
from kivymd.uix.screen import MDScreen
from kivy.factory import Factory
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.toolbar import MDToolbar
from kivymd.toast import toast
from bs4 import BeautifulSoup
from kivymd.app import MDApp
from kivy.properties import StringProperty,ObjectProperty
from kivy.utils import get_color_from_hex
KV = '''
#: import HtmlLexer pygments.lexers.html.HtmlLexer
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import SliverToolbar __main__.SliverToolbar
#:set text_color get_color_from_hex("#4a4939")
#:set focus_color get_color_from_hex("#e7e4c0")
#:set ripple_color get_color_from_hex("#c5bdd2")
#:set bg_color get_color_from_hex("#f7f4e7")
#:set selected_color get_color_from_hex("#0c6c4d")
<ItemForCustomBottomSheet@OneLineListItem>:
    on_release:app.imagescreen()
    
<Ca>:
	elevation:20
	ripple_behavior:True
	size_hint:None,None
	size:dp(360),dp(130)
	on_release:app.oneimage()
	FitImage:
		id:ab
		source:root.source
<MyLabel@MDLabel>
    valign: "center"
    theme_text_color: "Custom"
    text_color: 1,1,1,1
<Lan@MDCard+FitImage>	
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: focus_color
    unfocus_color: bg_color
    text_color: text_color
    icon_color: text_color
    ripple_color: ripple_color
    selected_color: selected_color


<DrawerLabelItem@MDNavigationDrawerItem>
    bg_color: bg_color
    text_color: text_color
    icon_color: text_color
    _no_ripple_effect: True

<ContentCustomSheet@BoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height: "180dp"
    ScrollView
	    MDGridLayout:
	    	cols: 1
	        adaptive_height: True
	        ItemForCustomBottomSheet:
	        	
	        	text:"images in the website"
	        	
	        OneLineListItem:
	        	text:"videos in the website"
	        OneLineListItem:
	        	text:"audios in the website"
	        	
    
    		
    
MDScreen:

    MDNavigationLayout:

        ScreenManager:
			id:a
            MDScreen:
            	name:"home screen"
            	MDFloatLayout:
					MDBoxLayout:
						spacing:dp(7)
						orientation:"vertical"
		                MDToolbar:
		                    id:toolbar
		                    title: "Home screen"
		                    elevation: 10
		                    pos_hint: {"top": 1}
		                    md_bg_color: focus_color
		                    specific_text_color: text_color

		                    left_action_items:
		                        [                             [                             'menu', lambda x:                             nav_drawer.set_state("open")                             if nav_drawer.state == "close" else                             nav_drawer.set_state("close")                             ]                             ]
		                    
						ScrollView: 
							do_scroll_x: False
		    				do_scroll_y: True
							MDBoxLayout:
								adaptive_size: True
								orientation:"vertical"
								spacing:dp(15)
								
								
								MD3Card:
									md_bg_color:get_color_from_hex("#f4dedc")
									orientation:"vertical"
									size_hint: None, None
				   				 size: "360dp", "200dp"
				   				 elevation:10
				   				 radius:[30,]
				   				 spacing:dp(5)
				   				 on_release:app.change_to_whole_screen()
								
									FitImage:
										source:"code-1076536__480.webp"
									
										elevation:15
				   				 	radius:[30,]
				   				 MDLabel:
								    	text:"Scrap whole website"
								    	pos_hint:{"center_x":.5}
								   	 adaptive_size: True
								   	 theme_text_color: "Custom"
								   	 outline_width:10
								   	 outline_color:(0,1,0)
								   	 text_color:0,0,1,1
			
				   				 
								MD3Card:
									size_hint: None, None
				   				 size: "360dp", "100dp"
				   				 elevation:15
				   				 radius:[30,]
									MDLabel:
										text:"click"
									
			MDScreen:
				name:"scrap_web"	
				MDFloatLayout:
					MDBoxLayout:
						orientation:"vertical"
						spacing:dp(8)
						MDToolbar:
		                    title: "Scrap whole website"
		                    elevation: 10
		                    pos_hint: {"top": 1}
		                    md_bg_color: focus_color
		                    specific_text_color: text_color
		                    left_action_items:
		                        [                             [                             'menu', lambda x:                             nav_drawer.set_state("open")                             if nav_drawer.state == "close" else                             nav_drawer.set_state("close")                             ]                             ]
						MD3Card:
							orientation:"horizontal"
							size_hint: None, None
							pos_hint:{"top":1}
					   	 size: "360dp", "40dp"
				   		 elevation:15
					   	 radius:[30,]
					   	 TextInput:
					   	 	id:enter_url_inputbox
				    			hint_text:"enter url example https://xyz.com"
						    	background_color:0,0,0,0
						    	font_size:"20sp"
						    	multiline:False
							    cursor_width:4	
							MDIconButton:
								icon:"play"
								on_release:app.get_code()						
									
							
															    
																			
							    
							
						MD3Card:
						    size: "360dp", "800dp"
						    orientation:"vertical"		 
						    ScrollView:
						    	id:scroll_code
						    	do_scroll_x: False
		    					do_scroll_y: True
		    					
								CodeInput:
									id:whole_code_text
									
									hint_text:"after entering url press play button to get the code"
	#								adaptive_height:True
									multiline:True
									cursor_width:4
									size_hint:1,None
									height:self.minimum_height
									lexer:HtmlLexer()
									background_color:0,0,0,0
							
					MDSpinner:
					    id:sp
				        size_hint: None, None
				        size: dp(46), dp(46)
				        pos_hint: {'center_x': .5, 'center_y': .5}
				        active: True if whole_code_text.text=="" and enter_url_inputbox.text!="" else False		                				              			       		 					              			                        							               				           		 				                				              			       		 					              			                        											           		 				                				              			       		 					              			                        							
				           		 				                				              			       		 					              			                        							                
			MDScreen:
				name:"imagescreen"
				MDSliverAppbar:
					toolbar_cls: SliverToolbar()
					MDSliverAppbarHeader:

            			MDRelativeLayout:
            				adaptive_height:True
            				MDLabel:
            					text:"All image are shown here"

					MDSliverAppbarContent:
			        	id: box
			            orientation: "vertical"
			            padding: "12dp"
			            spacing: "12dp"
			            adaptive_height: True
						
				    
						MDBoxLayout:
							id:bo
							orientation:"vertical"	
							size_hint:None,None
							adaptive_height: True
								
			OneImage:
				name:"Oneimage"
				
				MDLabel:
					text:"not wroked"						
													
																	
											
				
					                    

        MDNavigationDrawer:
            id: nav_drawer
            type:"standard"
            enable_swiping:True
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: bg_color

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Web Scrapper"
                    title_color: text_color
                    text: "Header text"
                    title_color: text_color
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Scrap Web"

                DrawerClickableItem:
                    icon: "home"
#                    right_text: "+99"
                    text_right_color: text_color
                    text: "Home"
                    on_release:a.current="home screen"

                DrawerClickableItem:
                    icon: "web"
                    text: "Full web scrap"
                    on_release:a.current="scrap_web"

                    

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "#kivy"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "#kivymd"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "#akivymd"
'''
#req = UrlRequest('https://httpbin.org/headers', got_json) 
class Ca(MDCard):
	source=StringProperty()
		
		
class Tab(MDTabsBase,MDFloatLayout):
	pass
class SliverToolbar(MDToolbar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type_height = "medium"
        self.headline_text = "Headline medium"
        self.left_action_items = [["arrow-left", lambda x: x]]
        self.right_action_items = [
            ["attachment", lambda x: x],
            ["calendar", lambda x: x],
            ["dots-vertical", lambda x: x],
        ]
class OneImage(MDScreen):
	pass
	
	
class MD3Card(MDCard, RoundedRectangularElevationBehavior):
	text = StringProperty()
class Scrap(MDApp):
	custom_sheet = None
	def oneimage(self):
		self.root.ids.a.current="Oneimage"
	def build(self):
		self.theme_cls.primary_palette = "Indigo"
		return Builder.load_string(KV)
#	def got_json(req, result):
#		for key, value in req.resp_headers.items():
#			print('{}: {}'.format(key, value))

#		
			
	def get_code(self):
		url = self.root.ids.enter_url_inputbox.text		
		r = UrlRequest(url, self.got_code)
	
	def got_code(self, req, result):
#		store = JsonStore('hello.json')
		soup = BeautifulSoup(result, 'html.parser')
		code_text=soup.prettify()
		self.root.ids.whole_code_text.text=code_text
		self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
		self.custom_sheet.open()
		#for item in soup.find_all('img'):
#			self.root.ids.imagetab.add_widget(Ca(source=item['src']))
#		for item in soup.find_all('img'):
#		    self.root.ids.imagetab.add_widget(Ca(source=item['src']))
			
		
		for item in soup.find_all('img'):
			self.root.ids.bo.add_widget(Ca(source=item['src']))
			
			
#			self.root.ids.whole_code_text.text+=item['src']
#			store.put('tio', name=self.root.ids.whole_code_text.text)		
#		self.root.ids.whole_code_text.text=code_text 
	def change_to_whole_screen(self):
		self.root.ids.a.current="scrap_web"
	def imagescreen(self):
		self.root.ids.a.current="imagescreen"
	#def on_start(self):
#		store = JsonStore('hello.json')
#		print('tito is', store.get('tio')['name'])	
#	def get_code(self):
#		try:
#		    url = self.root.ids.enter_url_inputbox.text
#		    r = requests.get(url)
#		    soup = BeautifulSoup(r.content, 'html.parser')
#		    code_text=soup.prettify()
#		    self.root.ids.whole_code_text.text=code_text 
#		    for item in soup.find_all('img'):
#		    	self.root.ids.bo.add_widget(Ca(source=item['src']))
#		    	self.root.ids.whole_code_text.text+=item['src']
#		except:
#			toast("something went wrong check is internet connection is on and url is correct",gravity=70)		    	
#		    	
		    
		    
				
	
Scrap().run()