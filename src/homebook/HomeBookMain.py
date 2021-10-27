# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from homebook import homebookOfCRUD
import homebook
import sqlite3
from homebook.pieChart import pieChart
import matplotlib.pyplot as plt


# tableView = 1000

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1005,520 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 255, 227, 187 ) )
        
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"시리얼 번호", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        gbSizer1.Add( self.m_staticText16, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txtNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        gbSizer1.Add( self.txtNo, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 6 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"날짜", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        gbSizer1.Add( self.m_staticText18, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txtDay = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.txtDay, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"구분", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        gbSizer1.Add( self.m_staticText19, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.radioRev = wx.RadioButton( self, wx.ID_ANY, u"수입", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.radioRev, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.radioExp = wx.RadioButton( self, wx.ID_ANY, u"지출", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.radioExp, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"항목구분", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        gbSizer1.Add( self.m_staticText20, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"세부내용", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )
        gbSizer1.Add( self.m_staticText24, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txtRemark = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.txtRemark, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        
        comboAccountChoices = [ u"월급", u"상여금", u"기타수입", u"식비", u"교통비", u"생필품", u"의류", u"의료비/건강비", u"통신비", u"공과금" ]
        self.comboAccount = wx.ComboBox( self, wx.ID_ANY, u"선택하세요", wx.DefaultPosition, wx.DefaultSize, comboAccountChoices, 0 )
        gbSizer1.Add( self.comboAccount, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"세부금액", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )
        gbSizer1.Add( self.m_staticText21, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"수입", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )
        gbSizer1.Add( self.m_staticText22, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txtRev = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.txtRev, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
        
        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"지출", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )
        gbSizer1.Add( self.m_staticText23, wx.GBPosition( 5, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txtExp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.txtExp, wx.GBPosition( 5, 5 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
        
        self.m_button9 = wx.Button( self, wx.ID_ANY, u"INSERT", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button9.SetBackgroundColour( wx.Colour( 255, 210, 210 ) )
        
        gbSizer1.Add( self.m_button9, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button10 = wx.Button( self, wx.ID_ANY, u"UPDATE", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button10.SetBackgroundColour( wx.Colour( 255, 210, 210 ) )
        
        gbSizer1.Add( self.m_button10, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button11 = wx.Button( self, wx.ID_ANY, u"DELETE", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button11.SetBackgroundColour( wx.Colour( 255, 210, 210 ) )
        
        gbSizer1.Add( self.m_button11, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button12 = wx.Button( self, wx.ID_ANY, u"FIND", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button12.SetBackgroundColour( wx.Colour( 255, 210, 210 ) )
        
        gbSizer1.Add( self.m_button12, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button13 = wx.Button( self, wx.ID_ANY, u"SELECTALL", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button13.SetBackgroundColour( wx.Colour( 255, 210, 210 ) )
        
        gbSizer1.Add( self.m_button13, wx.GBPosition( 6, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button14 = wx.Button( self, wx.ID_ANY, u"CLEAR", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button14.SetBackgroundColour( wx.Colour( 255, 210, 210 ) )
        
        ##
        gbSizer1.Add( self.m_button14, wx.GBPosition( 6, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,200 ), wx.LC_REPORT|wx.BORDER_SUNKEN )
        #self.list.SetBackgroundColour( wx.Colour( 180, 230, 230 ) )
        
        self.list.InsertColumn(0, '번호')
        self.list.InsertColumn(1, '날짜', wx.Layout_RightToLeft)
        self.list.InsertColumn(2, '수입/지출', wx.Layout_RightToLeft)
        self.list.InsertColumn(3, '항목', wx.Layout_RightToLeft)
        self.list.InsertColumn(4, '내용', wx.Layout_RightToLeft)
        self.list.InsertColumn(5, '수입', wx.Layout_RightToLeft)
        self.list.InsertColumn(6, '   지출', width=300)
        
        gbSizer1.Add( self.list, wx.GBPosition( 7, 0 ), wx.GBSpan( 16, 7 ), wx.ALL|wx.EXPAND, 5 )
        ##
        
        self.panel = pieChart(self)
        # self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 450,430 ), wx.TAB_TRAVERSAL )
        self.panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
    
        gbSizer1.Add( self.panel, wx.GBPosition( 1, 8 ), wx.GBSpan( 20, 12 ), wx.EXPAND |wx.ALL, 5 )
        
        self.m_button141 = wx.Button( self, wx.ID_ANY, u"수입/수출", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button141.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )
        
        gbSizer1.Add( self.m_button141, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )
        gbSizer1.Add( self.m_staticText26, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button1411 = wx.Button( self, wx.ID_ANY, u"기간차트", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button1411.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )
        
        gbSizer1.Add( self.m_button1411, wx.GBPosition( 0, 12 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txtStart = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.txtStart, wx.GBPosition( 0, 13 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText28.Wrap( -1 )
        gbSizer1.Add( self.m_staticText28, wx.GBPosition( 0, 14 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txtEnd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.txtEnd, wx.GBPosition( 0, 15 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( gbSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button9.Bind( wx.EVT_BUTTON, self.OnInsert )
        self.m_button10.Bind( wx.EVT_BUTTON, self.OnUpdate )
        self.m_button11.Bind( wx.EVT_BUTTON, self.OnDelete )
        self.m_button12.Bind( wx.EVT_BUTTON, self.OnFind )
        self.m_button13.Bind( wx.EVT_BUTTON, self.OnSelectAll )
        self.m_button14.Bind( wx.EVT_BUTTON, self.OnClear )
        self.list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.handle )
        self.m_button141.Bind( wx.EVT_BUTTON, self.OnPieChart )
        self.m_button1411.Bind( wx.EVT_BUTTON, self.OnBarChart )
    
    def __del__( self ):
        pass
    
        #
        
        # self.list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,200 ), wx.LC_REPORT|wx.BORDER_SUNKEN )
        #
        # self.list.InsertColumn(0, '번호')
        # self.list.InsertColumn(1, '날짜', wx.Layout_RightToLeft)
        # self.list.InsertColumn(2, '수입/지출', wx.Layout_RightToLeft)
        # self.list.InsertColumn(3, '항목', wx.Layout_RightToLeft)
        # self.list.InsertColumn(4, '내용', wx.Layout_RightToLeft)
        # self.list.InsertColumn(5, '수입', wx.Layout_RightToLeft)
        # self.list.InsertColumn(6, '   지출', width=300)
        #
        # gbSizer1.Add( self.list, wx.GBPosition( 7, 0 ), wx.GBSpan( 16, 7 ), wx.ALL|wx.EXPAND, 5 )
        
        #

        # self.list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.handle )
    # Virtual event handlers, overide them in your derived class
    def OnInsert( self, event ):
        day = self.txtDay.GetValue()
        
        if (self.radioRev.GetValue()):
            section = '수입'
            pass
        
        else:
            section = '지출'
            pass
        
        accounttitle = self.comboAccount.GetValue()
        remark = self.txtRemark.GetValue()
        revenue = self.txtRev.GetValue()
        expense = self.txtExp.GetValue()
        
        try:
            homebookOfCRUD.insertData(day,section,accounttitle,remark,revenue,expense)
        except:
            print('예외발생!')
        finally:
            print("등록성공")
        event.Skip()
    
    def OnUpdate( self, event ):
        day = self.txtDay.GetValue()
        
        if(self.radioRev.GetValue()):
            section = '수입'
        elif(self.radioExp.GetValue()):
            section = '지출'
            
        accounttitle = self.comboAccount.GetValue()
        remark = self.txtRemark.GetValue()
        revenue = self.txtRev.GetValue()
        expense = self.txtExp.GetValue()
        no = self.txtNo.GetValue()
        try:
            homebookOfCRUD.update((day,section,accounttitle,remark,revenue, expense,no))
        except:
            print('예외발생!')
        finally:
            print('수정완료!')
        event.Skip()

    
    def OnDelete( self, event ):
        no = self.txtNo.GetValue()
        try:
            homebookOfCRUD.delete(no)
        except:
            print('예외발생!')
        finally:
            print('삭제완료!')

        event.Skip()
    
    def OnFind( self, event ):
        conn = sqlite3.connect("homebook.db")
        cur = conn.cursor()
        sql = 'SELECT * FROM HOMEBOOK WHERE DAY = ?'
        try:
            day = str(self.txtDay.GetValue())
            cur.execute(sql,(day,))
            rows = cur.fetchall()
            x = 0
            수입 = 0
            지출 = 0
            self.list.DeleteAllItems()
            for row in rows:
                self.list.InsertItem(x, str(row[0]))
                self.list.SetItem(x, 1, row[1])
                self.list.SetItem(x, 2, row[2])
                self.list.SetItem(x, 3, row[3])
                self.list.SetItem(x, 4, row[4])
                self.list.SetItem(x, 5, str(row[5]))
                self.list.SetItem(x, 6, str(row[6]))
                x += 1
                수입 += row[5]
                지출 += row[6]
        except Exception as e:           
            wx.MessageBox("찾는 자료가 없습니다.", "Message" ,wx.OK | wx.ICON_INFORMATION)  
        finally:
            cur.close()
            conn.close()
        event.Skip()

    def OnSelectAll( self, event ):
        self.list.DeleteAllItems()
        rows = homebookOfCRUD.selectAll()
        x = 0
        수입 = 0
        지출 = 0
        for row in rows:
            self.list.InsertItem(x, str(row[0]))
            self.list.SetItem(x, 1, row[1])
            self.list.SetItem(x, 2, row[2])
            self.list.SetItem(x, 3, row[3])
            self.list.SetItem(x, 4, row[4])
            self.list.SetItem(x, 5, str(row[5]))
            self.list.SetItem(x, 6, str(row[6]))
            x += 1
            수입 += row[5]
            지출 += row[6]
        event.Skip()
    
    def OnClear( self, event ):
        self.txtNo.Clear()
        self.txtDay.Clear()

        self.comboAccount.Clear()
        
        self.radioRev.SetValue(int(0))
        self.radioExp.SetValue(int(0))
        
        self.comboAccount.SetValue("선택하세요")
        self.txtRemark.Clear()
        
        self.txtRev.Clear()
        self.txtExp.Clear()
        self.list.DeleteAllItems()
        
        # self.panel.ClearBackground()
        
        self.txtStart.Clear()
        self.txtEnd.Clear()
        
        event.Skip()
        
    def btnSelect( self, event ):
        conn = sqlite3.connect("homebook.db")
        cur = conn.cursor()
        sql = "SELECT * FROM HOMEBOOK WHERE DAY BETWEEN ? AND ?"
        try:
            firstDate = str(self.txtStart.GetValue())
            secondDate = str(self.txtEnd.GetValue())
            cur.execute(sql, (firstDate, secondDate))
            rows = cur.fetchall()
            x = 0
            수입 = 0
            지출 = 0
            self.list.DeleteAllItems()
            for row in rows:
                self.list.InsertItem(x, str(row[0]))
                self.list.SetItem(x, 1, row[1])
                self.list.SetItem(x, 2, row[2])
                self.list.SetItem(x, 3, row[3])
                self.list.SetItem(x, 4, row[4])
                self.list.SetItem(x, 5, str(row[5]))
                self.list.SetItem(x, 6, str(row[6]))
                수입 += row[5]
                지출 += row[6]
                x += 1
            self.txtRev.SetLabel(str(수입))
            self.txtExp.SetLabel(str(지출))
            
        except Exception as e:
            print(e)
            wx.MessageBox("찾는 자료가 없습니다.", "Message" , wx.OK | wx.ICON_INFORMATION)  
        finally: 
            cur.close()
            conn.close() 
        event.Skip()
    
    def OnPieChart( self, event ):
        rows = homebookOfCRUD.selectAll()
        totalRev = 0
        totalExp = 0
    
        for row in rows:
            if row[2] == '수입':
                totalRev += int(row[5])
            elif row[2] == '지출':
                totalExp += int(row[6])
        self.panel.SetData({"수입":totalRev,"지출":totalExp}) 
        
        event.Skip()
        
    def OnBarChart( self, event ):
        firstDate = str(self.txtStart.GetValue())
        secondDate = str(self.txtEnd.GetValue())   
        rows = homebookOfCRUD.selectDate(firstDate, secondDate)
        self.OnFind(event)
        월급 = 0 
        상여금 = 0 
        기타수입 = 0 
        식비 = 0 
        교통비 = 0 
        생필품 = 0
        의류 = 0 
        의료비 = 0 
        통신비 = 0 
        공과금 = 0 
        for row in rows:
            if row[3] == '월급':
                월급 += int(row[5])
            elif row[3] == '상여금':
                상여금 += int(row[5])
            elif row[3] == '기타수입':
                기타수입 += int(row[5])
            elif row[3] == '식비':
                식비 += int(row[6])
            elif  row[3] == '교통비':
                교통비 += int(row[6])
            elif row[3] == '생필품':
                생필품 += int(row[6])
            elif row[3] == '의류':
                의류 += int(row[6])
            elif row[3] == '의료비':
                의료비 += int(row[6])
            elif row[3] == '통신비':
                통신비 += int(row[6])
            elif row[3] == '공과금':
                공과금 += int(row[6])
        self.panel.SetData2({"월급":월급,"상여금":상여금,"기타수입":기타수입,"식비":식비,"교통비":교통비,"생필품":생필품,"의류":의류,"의료비":의료비,"통신비":통신비,"공과금":공과금}) 
        event.Skip()
        
    def handle( self, event ):
        num = event.GetIndex()
        id = self.list.GetItem(num, col=0).GetText()
        day = self.list.GetItem(num, col=1).GetText()
        section = self.list.GetItem(num, col=2).GetText()
        accounttitle = self.list.GetItem(num, col=3).GetText()
        remark = self.list.GetItem(num, col=4).GetText()
        revenue = self.list.GetItem(num, col=5).GetText()
        expense= self.list.GetItem(num, col=6).GetText()
        self.txtNo.SetValue(id)
        self.txtDay.SetValue(day)
        if section == '수입':
            self.radioRev.SetValue(1)
        else:
            section == '지출'
            self.radioExp.SetValue(1)
            
        self.comboAccount.SetValue(accounttitle)
        self.txtRemark.SetValue(remark)
        self.txtRev.SetValue(revenue)
        self.txtExp.SetValue(expense)
        event.Skip()
    
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame2(None)
    frame.Show()
    app.MainLoop()

