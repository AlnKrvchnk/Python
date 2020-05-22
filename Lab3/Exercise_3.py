import wx
import os
import Ex3
import datetime
import os.path

ID_FILE=1
EXPORT=2
ADD=3
VIEW=4

class MyFrame(wx.Frame):
     def __init__(self,parent,title):
          super().__init__(parent,title=title)
          self.SetSize((600,400))
          
          panel = wx.Panel(self)
          sampleList=[]
          tb = wx.TextCtrl(panel,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.TE_RICH)
          self.tb=tb
          
          sizer = wx.GridSizer(1,0,0,0)
          sizer.Add(tb,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM,border=5)
          panel.SetSizer(sizer)
          
          menubar=wx.MenuBar()
          fileMenu=wx.Menu()
          
          fileMenu.Append(ID_FILE,"Открыть...",)
          menubar.Append(fileMenu,"&Файл")
          
          logMenu=wx.Menu()
          
          logMenu.Append(EXPORT,'Экспорт...')
          logMenu.Append(ADD,'Добавить в лог')
          logMenu.Append(VIEW,'Просмотр')
          menubar.Append(logMenu,"&Лог")
          
          self.SetMenuBar(menubar)
          
          statusbar=self.CreateStatusBar(2)
          self.statusbar=statusbar
          
          statusbar.SetStatusWidths([-6,-4])
          self.statusbar.SetStatusText('Открыт лог',0)
          
          self.Bind(wx.EVT_MENU,self.onOpen,id=ID_FILE)
          self.Bind(wx.EVT_MENU,self.addLog,id=ADD)
          self.Bind(wx.EVT_MENU,self.viewLog,id=VIEW)
          self.Bind(wx.EVT_MENU,self.Export,id=EXPORT )
          
     def Export(self,event):
          self.dirname = " "
          openDlg = wx.FileDialog(self, "Выберите файл...", self.dirname, " ", "*.*", wx.FD_OPEN) # создаём диалог
          if openDlg.ShowModal() == wx.ID_OK: # при выборе файла
                self.filename = openDlg.GetFilename() # ловим название файла
                self.dirname = openDlg.GetDirectory() # и папку, в которой он находится
                path=str(self.dirname)+'\\'+str(self.filename)
                f=open(path,'w')
                f.write(self.tb.GetValue())

     def viewLog(self,event):
          dlg=wx.MessageBox('Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!', 'Просмотрето лог', wx.YES_NO |wx.YES,self)
          if dlg==wx.YES:
               f=open('script18.log.','r')
               self.tb.Clear()
               self.tb.AppendText(f.read())
          
     def addLog(self,event):
          if os.path.exists('script18.log')==False:
               print(os.path.exists('script18.log.txt'))
               dlg=wx.MessageBox('Файл лога не найден. Файл будет создан автоматически.', 'Файл не найден', wx.OK |wx.CENTER,self)
               if dlg==wx.OK:
                    f=open('script18.log.','w')
          else:
               f=open('script18.log.','a')
          f.write(self.tb.GetValue())

          
     def onOpen(self, event):
        self.dirname = " "
        openDlg = wx.FileDialog(self, "Выберите файл...", self.dirname, " ", "*.*", wx.FD_OPEN) # создаём диалог
        if openDlg.ShowModal() == wx.ID_OK: # при выборе файла
                self.filename = openDlg.GetFilename() # ловим название файла
                self.dirname = openDlg.GetDirectory() # и папку, в которой он находится
                path=str(self.dirname)+'\\'+str(self.filename)
                self.statusbar.SetStatusText('Обработан файл: '+str(self.filename),0)
                self.statusbar.SetStatusText(self.formatSize(str(os.path.getsize(self.dirname+'\\'+self.filename))),1)
                now = datetime.datetime.now()
                self.tb.AppendText('Файл: '+path+ ' был обработан:'+now.strftime("%d.%m.%Y %H:%M") +':\n' )  
                for s in Ex3.read(path):
                     self.tb.AppendText(str(s))
                self.tb.AppendText('\n')    
                
                f = open(os.path.join(self.dirname,self.filename), "r") # открываем файл
                #self.control.SetValue(f.read()) # отображаем в текстовом поле
                f.close()
                
     def formatSize(self,size):
          leng=len(size)-3
          string=' '
          while size!='':
               if len(size)<4:
                    string=size+' '+string
                    break
               string=size[-3:]+' '+string
               size=size[:-3]
          return string+'байт' 
          
          

          
app = wx.App()
wnd = MyFrame(None, 'Kravchenko Alina Exercise 3')
wnd.Show(True)
app.MainLoop()
 
