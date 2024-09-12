# LastnameP11
# Programmer: Your Name
# Email: your.email@example.com
# Purpose: demonstrate how to use a GUI

import wx
from LastnameP10 import GeoPoint, read_points_from_file, find_closest_point

class GeoPointApp(wx.Frame):
    def __init__(self, *args, **kw):
        super(GeoPointApp, self).__init__(*args, **kw)        
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='File Name:')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.file_name = wx.TextCtrl(panel)
        hbox1.Add(self.file_name, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Your Latitude:')
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        self.user_lat = wx.TextCtrl(panel)
        hbox2.Add(self.user_lat, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(panel, label='Your Longitude:')
        hbox3.Add(st3, flag=wx.RIGHT, border=8)
        self.user_lon = wx.TextCtrl(panel)
        hbox3.Add(self.user_lon, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(panel, label='Find Closest Point', size=(150, 30))
        hbox4.Add(btn)
        btn.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        vbox.Add(hbox4, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        st4 = wx.StaticText(panel, label='Closest Point:')
        hbox5.Add(st4, flag=wx.RIGHT, border=8)
        self.result = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY)
        hbox5.Add(self.result, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox5, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, border=10)

        panel.SetSizer(vbox)

        self.SetTitle('GeoPoint Finder')
        self.Centre()

    def OnButtonClick(self, event):
        file_name = self.file_name.GetValue()
        try:
            user_lat = float(self.user_lat.GetValue())
            user_lon = float(self.user_lon.GetValue())
        except ValueError:
            wx.MessageBox('Please enter valid numbers for latitude and longitude.', 'Error', wx.OK | wx.ICON_ERROR)
            return

        try:
            point_list = read_points_from_file(file_name)
        except FileNotFoundError:
            wx.MessageBox(f'File {file_name} not found.', 'Error', wx.OK | wx.ICON_ERROR)
            return

        user_point = GeoPoint(user_lat, user_lon, "Your Location")
        closest_point = find_closest_point(user_point, point_list)
        
        result_msg = f"You are closest to {closest_point.description} which is located at ({closest_point.lat}, {closest_point.lon})"
        self.result.SetValue(result_msg)

def main():
    app = wx.App()
    ex = GeoPointApp(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
