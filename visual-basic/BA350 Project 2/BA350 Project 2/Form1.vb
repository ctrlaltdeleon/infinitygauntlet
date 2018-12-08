Public Class ConferenceRegistrationForm
    Private Sub ExitCtrlQToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles ExitCtrlQToolStripMenuItem.Click
        Me.Close()
    End Sub

    Private Sub ResetCtrlRToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles ResetCtrlRToolStripMenuItem.Click
        txtNameEntry.Text = String.Empty
        txtEmailEntry.Text = String.Empty
    End Sub

    Private Sub btnConferenceOptions_Click(sender As Object, e As EventArgs) Handles btnConferenceOptions.Click
        If txtEmailEntry.Text = String.Empty Then
            txtNameEntry.Text = String.Empty
            MessageBox.Show("One or more fields are empty, please fill in the respective fields.")
        Else ConferenceOptionsForm.Show()
        End If

    End Sub

End Class