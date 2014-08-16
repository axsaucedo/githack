Public Class Form1

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        tb_passwd.PasswordChar = Chr(149)
    End Sub

    Private Sub btn_login_Click(sender As Object, e As EventArgs) Handles btn_login.Click
        If tb_email.Text <> "" Or tb_email.Text <> "" Then
            My.Computer.Registry.CurrentUser.CreateSubKey("Software\GitHackClient")
            My.Computer.Registry.SetValue("HKEY_CURRENT_USER\Software\GitHackClient", "login", tb_email.Text)
            My.Computer.Registry.SetValue("HKEY_CURRENT_USER\Software\GitHackClient", "pass", tb_passwd.Text)
        Else
            MsgBox("You need to return and input all data", MsgBoxStyle.OkOnly, "Error")
        End If
    End Sub
End Class
