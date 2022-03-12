<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class ConferenceRegistrationForm
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
        Me.MenuStrip1 = New System.Windows.Forms.MenuStrip()
        Me.FileToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.ResetCtrlRToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.ExitCtrlQToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.HelpToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.AboutToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.GroupBox1 = New System.Windows.Forms.GroupBox()
        Me.txtNameEntry = New System.Windows.Forms.TextBox()
        Me.txtEmailEntry = New System.Windows.Forms.TextBox()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.btnConferenceOptions = New System.Windows.Forms.Button()
        Me.MenuStrip1.SuspendLayout()
        Me.GroupBox1.SuspendLayout()
        Me.SuspendLayout()
        '
        'MenuStrip1
        '
        Me.MenuStrip1.ImageScalingSize = New System.Drawing.Size(20, 20)
        Me.MenuStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.FileToolStripMenuItem, Me.HelpToolStripMenuItem})
        Me.MenuStrip1.Location = New System.Drawing.Point(0, 0)
        Me.MenuStrip1.Name = "MenuStrip1"
        Me.MenuStrip1.Size = New System.Drawing.Size(800, 28)
        Me.MenuStrip1.TabIndex = 0
        Me.MenuStrip1.Text = "MenuStrip1"
        '
        'FileToolStripMenuItem
        '
        Me.FileToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.ResetCtrlRToolStripMenuItem, Me.ExitCtrlQToolStripMenuItem})
        Me.FileToolStripMenuItem.Name = "FileToolStripMenuItem"
        Me.FileToolStripMenuItem.Size = New System.Drawing.Size(44, 24)
        Me.FileToolStripMenuItem.Text = "&File"
        '
        'ResetCtrlRToolStripMenuItem
        '
        Me.ResetCtrlRToolStripMenuItem.Name = "ResetCtrlRToolStripMenuItem"
        Me.ResetCtrlRToolStripMenuItem.ShortcutKeyDisplayString = "Ctrl + R"
        Me.ResetCtrlRToolStripMenuItem.Size = New System.Drawing.Size(216, 26)
        Me.ResetCtrlRToolStripMenuItem.Text = "Reset "
        '
        'ExitCtrlQToolStripMenuItem
        '
        Me.ExitCtrlQToolStripMenuItem.Name = "ExitCtrlQToolStripMenuItem"
        Me.ExitCtrlQToolStripMenuItem.ShortcutKeyDisplayString = "Ctrl + Q"
        Me.ExitCtrlQToolStripMenuItem.Size = New System.Drawing.Size(216, 26)
        Me.ExitCtrlQToolStripMenuItem.Text = "Exit "
        '
        'HelpToolStripMenuItem
        '
        Me.HelpToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.AboutToolStripMenuItem})
        Me.HelpToolStripMenuItem.Name = "HelpToolStripMenuItem"
        Me.HelpToolStripMenuItem.Size = New System.Drawing.Size(53, 24)
        Me.HelpToolStripMenuItem.Text = "&Help"
        '
        'AboutToolStripMenuItem
        '
        Me.AboutToolStripMenuItem.Name = "AboutToolStripMenuItem"
        Me.AboutToolStripMenuItem.Size = New System.Drawing.Size(216, 26)
        Me.AboutToolStripMenuItem.Text = "About"
        '
        'GroupBox1
        '
        Me.GroupBox1.Controls.Add(Me.txtNameEntry)
        Me.GroupBox1.Controls.Add(Me.txtEmailEntry)
        Me.GroupBox1.Controls.Add(Me.Label2)
        Me.GroupBox1.Controls.Add(Me.Label1)
        Me.GroupBox1.Location = New System.Drawing.Point(76, 125)
        Me.GroupBox1.Name = "GroupBox1"
        Me.GroupBox1.Size = New System.Drawing.Size(648, 180)
        Me.GroupBox1.TabIndex = 1
        Me.GroupBox1.TabStop = False
        Me.GroupBox1.Text = "Registrant"
        '
        'txtNameEntry
        '
        Me.txtNameEntry.Location = New System.Drawing.Point(91, 64)
        Me.txtNameEntry.Name = "txtNameEntry"
        Me.txtNameEntry.Size = New System.Drawing.Size(222, 22)
        Me.txtNameEntry.TabIndex = 3
        '
        'txtEmailEntry
        '
        Me.txtEmailEntry.Location = New System.Drawing.Point(394, 64)
        Me.txtEmailEntry.Name = "txtEmailEntry"
        Me.txtEmailEntry.Size = New System.Drawing.Size(222, 22)
        Me.txtEmailEntry.TabIndex = 2
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(331, 64)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(42, 17)
        Me.Label2.TabIndex = 1
        Me.Label2.Text = "Email"
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(40, 64)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(45, 17)
        Me.Label1.TabIndex = 0
        Me.Label1.Text = "Name"
        '
        'btnConferenceOptions
        '
        Me.btnConferenceOptions.FlatStyle = System.Windows.Forms.FlatStyle.System
        Me.btnConferenceOptions.Location = New System.Drawing.Point(291, 348)
        Me.btnConferenceOptions.Name = "btnConferenceOptions"
        Me.btnConferenceOptions.Size = New System.Drawing.Size(268, 43)
        Me.btnConferenceOptions.TabIndex = 2
        Me.btnConferenceOptions.Text = "Select Conference Options"
        Me.btnConferenceOptions.UseVisualStyleBackColor = True
        '
        'ConferenceRegistrationForm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(8.0!, 16.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(800, 450)
        Me.Controls.Add(Me.btnConferenceOptions)
        Me.Controls.Add(Me.GroupBox1)
        Me.Controls.Add(Me.MenuStrip1)
        Me.MainMenuStrip = Me.MenuStrip1
        Me.Name = "ConferenceRegistrationForm"
        Me.Text = "Conference Registration System"
        Me.MenuStrip1.ResumeLayout(False)
        Me.MenuStrip1.PerformLayout()
        Me.GroupBox1.ResumeLayout(False)
        Me.GroupBox1.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents MenuStrip1 As MenuStrip
    Friend WithEvents FileToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents ResetCtrlRToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents ExitCtrlQToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents HelpToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents AboutToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents GroupBox1 As GroupBox
    Friend WithEvents txtNameEntry As TextBox
    Friend WithEvents txtEmailEntry As TextBox
    Friend WithEvents Label2 As Label
    Friend WithEvents Label1 As Label
    Friend WithEvents btnConferenceOptions As Button
End Class
