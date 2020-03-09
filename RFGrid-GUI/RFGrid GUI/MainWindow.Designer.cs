namespace RFGrid_GUI
{
    partial class MainWindow
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainWindow));
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.displayCalibrationGroupBox = new System.Windows.Forms.GroupBox();
            this.YLabel = new System.Windows.Forms.Label();
            this.XLabel = new System.Windows.Forms.Label();
            this.dispCalibYBox = new System.Windows.Forms.TextBox();
            this.dispCalibrateButton = new System.Windows.Forms.Button();
            this.displayInfoButton = new System.Windows.Forms.Button();
            this.dispCalibXBox = new System.Windows.Forms.TextBox();
            this.gridSizeLabel = new System.Windows.Forms.Label();
            this.connectedPortLabel = new System.Windows.Forms.Label();
            this.portTextLabel = new System.Windows.Forms.Label();
            this.backgroundCalibrationGroupBox = new System.Windows.Forms.GroupBox();
            this.backgroundCalibPictureBox = new System.Windows.Forms.PictureBox();
            this.label6 = new System.Windows.Forms.Label();
            this.backgroundCalibButton = new System.Windows.Forms.Button();
            this.backgroundImgButton = new System.Windows.Forms.Button();
            this.backgroundImgTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.debugTextBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.ApplicationsGroupBox = new System.Windows.Forms.GroupBox();
            this.ApplicationsRefreshButton = new System.Windows.Forms.Button();
            this.DeleteApplicationButton = new System.Windows.Forms.Button();
            this.LoadApplicationButton = new System.Windows.Forms.Button();
            this.createNewApplicationButton = new System.Windows.Forms.Button();
            this.ApplicationsList = new System.Windows.Forms.ListBox();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exitToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.settingsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.chooseCOMToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.installModulesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.LaunchButton = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.loadedConfigurationLabel = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.tagInfoListView = new System.Windows.Forms.ListView();
            this.IDLabel = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.ImageLabelListView = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.EntranceSoundLabel = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.UpdateSoundListView = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.TagCreatorGroupBox = new System.Windows.Forms.GroupBox();
            this.EntranceSoundPlayButton = new System.Windows.Forms.Button();
            this.UpdateSoundPlayButton = new System.Windows.Forms.Button();
            this.label10 = new System.Windows.Forms.Label();
            this.tagCreatorPreviewBox = new System.Windows.Forms.PictureBox();
            this.label8 = new System.Windows.Forms.Label();
            this.secondSoundButton = new System.Windows.Forms.Button();
            this.secondSoundTextBox = new System.Windows.Forms.TextBox();
            this.tagGetIdButton = new System.Windows.Forms.Button();
            this.tagBox = new System.Windows.Forms.TextBox();
            this.soundButton = new System.Windows.Forms.Button();
            this.tagLabel = new System.Windows.Forms.Label();
            this.soundTextBox = new System.Windows.Forms.TextBox();
            this.imageLabel = new System.Windows.Forms.Label();
            this.clearButton = new System.Windows.Forms.Button();
            this.label9 = new System.Windows.Forms.Label();
            this.saveButton = new System.Windows.Forms.Button();
            this.imageTextBox = new System.Windows.Forms.TextBox();
            this.imageButton = new System.Windows.Forms.Button();
            this.stopPlayingButton = new System.Windows.Forms.Button();
            this.errorProvider1 = new System.Windows.Forms.ErrorProvider(this.components);
            this.displayCalibrationGroupBox.SuspendLayout();
            this.backgroundCalibrationGroupBox.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.backgroundCalibPictureBox)).BeginInit();
            this.ApplicationsGroupBox.SuspendLayout();
            this.menuStrip1.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.TagCreatorGroupBox.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.tagCreatorPreviewBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.errorProvider1)).BeginInit();
            this.SuspendLayout();
            // 
            // displayCalibrationGroupBox
            // 
            this.displayCalibrationGroupBox.BackColor = System.Drawing.Color.Transparent;
            this.displayCalibrationGroupBox.Controls.Add(this.YLabel);
            this.displayCalibrationGroupBox.Controls.Add(this.XLabel);
            this.displayCalibrationGroupBox.Controls.Add(this.dispCalibYBox);
            this.displayCalibrationGroupBox.Controls.Add(this.dispCalibrateButton);
            this.displayCalibrationGroupBox.Controls.Add(this.displayInfoButton);
            this.displayCalibrationGroupBox.Controls.Add(this.dispCalibXBox);
            this.displayCalibrationGroupBox.Controls.Add(this.gridSizeLabel);
            this.displayCalibrationGroupBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.displayCalibrationGroupBox.ForeColor = System.Drawing.Color.Black;
            this.displayCalibrationGroupBox.Location = new System.Drawing.Point(502, 60);
            this.displayCalibrationGroupBox.Name = "displayCalibrationGroupBox";
            this.displayCalibrationGroupBox.Size = new System.Drawing.Size(659, 189);
            this.displayCalibrationGroupBox.TabIndex = 12;
            this.displayCalibrationGroupBox.TabStop = false;
            this.displayCalibrationGroupBox.Text = "1) Display Calibration";
            // 
            // YLabel
            // 
            this.YLabel.AutoSize = true;
            this.YLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.YLabel.Location = new System.Drawing.Point(24, 90);
            this.YLabel.Name = "YLabel";
            this.YLabel.Size = new System.Drawing.Size(24, 20);
            this.YLabel.TabIndex = 6;
            this.YLabel.Text = "Y :";
            // 
            // XLabel
            // 
            this.XLabel.AutoSize = true;
            this.XLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.XLabel.Location = new System.Drawing.Point(24, 60);
            this.XLabel.Name = "XLabel";
            this.XLabel.Size = new System.Drawing.Size(26, 20);
            this.XLabel.TabIndex = 5;
            this.XLabel.Text = "X :";
            // 
            // dispCalibYBox
            // 
            this.dispCalibYBox.BackColor = System.Drawing.Color.Snow;
            this.dispCalibYBox.Location = new System.Drawing.Point(56, 92);
            this.dispCalibYBox.MaxLength = 2;
            this.dispCalibYBox.Name = "dispCalibYBox";
            this.dispCalibYBox.Size = new System.Drawing.Size(59, 26);
            this.dispCalibYBox.TabIndex = 4;
            this.dispCalibYBox.Text = "8";
            this.dispCalibYBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.dispCalibYBox.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.DispCalibYBox_TextChanged);
            // 
            // dispCalibrateButton
            // 
            this.dispCalibrateButton.BackColor = System.Drawing.SystemColors.Control;
            this.dispCalibrateButton.FlatAppearance.BorderSize = 0;
            this.dispCalibrateButton.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.dispCalibrateButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.dispCalibrateButton.Location = new System.Drawing.Point(38, 135);
            this.dispCalibrateButton.Name = "dispCalibrateButton";
            this.dispCalibrateButton.Size = new System.Drawing.Size(87, 24);
            this.dispCalibrateButton.TabIndex = 3;
            this.dispCalibrateButton.Text = "Calibrate";
            this.dispCalibrateButton.UseVisualStyleBackColor = true;
            this.dispCalibrateButton.Click += new System.EventHandler(this.DispCalibrateButton_Click);
            // 
            // displayInfoButton
            // 
            this.displayInfoButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(61)))), ((int)(((byte)(64)))), ((int)(((byte)(71)))));
            this.displayInfoButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.displayInfoButton.Font = new System.Drawing.Font("Calibri", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.displayInfoButton.ForeColor = System.Drawing.Color.White;
            this.displayInfoButton.Location = new System.Drawing.Point(152, 25);
            this.displayInfoButton.Name = "displayInfoButton";
            this.displayInfoButton.Size = new System.Drawing.Size(22, 23);
            this.displayInfoButton.TabIndex = 2;
            this.displayInfoButton.Text = "?";
            this.displayInfoButton.UseVisualStyleBackColor = false;
            this.displayInfoButton.Click += new System.EventHandler(this.DisplayInfoButton_Click);
            // 
            // dispCalibXBox
            // 
            this.dispCalibXBox.BackColor = System.Drawing.Color.Snow;
            this.dispCalibXBox.Location = new System.Drawing.Point(56, 60);
            this.dispCalibXBox.MaxLength = 2;
            this.dispCalibXBox.Name = "dispCalibXBox";
            this.dispCalibXBox.Size = new System.Drawing.Size(59, 26);
            this.dispCalibXBox.TabIndex = 1;
            this.dispCalibXBox.Text = "8";
            this.dispCalibXBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.dispCalibXBox.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.DispCalibXBox_TextChanged);
            // 
            // gridSizeLabel
            // 
            this.gridSizeLabel.AutoSize = true;
            this.gridSizeLabel.Font = new System.Drawing.Font("Century Gothic", 12F);
            this.gridSizeLabel.Location = new System.Drawing.Point(14, 27);
            this.gridSizeLabel.Name = "gridSizeLabel";
            this.gridSizeLabel.Size = new System.Drawing.Size(132, 21);
            this.gridSizeLabel.TabIndex = 0;
            this.gridSizeLabel.Text = "Grid Dimensions";
            // 
            // connectedPortLabel
            // 
            this.connectedPortLabel.AutoSize = true;
            this.connectedPortLabel.Enabled = false;
            this.connectedPortLabel.ForeColor = System.Drawing.Color.Black;
            this.connectedPortLabel.Location = new System.Drawing.Point(982, 34);
            this.connectedPortLabel.Name = "connectedPortLabel";
            this.connectedPortLabel.Size = new System.Drawing.Size(84, 13);
            this.connectedPortLabel.TabIndex = 13;
            this.connectedPortLabel.Text = "Connected Port:";
            this.connectedPortLabel.Visible = false;
            // 
            // portTextLabel
            // 
            this.portTextLabel.AutoSize = true;
            this.portTextLabel.Enabled = false;
            this.portTextLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.portTextLabel.ForeColor = System.Drawing.Color.Black;
            this.portTextLabel.Location = new System.Drawing.Point(1072, 34);
            this.portTextLabel.Name = "portTextLabel";
            this.portTextLabel.Size = new System.Drawing.Size(22, 13);
            this.portTextLabel.TabIndex = 14;
            this.portTextLabel.Text = "NA";
            this.portTextLabel.Visible = false;
            // 
            // backgroundCalibrationGroupBox
            // 
            this.backgroundCalibrationGroupBox.BackColor = System.Drawing.Color.Transparent;
            this.backgroundCalibrationGroupBox.Controls.Add(this.backgroundCalibPictureBox);
            this.backgroundCalibrationGroupBox.Controls.Add(this.label6);
            this.backgroundCalibrationGroupBox.Controls.Add(this.backgroundCalibButton);
            this.backgroundCalibrationGroupBox.Controls.Add(this.backgroundImgButton);
            this.backgroundCalibrationGroupBox.Controls.Add(this.backgroundImgTextBox);
            this.backgroundCalibrationGroupBox.Controls.Add(this.label2);
            this.backgroundCalibrationGroupBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.backgroundCalibrationGroupBox.ForeColor = System.Drawing.Color.Black;
            this.backgroundCalibrationGroupBox.Location = new System.Drawing.Point(502, 255);
            this.backgroundCalibrationGroupBox.Name = "backgroundCalibrationGroupBox";
            this.backgroundCalibrationGroupBox.Size = new System.Drawing.Size(659, 222);
            this.backgroundCalibrationGroupBox.TabIndex = 15;
            this.backgroundCalibrationGroupBox.TabStop = false;
            this.backgroundCalibrationGroupBox.Text = "2) Background Calibration";
            // 
            // backgroundCalibPictureBox
            // 
            this.backgroundCalibPictureBox.Location = new System.Drawing.Point(371, 31);
            this.backgroundCalibPictureBox.Name = "backgroundCalibPictureBox";
            this.backgroundCalibPictureBox.Size = new System.Drawing.Size(225, 185);
            this.backgroundCalibPictureBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.backgroundCalibPictureBox.TabIndex = 9;
            this.backgroundCalibPictureBox.TabStop = false;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(296, 31);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(69, 18);
            this.label6.TabIndex = 8;
            this.label6.Text = "Preview:";
            // 
            // backgroundCalibButton
            // 
            this.backgroundCalibButton.BackColor = System.Drawing.SystemColors.Control;
            this.backgroundCalibButton.FlatAppearance.BorderSize = 0;
            this.backgroundCalibButton.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.backgroundCalibButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.backgroundCalibButton.Location = new System.Drawing.Point(59, 174);
            this.backgroundCalibButton.Name = "backgroundCalibButton";
            this.backgroundCalibButton.Size = new System.Drawing.Size(87, 26);
            this.backgroundCalibButton.TabIndex = 3;
            this.backgroundCalibButton.Text = "Calibrate";
            this.backgroundCalibButton.UseVisualStyleBackColor = true;
            this.backgroundCalibButton.Click += new System.EventHandler(this.BackgroundCalibButton_Click);
            // 
            // backgroundImgButton
            // 
            this.backgroundImgButton.BackColor = System.Drawing.SystemColors.Control;
            this.backgroundImgButton.FlatAppearance.BorderSize = 0;
            this.backgroundImgButton.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.backgroundImgButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.backgroundImgButton.Location = new System.Drawing.Point(217, 77);
            this.backgroundImgButton.Name = "backgroundImgButton";
            this.backgroundImgButton.Size = new System.Drawing.Size(82, 25);
            this.backgroundImgButton.TabIndex = 2;
            this.backgroundImgButton.Text = "Browse";
            this.backgroundImgButton.UseVisualStyleBackColor = true;
            this.backgroundImgButton.Click += new System.EventHandler(this.BackgroundImgButton_Click);
            // 
            // backgroundImgTextBox
            // 
            this.backgroundImgTextBox.BackColor = System.Drawing.Color.Snow;
            this.backgroundImgTextBox.Location = new System.Drawing.Point(14, 77);
            this.backgroundImgTextBox.Name = "backgroundImgTextBox";
            this.backgroundImgTextBox.Size = new System.Drawing.Size(181, 26);
            this.backgroundImgTextBox.TabIndex = 1;
            this.backgroundImgTextBox.Text = "default.jpg";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.label2.Location = new System.Drawing.Point(10, 35);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(151, 20);
            this.label2.TabIndex = 0;
            this.label2.Text = "Background Image";
            // 
            // debugTextBox
            // 
            this.debugTextBox.BackColor = System.Drawing.Color.Snow;
            this.debugTextBox.Location = new System.Drawing.Point(12, 755);
            this.debugTextBox.Multiline = true;
            this.debugTextBox.Name = "debugTextBox";
            this.debugTextBox.ReadOnly = true;
            this.debugTextBox.Size = new System.Drawing.Size(969, 116);
            this.debugTextBox.TabIndex = 16;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.label3.ForeColor = System.Drawing.Color.Black;
            this.label3.Location = new System.Drawing.Point(12, 734);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(57, 18);
            this.label3.TabIndex = 17;
            this.label3.Text = "Output";
            // 
            // ApplicationsGroupBox
            // 
            this.ApplicationsGroupBox.Controls.Add(this.ApplicationsRefreshButton);
            this.ApplicationsGroupBox.Controls.Add(this.DeleteApplicationButton);
            this.ApplicationsGroupBox.Controls.Add(this.LoadApplicationButton);
            this.ApplicationsGroupBox.Controls.Add(this.createNewApplicationButton);
            this.ApplicationsGroupBox.Controls.Add(this.ApplicationsList);
            this.ApplicationsGroupBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.ApplicationsGroupBox.ForeColor = System.Drawing.Color.Black;
            this.ApplicationsGroupBox.Location = new System.Drawing.Point(19, 60);
            this.ApplicationsGroupBox.Name = "ApplicationsGroupBox";
            this.ApplicationsGroupBox.Size = new System.Drawing.Size(472, 189);
            this.ApplicationsGroupBox.TabIndex = 18;
            this.ApplicationsGroupBox.TabStop = false;
            this.ApplicationsGroupBox.Text = "Applications";
            // 
            // ApplicationsRefreshButton
            // 
            this.ApplicationsRefreshButton.BackColor = System.Drawing.SystemColors.Control;
            this.ApplicationsRefreshButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.ApplicationsRefreshButton.FlatAppearance.BorderSize = 0;
            this.ApplicationsRefreshButton.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.ApplicationsRefreshButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.ApplicationsRefreshButton.Location = new System.Drawing.Point(367, 27);
            this.ApplicationsRefreshButton.Name = "ApplicationsRefreshButton";
            this.ApplicationsRefreshButton.Size = new System.Drawing.Size(86, 24);
            this.ApplicationsRefreshButton.TabIndex = 2;
            this.ApplicationsRefreshButton.Text = "Refresh";
            this.ApplicationsRefreshButton.UseVisualStyleBackColor = true;
            this.ApplicationsRefreshButton.Click += new System.EventHandler(this.ApplicationsRefreshButton_Click);
            // 
            // DeleteApplicationButton
            // 
            this.DeleteApplicationButton.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.DeleteApplicationButton.FlatAppearance.BorderSize = 0;
            this.DeleteApplicationButton.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.DeleteApplicationButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.DeleteApplicationButton.Location = new System.Drawing.Point(367, 124);
            this.DeleteApplicationButton.Name = "DeleteApplicationButton";
            this.DeleteApplicationButton.Size = new System.Drawing.Size(86, 24);
            this.DeleteApplicationButton.TabIndex = 23;
            this.DeleteApplicationButton.Text = "Delete";
            this.DeleteApplicationButton.UseVisualStyleBackColor = true;
            this.DeleteApplicationButton.Click += new System.EventHandler(this.DeleteApplicationButton_Click);
            // 
            // LoadApplicationButton
            // 
            this.LoadApplicationButton.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.LoadApplicationButton.FlatAppearance.BorderSize = 0;
            this.LoadApplicationButton.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.LoadApplicationButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.LoadApplicationButton.Location = new System.Drawing.Point(367, 93);
            this.LoadApplicationButton.Name = "LoadApplicationButton";
            this.LoadApplicationButton.Size = new System.Drawing.Size(87, 25);
            this.LoadApplicationButton.TabIndex = 21;
            this.LoadApplicationButton.Text = "Load";
            this.LoadApplicationButton.UseVisualStyleBackColor = true;
            this.LoadApplicationButton.Click += new System.EventHandler(this.openExistingApplicationButton_Click);
            // 
            // createNewApplicationButton
            // 
            this.createNewApplicationButton.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.createNewApplicationButton.FlatAppearance.BorderSize = 0;
            this.createNewApplicationButton.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.createNewApplicationButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.createNewApplicationButton.Location = new System.Drawing.Point(366, 60);
            this.createNewApplicationButton.Name = "createNewApplicationButton";
            this.createNewApplicationButton.Size = new System.Drawing.Size(86, 26);
            this.createNewApplicationButton.TabIndex = 22;
            this.createNewApplicationButton.Text = "New Game";
            this.createNewApplicationButton.UseVisualStyleBackColor = true;
            this.createNewApplicationButton.Click += new System.EventHandler(this.createNewApplicationButton_Click);
            // 
            // ApplicationsList
            // 
            this.ApplicationsList.BackColor = System.Drawing.Color.Snow;
            this.ApplicationsList.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.ApplicationsList.FormattingEnabled = true;
            this.ApplicationsList.ItemHeight = 20;
            this.ApplicationsList.Location = new System.Drawing.Point(15, 25);
            this.ApplicationsList.Name = "ApplicationsList";
            this.ApplicationsList.Size = new System.Drawing.Size(324, 144);
            this.ApplicationsList.TabIndex = 0;
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.aboutToolStripMenuItem,
            this.exitToolStripMenuItem});
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(50, 20);
            this.toolStripMenuItem1.Text = "Menu";
            // 
            // aboutToolStripMenuItem
            // 
            this.aboutToolStripMenuItem.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(81)))), ((int)(((byte)(84)))), ((int)(((byte)(101)))));
            this.aboutToolStripMenuItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.aboutToolStripMenuItem.ForeColor = System.Drawing.Color.White;
            this.aboutToolStripMenuItem.Name = "aboutToolStripMenuItem";
            this.aboutToolStripMenuItem.Size = new System.Drawing.Size(107, 22);
            this.aboutToolStripMenuItem.Text = "About";
            this.aboutToolStripMenuItem.Click += new System.EventHandler(this.AboutToolStripMenuItem_Click);
            // 
            // exitToolStripMenuItem
            // 
            this.exitToolStripMenuItem.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(81)))), ((int)(((byte)(84)))), ((int)(((byte)(101)))));
            this.exitToolStripMenuItem.ForeColor = System.Drawing.Color.White;
            this.exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            this.exitToolStripMenuItem.Size = new System.Drawing.Size(107, 22);
            this.exitToolStripMenuItem.Text = "Exit";
            this.exitToolStripMenuItem.Click += new System.EventHandler(this.ExitToolStripMenuItem_Click);
            // 
            // settingsToolStripMenuItem
            // 
            this.settingsToolStripMenuItem.BackColor = System.Drawing.SystemColors.Control;
            this.settingsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.chooseCOMToolStripMenuItem,
            this.installModulesToolStripMenuItem});
            this.settingsToolStripMenuItem.ForeColor = System.Drawing.Color.Black;
            this.settingsToolStripMenuItem.Name = "settingsToolStripMenuItem";
            this.settingsToolStripMenuItem.Size = new System.Drawing.Size(61, 20);
            this.settingsToolStripMenuItem.Text = "Settings";
            // 
            // chooseCOMToolStripMenuItem
            // 
            this.chooseCOMToolStripMenuItem.BackColor = System.Drawing.SystemColors.Control;
            this.chooseCOMToolStripMenuItem.ForeColor = System.Drawing.Color.Black;
            this.chooseCOMToolStripMenuItem.Name = "chooseCOMToolStripMenuItem";
            this.chooseCOMToolStripMenuItem.Size = new System.Drawing.Size(195, 22);
            this.chooseCOMToolStripMenuItem.Text = "Select Connection Port";
            this.chooseCOMToolStripMenuItem.Click += new System.EventHandler(this.ChooseCOMToolStripMenuItem_Click);
            // 
            // installModulesToolStripMenuItem
            // 
            this.installModulesToolStripMenuItem.BackColor = System.Drawing.SystemColors.Control;
            this.installModulesToolStripMenuItem.ForeColor = System.Drawing.Color.Black;
            this.installModulesToolStripMenuItem.Name = "installModulesToolStripMenuItem";
            this.installModulesToolStripMenuItem.Size = new System.Drawing.Size(195, 22);
            this.installModulesToolStripMenuItem.Text = "Install Modules";
            this.installModulesToolStripMenuItem.Click += new System.EventHandler(this.InstallModulesToolStripMenuItem_Click);
            // 
            // menuStrip1
            // 
            this.menuStrip1.BackColor = System.Drawing.SystemColors.Control;
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripMenuItem1,
            this.settingsToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1168, 24);
            this.menuStrip1.TabIndex = 10;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // LaunchButton
            // 
            this.LaunchButton.BackColor = System.Drawing.SystemColors.Control;
            this.LaunchButton.FlatAppearance.BorderSize = 0;
            this.LaunchButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.LaunchButton.Location = new System.Drawing.Point(991, 755);
            this.LaunchButton.Name = "LaunchButton";
            this.LaunchButton.Size = new System.Drawing.Size(170, 108);
            this.LaunchButton.TabIndex = 19;
            this.LaunchButton.Text = "Click to Launch";
            this.LaunchButton.UseVisualStyleBackColor = false;
            this.LaunchButton.Click += new System.EventHandler(this.LaunchButton_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.ForeColor = System.Drawing.Color.Black;
            this.label5.Location = new System.Drawing.Point(16, 34);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(114, 13);
            this.label5.TabIndex = 20;
            this.label5.Text = "Loaded Configuration: ";
            // 
            // loadedConfigurationLabel
            // 
            this.loadedConfigurationLabel.AutoSize = true;
            this.loadedConfigurationLabel.ForeColor = System.Drawing.Color.Black;
            this.loadedConfigurationLabel.Location = new System.Drawing.Point(131, 34);
            this.loadedConfigurationLabel.Name = "loadedConfigurationLabel";
            this.loadedConfigurationLabel.Size = new System.Drawing.Size(27, 13);
            this.loadedConfigurationLabel.TabIndex = 21;
            this.loadedConfigurationLabel.Text = "N/A";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.tagInfoListView);
            this.groupBox1.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.groupBox1.Location = new System.Drawing.Point(19, 255);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(472, 468);
            this.groupBox1.TabIndex = 22;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Tag Info";
            // 
            // tagInfoListView
            // 
            this.tagInfoListView.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.IDLabel,
            this.ImageLabelListView,
            this.EntranceSoundLabel,
            this.UpdateSoundListView});
            this.tagInfoListView.Font = new System.Drawing.Font("Century Gothic", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tagInfoListView.HideSelection = false;
            this.tagInfoListView.Location = new System.Drawing.Point(6, 25);
            this.tagInfoListView.MultiSelect = false;
            this.tagInfoListView.Name = "tagInfoListView";
            this.tagInfoListView.Size = new System.Drawing.Size(460, 419);
            this.tagInfoListView.TabIndex = 31;
            this.tagInfoListView.UseCompatibleStateImageBehavior = false;
            this.tagInfoListView.View = System.Windows.Forms.View.Details;
            this.tagInfoListView.SelectedIndexChanged += new System.EventHandler(this.TagInfoListView_SelectedIndexChanged);
            // 
            // IDLabel
            // 
            this.IDLabel.Text = "ID";
            this.IDLabel.Width = 119;
            // 
            // ImageLabelListView
            // 
            this.ImageLabelListView.Text = "Image";
            this.ImageLabelListView.Width = 94;
            // 
            // EntranceSoundLabel
            // 
            this.EntranceSoundLabel.Text = "Entrance Sound";
            this.EntranceSoundLabel.Width = 129;
            // 
            // UpdateSoundListView
            // 
            this.UpdateSoundListView.Text = "Update Sound";
            this.UpdateSoundListView.Width = 113;
            // 
            // TagCreatorGroupBox
            // 
            this.TagCreatorGroupBox.BackColor = System.Drawing.Color.Transparent;
            this.TagCreatorGroupBox.Controls.Add(this.stopPlayingButton);
            this.TagCreatorGroupBox.Controls.Add(this.EntranceSoundPlayButton);
            this.TagCreatorGroupBox.Controls.Add(this.UpdateSoundPlayButton);
            this.TagCreatorGroupBox.Controls.Add(this.label10);
            this.TagCreatorGroupBox.Controls.Add(this.tagCreatorPreviewBox);
            this.TagCreatorGroupBox.Controls.Add(this.label8);
            this.TagCreatorGroupBox.Controls.Add(this.secondSoundButton);
            this.TagCreatorGroupBox.Controls.Add(this.secondSoundTextBox);
            this.TagCreatorGroupBox.Controls.Add(this.tagGetIdButton);
            this.TagCreatorGroupBox.Controls.Add(this.tagBox);
            this.TagCreatorGroupBox.Controls.Add(this.soundButton);
            this.TagCreatorGroupBox.Controls.Add(this.tagLabel);
            this.TagCreatorGroupBox.Controls.Add(this.soundTextBox);
            this.TagCreatorGroupBox.Controls.Add(this.imageLabel);
            this.TagCreatorGroupBox.Controls.Add(this.clearButton);
            this.TagCreatorGroupBox.Controls.Add(this.label9);
            this.TagCreatorGroupBox.Controls.Add(this.saveButton);
            this.TagCreatorGroupBox.Controls.Add(this.imageTextBox);
            this.TagCreatorGroupBox.Controls.Add(this.imageButton);
            this.TagCreatorGroupBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.TagCreatorGroupBox.ForeColor = System.Drawing.Color.Black;
            this.TagCreatorGroupBox.Location = new System.Drawing.Point(502, 483);
            this.TagCreatorGroupBox.Name = "TagCreatorGroupBox";
            this.TagCreatorGroupBox.Size = new System.Drawing.Size(659, 240);
            this.TagCreatorGroupBox.TabIndex = 23;
            this.TagCreatorGroupBox.TabStop = false;
            this.TagCreatorGroupBox.Text = "3) Tag Creator";
            // 
            // EntranceSoundPlayButton
            // 
            this.EntranceSoundPlayButton.Location = new System.Drawing.Point(6, 100);
            this.EntranceSoundPlayButton.Name = "EntranceSoundPlayButton";
            this.EntranceSoundPlayButton.Size = new System.Drawing.Size(25, 24);
            this.EntranceSoundPlayButton.TabIndex = 17;
            this.EntranceSoundPlayButton.Text = "▶️";
            this.EntranceSoundPlayButton.UseVisualStyleBackColor = true;
            this.EntranceSoundPlayButton.Click += new System.EventHandler(this.EntranceSoundPlayButton_Click);
            // 
            // UpdateSoundPlayButton
            // 
            this.UpdateSoundPlayButton.Location = new System.Drawing.Point(6, 134);
            this.UpdateSoundPlayButton.Name = "UpdateSoundPlayButton";
            this.UpdateSoundPlayButton.Size = new System.Drawing.Size(25, 25);
            this.UpdateSoundPlayButton.TabIndex = 16;
            this.UpdateSoundPlayButton.Text = "▶️";
            this.UpdateSoundPlayButton.UseVisualStyleBackColor = true;
            this.UpdateSoundPlayButton.Click += new System.EventHandler(this.UpdateSoundPlayButton_Click);
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(462, 25);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(69, 18);
            this.label10.TabIndex = 15;
            this.label10.Text = "Preview:";
            // 
            // tagCreatorPreviewBox
            // 
            this.tagCreatorPreviewBox.Location = new System.Drawing.Point(537, 25);
            this.tagCreatorPreviewBox.Name = "tagCreatorPreviewBox";
            this.tagCreatorPreviewBox.Size = new System.Drawing.Size(111, 99);
            this.tagCreatorPreviewBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.tagCreatorPreviewBox.TabIndex = 14;
            this.tagCreatorPreviewBox.TabStop = false;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.label8.Location = new System.Drawing.Point(34, 136);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(122, 20);
            this.label8.TabIndex = 13;
            this.label8.Text = "Update Sound :";
            // 
            // secondSoundButton
            // 
            this.secondSoundButton.BackColor = System.Drawing.SystemColors.Control;
            this.secondSoundButton.FlatAppearance.BorderSize = 0;
            this.secondSoundButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.secondSoundButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.secondSoundButton.Location = new System.Drawing.Point(381, 134);
            this.secondSoundButton.Name = "secondSoundButton";
            this.secondSoundButton.Size = new System.Drawing.Size(75, 23);
            this.secondSoundButton.TabIndex = 12;
            this.secondSoundButton.Text = "Browse";
            this.secondSoundButton.UseVisualStyleBackColor = true;
            this.secondSoundButton.Click += new System.EventHandler(this.SecondSoundButton_Click);
            // 
            // secondSoundTextBox
            // 
            this.secondSoundTextBox.BackColor = System.Drawing.Color.Snow;
            this.secondSoundTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F);
            this.secondSoundTextBox.Location = new System.Drawing.Point(197, 137);
            this.secondSoundTextBox.Name = "secondSoundTextBox";
            this.secondSoundTextBox.Size = new System.Drawing.Size(167, 22);
            this.secondSoundTextBox.TabIndex = 11;
            // 
            // tagGetIdButton
            // 
            this.tagGetIdButton.BackColor = System.Drawing.SystemColors.Control;
            this.tagGetIdButton.FlatAppearance.BorderSize = 0;
            this.tagGetIdButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.tagGetIdButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.tagGetIdButton.Location = new System.Drawing.Point(247, 190);
            this.tagGetIdButton.Name = "tagGetIdButton";
            this.tagGetIdButton.Size = new System.Drawing.Size(100, 26);
            this.tagGetIdButton.TabIndex = 10;
            this.tagGetIdButton.Text = "Scan Tag";
            this.tagGetIdButton.UseVisualStyleBackColor = true;
            this.tagGetIdButton.Click += new System.EventHandler(this.TagGetIdButton_Click);
            // 
            // tagBox
            // 
            this.tagBox.BackColor = System.Drawing.Color.Snow;
            this.tagBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tagBox.ForeColor = System.Drawing.Color.Black;
            this.tagBox.Location = new System.Drawing.Point(198, 23);
            this.tagBox.Name = "tagBox";
            this.tagBox.Size = new System.Drawing.Size(167, 22);
            this.tagBox.TabIndex = 3;
            // 
            // soundButton
            // 
            this.soundButton.BackColor = System.Drawing.SystemColors.Control;
            this.soundButton.FlatAppearance.BorderSize = 0;
            this.soundButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.soundButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.soundButton.Location = new System.Drawing.Point(381, 97);
            this.soundButton.Name = "soundButton";
            this.soundButton.Size = new System.Drawing.Size(75, 23);
            this.soundButton.TabIndex = 9;
            this.soundButton.Text = "Browse";
            this.soundButton.UseVisualStyleBackColor = true;
            this.soundButton.Click += new System.EventHandler(this.SoundButton_Click);
            // 
            // tagLabel
            // 
            this.tagLabel.AutoSize = true;
            this.tagLabel.BackColor = System.Drawing.Color.Transparent;
            this.tagLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.tagLabel.ForeColor = System.Drawing.Color.Black;
            this.tagLabel.Location = new System.Drawing.Point(34, 25);
            this.tagLabel.Name = "tagLabel";
            this.tagLabel.Size = new System.Drawing.Size(62, 20);
            this.tagLabel.TabIndex = 0;
            this.tagLabel.Text = "Tag ID :";
            // 
            // soundTextBox
            // 
            this.soundTextBox.BackColor = System.Drawing.Color.Snow;
            this.soundTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.soundTextBox.ForeColor = System.Drawing.Color.Black;
            this.soundTextBox.Location = new System.Drawing.Point(197, 100);
            this.soundTextBox.Name = "soundTextBox";
            this.soundTextBox.Size = new System.Drawing.Size(167, 22);
            this.soundTextBox.TabIndex = 8;
            // 
            // imageLabel
            // 
            this.imageLabel.BackColor = System.Drawing.Color.Transparent;
            this.imageLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.imageLabel.ForeColor = System.Drawing.Color.Black;
            this.imageLabel.Location = new System.Drawing.Point(33, 65);
            this.imageLabel.Name = "imageLabel";
            this.imageLabel.Size = new System.Drawing.Size(72, 26);
            this.imageLabel.TabIndex = 1;
            this.imageLabel.Text = "Image :";
            // 
            // clearButton
            // 
            this.clearButton.BackColor = System.Drawing.SystemColors.Control;
            this.clearButton.FlatAppearance.BorderSize = 0;
            this.clearButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.clearButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.clearButton.Location = new System.Drawing.Point(381, 23);
            this.clearButton.Name = "clearButton";
            this.clearButton.Size = new System.Drawing.Size(75, 23);
            this.clearButton.TabIndex = 7;
            this.clearButton.Text = "Clear";
            this.clearButton.UseVisualStyleBackColor = true;
            this.clearButton.Click += new System.EventHandler(this.ClearButton_Click);
            // 
            // label9
            // 
            this.label9.BackColor = System.Drawing.Color.Transparent;
            this.label9.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.label9.ForeColor = System.Drawing.Color.Black;
            this.label9.Location = new System.Drawing.Point(33, 102);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(141, 18);
            this.label9.TabIndex = 2;
            this.label9.Text = "Entrance Sound:";
            // 
            // saveButton
            // 
            this.saveButton.BackColor = System.Drawing.SystemColors.Control;
            this.saveButton.FlatAppearance.BorderSize = 0;
            this.saveButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.saveButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.saveButton.Location = new System.Drawing.Point(84, 190);
            this.saveButton.Name = "saveButton";
            this.saveButton.Size = new System.Drawing.Size(100, 26);
            this.saveButton.TabIndex = 6;
            this.saveButton.Text = "Save";
            this.saveButton.UseVisualStyleBackColor = true;
            this.saveButton.Click += new System.EventHandler(this.SaveButton_Click);
            // 
            // imageTextBox
            // 
            this.imageTextBox.BackColor = System.Drawing.Color.Snow;
            this.imageTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.imageTextBox.ForeColor = System.Drawing.Color.Black;
            this.imageTextBox.Location = new System.Drawing.Point(198, 63);
            this.imageTextBox.Name = "imageTextBox";
            this.imageTextBox.Size = new System.Drawing.Size(167, 22);
            this.imageTextBox.TabIndex = 4;
            // 
            // imageButton
            // 
            this.imageButton.BackColor = System.Drawing.SystemColors.Control;
            this.imageButton.FlatAppearance.BorderSize = 0;
            this.imageButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.imageButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.imageButton.Location = new System.Drawing.Point(381, 59);
            this.imageButton.Name = "imageButton";
            this.imageButton.Size = new System.Drawing.Size(75, 23);
            this.imageButton.TabIndex = 5;
            this.imageButton.Text = "Browse";
            this.imageButton.UseVisualStyleBackColor = true;
            this.imageButton.Click += new System.EventHandler(this.ImageButton_Click);
            // 
            // stopPlayingButton
            // 
            this.stopPlayingButton.Location = new System.Drawing.Point(6, 190);
            this.stopPlayingButton.Name = "stopPlayingButton";
            this.stopPlayingButton.Size = new System.Drawing.Size(25, 25);
            this.stopPlayingButton.TabIndex = 18;
            this.stopPlayingButton.Text = "❌";
            this.stopPlayingButton.UseVisualStyleBackColor = true;
            this.stopPlayingButton.Click += new System.EventHandler(this.StopPlayingButton_Click);
            // 
            // errorProvider1
            // 
            this.errorProvider1.ContainerControl = this;
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSize = true;
            this.BackColor = System.Drawing.SystemColors.Control;
            this.ClientSize = new System.Drawing.Size(1168, 875);
            this.Controls.Add(this.TagCreatorGroupBox);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.loadedConfigurationLabel);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.LaunchButton);
            this.Controls.Add(this.ApplicationsGroupBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.debugTextBox);
            this.Controls.Add(this.backgroundCalibrationGroupBox);
            this.Controls.Add(this.portTextLabel);
            this.Controls.Add(this.connectedPortLabel);
            this.Controls.Add(this.displayCalibrationGroupBox);
            this.Controls.Add(this.menuStrip1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MainMenuStrip = this.menuStrip1;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "MainWindow";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Interactive RFID Display";
            this.displayCalibrationGroupBox.ResumeLayout(false);
            this.displayCalibrationGroupBox.PerformLayout();
            this.backgroundCalibrationGroupBox.ResumeLayout(false);
            this.backgroundCalibrationGroupBox.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.backgroundCalibPictureBox)).EndInit();
            this.ApplicationsGroupBox.ResumeLayout(false);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.TagCreatorGroupBox.ResumeLayout(false);
            this.TagCreatorGroupBox.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.tagCreatorPreviewBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.errorProvider1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.GroupBox displayCalibrationGroupBox;
        private System.Windows.Forms.Label connectedPortLabel;
        private System.Windows.Forms.Label portTextLabel;
        private System.Windows.Forms.Button displayInfoButton;
        private System.Windows.Forms.TextBox dispCalibXBox;
        private System.Windows.Forms.Label gridSizeLabel;
        private System.Windows.Forms.Button dispCalibrateButton;
        private System.Windows.Forms.GroupBox backgroundCalibrationGroupBox;
        private System.Windows.Forms.Button backgroundImgButton;
        private System.Windows.Forms.TextBox backgroundImgTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox debugTextBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button backgroundCalibButton;
        private System.Windows.Forms.TextBox dispCalibYBox;
        private System.Windows.Forms.Label YLabel;
        private System.Windows.Forms.Label XLabel;
        private System.Windows.Forms.GroupBox ApplicationsGroupBox;
        private System.Windows.Forms.Button ApplicationsRefreshButton;
        private System.Windows.Forms.ListBox ApplicationsList;
        private System.Windows.Forms.Button createNewApplicationButton;
        private System.Windows.Forms.Button LoadApplicationButton;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem aboutToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exitToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem settingsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem chooseCOMToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem installModulesToolStripMenuItem;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.Button DeleteApplicationButton;
        private System.Windows.Forms.Button LaunchButton;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label loadedConfigurationLabel;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.PictureBox backgroundCalibPictureBox;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox TagCreatorGroupBox;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Button secondSoundButton;
        private System.Windows.Forms.TextBox secondSoundTextBox;
        private System.Windows.Forms.Button tagGetIdButton;
        private System.Windows.Forms.TextBox tagBox;
        private System.Windows.Forms.Button soundButton;
        private System.Windows.Forms.Label tagLabel;
        private System.Windows.Forms.TextBox soundTextBox;
        private System.Windows.Forms.Label imageLabel;
        private System.Windows.Forms.Button clearButton;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Button saveButton;
        private System.Windows.Forms.TextBox imageTextBox;
        private System.Windows.Forms.Button imageButton;
        private System.Windows.Forms.Button EntranceSoundPlayButton;
        private System.Windows.Forms.Button UpdateSoundPlayButton;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.PictureBox tagCreatorPreviewBox;
        private System.Windows.Forms.ListView tagInfoListView;
        private System.Windows.Forms.ColumnHeader IDLabel;
        private System.Windows.Forms.ColumnHeader ImageLabelListView;
        private System.Windows.Forms.ColumnHeader EntranceSoundLabel;
        private System.Windows.Forms.ColumnHeader UpdateSoundListView;
        private System.Windows.Forms.Button stopPlayingButton;
        private System.Windows.Forms.ErrorProvider errorProvider1;
    }
}

