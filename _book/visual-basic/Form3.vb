Public Class ConferenceConfirmationForm
    Private Sub ConferenceConfirmationForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        lblName.Text = ConferenceRegistrationForm.txtNameEntry.Text
        lblEmail.Text = ConferenceRegistrationForm.txtEmailEntry.Text
        lblTotal.Text = ConferenceOptionsForm.TotalCost()
    End Sub

    Private Sub btnClose_Click(sender As Object, e As EventArgs) Handles btnClose.Click
        Me.Close()
        ConferenceOptionsForm.Close()
        ConferenceRegistrationForm.Close()
    End Sub
End Class