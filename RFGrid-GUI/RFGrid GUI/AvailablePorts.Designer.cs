namespace RFGrid_GUI
{
    partial class AvailablePorts
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(AvailablePorts));
            this.PortList = new System.Windows.Forms.ListBox();
            this.label1 = new System.Windows.Forms.Label();
            this.refreshButton = new System.Windows.Forms.Button();
            this.saveButtonPorts = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // PortList
            // 
            this.PortList.BackColor = System.Drawing.Color.GhostWhite;
            this.PortList.FormattingEnabled = true;
            this.PortList.Location = new System.Drawing.Point(21, 39);
            this.PortList.Name = "PortList";
            this.PortList.Size = new System.Drawing.Size(221, 147);
            this.PortList.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.Black;
            this.label1.Location = new System.Drawing.Point(18, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(118, 20);
            this.label1.TabIndex = 1;
            this.label1.Text = "Available Ports";
            // 
            // refreshButton
            // 
            this.refreshButton.BackColor = System.Drawing.SystemColors.Control;
            this.refreshButton.FlatAppearance.BorderSize = 0;
            this.refreshButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.refreshButton.Location = new System.Drawing.Point(254, 39);
            this.refreshButton.Name = "refreshButton";
            this.refreshButton.Size = new System.Drawing.Size(75, 23);
            this.refreshButton.TabIndex = 2;
            this.refreshButton.Text = "Refresh";
            this.refreshButton.UseVisualStyleBackColor = true;
            this.refreshButton.Click += new System.EventHandler(this.RefreshButton_Click);
            // 
            // saveButtonPorts
            // 
            this.saveButtonPorts.BackColor = System.Drawing.SystemColors.Control;
            this.saveButtonPorts.FlatAppearance.BorderSize = 0;
            this.saveButtonPorts.ForeColor = System.Drawing.SystemColors.ControlText;
            this.saveButtonPorts.Location = new System.Drawing.Point(136, 204);
            this.saveButtonPorts.Name = "saveButtonPorts";
            this.saveButtonPorts.Size = new System.Drawing.Size(75, 23);
            this.saveButtonPorts.TabIndex = 3;
            this.saveButtonPorts.Text = "Save";
            this.saveButtonPorts.UseVisualStyleBackColor = true;
            this.saveButtonPorts.Click += new System.EventHandler(this.SaveButtonPorts_Click);
            // 
            // AvailablePorts
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Control;
            this.ClientSize = new System.Drawing.Size(341, 249);
            this.Controls.Add(this.saveButtonPorts);
            this.Controls.Add(this.refreshButton);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.PortList);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "AvailablePorts";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Select a COM Port";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox PortList;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button refreshButton;
        private System.Windows.Forms.Button saveButtonPorts;
       
    }
}