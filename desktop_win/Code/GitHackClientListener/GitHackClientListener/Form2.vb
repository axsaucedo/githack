Imports System.IO
Imports System.Text

Public Class Form2

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        If FBD1.ShowDialog = DialogResult.OK Then TextBox1.Text = FBD1.SelectedPath
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        If TextBox1.Text <> "" And TextBox2.Text <> "" Then
            Dim path As String = TextBox1.Text & "\.git\hooks\commit-msg"

            Dim FI As IO.FileInfo = New IO.FileInfo(path)

            Dim writestring = "git diff --no-ext-diff --minimal HEAD > /c/githack/" & TextBox2.Text & ".txt"
            If FI.Exists Then
                Dim st As String
                Dim is_script_install = 0
                Dim sr As StreamReader = New StreamReader(path)
                While sr.Peek <> -1
                    st = sr.ReadLine()
                    Dim len = st.Length
                    If len > 51 Then
                        If st.Substring(0, 51) = "git diff --no-ext-diff --minimal HEAD > /c/githack/" Then
                            is_script_install = 1
                        End If
                    End If
                End While
                sr.Close()
                If is_script_install = 0 Then
                    My.Computer.FileSystem.WriteAllText(path, vbCrLf & writestring & vbCrLf, True)
                End If
            Else
                ' Create or overwrite the file.
                Dim fs As FileStream = File.Create(path)

                ' Add text to the file.
                Dim info As Byte() = New UTF8Encoding(True).GetBytes("#!/bin/sh" & vbCrLf)
                fs.Write(info, 0, info.Length)
                info = New UTF8Encoding(True).GetBytes("#" & vbCrLf)
                fs.Write(info, 0, info.Length)
                info = New UTF8Encoding(True).GetBytes(writestring)
                fs.Write(info, 0, info.Length)
                fs.Close()
                Me.Close()
            End If
        Else
            MsgBox("You need to return and input all data", MsgBoxStyle.OkOnly, "Error")
        End If
    End Sub
End Class