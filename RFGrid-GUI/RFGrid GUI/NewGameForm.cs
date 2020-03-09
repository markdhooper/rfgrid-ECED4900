using System;
using System.Windows.Forms;

namespace RFGrid_GUI
{
    public partial class NewGameForm : Form
    {
        private MainWindow _mainForm = null;
        public NewGameForm(MainWindow mainForm)
        {
            _mainForm = mainForm;
            InitializeComponent();
        }


        private void CreateNewGameButton_Click(object sender, EventArgs e)
        {
            string sourceFolder = (System.IO.Directory.GetCurrentDirectory() + @"\applications\defaultAssets\");
            string newFolderPath = System.IO.Directory.GetCurrentDirectory() + @"\applications\" + applicationFolderTextBox.Text;
            if (applicationFolderTextBox.Text.Length != 0)
            {
                if (!System.IO.Directory.Exists(newFolderPath))
                {
                    if (System.IO.Directory.Exists(sourceFolder))
                    {
                        System.IO.Directory.CreateDirectory(newFolderPath);
                        _mainForm.DirectoryCopy(sourceFolder, newFolderPath);
                        System.IO.File.Move((System.IO.Directory.GetCurrentDirectory() + @"\applications\" + applicationFolderTextBox.Text + @"\rfgridGame.py"),
                            (System.IO.Directory.GetCurrentDirectory() + @"\applications\" + applicationFolderTextBox.Text + @"\" + applicationFolderTextBox.Text + ".py"));
                        string info = "New game folder sucessfully created!";
                        DialogResult result = System.Windows.Forms.MessageBox.Show(info, "About", MessageBoxButtons.OK, MessageBoxIcon.Information);
                        if (result == DialogResult.OK)
                        {
                            this.Close();
                            _mainForm.ApplicationsRefreshButton_Click(createNewGameButton, e);
                        }

                    }
                    else
                    {
                        string info = "Make sure defaultAssets folder is located in applications folder.";
                        System.Windows.Forms.MessageBox.Show(info, "About", MessageBoxButtons.OK, MessageBoxIcon.Information);

                    }
                }
                else
                {
                    System.Windows.Forms.MessageBox.Show("Game folder already exists.", "About", MessageBoxButtons.OK, MessageBoxIcon.Information);

                }


            }
        }

    }
}
