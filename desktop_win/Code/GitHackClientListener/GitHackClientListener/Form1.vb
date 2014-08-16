Imports System.Net
Imports System.IO
Imports System.Text
Imports Newtonsoft.Json
Imports Newtonsoft.Json.Linq


Public Class Form1

    Public json_string, response, usr, password As String

    Private Sub Form1_FormClosing(sender As Object, e As FormClosingEventArgs) Handles Me.FormClosing
        Me.Hide()
        e.Cancel = True

    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Control.CheckForIllegalCrossThreadCalls = False

        Dim wacher As New FileSystemWatcher("C:\githack\")

        AddHandler wacher.Created, AddressOf ParseIt

        wacher.EnableRaisingEvents = True
        get_login_data()

        While usr = "" Or password = ""
            Dim myProcess As Process = Process.Start(Application.StartupPath & "\GitHackLogin.exe")
            Do While Not myProcess.HasExited
                Application.DoEvents()
            Loop
            myProcess.WaitForExit()
            myProcess.Close()
            get_login_data()
        End While

    End Sub

    Private Sub NotifyIcon1_MouseDoubleClick(sender As Object, e As MouseEventArgs) Handles NotifyIcon1.MouseDoubleClick
        Me.Show()
    End Sub
    Private Sub ParseIt(source As Object, e As FileSystemEventArgs)
        System.Threading.Thread.Sleep(2000)


        Dim sr As StreamReader = New StreamReader(e.FullPath)

        Dim linesadded = -1, linesremoved = -1
        Dim inputtime As Long
        Dim st, vimsupport As String
        inputtime = UnixTimestamp(Date.UtcNow)
        vimsupport = "0"
        While sr.Peek <> -1
            st = sr.ReadLine()
            If st.Substring(0, 1) = "+" Then
                linesadded = linesadded + 1
            End If
            If st.Substring(0, 1) = "-" Then
                linesremoved = linesremoved + 1
            End If
        End While
        sr.Close()

        Dim url = New Uri("http://githack.ninja/usercommit/")
        Dim data = Encoding.UTF8.GetBytes("{" & Chr(34) & "linesadded" & Chr(34) & " : " & linesadded & ", " & Chr(34) & "linesremoved" & Chr(34) & " : " & linesremoved & ", " & Chr(34) & "inputtime" & Chr(34) & " : " & inputtime / 1000 & ", " & Chr(34) & "inputsessions" & Chr(34) & " : 0" & ", " & Chr(34) & "user" & Chr(34) & " : " & Chr(34) & usr & Chr(34) & ", " & Chr(34) & "password" & Chr(34) & " : " & Chr(34) & password & Chr(34) & ", " & Chr(34) & "vimsupport" & Chr(34) & " : " & vimsupport & "}")
        response = SendRequest(url, data, "application/json", "POST")

        Dim json_resp = JObject.Parse(response)
        Dim text As String
        text = json_resp.GetValue("text")

        response = text

        TB.Text = TB.Text & response
        Me.Visible = True

        File.Delete(e.FullPath)
    End Sub

    Private Function SendRequest(uri As Uri, jsonDataBytes As Byte(), contentType As String, method As String) As String
        Dim req As WebRequest = WebRequest.Create(uri)
        req.ContentType = contentType
        req.Method = method
        req.ContentLength = jsonDataBytes.Length


        Dim stream = req.GetRequestStream()
        stream.Write(jsonDataBytes, 0, jsonDataBytes.Length)
        stream.Close()

        Dim response = CType(req.GetResponse(), HttpWebResponse)

        Dim reader = New StreamReader(response.GetResponseStream)

        Dim res = reader.ReadToEnd()
        reader.Close()

        response.Close()
        Return res
    End Function
    Private Function UnixTimestamp(target As DateTime) As Long
        Dim Unidate = New DateTime(1970, 1, 1, 0, 0, 0, target.Kind)
        Dim hubspotTimestamp = System.Convert.ToInt64((target - Unidate).TotalSeconds)

        Return hubspotTimestamp * 1000
    End Function

    Private Sub ВыходToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles ВыходToolStripMenuItem.Click
        NotifyIcon1.Dispose()

        Process.GetCurrentProcess().Kill()

    End Sub

    Private Sub Form1_MouseClick(sender As Object, e As MouseEventArgs) Handles Me.MouseClick
        TB.Text = TB.Text & response
    End Sub

    Private Sub AddNewGitRepoToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles AddNewGitRepoToolStripMenuItem.Click
        Form2.Show()

    End Sub

    Private Function get_login_data()
        usr = My.Computer.Registry.GetValue("HKEY_CURRENT_USER\Software\GitHackClient", "login", "")
        password = My.Computer.Registry.GetValue("HKEY_CURRENT_USER\Software\GitHackClient", "pass", "")
    End Function

    Private Sub GithackPrrofileToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles GithackPrrofileToolStripMenuItem.Click
        Process.Start("http://githack.ninja/accounts/view/")
    End Sub
End Class

