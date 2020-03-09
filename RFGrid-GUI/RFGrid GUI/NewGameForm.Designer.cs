namespace RFGrid_GUI
{
    partial class NewGameForm
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(NewGameForm));
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.label2 = new System.Windows.Forms.Label();
            this.createNewGameButton = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.applicationFolderTextBox = new System.Windows.Forms.TextBox();
            this.groupBox4.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox4
            // 
            this.groupBox4.BackColor = System.Drawing.SystemColors.Control;
            this.groupBox4.Controls.Add(this.label2);
            this.groupBox4.Controls.Add(this.createNewGameButton);
            this.groupBox4.Controls.Add(this.label1);
            this.groupBox4.Controls.Add(this.applicationFolderTextBox);
            this.groupBox4.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.groupBox4.ForeColor = System.Drawing.Color.Black;
            this.groupBox4.Location = new System.Drawing.Point(12, 4);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(383, 193);
            this.groupBox4.TabIndex = 21;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "Application Form";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.ForeColor = System.Drawing.Color.Black;
            this.label2.Location = new System.Drawing.Point(50, 92);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(56, 17);
            this.label2.TabIndex = 22;
            this.label2.Text = "Name :";
            // 
            // createNewGameButton
            // 
            this.createNewGameButton.BackColor = System.Drawing.SystemColors.Control;
            this.createNewGameButton.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.createNewGameButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.createNewGameButton.Location = new System.Drawing.Point(149, 145);
            this.createNewGameButton.Name = "createNewGameButton";
            this.createNewGameButton.Size = new System.Drawing.Size(75, 23);
            this.createNewGameButton.TabIndex = 21;
            this.createNewGameButton.Text = "Create";
            this.createNewGameButton.UseVisualStyleBackColor = true;
            this.createNewGameButton.Click += new System.EventHandler(this.CreateNewGameButton_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.Black;
            this.label1.Location = new System.Drawing.Point(49, 48);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(292, 21);
            this.label1.TabIndex = 20;
            this.label1.Text = "Please Enter New Application Name";
            // 
            // applicationFolderTextBox
            // 
            this.applicationFolderTextBox.Location = new System.Drawing.Point(110, 89);
            this.applicationFolderTextBox.Name = "applicationFolderTextBox";
            this.applicationFolderTextBox.Size = new System.Drawing.Size(200, 23);
            this.applicationFolderTextBox.TabIndex = 19;
            // 
            // NewGameForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Control;
            this.ClientSize = new System.Drawing.Size(407, 209);
            this.Controls.Add(this.groupBox4);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "NewGameForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Create a New Application";
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.TextBox applicationFolderTextBox;
        private System.Windows.Forms.Button createNewGameButton;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
    }
}