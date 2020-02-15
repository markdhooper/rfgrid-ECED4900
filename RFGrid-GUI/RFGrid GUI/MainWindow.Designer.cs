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
            this.tagLabel = new System.Windows.Forms.Label();
            this.imageLabel = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.tagBox = new System.Windows.Forms.TextBox();
            this.imageTextBox = new System.Windows.Forms.TextBox();
            this.imageButton = new System.Windows.Forms.Button();
            this.saveButton = new System.Windows.Forms.Button();
            this.clearButton = new System.Windows.Forms.Button();
            this.soundTextBox = new System.Windows.Forms.TextBox();
            this.soundButton = new System.Windows.Forms.Button();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.TagCreatorGroupBox = new System.Windows.Forms.GroupBox();
            this.label4 = new System.Windows.Forms.Label();
            this.secondSoundButton = new System.Windows.Forms.Button();
            this.secondSoundTextBox = new System.Windows.Forms.TextBox();
            this.tagGetIdButton = new System.Windows.Forms.Button();
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
            this.backgroundCalibButton = new System.Windows.Forms.Button();
            this.backgroundImgButton = new System.Windows.Forms.Button();
            this.backgroundImgTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.debugTextBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.ApplicationsGroupBox = new System.Windows.Forms.GroupBox();
            this.DeleteApplicationButton = new System.Windows.Forms.Button();
            this.LoadApplicationButton = new System.Windows.Forms.Button();
            this.createNewApplicationButton = new System.Windows.Forms.Button();
            this.ApplicationsRefreshButton = new System.Windows.Forms.Button();
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
            this.TagCreatorGroupBox.SuspendLayout();
            this.displayCalibrationGroupBox.SuspendLayout();
            this.backgroundCalibrationGroupBox.SuspendLayout();
            this.ApplicationsGroupBox.SuspendLayout();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // tagLabel
            // 
            this.tagLabel.AutoSize = true;
            this.tagLabel.BackColor = System.Drawing.Color.Transparent;
            this.tagLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.tagLabel.ForeColor = System.Drawing.Color.White;
            this.tagLabel.Location = new System.Drawing.Point(6, 35);
            this.tagLabel.Name = "tagLabel";
            this.tagLabel.Size = new System.Drawing.Size(62, 20);
            this.tagLabel.TabIndex = 0;
            this.tagLabel.Text = "Tag ID :";
            // 
            // imageLabel
            // 
            this.imageLabel.BackColor = System.Drawing.Color.Transparent;
            this.imageLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.imageLabel.ForeColor = System.Drawing.Color.White;
            this.imageLabel.Location = new System.Drawing.Point(5, 75);
            this.imageLabel.Name = "imageLabel";
            this.imageLabel.Size = new System.Drawing.Size(72, 26);
            this.imageLabel.TabIndex = 1;
            this.imageLabel.Text = "Image :";
            // 
            // label1
            // 
            this.label1.BackColor = System.Drawing.Color.Transparent;
            this.label1.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.label1.ForeColor = System.Drawing.Color.White;
            this.label1.Location = new System.Drawing.Point(5, 112);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(144, 18);
            this.label1.TabIndex = 2;
            this.label1.Text = "Entrance Sound:";
            // 
            // tagBox
            // 
            this.tagBox.BackColor = System.Drawing.Color.Snow;
            this.tagBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tagBox.ForeColor = System.Drawing.Color.Black;
            this.tagBox.Location = new System.Drawing.Point(156, 35);
            this.tagBox.Name = "tagBox";
            this.tagBox.Size = new System.Drawing.Size(167, 22);
            this.tagBox.TabIndex = 3;
            // 
            // imageTextBox
            // 
            this.imageTextBox.BackColor = System.Drawing.Color.Snow;
            this.imageTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.imageTextBox.ForeColor = System.Drawing.Color.Black;
            this.imageTextBox.Location = new System.Drawing.Point(156, 75);
            this.imageTextBox.Name = "imageTextBox";
            this.imageTextBox.Size = new System.Drawing.Size(167, 22);
            this.imageTextBox.TabIndex = 4;
            // 
            // imageButton
            // 
            this.imageButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(41)))), ((int)(((byte)(54)))), ((int)(((byte)(67)))));
            this.imageButton.FlatAppearance.BorderSize = 0;
            this.imageButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.imageButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.imageButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.imageButton.Location = new System.Drawing.Point(339, 71);
            this.imageButton.Name = "imageButton";
            this.imageButton.Size = new System.Drawing.Size(75, 23);
            this.imageButton.TabIndex = 5;
            this.imageButton.Text = "Browse";
            this.imageButton.UseVisualStyleBackColor = false;
            this.imageButton.Click += new System.EventHandler(this.ImageButton_Click);
            // 
            // saveButton
            // 
            this.saveButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(87)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.saveButton.FlatAppearance.BorderSize = 0;
            this.saveButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.saveButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.saveButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.saveButton.Location = new System.Drawing.Point(84, 190);
            this.saveButton.Name = "saveButton";
            this.saveButton.Size = new System.Drawing.Size(100, 26);
            this.saveButton.TabIndex = 6;
            this.saveButton.Text = "Save";
            this.saveButton.UseVisualStyleBackColor = false;
            this.saveButton.Click += new System.EventHandler(this.SaveButton_Click);
            // 
            // clearButton
            // 
            this.clearButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(41)))), ((int)(((byte)(54)))), ((int)(((byte)(67)))));
            this.clearButton.FlatAppearance.BorderSize = 0;
            this.clearButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.clearButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.clearButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.clearButton.Location = new System.Drawing.Point(339, 35);
            this.clearButton.Name = "clearButton";
            this.clearButton.Size = new System.Drawing.Size(75, 23);
            this.clearButton.TabIndex = 7;
            this.clearButton.Text = "Clear";
            this.clearButton.UseVisualStyleBackColor = false;
            this.clearButton.Click += new System.EventHandler(this.ClearButton_Click);
            // 
            // soundTextBox
            // 
            this.soundTextBox.BackColor = System.Drawing.Color.Snow;
            this.soundTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.soundTextBox.ForeColor = System.Drawing.Color.Black;
            this.soundTextBox.Location = new System.Drawing.Point(155, 112);
            this.soundTextBox.Name = "soundTextBox";
            this.soundTextBox.Size = new System.Drawing.Size(167, 22);
            this.soundTextBox.TabIndex = 8;
            // 
            // soundButton
            // 
            this.soundButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(41)))), ((int)(((byte)(54)))), ((int)(((byte)(67)))));
            this.soundButton.FlatAppearance.BorderSize = 0;
            this.soundButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.soundButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.soundButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.soundButton.Location = new System.Drawing.Point(339, 109);
            this.soundButton.Name = "soundButton";
            this.soundButton.Size = new System.Drawing.Size(75, 23);
            this.soundButton.TabIndex = 9;
            this.soundButton.Text = "Browse";
            this.soundButton.UseVisualStyleBackColor = false;
            this.soundButton.Click += new System.EventHandler(this.SoundButton_Click);
            // 
            // TagCreatorGroupBox
            // 
            this.TagCreatorGroupBox.BackColor = System.Drawing.Color.Transparent;
            this.TagCreatorGroupBox.Controls.Add(this.label4);
            this.TagCreatorGroupBox.Controls.Add(this.secondSoundButton);
            this.TagCreatorGroupBox.Controls.Add(this.secondSoundTextBox);
            this.TagCreatorGroupBox.Controls.Add(this.tagGetIdButton);
            this.TagCreatorGroupBox.Controls.Add(this.tagBox);
            this.TagCreatorGroupBox.Controls.Add(this.soundButton);
            this.TagCreatorGroupBox.Controls.Add(this.tagLabel);
            this.TagCreatorGroupBox.Controls.Add(this.soundTextBox);
            this.TagCreatorGroupBox.Controls.Add(this.imageLabel);
            this.TagCreatorGroupBox.Controls.Add(this.clearButton);
            this.TagCreatorGroupBox.Controls.Add(this.label1);
            this.TagCreatorGroupBox.Controls.Add(this.saveButton);
            this.TagCreatorGroupBox.Controls.Add(this.imageTextBox);
            this.TagCreatorGroupBox.Controls.Add(this.imageButton);
            this.TagCreatorGroupBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.TagCreatorGroupBox.ForeColor = System.Drawing.Color.White;
            this.TagCreatorGroupBox.Location = new System.Drawing.Point(25, 255);
            this.TagCreatorGroupBox.Name = "TagCreatorGroupBox";
            this.TagCreatorGroupBox.Size = new System.Drawing.Size(433, 222);
            this.TagCreatorGroupBox.TabIndex = 11;
            this.TagCreatorGroupBox.TabStop = false;
            this.TagCreatorGroupBox.Text = "Tag Creator";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.label4.Location = new System.Drawing.Point(6, 146);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(122, 20);
            this.label4.TabIndex = 13;
            this.label4.Text = "Update Sound :";
            // 
            // secondSoundButton
            // 
            this.secondSoundButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(41)))), ((int)(((byte)(54)))), ((int)(((byte)(67)))));
            this.secondSoundButton.FlatAppearance.BorderSize = 0;
            this.secondSoundButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.secondSoundButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.secondSoundButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.secondSoundButton.Location = new System.Drawing.Point(339, 146);
            this.secondSoundButton.Name = "secondSoundButton";
            this.secondSoundButton.Size = new System.Drawing.Size(75, 23);
            this.secondSoundButton.TabIndex = 12;
            this.secondSoundButton.Text = "Browse";
            this.secondSoundButton.UseVisualStyleBackColor = false;
            this.secondSoundButton.Click += new System.EventHandler(this.SecondSoundButton_Click);
            // 
            // secondSoundTextBox
            // 
            this.secondSoundTextBox.BackColor = System.Drawing.Color.Snow;
            this.secondSoundTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F);
            this.secondSoundTextBox.Location = new System.Drawing.Point(155, 149);
            this.secondSoundTextBox.Name = "secondSoundTextBox";
            this.secondSoundTextBox.Size = new System.Drawing.Size(167, 22);
            this.secondSoundTextBox.TabIndex = 11;
            // 
            // tagGetIdButton
            // 
            this.tagGetIdButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(41)))), ((int)(((byte)(54)))), ((int)(((byte)(67)))));
            this.tagGetIdButton.FlatAppearance.BorderSize = 0;
            this.tagGetIdButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.tagGetIdButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.tagGetIdButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.tagGetIdButton.Location = new System.Drawing.Point(247, 190);
            this.tagGetIdButton.Name = "tagGetIdButton";
            this.tagGetIdButton.Size = new System.Drawing.Size(100, 26);
            this.tagGetIdButton.TabIndex = 10;
            this.tagGetIdButton.Text = "Scan Tag";
            this.tagGetIdButton.UseVisualStyleBackColor = false;
            this.tagGetIdButton.Click += new System.EventHandler(this.TagGetIdButton_Click);
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
            this.displayCalibrationGroupBox.ForeColor = System.Drawing.Color.White;
            this.displayCalibrationGroupBox.Location = new System.Drawing.Point(386, 60);
            this.displayCalibrationGroupBox.Name = "displayCalibrationGroupBox";
            this.displayCalibrationGroupBox.Size = new System.Drawing.Size(299, 189);
            this.displayCalibrationGroupBox.TabIndex = 12;
            this.displayCalibrationGroupBox.TabStop = false;
            this.displayCalibrationGroupBox.Text = "Display Calibration";
            // 
            // YLabel
            // 
            this.YLabel.AutoSize = true;
            this.YLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.YLabel.Location = new System.Drawing.Point(104, 89);
            this.YLabel.Name = "YLabel";
            this.YLabel.Size = new System.Drawing.Size(24, 20);
            this.YLabel.TabIndex = 6;
            this.YLabel.Text = "Y :";
            // 
            // XLabel
            // 
            this.XLabel.AutoSize = true;
            this.XLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.XLabel.Location = new System.Drawing.Point(104, 59);
            this.XLabel.Name = "XLabel";
            this.XLabel.Size = new System.Drawing.Size(26, 20);
            this.XLabel.TabIndex = 5;
            this.XLabel.Text = "X :";
            // 
            // dispCalibYBox
            // 
            this.dispCalibYBox.BackColor = System.Drawing.Color.Snow;
            this.dispCalibYBox.Location = new System.Drawing.Point(136, 91);
            this.dispCalibYBox.MaxLength = 2;
            this.dispCalibYBox.Name = "dispCalibYBox";
            this.dispCalibYBox.Size = new System.Drawing.Size(45, 26);
            this.dispCalibYBox.TabIndex = 4;
            // 
            // dispCalibrateButton
            // 
            this.dispCalibrateButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.dispCalibrateButton.FlatAppearance.BorderSize = 0;
            this.dispCalibrateButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.dispCalibrateButton.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.dispCalibrateButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(61)))), ((int)(((byte)(64)))), ((int)(((byte)(71)))));
            this.dispCalibrateButton.Location = new System.Drawing.Point(108, 151);
            this.dispCalibrateButton.Name = "dispCalibrateButton";
            this.dispCalibrateButton.Size = new System.Drawing.Size(87, 23);
            this.dispCalibrateButton.TabIndex = 3;
            this.dispCalibrateButton.Text = "Calibrate";
            this.dispCalibrateButton.UseVisualStyleBackColor = false;
            this.dispCalibrateButton.Click += new System.EventHandler(this.DispCalibrateButton_Click);
            // 
            // displayInfoButton
            // 
            this.displayInfoButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(61)))), ((int)(((byte)(64)))), ((int)(((byte)(71)))));
            this.displayInfoButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.displayInfoButton.Font = new System.Drawing.Font("Calibri", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.displayInfoButton.ForeColor = System.Drawing.Color.White;
            this.displayInfoButton.Location = new System.Drawing.Point(213, 25);
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
            this.dispCalibXBox.Location = new System.Drawing.Point(136, 59);
            this.dispCalibXBox.MaxLength = 2;
            this.dispCalibXBox.Name = "dispCalibXBox";
            this.dispCalibXBox.Size = new System.Drawing.Size(45, 26);
            this.dispCalibXBox.TabIndex = 1;
            // 
            // gridSizeLabel
            // 
            this.gridSizeLabel.AutoSize = true;
            this.gridSizeLabel.Font = new System.Drawing.Font("Century Gothic", 12F);
            this.gridSizeLabel.Location = new System.Drawing.Point(79, 26);
            this.gridSizeLabel.Name = "gridSizeLabel";
            this.gridSizeLabel.Size = new System.Drawing.Size(132, 21);
            this.gridSizeLabel.TabIndex = 0;
            this.gridSizeLabel.Text = "Grid Dimensions";
            // 
            // connectedPortLabel
            // 
            this.connectedPortLabel.AutoSize = true;
            this.connectedPortLabel.Enabled = false;
            this.connectedPortLabel.ForeColor = System.Drawing.Color.White;
            this.connectedPortLabel.Location = new System.Drawing.Point(698, 34);
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
            this.portTextLabel.ForeColor = System.Drawing.Color.White;
            this.portTextLabel.Location = new System.Drawing.Point(788, 34);
            this.portTextLabel.Name = "portTextLabel";
            this.portTextLabel.Size = new System.Drawing.Size(22, 13);
            this.portTextLabel.TabIndex = 14;
            this.portTextLabel.Text = "NA";
            this.portTextLabel.Visible = false;
            // 
            // backgroundCalibrationGroupBox
            // 
            this.backgroundCalibrationGroupBox.Controls.Add(this.backgroundCalibButton);
            this.backgroundCalibrationGroupBox.Controls.Add(this.backgroundImgButton);
            this.backgroundCalibrationGroupBox.Controls.Add(this.backgroundImgTextBox);
            this.backgroundCalibrationGroupBox.Controls.Add(this.label2);
            this.backgroundCalibrationGroupBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.backgroundCalibrationGroupBox.ForeColor = System.Drawing.Color.White;
            this.backgroundCalibrationGroupBox.Location = new System.Drawing.Point(691, 60);
            this.backgroundCalibrationGroupBox.Name = "backgroundCalibrationGroupBox";
            this.backgroundCalibrationGroupBox.Size = new System.Drawing.Size(323, 189);
            this.backgroundCalibrationGroupBox.TabIndex = 15;
            this.backgroundCalibrationGroupBox.TabStop = false;
            this.backgroundCalibrationGroupBox.Text = "Background Calibration";
            // 
            // backgroundCalibButton
            // 
            this.backgroundCalibButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.backgroundCalibButton.FlatAppearance.BorderSize = 0;
            this.backgroundCalibButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.backgroundCalibButton.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.backgroundCalibButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(61)))), ((int)(((byte)(64)))), ((int)(((byte)(71)))));
            this.backgroundCalibButton.Location = new System.Drawing.Point(116, 151);
            this.backgroundCalibButton.Name = "backgroundCalibButton";
            this.backgroundCalibButton.Size = new System.Drawing.Size(87, 23);
            this.backgroundCalibButton.TabIndex = 3;
            this.backgroundCalibButton.Text = "Calibrate";
            this.backgroundCalibButton.UseVisualStyleBackColor = false;
            this.backgroundCalibButton.Click += new System.EventHandler(this.BackgroundCalibButton_Click);
            // 
            // backgroundImgButton
            // 
            this.backgroundImgButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(41)))), ((int)(((byte)(54)))), ((int)(((byte)(67)))));
            this.backgroundImgButton.FlatAppearance.BorderSize = 0;
            this.backgroundImgButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.backgroundImgButton.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.backgroundImgButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.backgroundImgButton.Location = new System.Drawing.Point(205, 69);
            this.backgroundImgButton.Name = "backgroundImgButton";
            this.backgroundImgButton.Size = new System.Drawing.Size(94, 23);
            this.backgroundImgButton.TabIndex = 2;
            this.backgroundImgButton.Text = "Browse";
            this.backgroundImgButton.UseVisualStyleBackColor = false;
            this.backgroundImgButton.Click += new System.EventHandler(this.BackgroundImgButton_Click);
            // 
            // backgroundImgTextBox
            // 
            this.backgroundImgTextBox.BackColor = System.Drawing.Color.Snow;
            this.backgroundImgTextBox.Location = new System.Drawing.Point(9, 69);
            this.backgroundImgTextBox.Name = "backgroundImgTextBox";
            this.backgroundImgTextBox.Size = new System.Drawing.Size(181, 26);
            this.backgroundImgTextBox.TabIndex = 1;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.label2.Location = new System.Drawing.Point(6, 35);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(151, 20);
            this.label2.TabIndex = 0;
            this.label2.Text = "Background Image";
            // 
            // debugTextBox
            // 
            this.debugTextBox.BackColor = System.Drawing.Color.Snow;
            this.debugTextBox.Location = new System.Drawing.Point(19, 519);
            this.debugTextBox.Multiline = true;
            this.debugTextBox.Name = "debugTextBox";
            this.debugTextBox.ReadOnly = true;
            this.debugTextBox.Size = new System.Drawing.Size(995, 116);
            this.debugTextBox.TabIndex = 16;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.label3.ForeColor = System.Drawing.Color.White;
            this.label3.Location = new System.Drawing.Point(22, 489);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(57, 18);
            this.label3.TabIndex = 17;
            this.label3.Text = "Output";
            // 
            // ApplicationsGroupBox
            // 
            this.ApplicationsGroupBox.Controls.Add(this.DeleteApplicationButton);
            this.ApplicationsGroupBox.Controls.Add(this.LoadApplicationButton);
            this.ApplicationsGroupBox.Controls.Add(this.createNewApplicationButton);
            this.ApplicationsGroupBox.Controls.Add(this.ApplicationsRefreshButton);
            this.ApplicationsGroupBox.Controls.Add(this.ApplicationsList);
            this.ApplicationsGroupBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.ApplicationsGroupBox.ForeColor = System.Drawing.Color.White;
            this.ApplicationsGroupBox.Location = new System.Drawing.Point(19, 60);
            this.ApplicationsGroupBox.Name = "ApplicationsGroupBox";
            this.ApplicationsGroupBox.Size = new System.Drawing.Size(361, 189);
            this.ApplicationsGroupBox.TabIndex = 18;
            this.ApplicationsGroupBox.TabStop = false;
            this.ApplicationsGroupBox.Text = "Applications";
            // 
            // DeleteApplicationButton
            // 
            this.DeleteApplicationButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(41)))), ((int)(((byte)(54)))), ((int)(((byte)(67)))));
            this.DeleteApplicationButton.FlatAppearance.BorderSize = 0;
            this.DeleteApplicationButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.DeleteApplicationButton.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.DeleteApplicationButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.DeleteApplicationButton.Location = new System.Drawing.Point(254, 147);
            this.DeleteApplicationButton.Name = "DeleteApplicationButton";
            this.DeleteApplicationButton.Size = new System.Drawing.Size(75, 23);
            this.DeleteApplicationButton.TabIndex = 23;
            this.DeleteApplicationButton.Text = "Delete";
            this.DeleteApplicationButton.UseVisualStyleBackColor = false;
            this.DeleteApplicationButton.Click += new System.EventHandler(this.DeleteApplicationButton_Click);
            // 
            // LoadApplicationButton
            // 
            this.LoadApplicationButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(41)))), ((int)(((byte)(54)))), ((int)(((byte)(67)))));
            this.LoadApplicationButton.FlatAppearance.BorderSize = 0;
            this.LoadApplicationButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.LoadApplicationButton.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LoadApplicationButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.LoadApplicationButton.Location = new System.Drawing.Point(253, 108);
            this.LoadApplicationButton.Name = "LoadApplicationButton";
            this.LoadApplicationButton.Size = new System.Drawing.Size(76, 23);
            this.LoadApplicationButton.TabIndex = 21;
            this.LoadApplicationButton.Text = "Load";
            this.LoadApplicationButton.UseVisualStyleBackColor = false;
            this.LoadApplicationButton.Click += new System.EventHandler(this.openExistingApplicationButton_Click);
            // 
            // createNewApplicationButton
            // 
            this.createNewApplicationButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(41)))), ((int)(((byte)(54)))), ((int)(((byte)(67)))));
            this.createNewApplicationButton.FlatAppearance.BorderSize = 0;
            this.createNewApplicationButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.createNewApplicationButton.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.createNewApplicationButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.createNewApplicationButton.Location = new System.Drawing.Point(254, 65);
            this.createNewApplicationButton.Name = "createNewApplicationButton";
            this.createNewApplicationButton.Size = new System.Drawing.Size(77, 23);
            this.createNewApplicationButton.TabIndex = 22;
            this.createNewApplicationButton.Text = "New Game";
            this.createNewApplicationButton.UseVisualStyleBackColor = false;
            this.createNewApplicationButton.Click += new System.EventHandler(this.createNewApplicationButton_Click);
            // 
            // ApplicationsRefreshButton
            // 
            this.ApplicationsRefreshButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(41)))), ((int)(((byte)(54)))), ((int)(((byte)(67)))));
            this.ApplicationsRefreshButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.ApplicationsRefreshButton.FlatAppearance.BorderSize = 0;
            this.ApplicationsRefreshButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.ApplicationsRefreshButton.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ApplicationsRefreshButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.ApplicationsRefreshButton.Location = new System.Drawing.Point(254, 26);
            this.ApplicationsRefreshButton.Name = "ApplicationsRefreshButton";
            this.ApplicationsRefreshButton.Size = new System.Drawing.Size(77, 23);
            this.ApplicationsRefreshButton.TabIndex = 2;
            this.ApplicationsRefreshButton.Text = "Refresh";
            this.ApplicationsRefreshButton.UseVisualStyleBackColor = false;
            this.ApplicationsRefreshButton.Click += new System.EventHandler(this.ApplicationsRefreshButton_Click);
            // 
            // ApplicationsList
            // 
            this.ApplicationsList.BackColor = System.Drawing.Color.Snow;
            this.ApplicationsList.Font = new System.Drawing.Font("Century Gothic", 11.25F);
            this.ApplicationsList.FormattingEnabled = true;
            this.ApplicationsList.ItemHeight = 20;
            this.ApplicationsList.Location = new System.Drawing.Point(15, 25);
            this.ApplicationsList.Name = "ApplicationsList";
            this.ApplicationsList.ScrollAlwaysVisible = true;
            this.ApplicationsList.Size = new System.Drawing.Size(221, 144);
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
            this.settingsToolStripMenuItem.BackColor = System.Drawing.Color.GhostWhite;
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
            this.chooseCOMToolStripMenuItem.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(81)))), ((int)(((byte)(84)))), ((int)(((byte)(101)))));
            this.chooseCOMToolStripMenuItem.ForeColor = System.Drawing.Color.White;
            this.chooseCOMToolStripMenuItem.Name = "chooseCOMToolStripMenuItem";
            this.chooseCOMToolStripMenuItem.Size = new System.Drawing.Size(195, 22);
            this.chooseCOMToolStripMenuItem.Text = "Select Connection Port";
            this.chooseCOMToolStripMenuItem.Click += new System.EventHandler(this.ChooseCOMToolStripMenuItem_Click);
            // 
            // installModulesToolStripMenuItem
            // 
            this.installModulesToolStripMenuItem.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(81)))), ((int)(((byte)(84)))), ((int)(((byte)(101)))));
            this.installModulesToolStripMenuItem.ForeColor = System.Drawing.Color.White;
            this.installModulesToolStripMenuItem.Name = "installModulesToolStripMenuItem";
            this.installModulesToolStripMenuItem.Size = new System.Drawing.Size(195, 22);
            this.installModulesToolStripMenuItem.Text = "Install Modules";
            this.installModulesToolStripMenuItem.Click += new System.EventHandler(this.InstallModulesToolStripMenuItem_Click);
            // 
            // menuStrip1
            // 
            this.menuStrip1.BackColor = System.Drawing.Color.GhostWhite;
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripMenuItem1,
            this.settingsToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1019, 24);
            this.menuStrip1.TabIndex = 10;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // LaunchButton
            // 
            this.LaunchButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(244)))), ((int)(((byte)(241)))), ((int)(((byte)(187)))));
            this.LaunchButton.FlatAppearance.BorderSize = 0;
            this.LaunchButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.LaunchButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(61)))), ((int)(((byte)(64)))), ((int)(((byte)(71)))));
            this.LaunchButton.Location = new System.Drawing.Point(619, 344);
            this.LaunchButton.Name = "LaunchButton";
            this.LaunchButton.Size = new System.Drawing.Size(262, 86);
            this.LaunchButton.TabIndex = 19;
            this.LaunchButton.Text = "Click to Launch";
            this.LaunchButton.UseVisualStyleBackColor = false;
            this.LaunchButton.Click += new System.EventHandler(this.LaunchButton_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.ForeColor = System.Drawing.Color.White;
            this.label5.Location = new System.Drawing.Point(16, 34);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(114, 13);
            this.label5.TabIndex = 20;
            this.label5.Text = "Loaded Configuration: ";
            // 
            // loadedConfigurationLabel
            // 
            this.loadedConfigurationLabel.AutoSize = true;
            this.loadedConfigurationLabel.ForeColor = System.Drawing.Color.White;
            this.loadedConfigurationLabel.Location = new System.Drawing.Point(131, 34);
            this.loadedConfigurationLabel.Name = "loadedConfigurationLabel";
            this.loadedConfigurationLabel.Size = new System.Drawing.Size(22, 13);
            this.loadedConfigurationLabel.TabIndex = 21;
            this.loadedConfigurationLabel.Text = "NA";
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSize = true;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(81)))), ((int)(((byte)(84)))), ((int)(((byte)(101)))));
            this.ClientSize = new System.Drawing.Size(1019, 668);
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
            this.Controls.Add(this.TagCreatorGroupBox);
            this.Controls.Add(this.menuStrip1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MainMenuStrip = this.menuStrip1;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "MainWindow";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Interactive RFID Display";
            this.TagCreatorGroupBox.ResumeLayout(false);
            this.TagCreatorGroupBox.PerformLayout();
            this.displayCalibrationGroupBox.ResumeLayout(false);
            this.displayCalibrationGroupBox.PerformLayout();
            this.backgroundCalibrationGroupBox.ResumeLayout(false);
            this.backgroundCalibrationGroupBox.PerformLayout();
            this.ApplicationsGroupBox.ResumeLayout(false);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label tagLabel;
        private System.Windows.Forms.Label imageLabel;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tagBox;
        private System.Windows.Forms.TextBox imageTextBox;
        private System.Windows.Forms.Button imageButton;
        private System.Windows.Forms.Button saveButton;
        private System.Windows.Forms.Button clearButton;
        private System.Windows.Forms.TextBox soundTextBox;
        private System.Windows.Forms.Button soundButton;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.GroupBox TagCreatorGroupBox;
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
        private System.Windows.Forms.Button tagGetIdButton;
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
        private System.Windows.Forms.Button secondSoundButton;
        private System.Windows.Forms.TextBox secondSoundTextBox;
        private System.Windows.Forms.Button LaunchButton;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label loadedConfigurationLabel;
    }
}

