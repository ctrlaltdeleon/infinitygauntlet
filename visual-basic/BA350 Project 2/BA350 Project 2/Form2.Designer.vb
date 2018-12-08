<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class ConferenceOptionsForm
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.GroupBox1 = New System.Windows.Forms.GroupBox()
        Me.chkOpeningNightDinner = New System.Windows.Forms.CheckBox()
        Me.chkConferenceRegistration = New System.Windows.Forms.CheckBox()
        Me.GroupBox2 = New System.Windows.Forms.GroupBox()
        Me.lstboxWorkshops = New System.Windows.Forms.ListBox()
        Me.btnReset = New System.Windows.Forms.Button()
        Me.btnClose = New System.Windows.Forms.Button()
        Me.GroupBox1.SuspendLayout()
        Me.GroupBox2.SuspendLayout()
        Me.SuspendLayout()
        '
        'GroupBox1
        '
        Me.GroupBox1.Controls.Add(Me.chkOpeningNightDinner)
        Me.GroupBox1.Controls.Add(Me.chkConferenceRegistration)
        Me.GroupBox1.Location = New System.Drawing.Point(195, 40)
        Me.GroupBox1.Name = "GroupBox1"
        Me.GroupBox1.Size = New System.Drawing.Size(374, 151)
        Me.GroupBox1.TabIndex = 0
        Me.GroupBox1.TabStop = False
        Me.GroupBox1.Text = "Conference"
        '
        'chkOpeningNightDinner
        '
        Me.chkOpeningNightDinner.AutoSize = True
        Me.chkOpeningNightDinner.Location = New System.Drawing.Point(31, 100)
        Me.chkOpeningNightDinner.Name = "chkOpeningNightDinner"
        Me.chkOpeningNightDinner.Size = New System.Drawing.Size(279, 21)
        Me.chkOpeningNightDinner.TabIndex = 1
        Me.chkOpeningNightDinner.Text = "Opening Night Dinner with Keynote $30"
        Me.chkOpeningNightDinner.UseVisualStyleBackColor = True
        '
        'chkConferenceRegistration
        '
        Me.chkConferenceRegistration.AutoSize = True
        Me.chkConferenceRegistration.Location = New System.Drawing.Point(31, 53)
        Me.chkConferenceRegistration.Name = "chkConferenceRegistration"
        Me.chkConferenceRegistration.Size = New System.Drawing.Size(219, 21)
        Me.chkConferenceRegistration.TabIndex = 0
        Me.chkConferenceRegistration.Text = "Conference Registration $500"
        Me.chkConferenceRegistration.UseVisualStyleBackColor = True
        '
        'GroupBox2
        '
        Me.GroupBox2.Controls.Add(Me.lstboxWorkshops)
        Me.GroupBox2.Location = New System.Drawing.Point(195, 219)
        Me.GroupBox2.Name = "GroupBox2"
        Me.GroupBox2.Size = New System.Drawing.Size(374, 151)
        Me.GroupBox2.TabIndex = 1
        Me.GroupBox2.TabStop = False
        Me.GroupBox2.Text = "Preconference Workshops (Select one)"
        '
        'lstboxWorkshops
        '
        Me.lstboxWorkshops.FormattingEnabled = True
        Me.lstboxWorkshops.ItemHeight = 16
        Me.lstboxWorkshops.Items.AddRange(New Object() {"Introduction to E-commerce $200.", "The Future of the Web $150.", "Advanced Visual Basic $250."})
        Me.lstboxWorkshops.Location = New System.Drawing.Point(7, 31)
        Me.lstboxWorkshops.Name = "lstboxWorkshops"
        Me.lstboxWorkshops.Size = New System.Drawing.Size(302, 100)
        Me.lstboxWorkshops.TabIndex = 0
        '
        'btnReset
        '
        Me.btnReset.Location = New System.Drawing.Point(195, 398)
        Me.btnReset.Name = "btnReset"
        Me.btnReset.Size = New System.Drawing.Size(153, 40)
        Me.btnReset.TabIndex = 2
        Me.btnReset.Text = "Reset"
        Me.btnReset.UseVisualStyleBackColor = True
        '
        'btnClose
        '
        Me.btnClose.Location = New System.Drawing.Point(416, 398)
        Me.btnClose.Name = "btnClose"
        Me.btnClose.Size = New System.Drawing.Size(153, 40)
        Me.btnClose.TabIndex = 3
        Me.btnClose.Text = "Close"
        Me.btnClose.UseVisualStyleBackColor = True
        '
        'ConferenceOptionsForm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(8.0!, 16.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(800, 450)
        Me.Controls.Add(Me.btnClose)
        Me.Controls.Add(Me.btnReset)
        Me.Controls.Add(Me.GroupBox2)
        Me.Controls.Add(Me.GroupBox1)
        Me.Name = "ConferenceOptionsForm"
        Me.Text = "Conference Options"
        Me.GroupBox1.ResumeLayout(False)
        Me.GroupBox1.PerformLayout()
        Me.GroupBox2.ResumeLayout(False)
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents GroupBox1 As GroupBox
    Friend WithEvents GroupBox2 As GroupBox
    Friend WithEvents lstboxWorkshops As ListBox
    Friend WithEvents btnReset As Button
    Friend WithEvents btnClose As Button
    Friend WithEvents chkOpeningNightDinner As CheckBox
    Friend WithEvents chkConferenceRegistration As CheckBox
End Class
