import wx
import Exercise_4
ID_BUT=1
class MyFrame(wx.Frame):
     def __init__(self,parent,title):
          super().__init__(parent,title=title)
          self.SetSize((500,400))

          panel=wx.Panel(self)
          vbox=wx.BoxSizer(wx.VERTICAL)
          
          hbox1=wx.BoxSizer(wx.HORIZONTAL)
          tb = wx.TextCtrl(panel)
          self.tb=tb
          hbox1.Add((wx.StaticText(panel,label="Строка:")),flag=wx.LEFT|wx.RIGHT|wx.TOP,border=5)
          hbox1.Add(self.tb,flag=wx.LEFT|wx.TOP|wx.RIGHT,proportion=1)
          vbox.Add(hbox1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM,border=25)

          hbox2=wx.BoxSizer(wx.HORIZONTAL)
          cb1=wx.CheckBox(panel,label="Удалить все слова размером меньше")
          self.cb1=cb1
          spin = wx.SpinCtrl(panel,value='0', min=0, max=100)
          self.spin=spin
          hbox2.Add(cb1,flag=wx.LEFT|wx.TOP,border=5)
          hbox2.Add(self.spin,flag=wx.LEFT,border=10)
          hbox2.Add((wx.StaticText(panel,label="букв")),flag=wx.LEFT|wx.RIGHT|wx.TOP,border=10)
          vbox.Add(hbox2,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=60)

          vbox.Add((wx.StaticText(panel,label="")),flag=wx.LEFT,border=65)
          
          cb2=wx.CheckBox(panel,label="Заменить все цифры на *")
          self.cb2=cb2
          vbox.Add(cb2,flag=wx.LEFT,border=65)
          
          vbox.Add((wx.StaticText(panel,label="")),flag=wx.LEFT,border=65)

          cb3=wx.CheckBox(panel,label="Вставить по пробелу между символами")
          self.cb3=cb3
          vbox.Add(cb3,flag=wx.LEFT,border=65)

          vbox.Add((wx.StaticText(panel,label="")),flag=wx.LEFT,border=65)


          cb4=wx.CheckBox(panel,label="Сортировать слова в строке")
          self.cb4=cb4
          vbox.Add(cb4,flag=wx.LEFT,border=65)

          vbox.Add((wx.StaticText(panel,label="")),flag=wx.LEFT,border=65)

          rb1=wx.RadioButton(panel,label="По размеру",style=wx.RB_GROUP)
          self.rb1=rb1
          vbox.Add(rb1,flag=wx.LEFT,border=85)

          rb2=wx.RadioButton(panel,label="Лексикографически")
          self.rb2=rb2
          vbox.Add(rb2,flag=wx.LEFT,border=85)

          vbox.Add((wx.StaticText(panel,label="")),flag=wx.LEFT,border=65)

          button=wx.Button(panel,id=ID_BUT,label="Формировать")
          self.button=button
          vbox.Add(button,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=100)

          hbox3=wx.BoxSizer(wx.HORIZONTAL)
          tb2 = wx.TextCtrl(panel)
          self.tb2=tb2
          hbox3.Add((wx.StaticText(panel,label="Результат:")),flag=wx.LEFT|wx.RIGHT|wx.TOP,border=5)
          hbox3.Add(self.tb2,flag=wx.LEFT|wx.TOP|wx.RIGHT,proportion=1)
          vbox.Add(hbox3,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM,border=15)

          panel.SetSizer(vbox)
          
          #self.Bind(wx.EVT_CHECKBOX, self.checkCb4, self.cb4)

          self.Bind(wx.EVT_BUTTON,self.enterButton,id=ID_BUT)
     #def checkCb4(self,event):
          #if self.cb4.GetValue()==True:
               
         
     def enterButton(self,event):
         
          string=self.tb.GetValue()
          self.string=string
          self.sf = Exercise_4.StribngFormatter(string)
          if self.cb1.GetValue()==True:
               self.string=self.sf.delword(int(self.spin.GetValue()))
          if self.cb2.GetValue()==True:
               self.string=self.sf.change()
          if self.cb3.GetValue()==True:
               self.string=self.sf.space()
          if self.cb4.GetValue()==True:
               if self.rb1.GetValue()==True:
                    self.string=self.sf.sortbylen()
               if self.rb2.GetValue()==True:
                    self.string=self.sf.sort()
          self.tb2.Clear()
          self.tb2.SetValue(self.string)
          
       
app = wx.App()
wnd = MyFrame(None, 'Kravchenko Alina Exercise 5')
wnd.Show(True)
app.MainLoop()
 
