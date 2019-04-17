Public Class ConferenceOptionsForm

    Public Function TotalCost()
        Dim dblRegistration As Double
        Dim dblOpeningNight As Double
        Dim dblOptCon As Double

        If chkConferenceRegistration.Checked = True Then
            dblRegistration += 500
        Else
            dblRegistration = 0
        End If

        If chkOpeningNightDinner.Checked = True Then
            dblOpeningNight += 30
        Else
            dblOpeningNight = 0
        End If

        If lstboxWorkshops.SelectedIndex = 0 Then
            dblOptCon += 200
        ElseIf lstboxWorkshops.SelectedIndex = 1 Then
            dblOptCon += 150
        ElseIf lstboxWorkshops.SelectedIndex = 2 Then
            dblOptCon += 250
        ElseIf lstboxWorkshops.SelectedIndex = -1 Then
            dblOptCon = 0
        End If

        dblTotalCost = (dblRegistration + dblOpeningNight + dblOptCon).ToString("c")

        Return dblTotalCost
    End Function


    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles btnClose.Click
        If chkConferenceRegistration.Checked = False Then
            MessageBox.Show("It is required to purchase a conference registration ticket!")
        Else
            ConferenceConfirmationForm.Show()
            ConferenceRegistrationForm.Hide()
            Me.Hide()
        End If
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles btnReset.Click
        lstboxWorkshops.ClearSelected()
        chkConferenceRegistration.Checked = False
        chkOpeningNightDinner.Checked = False
    End Sub
End Class